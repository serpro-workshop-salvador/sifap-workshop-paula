# Notas de leitura de DEFINE DATA

> **Trilha:** [Kit do Time](../README.md) > [Estágio 1](README.md) > **Notas de leitura**

**Vocabulário de tipos e dimensões utilizado na leitura condicional dos programas.** Variáveis de mesmo formato são agrupadas; o agrupamento não afirma que tenham o mesmo significado de negócio.

| Campo | Valor |
|---|---|
| Data | 2026-09-17 |
| Escopo | Declarações dos 22 membros Natural; JCLs documentados no mapa de dependências |
| Formatos | A: alfanumérico; N: numérico; P: compactado; L: lógico; intervalos indicam arrays |
| Fontes persistidas | As projeções de view estão nas faixas DEFINE DATA citadas; campos, formatos e domínios completos por família estão em [data-map.md](data-map.md) |
| Limite | Comentários de propósito não comprovam uso; os acessos efetivos estão em [dependency-map.md](dependency-map.md) |

## Declarações compartilhadas

### Auditoria

Aplicável a CADBENEF, CADDEPEN, CADPROG, BATCHPGT, BATCHCON, CALCCORR e CONSBENF, conforme cada declaração e inclusão. Fonte do contrato: [CCAUDIT.NSC:20-43](legacy-sifap/natural-programs/CCAUDIT.NSC#L20).

| Formato | Variáveis | Comentário/contexto |
|---|---|---|
| A2 | `#AUD-ACTION` | Ação fornecida pelo chamador |
| A4 | `#AUD-ENTITY` | Tipo de entidade |
| A15 | `#AUD-ID` | Chave fornecida pelo chamador |
| A11 | `#AUD-CPF` | CPF afetado ou branco |
| A80 | `#AUD-DESCR` | Descrição livre |
| N15 | `#AUD-SEQ` | Semente da sequência |
| N7 | `#AUD-TIMN` | Valor de trabalho de `*TIMN` |

A view comum tem NUM-AUDIT N15, DT-EVENT N8, HR-EVENT N6, TS-EVENT N14, COD-ACTION A2, COD-MODULE A8, DESCR-ACTION A80, TYPE-ENTITY A4, ID-ENTITY A15, NUM-CPF-AFFECTED A11, USR-EVENT A8, NAME-JOB-BATCH A16 e STAT-BATCH A1. BATCHCON acrescenta AMT-PREV/AMT-NEW A60. São projeções parciais de AUDIT, não todos os campos do DDM.

### Copycode de CPF

Campos declarados por CADDEPEN e SUBVALCP para [CCVALCPF.NSC:19-30](legacy-sifap/natural-programs/CCVALCPF.NSC#L19):

| Formato | Variáveis | Comentário/contexto |
|---|---|---|
| A11 | `#CPF-STR` | Entrada textual |
| L | `#CPF-OK`, `#CPF-EQUAL` | Resultado e comparação de igualdade |
| N1/1:11 | `#CPF-DIG` | Onze dígitos |
| N5 | `#CPF-SUM`, `#CPF-QUOT` | Soma e quociente |
| N2 | `#CPF-REMAIN`, `#CPF-WEIGHT`, `#CPF-IDX` | Resto, peso e índice |
| N1 | `#CPF-DV1`, `#CPF-DV2` | Verificadores |

`#CPF-EQUAL` é usado dentro do texto incluído. As cópias internas dos outros programas têm nomes e formatos diferentes, registrados abaixo.

### PDAVALID

Fonte: [PDAVALID.NSA:43-57](legacy-sifap/natural-programs/PDAVALID.NSA#L43). As direções IN/OUT são comentários do contrato.

| Formato | Variáveis | Direção/comentário |
|---|---|---|
| A1 | `#PV-TYPE-DOC` | IN, C ou N |
| A11 | `#PV-CPF`, `#PV-NIS` | IN, documentos sem máscara |
| N4 | `#PV-COD-RETURN` | OUT, zero quando válido |
| A60 | `#PV-MSG` | OUT, mensagem |
| A1 | `#PV-IND-SPECIAL` | OUT, S especial ou N comum |

### PDACALC

Fonte: [PDACALC.NSA:49-79](legacy-sifap/natural-programs/PDACALC.NSA#L49).

| Formato | Variáveis | Direção/comentário |
|---|---|---|
| A11 | `#PC-CPF` | IN, chave CPF |
| A4 | `#PC-COD-PROGRAM` | IN, programa |
| N6 | `#PC-PERIOD` | IN, YYYYMM |
| A2 | `#PC-COD-REGION` | IN; domínio do comentário difere do DDM |
| P9.2 | `#PC-FAMILY-INCOME`, `#PC-AMT-BASE` | IN, renda e base |
| N2 | `#PC-QTY-DEPEND` | IN, quantidade |
| N3 | `#PC-AGE` | IN, idade |
| A1 | `#PC-STAT-BENEF` | IN, situação |
| P9.2 | `#PC-AMT-GROSS`, `#PC-AMT-DISC`, `#PC-AMT-BONUS`, `#PC-AMT-NET` | OUT, valores; a fórmula do comentário não substitui o fluxo executado |
| A1 | `#PC-TYPE-PAYMENT` | OUT, N/D/T no comentário |
| N4 | `#PC-COD-RETURN` | OUT, código |
| A60 | `#PC-MSG` | OUT, mensagem |

### LDASIFAP

Fonte: [LDASIFAP.NSL:32-107](legacy-sifap/natural-programs/LDASIFAP.NSL#L32). São declarações locais incorporadas por USING, não um serviço de configuração consultado em execução.

| Formato | Variáveis | Inicialização/comentário |
|---|---|---|
| N3.4/1:27 | `#L-TAB-REGION-FACTOR` | Fatores regionais fixados no fonte |
| A2/1:27 | `#L-TAB-REGION-UF`, `#L-VALID-UF` | Tabelas distintas de região/UF e UFs válidas |
| P9.2/1:5 | `#L-INCOME-BAND` | Tetos 300, 600, 1000, 1500 e 9999.99 |
| N3.4/1:5 | `#L-BAND-FACTOR` | 1.00, 0.85, 0.70, 0.55 e 0.40 |
| P9.2/1:4 | `#L-CONTRIB-BAND` | Tetos de contribuição |
| N3.2/1:4 | `#L-CONTRIB-RATE` | 0.03, 0.05, 0.07 e 0.09 |
| N2/1:12 | `#L-DAYS-MONTH` | Fevereiro inicializado com 29 |
| N8 | `#L-DT-TODAY` | YYYYMMDD |
| N4 | `#L-YEAR`, `#L-PERIOD-YEAR`, `#L-EXPANDED-YEAR`, `#L-COD-RETURN` | Anos e código de retorno |
| N2 | `#L-MONTH`, `#L-DAY`, `#L-PERIOD-MONTH`, `#L-AA-SHORT`, `#L-CENTURY-WINDOW`, `#L-I`, `#L-J`, `#L-K` | Pivô inicializado com 50; demais campos de trabalho |
| N6 | `#L-PERIOD` | YYYYMM |
| P13.2 | `#L-AMT-TEMP` | Temporário monetário |
| A78 | `#L-MSG` | Mensagem padrão |

## Cadastro

### CADBENEF

Fonte: [CADBENEF.NSP:13-104](legacy-sifap/natural-programs/CADBENEF.NSP#L13). Acrescenta PDAVALID e o grupo de auditoria acima; projeta BENEFIC e AUDIT.

| Formato | Variáveis de trabalho | Contexto |
|---|---|---|
| N11 | `#CPF`, `#NIS` | Entrada numérica de documentos |
| A60 | `#NAME`, `#MSG` | Nome e mensagem |
| N8 | `#DT-BIRTH`, `#CEP`, `#DT-TODAY` | Data, CEP e data corrente |
| A1 | `#SEX`, `#STATUS`, `#OPER`, `#RESULT` | Operação I/A; resultado corporativo separado |
| A80 | `#ADDRESS` | Maior que a rua A60 da view |
| A40 | `#CITY` | Cidade |
| A2 | `#UF` | UF |
| A15 | `#PHONE`, `#RG` | Contato/documento |
| N4 | `#COD-PROG`, `#YEAR-CURRENT`, `#YEAR-BIRTH` | Programa numérico na tela e anos |
| P9.2 | `#FAMILY-INCOME` | Renda |
| N2 | `#NUM-DEPEND`, `#COD-REGION`, `#QTY-ERRS`, `#WEIGHT`, `#I` | Quantidades, região e trabalho de CPF |
| N3 | `#AGE`, `#REMAIN` | Idade e resto |
| L | `#ERR`, `#CPF-VALID`, `#FOUND` | Controle |
| A60/1:10 | `#MSG-ERR` | Mensagens retornadas |
| A11 | `#CPF-STR` | Conversão de CPF |
| N1/1:11 | `#DIG` | Dígitos |
| N5 | `#SUM` | Soma |
| N1 | `#DV1`, `#DV2` | Verificadores |

### CADDEPEN

Fonte: [CADDEPEN.NSP:12-82](legacy-sifap/natural-programs/CADDEPEN.NSP#L12). Acrescenta LDASIFAP, auditoria e campos do copycode de CPF. Projeta BENEFIC, dependentes 1:10 e AUDIT.

| Formato | Variáveis de trabalho | Contexto |
|---|---|---|
| N11 | `#CPF-HOLDER`, `#CPF-DEPEND` | Entrada de titular/dependente |
| A11 | `#CPF-HOLDER-STR`, `#CPF-DEPEND-STR` | Chaves formatadas |
| A60 | `#NAME-DEPEND`, `#MSG` | Nome e mensagem |
| N8 | `#DT-BIRTH-DEPEND` | Nascimento |
| A2 | `#RELATION` | Parentesco |
| A15 | `#DOC-DEPEND` | Documento coletado, sem campo correspondente na view |
| A1 | `#SEX-DEPEND`, `#STAT-BENEF`, `#COUNT` | Sexo, situação e continuidade |
| N2 | `#NUM-DEPEND`, `#IDX` | Quantidade e ocorrência |
| L | `#FOUND`, `#ERR` | Controle |

### CADPROG

Fonte: [CADPROG.NSP:12-72](legacy-sifap/natural-programs/CADPROG.NSP#L12). Acrescenta LDASIFAP e auditoria; projeta SOCPROG e AUDIT.

| Formato | Variáveis de trabalho | Contexto |
|---|---|---|
| N4 / A4 | `#COD-PROG` / `#COD-PROG-A` | Código de tela e chave DDM |
| A60 | `#NAME-PROG`, `#MSG` | Nome e mensagem |
| A1 | `#TYPE`, `#STATUS`, `#OPER` | Tipo, situação e operação |
| P9.2 | `#AMT-BASE`, `#MAX-INCOME`, `#AMT-CALC` | Valores locais; campos correspondentes da view usam P7.2 |
| A5 | `#COD-ELIG` | Elegibilidade |
| N8 | `#DT-START`, `#DT-END` | Datas |
| N3 | `#AGE-MIN`, `#AGE-MAX` | Idades |
| N3.4 / N5.6 | `#FACTOR-ADJUST` / `#FACTOR-K` | Fatores locais; não confundir com formatos e campos persistidos |
| L | `#FOUND` | Controle da busca |

## Batch

### BATCHPGT

Fonte: [BATCHPGT.NSP:27-156](legacy-sifap/natural-programs/BATCHPGT.NSP#L27). Incorpora as duas PDAs, LDASIFAP e auditoria; projeta os quatro DDMs.

| Formato | Variáveis de trabalho | Contexto |
|---|---|---|
| N8 | `#QTY-PROCESSED`, `#QTY-ERRS`, `#QTY-IGNORED`, `#QTY-GENERATED`, `#QTY-REJECT`, `#DT-TODAY`, `#NUM-BATCH` | Contadores, data e lote |
| P13.2 | `#AMT-TOT-GROSS`, `#AMT-TOT-DISC`, `#AMT-TOT-NET`, `#AMT-TOT-BONUS` | Totais |
| N6 / A6 | `#PERIOD`, `#SEQ-BATCH` / `#PERIOD-A` | Competência e sequência |
| N2 | `#MONTH`, `#NUM-DEPEND`, `#COD-REGION`, `#J` | Mês, quantidade, região e índice |
| N4 | `#YEAR`, `#YEAR-BIRTH`, `#QTY-REMAIN` | Anos e resto de contagem |
| P9.2 | `#AMT-BASE`, `#AMT-BENF`, `#AMT-GROSS`, `#AMT-DISC`, `#AMT-NET`, `#AMT-BONUS`, `#AMT-13`, `#INCOME` | Cálculo local, distinto dos retornos da PDA |
| N11 | `#AMT-TEMP` | Centavos inteiros |
| N3.4 | `#FACTOR-REGION`, `#FACTOR-FAMILY`, `#FACTOR-INCOME`, `#FACTOR-AGE`, `#FACTOR-ADJUST` | Fatores locais |
| N3 | `#AGE` | Idade |
| A1 | `#TYPE-PROG`, `#TYPE-PAYMENT`, `#STAT-PROG` | Classificações |
| L | `#ERR-CALC` | Controle |
| N15 / A15 | `#SEQ-PAYMENT` / `#SEQ-PAYMENT-A` | Sequência numérica e representação no extrato |
| A120 | `#MSG-LOG`, `#LOG-ERR` | Log/rejeição |
| A11 / A17 | `#CPF-PREV` / `#KEY-CPF-PERIOD` | CPF anterior e chave composta |
| A9 / N9 | `#AMT-NET-A` / `#QTY-QUOT` | Valor textual do extrato e quociente |
| A240 | `#REC-EXTRACT` | Registro do work file 1 |
| N3.4/1:27 | `#TAB-REGION` | Cópia local de fatores |
| P9.2/1:5 / N3.4/1:5 | `#INCOME-BAND` / `#BAND-FACTOR` | Tetos e multiplicadores |

### BATCHREL

Fonte: [BATCHREL.NSP:22-78](legacy-sifap/natural-programs/BATCHREL.NSP#L22). Incorpora LDASIFAP; projeta PAYMENT e BENEFIC.

| Formato | Variáveis de trabalho | Contexto |
|---|---|---|
| N6 / N8 | `#PERIOD` / `#DT-TODAY`, `#QTY-OVERALL` | Competência, data e quantidade |
| P13.2/1:5 | `#TOT-REGION-GROSS`, `#TOT-REGION-DISC`, `#TOT-REGION-NET`, `#TOT-STS-GROSS` | Acumuladores por grupo |
| N8/1:5 | `#QTY-REGION`, `#QTY-STS` | Quantidades por grupo |
| A15/1:5 | `#NAME-REGION`, `#NAME-STS` | Rótulos |
| P15.2 | `#TOT-OVERALL-GROSS`, `#TOT-OVERALL-DISC`, `#TOT-OVERALL-NET` | Totais gerais |
| N2 | `#IDX-REGION`, `#COD-REGION`, `#IDX-STS`, `#I`, `#LINE`, `#MAX-LINES` | Índices e paginação |
| A1 / L | `#STATUS` / `#FOUND` | Campos auxiliares declarados |
| A132 / N4 | `#LINE-REPORT` / `#PAGE` | Registro e página |
| P13.2 / N15 | `#AMT-ROUND` / `#AMT-TEMP` | Arredondamento e temporário |

### BATCHCON

Fonte: [BATCHCON.NSP:20-103](legacy-sifap/natural-programs/BATCHCON.NSP#L20). Incorpora LDASIFAP e auditoria; projeta PAYMENT e AUDIT, incluindo valores escalares anterior/novo.

| Formato | Variáveis de trabalho | Contexto |
|---|---|---|
| A240 | `#REC-CNAB` | Registro bancário |
| A3 / A4 / A1 | `#CNAB-BANK` / `#CNAB-BATCH` / `#CNAB-TYPE-REC` | Cabeçalho do registro |
| A11 / A10 | `#CNAB-CPF` / `#CNAB-NUM-DOC` | CPF e documento externo |
| A15 | `#CNAB-AMT`, `#AMT-STR` | Valor bancário textual |
| A8 | `#CNAB-DT-PAYMENT` | Data textual |
| A2 | `#CNAB-COD-RETURN`, `#COD-RETURN` | Retorno |
| N6 / A6 | `#PERIOD`, `#HR-CURRENT` / `#PERIOD-A` | Competência/hora e texto |
| N8 | `#DT-TODAY`, `#DT-PAYMENT-WK`, `#QTY-READ`, `#QTY-RECONCILED`, `#QTY-DIVERGENT`, `#QTY-NOT-FOUND`, `#QTY-AUDIT` | Datas e contadores |
| N7 | `#TIMN-AUX` | Tempo antes da conversão |
| A60 | `#FILE-RETURN`, `#AMT-PREV-STR`, `#AMT-NEW-STR` | Nome informado e valores de auditoria |
| N11 | `#CPF-NUM` | Conversão numérica |
| P9.2 | `#AMT-RETURN`, `#AMT-PAYMENT-SIFAP`, `#DIFF` | Valores e diferença |
| N15 | `#AMT-CENT`, `#NUM-PAYMENT`, `#SEQ-AUDIT` | Centavos e sequências |
| L / A80 / N2 | `#FOUND` / `#MSG` / `#I` | Controle, mensagem e índice |

## Cálculo

### CALCBENF

Fonte: [CALCBENF.NSN:16-93](legacy-sifap/natural-programs/CALCBENF.NSN#L16). Recebe PDACALC e incorpora LDASIFAP; projeta BENEFIC, PAYMENT e SOCPROG.

| Formato | Variáveis de trabalho | Contexto |
|---|---|---|
| N11 / A11 | `#CPF`, `#AMT-TEMP` / `#CPF-STR` | CPF/centavos e chave textual |
| N6 / N2 | `#PERIOD` / `#MONTH`, `#NUM-DEP`, `#COD-REGION`, `#J` | Competência, quantidades e índice |
| N4 / N3 | `#YEAR`, `#YEAR-BIRTH` / `#AGE` | Anos e idade |
| P9.2 | `#AMT-BASE`, `#AMT-BENF`, `#AMT-GROSS`, `#AMT-DISC`, `#AMT-NET`, `#AMT-BONUS`, `#AMT-13`, `#AMT-TOTAL`, `#INCOME` | Valores de trabalho |
| N3.4 | `#FACTOR-REGION`, `#FACTOR-FAMILY`, `#FACTOR-INCOME`, `#FACTOR-AGE`, `#FACTOR-ADJUST` | Fatores |
| A4 | `#COD-PROG` | Programa |
| A1 | `#TYPE-PROG`, `#STATUS-BENEF`, `#TYPE-PAYMENT` | Classificações |
| A78 / L | `#MSG` / `#ERR` | Mensagem e controle |
| N8 | `#DT-TODAY`, `#DT-BIRTH` | Datas |
| N3.4/1:27 | `#TAB-REGION` | Tabela local |
| P9.2/1:5 / N3.4/1:5 | `#INCOME-BAND` / `#BAND-FACTOR` | Faixas e fatores |

### CALCCORR

Fonte: [CALCCORR.NSP:12-82](legacy-sifap/natural-programs/CALCCORR.NSP#L12). Incorpora PDAVALID, LDASIFAP e auditoria; projeta PAYMENT e AUDIT.

| Formato | Variáveis de trabalho | Contexto |
|---|---|---|
| N11 / A11 | `#CPF`, `#AMT-TEMP` / `#CPF-STR` | Entrada, centavos e chave |
| N6 | `#PERIOD-START`, `#PERIOD-END`, `#PERIOD-CURRENT` | Competências |
| N8 | `#DT-TODAY` | Data |
| P9.2 / P11.2 | `#AMT-ORIG`, `#AMT-CORR`, `#AMT-DIFF` / `#AMT-TOTAL-CORRECTION` | Valores e total |
| N5.6 / N3.6 | `#INDEX-ACCUM` / `#INDEX-MONTH` | Índices |
| N2 / N4 | `#MONTH-REF`, `#K`, `#MONTH-C` / `#YEAR-REF`, `#YEAR-C` | Data e posição na matriz |
| N5 / A60 | `#QTY-REC` / `#MSG` | Contagem e mensagem |
| N3.6/1:12 | `#IPCA-TAB` | Array mensal declarado |
| N4/1:10 | `#YEAR-TAB` | Anos disponíveis |
| N3.6/1:10,1:12 | `#IPCA-YEAR` | Matriz anual/mensal |

### CALCDSCT

Fonte: [CALCDSCT.NSP:12-57](legacy-sifap/natural-programs/CALCDSCT.NSP#L12). Incorpora LDASIFAP; projeta PAYMENT com PE 1:8 e BENEFIC.

| Formato | Variáveis de trabalho | Contexto |
|---|---|---|
| N11 / A11 / N15 | `#CPF`, `#AMT-TEMP` / `#CPF-STR` / `#NUM-PAYMENT` | Documento, centavos e número de pagamento |
| P9.2 | `#AMT-GROSS`, `#AMT-TOTAL-DISC`, `#AMT-DISC-ITEM`, `#AMT-MAX-DISC` | Valores e teto |
| P3.2 / A1 | `#PCT-DISC` / `#TYPE-DISC` | Percentual e tipo local, menor que A3 da view |
| N2 | `#NUM-DISC`, `#INDEX`, `#K` | Quantidade e índices |
| N8 / N6 | `#DT-TODAY` / `#PERIOD` | Data e competência |
| L / A60 | `#FOUND` / `#MSG` | Controle e mensagem |
| P9.2/1:4 / N3.2/1:4 | `#BAND-CONTRIB` / `#RATE-CONTRIB` | Tetos e alíquotas |

## Validação

### VALBENEF

Fonte: [VALBENEF.NSN:15-71](legacy-sifap/natural-programs/VALBENEF.NSN#L15). Incorpora LDASIFAP; a view de BENEFIC é apenas declarada.

| Formato | Parâmetros/variáveis | Contexto |
|---|---|---|
| A11 / A60 | `#CPF-STR` / `#NAME` | Parâmetros IN |
| N8 / A1 / A2 | `#DT-BIRTH`, `#CEP` / `#SEX`, `#STATUS` / `#UF` | Parâmetros IN |
| A1 / N2 / A60/1:10 | `#RESULT` / `#QTY-ERRS` / `#MSG-ERR` | Parâmetros OUT |
| A11 | `#CPF` | Cópia local |
| L | `#UF-OK`, `#CPF-VALID`, `#DT-VALID`, `#NAME-VALID`, `#ALL-EQUAL`, `#HAS-SPACE` | Indicadores |
| N1/1:11 | `#DIG` | Dígitos |
| N5 / N3 / N1 | `#SUM` / `#REMAIN` / `#DV1`, `#DV2` | Cálculo de CPF |
| N2 | `#WEIGHT`, `#I`, `#MONTH`, `#DAY`, `#POS` | Pesos, posições e data |
| N4 | `#YEAR`, `#YEAR-CURRENT` | Anos |
| N2/1:12 | `#DAYS-MONTH` | Calendário local |
| A60 / A1 | `#NAME-TEMP` / `#CHAR` | Trabalho de nome |
| A2/1:27 | `#UF-TAB` | UFs |

### VALDOCS

Fonte: [VALDOCS.NSP:14-52](legacy-sifap/natural-programs/VALDOCS.NSP#L14). Incorpora PDAVALID; a view de BENEFIC é apenas declarada.

| Formato | Variáveis de trabalho | Contexto |
|---|---|---|
| N11 | `#CPF`, `#NIS` | Documentos numéricos |
| A15 / A12 | `#RG`, `#CTPS` / `#TITLE` | Documentos adicionais |
| A1 / A60/1:5 | `#RESULT` / `#MSG` | Resultado e mensagens |
| N2 | `#QTY-ERRS`, `#I`, `#RG-LEN`, `#WEIGHT` | Contagem, índice, comprimento e peso |
| L | `#CPF-OK`, `#RG-OK`, `#DOC-SPECIAL-OK` | Indicadores independentes |
| A3 / A3/1:8 | `#PREFIX-CPF` / `#PREFIX-SPECIAL` | Prefixo e tabela |
| A11 / N1/1:11 | `#CPF-STR` / `#DIG` | Texto e dígitos |
| N5 / N3 / N1 | `#SUM` / `#REMAIN` / `#DV1`, `#DV2` | Cálculo |

### VALELEG

Fonte: [VALELEG.NSN:15-66](legacy-sifap/natural-programs/VALELEG.NSN#L15). Recebe PDACALC e incorpora LDASIFAP; projeta BENEFIC e SOCPROG.

| Formato | Variáveis de trabalho | Contexto |
|---|---|---|
| A11 / A4 | `#CPF-STR` / `#COD-PROG` | Chaves |
| L / A60/1:10 | `#ELIGIBLE`, `#ELIG-OK` / `#REASON` | Resultado e motivos |
| N2 | `#QTY-REASON`, `#NUM-DEP`, `#COD-REGION`, `#I` | Contagem, região e índice |
| N3 / N4 | `#AGE`, `#AGE-MIN`, `#AGE-MAX` / `#YEAR-BIRTH`, `#YEAR-CURRENT` | Idades e anos |
| P9.2 / P7.2 | `#INCOME` / `#MAX-INCOME` | Renda recebida/lida e teto per capita |
| A5 | `#COD-ELIG` | Código posicional |
| A1 | `#TYPE-PROG`, `#STATUS-BENEF`, `#DOCS-OK`, `#STAT-PROG` | Indicadores |
| A78 | `#MSG` | Mensagem local |

### SUBVALCP e SUBVALNI

SUBVALCP recebe PDAVALID e declara exatamente o conjunto de trabalho de CCVALCPF registrado acima: [SUBVALCP.NSN:28-42](legacy-sifap/natural-programs/SUBVALCP.NSN#L28).

SUBVALNI recebe a mesma PDA e acrescenta os campos de [SUBVALNI.NSN:38-50](legacy-sifap/natural-programs/SUBVALNI.NSN#L38):

| Formato | Variáveis | Comentário/contexto |
|---|---|---|
| A11 | `#NIS-STR` | Entrada textual |
| N1/1:11 | `#NIS-DIG` | Dígitos |
| N1/1:10 | `#NIS-WEIGHT` | Inicializado com 3,2,9,8,7,6,5,4,3,2 |
| N5 | `#NIS-SUM`, `#NIS-QUOT` | Soma e quociente |
| N2 | `#NIS-REMAIN`, `#NIS-IDX` | Resto e índice |
| N1 | `#NIS-DV` | Verificador |

## Consultas e relatórios

### CONSBENF

Fonte: [CONSBENF.NSP:18-104](legacy-sifap/natural-programs/CONSBENF.NSP#L18). Incorpora PDAVALID, LDASIFAP e auditoria; projeta BENEFIC, PAYMENT e AUDIT.

| Formato | Variáveis de trabalho | Contexto |
|---|---|---|
| N11 | `#CPF-SEARCH`, `#NIS-SEARCH`, `#CPF-NUM` | Pesquisas e conversão |
| A1 / A11 | `#TYPE-SEARCH` / `#CPF-A11`, `#CPF-STR` | Tipo e chaves |
| A14 / A80 / A60 / A15 | `#CPF-MASK` / `#ADDRESS` / `#MSG` / `#STATUS-DESCR` | Apresentação |
| N3 | `#I`, `#MAX-HIST`, `#QTY-HIST` | Índice e limites; MAX-HIST anotado como obsoleto |
| N6/1:12 | `#HIST-PERIOD` | Histórico declarado |
| P9.2/1:12 | `#HIST-GROSS`, `#HIST-NET` | Valores históricos declarados |
| A1/1:12 | `#HIST-STS`, `#HIST-TYPE` | Situação/tipo históricos declarados |
| A3 / A2 | `#CPF-P1`, `#CPF-P2`, `#CPF-P3` / `#CPF-P4` | Componentes da máscara |

### RELPGT

Fonte: [RELPGT.NSP:17-72](legacy-sifap/natural-programs/RELPGT.NSP#L17). Incorpora LDASIFAP; projeta PAYMENT e BENEFIC.

| Formato | Variáveis de trabalho | Contexto |
|---|---|---|
| N6 | `#PERIOD-START`, `#PERIOD-END` | Intervalo |
| N4 / A4 | `#COD-PROG-FILTER`, `#PAGE` / `#COD-PROG-A4`, `#PROG-PREV` | Filtro, página e controle de quebra |
| N8 | `#DT-TODAY`, `#QTY-REC`, `#QTY-SUB` | Data e contagens |
| N2 | `#LINE`, `#MAX-LINES` | Paginação |
| P13.2 | `#TOT-GROSS`, `#TOT-DISC`, `#TOT-NET`, `#TOT-BONUS`, `#SUB-GROSS`, `#SUB-NET` | Totais |
| A30 / A2 | `#NAME-BENEF` / `#UF-BENEF` | Nome abreviado e UF |
| A14 / A11 | `#CPF-MASK` / `#CPF-STR` | Máscara e CPF |
| A8 | `#TYPE-DESCR`, `#STATUS-DESCR` | Rótulos |
| A100 / A80 | `#SEP-100` / `#SEP-DASH80`, `#SEP-EQUAL80` | Separadores |

### RELAUDIT

Fonte: [RELAUDIT.NSP:18-66](legacy-sifap/natural-programs/RELAUDIT.NSP#L18). Incorpora LDASIFAP; projeta AUDIT sem os grupos MU de antes/depois.

| Formato | Variáveis de trabalho | Contexto |
|---|---|---|
| N8 | `#DT-START`, `#DT-END`, `#DT-TODAY`, `#QTY-TOTAL`, `#QTY-DISPLAYED`, `#QTY-FILTERED`, `#QTY-DAY`, `#QTY-INSERT`, `#QTY-UPDATE`, `#QTY-QUERY`, `#QTY-RECONCIL`, `#QTY-DIVERG`, `#QTY-OTHERS` | Datas e contadores |
| A2 / A8 / A4 | `#ACTION-FILTER` / `#USER-FILTER`, `#HR-FORMAT` / `#TABLE-FILTER` | Filtros e hora formatada |
| A1 | `#TYPE-OUTPUT` | T tela, I impressora no comentário |
| N4 / N2 | `#PAGE` / `#LINE`, `#MAX-LINES`, `#I` | Paginação/índice |
| A20 / A6 | `#ACTION-DESCR` / `#HR-STR` | Descrição e hora antes da formatação |
| A100 / A120 | `#SEP-100` / `#SEP-120` | Separadores |

## Conferência de leitura

- [x] Tipos, comprimentos e dimensões dos parâmetros e variáveis de trabalho foram registrados.
- [x] Campos compartilhados têm contrato explícito e chamadores identificados.
- [x] Views apenas declaradas foram diferenciadas de acessos efetivos.
- [ ] Conversões numéricas, comportamento de cursores e efeitos transacionais foram verificados em runtime Natural; não há execução disponível nesta sessão.

### Continue lendo

| Anterior | Próximo |
|---|---|
| [Inventário](inventory.md) | [Catálogo de regras](business-rules-catalog.md) |
