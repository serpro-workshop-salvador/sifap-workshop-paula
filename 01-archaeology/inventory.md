# Inventário do Legado: paula

> **Trilha:** [Kit do Time](../README.md) › [Estágio 1](README.md) › **Inventário**

**Inventário do Estágio 1.** Preserva o levantamento inicial por nomes e acrescenta o catálogo e a cobertura da leitura assistida dos membros Natural/JCL e das estruturas Adabas.

| Campo | Valor |
|---|---|
| **Público-alvo** | paula, responsável pelo estudo individual de todas as áreas |
| **Pré-requisitos** | Acesso ao diretório `legacy-sifap/` |
| **Estágio** | Estágio 1 — Arqueologia, Passo 1 |
| **Resultado esperado** | Contagens corretas, padrões de nomenclatura identificados e 3 itens estranhos sinalizados |

> [!NOTE]
> O kickoff foi realizado apenas por nomes e estrutura. O catálogo ao final foi acrescentado depois da leitura dos fontes; não infira que uma hipótese inicial de nomenclatura foi confirmada como regra de negócio.

**Data:** 2026-09-17
**Responsável:** paula
**Modalidade:** individual, cobrindo as cinco áreas do kit
**Caminho varrido:** `01-archaeology/legacy-sifap/`

As seções de contagem e nomenclatura preservam a primeira análise. A seção de
cobertura registra a revisão estática posterior. As antigas duplas são apenas
agrupamentos de assunto nesta execução; nenhum arquivo depende de outra pessoa
para ser investigado. A revisão humana e a escolha do recorte do H1 cabem a paula,
com o apoio do agente, sem simular aprovação já recebida.

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

## Catálogo dos 15 membros atribuídos

As finalidades são hipóteses de uma linha apoiadas no cabeçalho e no corpo lido, não especificações aprovadas. Datas e autoria permanecem na [cronologia canônica](legacy-sifap/CHRONOLOGY.md). O intervalo de leitura inclui início do arquivo até `END`; as regras condicionais estão em [business-rules-catalog.md](business-rules-catalog.md).

| Área do kit | Membro | Hipótese de finalidade | Leitura integral | DEFINE DATA |
|---|---|---|---|---|
| 1 | [CADBENEF.NSP](legacy-sifap/natural-programs/CADBENEF.NSP) | Manter cadastro por inclusão e alteração | 1-430 | 13-104 |
| 1 | [CADDEPEN.NSP](legacy-sifap/natural-programs/CADDEPEN.NSP) | Acrescentar dependentes ao grupo do titular | 1-247 | 12-82 |
| 1 | [CADPROG.NSP](legacy-sifap/natural-programs/CADPROG.NSP) | Incluir e consultar programas sociais | 1-188 | 12-72 |
| 2 | [BATCHPGT.NSP](legacy-sifap/natural-programs/BATCHPGT.NSP) | Gerar pagamentos e extrato de uma competência | 1-596 | 27-156 |
| 2 | [BATCHREL.NSP](legacy-sifap/natural-programs/BATCHREL.NSP) | Consolidar pagamentos por região e situação | 1-280 | 22-78 |
| 2 | [BATCHCON.NSP](legacy-sifap/natural-programs/BATCHCON.NSP) | Confrontar pagamentos com detalhes de retorno bancário | 1-347 | 20-103 |
| 3 | [CALCBENF.NSN](legacy-sifap/natural-programs/CALCBENF.NSN) | Calcular benefício, gravar pagamento e devolver valores | 1-378 | 16-93 |
| 3 | [CALCCORR.NSP](legacy-sifap/natural-programs/CALCCORR.NSP) | Aplicar correção a pagamentos selecionados | 1-255 | 12-82 |
| 3 | [CALCDSCT.NSP](legacy-sifap/natural-programs/CALCDSCT.NSP) | Calcular contribuição e descontos de um pagamento | 1-217 | 12-57 |
| 4 | [VALBENEF.NSN](legacy-sifap/natural-programs/VALBENEF.NSN) | Retornar inconsistências de dados cadastrais | 1-333 | 15-71 |
| 4 | [VALDOCS.NSP](legacy-sifap/natural-programs/VALDOCS.NSP) | Validar documentos em tela com tratamento de prefixos especiais | 1-243 | 14-52 |
| 4 | [VALELEG.NSN](legacy-sifap/natural-programs/VALELEG.NSN) | Avaliar elegibilidade usando beneficiário e programa | 1-269 | 15-66 |
| 5 | [CONSBENF.NSP](legacy-sifap/natural-programs/CONSBENF.NSP) | Consultar cadastro por CPF/NIS e exibir pagamentos | 1-316 | 18-104 |
| 5 | [RELPGT.NSP](legacy-sifap/natural-programs/RELPGT.NSP) | Imprimir detalhe, subtotais e total de pagamentos | 1-273 | 17-72 |
| 5 | [RELAUDIT.NSP](legacy-sifap/natural-programs/RELAUDIT.NSP) | Apresentar eventos e distribuição diária de auditoria | 1-305 | 18-66 |

## Catálogo dos nove membros de apoio

| Membro | Tipo | Hipótese de finalidade | Evidência de leitura |
|---|---|---|---|
| [PDAVALID.NSA](legacy-sifap/natural-programs/PDAVALID.NSA) | PDA | Contrato da família CPF/NIS | 1-57; DEFINE DATA 43-57 |
| [PDACALC.NSA](legacy-sifap/natural-programs/PDACALC.NSA) | PDA | Contrato de contexto e resultados da cadeia de pagamentos | 1-79; DEFINE DATA 49-79 |
| [LDASIFAP.NSL](legacy-sifap/natural-programs/LDASIFAP.NSL) | LDA | Declarações e tabelas locais reutilizáveis | 1-107; DEFINE DATA 32-107 |
| [CCVALCPF.NSC](legacy-sifap/natural-programs/CCVALCPF.NSC) | Copycode | Rotina inserida de validação de CPF | 1-130, incluindo campos requeridos e sub-rotina |
| [CCAUDIT.NSC](legacy-sifap/natural-programs/CCAUDIT.NSC) | Copycode | Rotina inserida de gravação de evento | 1-100, incluindo contrato da view e controle transacional |
| [SUBVALCP.NSN](legacy-sifap/natural-programs/SUBVALCP.NSN) | Subprograma | Adaptar CPF ao copycode e devolver diagnóstico | 1-96; DEFINE DATA 28-42 |
| [SUBVALNI.NSN](legacy-sifap/natural-programs/SUBVALNI.NSN) | Subprograma | Validar NIS e devolver diagnóstico | 1-152; DEFINE DATA 38-50 |
| [SIFAPJ01.jcl](legacy-sifap/natural-programs/SIFAPJ01.jcl) | JCL | Invocar folha e condicionar cópia/step de aviso | Arquivo integral; CMSYNIN 69-74 e condições 80/92 |
| [SIFAPJ02.jcl](legacy-sifap/natural-programs/SIFAPJ02.jcl) | JCL | Invocar relatório consolidado e detalhado | Arquivo integral; CMSYNIN 66-71 e 94-101 |

`VALBENEF` não faz parte destes nove: é um dos 15 atribuídos. Copycodes não possuem `DEFINE DATA` próprio, mas documentam campos que precisam existir no objeto que os inclui.

## Cobertura Adabas e artefatos

| Fonte | Leitura integral | Artefato de confronto |
|---|---|---|
| [BENEFIC.ddm](legacy-sifap/adabas-ddms/BENEFIC.ddm) | 1-179 | [data-map.md](data-map.md) |
| [SOCPROG.ddm](legacy-sifap/adabas-ddms/SOCPROG.ddm) | 1-126 | [data-map.md](data-map.md) |
| [PAYMENT.ddm](legacy-sifap/adabas-ddms/PAYMENT.ddm) | 1-165 | [data-map.md](data-map.md) |
| [AUDIT.ddm](legacy-sifap/adabas-ddms/AUDIT.ddm) | 1-147 | [data-map.md](data-map.md) |
| [FDT-150-BENEFICIARY.txt](legacy-sifap/adabas-ddms/FDT-150-BENEFICIARY.txt) | 1-156, até END OF REPORT | [data-map.md](data-map.md) |

**Cobertura estática:** 15/15 atribuídos, 9/9 de apoio, 4/4 DDMs e 1/1 FDT fornecida. Isto não é prova de execução, equivalência, completude do ambiente de produção nem validação dos 20 mistérios canônicos.

**Ordem de revisão após a leitura:** conferir o [grafo](dependency-map.md), confrontar as perguntas com o [mapa de dados](data-map.md), revisar o vocabulário no [glossário](glossary.md) e registrar a decisão de paula no [relatório](discovery-report.md). Esta é a revisão H1 individual guiada; não há passagem de trabalho a outra dupla.

## Conferência reproduzível

As ferramentas desta sessão enumeraram nomes e conferiram instruções por busca. Para reconferir a árvore sem abrir os fontes:

```bash
find 01-archaeology/legacy-sifap -type d
find 01-archaeology/legacy-sifap -type f
```

Os comandos acima são uma referência para revisão; não foram executados nesta sessão. Não foram medidos tamanhos em bytes nem executados programas Natural.

## Definição de pronto

- [x] O inventário existe com contagens corretas.
- [x] 3 padrões de nomenclatura ou mais identificados.
- [x] 3 itens estranhos sinalizados.
- [x] Os 24 membros possuem hipótese de finalidade e registro de leitura estática.
- [x] Os quatro DDMs e a FDT possuem mapa de dados de apoio.
- [x] paula está identificada como responsável por todo o escopo, em modalidade individual.
- [x] Aceite H1 do recorte de consulta de programa por código recebido de paula em 2026-09-17 e registrado no [relatório](discovery-report.md#revisão-h1-guiada).
- [ ] paula forneceu as associações de mistérios canônicos.

---

### Continue lendo

| Anterior | Próximo |
|---|---|
| [GUIDE do Estágio 1](GUIDE.md)<br/><sub>Cronograma passo a passo.</sub> | [Catálogo de Regras](business-rules-catalog.md)<br/><sub>Passo 2 — extração de regras.</sub> |

<sub>[Voltar ao índice do kit](../README.md)</sub>
