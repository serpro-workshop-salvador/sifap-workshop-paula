#!/usr/bin/env python3
"""Valida se os documentos do kit concordam com os cabeçalhos dos fontes do SIFAP.

Por que este gate existe
------------------------
O acervo tem duas camadas. Documentos de época sobre o SIFAP *podem* contradizer
o código: o desvio da documentação é a lição do Estágio 1, e cada divergência
deliberada está registrada em DECLARED-DRIFT.md. Os guias do próprio kit *não*
podem contradizer o código: um guia que atribui um programa à pessoa errada
manda a dupla para a evidência errada e quebra o exercício que deveria ensinar.

Este script transforma essa distinção em um gate de build. Ele lê os cabeçalhos
`* AUTHOR:` e `* DATE:` diretamente do acervo somente leitura e depois confere
as tabelas dos documentos de verdade do kit contra eles.

O que é verificado
------------------
1. Todo membro Natural, JCL e DDM tem cabeçalho AUTHOR e DATE analisável.
2. As tabelas canônicas em 01-archaeology/legacy-sifap/CHRONOLOGY.md coincidem
   exatamente com esses cabeçalhos (autoria e data completa de criação).
3. A tabela de atribuição por dupla em natural-programs/README.md coincide com
   eles (autoria e ano de criação).
4. O intervalo do acervo afirmado em CHRONOLOGY.md é igual ao intervalo real.
5. DECLARED-DRIFT.md tem identificadores únicos e cita apenas arquivos existentes.

Restrições de projeto
---------------------
Python 3.11+, apenas biblioteca padrão, para que a integração contínua não
precise de `pip install`. Só são conferidas tabelas situadas sob um título
nomeado, o que mantém prosa e tabelas narrativas derivadas fora de escopo por
construção.

Código de saída
---------------
Diferente de zero quando há qualquer erro, com uma anotação `::error` por achado.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
CORPUS = REPO_ROOT / "01-archaeology" / "legacy-sifap"
PROGRAMS = CORPUS / "natural-programs"
DDMS = CORPUS / "adabas-ddms"
CHRONOLOGY = CORPUS / "CHRONOLOGY.md"
DRIFT = CORPUS / "DECLARED-DRIFT.md"
PROGRAMS_README = PROGRAMS / "README.md"

MEMBER_SUFFIXES = (".NSP", ".NSN", ".NSC", ".NSA", ".NSL", ".jcl")

# Membros Natural usam `* AUTHOR:`; o JCL usa `//* AUTHOR...:`. Um único
# padrão cobre os dois, porque tudo antes da palavra-chave é pontuação de
# comentário.
AUTHOR_RE = re.compile(
    r"^\s*(?://)?\*\s*AUTHOR\.*:\s*(.+?)\s*$", re.IGNORECASE)
DATE_RE = re.compile(
    r"^\s*(?://)?\*\s*DATE\.*:\s*(\d{2}/\d{2}/\d{4})\s*$", re.IGNORECASE)
HEADER_SCAN_LINES = 20

YEAR_RE = re.compile(r"\b(19[89]\d|20[0-2]\d)\b")
FULL_DATE_RE = re.compile(r"\b\d{2}/\d{2}/\d{4}\b")
DRIFT_ID_RE = re.compile(r"`(DRIFT-\d{2})`")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)#]+)(?:#[^)]*)?\)")

# A afirmação sobre o intervalo decorrido é a única frase em prosa que este
# gate lê, então precisa da redação da branch em que roda. Caminhos, números
# de seção e dados das tabelas são idênticos em todas as edições.
SPAN_PHRASE = {
    "en": "{n} calendar years",
    "pt-br": "{n} anos civis",
    "es": "{n} años naturales",
}


def branch_language() -> str:
    metadata = REPO_ROOT / ".github" / "language.json"
    if not metadata.is_file():
        return "en"
    try:
        return json.loads(metadata.read_text(encoding="utf-8")).get("language", "en")
    except json.JSONDecodeError:
        return "en"


class Reporter:
    """Reúne os achados e imprime anotações do GitHub Actions."""

    def __init__(self) -> None:
        self.errors: list[str] = []

    def error(self, file: Path | str, message: str) -> None:
        rel = file if isinstance(
            file, str) else file.relative_to(REPO_ROOT).as_posix()
        self.errors.append(f"{rel}: {message}")
        print(f"::error file={rel}::{message}")


def normalize(text: str) -> str:
    """Normaliza caixa, pontuação e espaços para comparar nomes com segurança."""
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def read_header(path: Path) -> tuple[str | None, str | None]:
    author = date = None
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines()[:HEADER_SCAN_LINES]:
        if author is None and (match := AUTHOR_RE.match(line)):
            author = match.group(1)
        if date is None and (match := DATE_RE.match(line)):
            date = match.group(1)
    return author, date


def collect_corpus(reporter: Reporter) -> dict[str, tuple[str, str]]:
    """Mapeia cada artefato do acervo para sua (autoria, dd/mm/aaaa) declarada."""
    canon: dict[str, tuple[str, str]] = {}
    sources = [p for p in sorted(PROGRAMS.iterdir())
               if p.suffix in MEMBER_SUFFIXES]
    sources += sorted(DDMS.glob("*.ddm"))
    for path in sources:
        author, date = read_header(path)
        if author is None or date is None:
            reporter.error(
                path, "o cabeçalho não tem uma linha '* AUTHOR:' ou '* DATE:' analisável")
            continue
        canon[path.name] = (author, date)
    return canon


def table_under_heading(path: Path, heading_pattern: str) -> list[tuple[int, str]]:
    """Devolve a primeira tabela Markdown após um título, como (linha, conteúdo)."""
    heading_re = re.compile(heading_pattern)
    lines = path.read_text(encoding="utf-8").splitlines()
    rows: list[tuple[int, str]] = []
    in_section = seen_table = False
    for index, line in enumerate(lines, start=1):
        if line.startswith("#"):
            if in_section and seen_table:
                break
            in_section = bool(heading_re.search(line))
            continue
        if not in_section:
            continue
        if line.lstrip().startswith("|"):
            seen_table = True
            rows.append((index, line))
        elif seen_table and line.strip():
            break
    return rows


def check_table(
    path: Path,
    heading_pattern: str,
    canon: dict[str, tuple[str, str]],
    reporter: Reporter,
    *,
    full_date: bool,
) -> int:
    """Confere se cada linha de artefato da tabela bate com os cabeçalhos."""
    checked = 0
    other_authors = {normalize(author) for author, _ in canon.values()}
    for line_no, row in table_under_heading(path, heading_pattern):
        cells = [cell.strip() for cell in row.strip().strip("|").split("|")]
        if all(set(cell) <= set("-: ") for cell in cells):
            continue
        named = [name for name in canon if f"`{name}`" in row]
        if len(named) != 1:
            continue
        name = named[0]
        author, date = canon[name]
        haystack = normalize(row)
        location = f"{path.relative_to(REPO_ROOT).as_posix()}:{line_no}"

        if normalize(author) not in haystack:
            wrong = sorted(o for o in other_authors if o !=
                           normalize(author) and o in haystack)
            detail = f" (a linha cita '{wrong[0]}')" if wrong else ""
            reporter.error(
                location, f"{name} tem autoria '{author}' em seu cabeçalho{detail}")

        expected = date if full_date else date[-4:]
        found = FULL_DATE_RE.findall(
            row) if full_date else YEAR_RE.findall(row)
        if expected not in found:
            kind = "data de criação" if full_date else "ano de criação"
            reporter.error(
                location, f"{name} tem {kind} {expected} em seu cabeçalho; a linha diz {found or 'nada'}")
        checked += 1
    return checked


def check_corpus_span(canon: dict[str, tuple[str, str]], reporter: Reporter) -> None:
    """O intervalo declarado precisa ser igual ao que o acervo realmente cobre."""
    years = sorted(date[-4:] for _, date in canon.values())
    text = CHRONOLOGY.read_text(encoding="utf-8")
    section = text.split("## 2.")[1].split("## 3.")[
        0] if "## 2." in text else ""
    if years[0] not in section:
        reporter.error(
            CHRONOLOGY, f"o fonte datado mais antigo é {years[0]}, que a seção 2 não declara")
    elapsed = 2026 - int(years[0])
    template = SPAN_PHRASE.get(branch_language(), SPAN_PHRASE["en"])
    phrase = template.format(n=elapsed)
    if phrase not in section:
        reporter.error(
            CHRONOLOGY, f"o intervalo de {years[0]} até o ano de referência 2026 é '{phrase}'")


def check_drift_register(reporter: Reporter) -> None:
    text = DRIFT.read_text(encoding="utf-8")
    ids = DRIFT_ID_RE.findall(text)
    if len(ids) != len(set(ids)):
        reporter.error(DRIFT, "identificador DRIFT- duplicado no registro")
    for target in {t for t in LINK_RE.findall(text) if not t.startswith(("http", "mailto"))}:
        if not (DRIFT.parent / target).resolve().exists():
            reporter.error(
                DRIFT, f"o registro aponta para um arquivo inexistente: {target}")


def main() -> int:
    reporter = Reporter()
    canon = collect_corpus(reporter)
    if not canon:
        reporter.error("01-archaeology/legacy-sifap",
                       "nenhum fonte legado encontrado para servir de referência")
        return 1

    checked = check_table(CHRONOLOGY, r"3\.1\.", canon,
                          reporter, full_date=True)
    checked += check_table(CHRONOLOGY, r"3\.2\.", canon,
                           reporter, full_date=True)
    checked += check_table(CHRONOLOGY, r"^## 4\.",
                           canon, reporter, full_date=True)
    checked += check_table(PROGRAMS_README, r"^## 1\.",
                           canon, reporter, full_date=False)
    check_corpus_span(canon, reporter)
    check_drift_register(reporter)

    print(
        f"\nGate de cronologia: {len(canon)} artefatos legados lidos, {checked} linhas de tabela conferidas.")
    if reporter.errors:
        print(f"FALHOU: {len(reporter.errors)} erro(s) de cronologia.")
        for finding in reporter.errors:
            print(f"  - {finding}")
        return 1
    print("APROVADO: toda tabela do kit concorda com os cabeçalhos dos fontes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
