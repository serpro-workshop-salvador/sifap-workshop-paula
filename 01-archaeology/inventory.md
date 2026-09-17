# Inventário do Legado — Time `<preencher>`

> **Trilha:** [Kit do Time](../README.md) › [Estágio 1](README.md) › **Inventário**

**Primeiro artefato do Estágio 1.** Varra a estrutura e conte os arquivos sem abrir nenhum programa — use apenas os nomes de arquivo e a estrutura de pastas.

| Campo | Valor |
|---|---|
| **Público-alvo** | Dupla responsável pela varredura inicial |
| **Pré-requisitos** | Acesso ao diretório `legacy-sifap/` |
| **Estágio** | Estágio 1 — Arqueologia, Passo 1 |
| **Resultado esperado** | Contagens corretas, padrões de nomenclatura identificados e 3 itens estranhos sinalizados |

> [!NOTE]
> Monte este inventário sem abrir nenhum programa. Trabalhe apenas com nomes de arquivo e estrutura de pastas. Ele será revisado à medida que o time extrai regras, mapeia dependências e registra mistérios.

**Data:** 2026-09-17
**Dupla responsável:** `<preencher>`
**Caminho varrido:** `01-archaeology/legacy-sifap/`

Esta é a primeira análise do acervo. As hipóteses abaixo serão revisadas durante a
leitura dos arquivos e o rastreamento explícito das dependências.

---

## Estrutura de pastas

```text
legacy-sifap/                         (42 arquivos)
├── CHRONOLOGY.md
├── DECLARED-DRIFT.md
├── HOW-TO-READ-NATURAL.md
├── README.md
├── adabas-ddms/                     (6 arquivos)
├── legacy-docs/                     (7 arquivos)
└── natural-programs/                (25 arquivos)
```

**Total:** 4 diretórios contando a raiz (3 subdiretórios). Não há outros níveis de
diretórios abaixo dos três exibidos.

---

## Contagem de arquivos por tipo

| Extensão | Contagem | Finalidade provável |
|---|---|---|
| `.NSP` | 12 | Fonte de programa Natural |
| `.NSN` | 5 | Fonte de subprograma Natural |
| `.NSC` | 2 | Copycode Natural |
| `.NSA` | 2 | Área de dados Natural |
| `.NSL` | 1 | Área de dados local Natural |
| `.jcl` | 2 | Definição de job batch |
| `.ddm` | 4 | Data Definition Module (Adabas) |
| `.cpy` | 0 | Nenhum copycode com esta extensão foi encontrado |
| `.map` | 0 | Nenhuma definição de tela com esta extensão foi encontrada |
| `.txt` | 1 | Listagem ou documentação em texto simples |
| `.md` | 10 | Documentação e índices em Markdown |
| `.docx` | 3 | Documentação em formato Word |
| **Total** | **42** | Soma de todos os arquivos encontrados |

---

## Padrões da convenção de nomes

| Prefixo | Contagem | Hipótese de domínio |
|---|---|---|
| `BAT` (`BATCH*`) | 3 | Provável família de pontos de entrada batch; confirmar no rastreamento dos jobs |
| `CAD` | 3 | Família relacionada pelo nome; finalidade desconhecida até a leitura |
| `CAL` (`CALC*`) | 3 | Família relacionada pelo nome; finalidade desconhecida até a leitura |
| `CC` | 2 | Prováveis copycodes, hipótese apoiada apenas pela extensão `.NSC` |
| `PDA` | 2 | Prováveis áreas de parâmetros, hipótese apoiada pelo prefixo e pela extensão `.NSA` |
| `REL` | 2 | Família relacionada pelo nome; finalidade desconhecida até a leitura |
| `SIF` (`SIFAPJ*`) | 2 | Prováveis jobs numerados, hipótese apoiada apenas pela extensão `.jcl` |
| `SUB` | 2 | Prováveis subprogramas chamáveis, hipótese apoiada pelo prefixo e pela extensão `.NSN` |
| `VAL` | 3 | Família relacionada pelo nome; finalidade desconhecida até a leitura |
| `REA` (`README.md`) | 4 | Índice repetido na raiz e em cada subdiretório |

---

## Itens estranhos (top 3)

| # | Caminho do arquivo | O que o torna estranho | Investigação sugerida |
|---|---|---|---|
| 1 | `adabas-ddms/FDT-150-BENEFICIARY.txt` | Único arquivo `.txt`, único prefixo `FDT` e único nome com segmento numérico nessa pasta | Verificar depois se é uma listagem de estrutura e como se relaciona aos DDMs |
| 2 | `natural-programs/LDASIFAP.NSL` | Único arquivo com extensão `.NSL` | Identificar, durante o mapa de dependências, quais membros usam essa área local |
| 3 | `legacy-docs/TECHNICAL-MANUAL-SIFAP-2008.docx` | Nome de arquivo mais longo do acervo e mesmo nome-base de um arquivo `.md` | Tratar os dois formatos como representações candidatas da mesma fonte e comparar apenas na etapa de leitura documental |

---

## Ordem de leitura proposta

1. Começar pelos candidatos a pontos de entrada batch: `SIFAPJ*.jcl` e, em seguida,
   `BATCH*.NSP`. A prioridade decorre somente dos nomes e extensões.
2. Ler os quatro arquivos `.ddm` e depois a listagem `FDT-150-BENEFICIARY.txt` para
   formar uma hipótese do modelo de dados antes de aprofundar a lógica.
3. Investigar os candidatos a maior conectividade por nomes compartilhados:
   `PDACALC.NSA` com `CALC*`, e `PDAVALID.NSA`, `CCVALCPF.NSC` e `SUBVAL*.NSN`
   com `VAL*`.
4. Só então percorrer as demais famílias (`CAD*`, `REL*` e nomes únicos) e a
   documentação histórica.

Esta ordem é uma hipótese baseada apenas em metadados. Ela deverá mudar se o
rastreamento de `CALLNAT`, `INCLUDE`, `USING` e dos JCLs revelar outras dependências.

---

## Definição de pronto

- [x] O inventário existe com contagens corretas.
- [x] 3 padrões de nomenclatura ou mais identificados.
- [x] 3 itens estranhos sinalizados.

---

### Continue lendo

| Anterior | Próximo |
|---|---|
| [GUIDE do Estágio 1](GUIDE.md)<br/><sub>Cronograma passo a passo.</sub> | [Catálogo de Regras](business-rules-catalog.md)<br/><sub>Passo 2 — extração de regras.</sub> |

<sub>[Voltar ao índice do kit](../README.md)</sub>
