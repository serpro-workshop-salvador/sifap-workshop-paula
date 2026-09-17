# Glossário do SIFAP Legado

> **Trilha:** [Kit do Time](../README.md) › [Estágio 1](README.md) › **Glossário**

**Glossário da execução individual de paula no Estágio 1.** Registra os termos selecionados na leitura Natural/Adabas e separa significados literais de interpretações ainda não validadas.

| Campo | Valor |
|---|---|
| **Público-alvo** | paula, responsável pela revisão de todas as áreas |
| **Pré-requisitos** | Abrir os arquivos `.NSN` e `.ddm` atribuídos |
| **Estágio** | Estágio 1 — Arqueologia |
| **Resultado esperado** | 30 termos ou mais, com programa de origem e status CONFIRMADO/HIPÓTESE |

> [!NOTE]
> Guia passo a passo: [`GUIDE.md`](GUIDE.md).

---

## Por que o glossário importa

Sistemas legados têm vocabulário próprio, raramente documentado em um lugar acessível — ele vive em nomes de variável, abreviações de campo e comentários de código. Se o time do Estágio 2 não souber o que significam `DSCT`, `BENF`, `PE` ou `CTC`, vai escrever uma especificação baseada em suposições sobre esses termos.

O glossário transforma abreviações de 3 a 6 caracteres em uma linguagem ubíqua compartilhada pelo time inteiro — e dá a base para os nomes de entidades e atributos do modelo de domínio no Estágio 3.

**Erro comum:** marcar um termo como CONFIRMADO sem evidência literal no código ou na documentação histórica. Se você inferiu o significado pelo contexto, marque como HIPÓTESE e identifique quem é responsável pela validação.

---

## Como preencher

| Coluna | O que registrar |
|---|---|
| **Termo** | A abreviação ou sigla exatamente como aparece no código. |
| **Expansão** | O significado completo do termo. |
| **Programa** | O arquivo `.NSN` ou `.ddm` onde o termo foi encontrado. |
| **Contexto** | Explicação breve de como e onde o termo é usado. |
| **Status** | `CONFIRMADO` — evidência literal no código ou na documentação. `HIPÓTESE` — inferido do contexto e aguardando validação. |

### Dica de extração com o modo Ask do GitHub Copilot

Antes de usar o prompt abaixo, cole no chat o conteúdo de 2 a 3 arquivos `.NSN`:

> "Liste todas as abreviações e siglas usadas neste código Natural. Para cada uma, sugira a expansão e marque como 'CONFIRMADO' ou 'HIPÓTESE'."

Compare a sugestão do Copilot com o que você observou diretamente no código. Se coincidirem, registre como CONFIRMADO; caso contrário, registre como HIPÓTESE.

---

## Termos encontrados

| # | Termo | Expansão | Programa | Contexto | Status |
|---|---|---|---|---|---|
| 1 | BENEFIC | Cadastro de beneficiários | [BENEFIC.ddm:31](legacy-sifap/adabas-ddms/BENEFIC.ddm#L31) | DDM do arquivo 150; não confundir nome lógico com número físico | CONFIRMADO |
| 2 | NUM-CPF | CPF sem formatação | [BENEFIC.ddm:40](legacy-sifap/adabas-ddms/BENEFIC.ddm#L40) | Chave alfanumérica A11, com descritor único | CONFIRMADO |
| 3 | NUM-NIS | NIS/PIS-PASEP | [BENEFIC.ddm:52](legacy-sifap/adabas-ddms/BENEFIC.ddm#L52) | N11, único e sujeito à supressão de nulos | CONFIRMADO |
| 4 | STAT-BENEFICIARY | Situação do beneficiário | [BENEFIC.ddm:74-75](legacy-sifap/adabas-ddms/BENEFIC.ddm#L74) | A ativo, S suspenso, C cancelado, I inativo, D desligado, conforme o DDM | CONFIRMADO |
| 5 | COD-PROGRAM | Código de programa social | [SOCPROG.ddm:28](legacy-sifap/adabas-ddms/SOCPROG.ddm#L28) | A4 único na tabela de programas | CONFIRMADO |
| 6 | GRP-DEPEND | Grupo de dependentes | [BENEFIC.ddm:87](legacy-sifap/adabas-ddms/BENEFIC.ddm#L87) | Grupo periódico de dez ocorrências; capacidade não equivale ao limite de negócio | CONFIRMADO |
| 7 | QTY-DEPEND | Quantidade de dependentes ativos | [BENEFIC.ddm:81](legacy-sifap/adabas-ddms/BENEFIC.ddm#L81) | Descrição do campo N2; concordância com as ocorrências precisa ser verificada | CONFIRMADO |
| 8 | RELATION | Código de parentesco | [BENEFIC.ddm:91-92](legacy-sifap/adabas-ddms/BENEFIC.ddm#L91), [CADDEPEN.NSP:152-156](legacy-sifap/natural-programs/CADDEPEN.NSP#L152) | Conjuntos de códigos divergem; revisão de paula na área de cadastro | HIPÓTESE |
| 9 | AMT-FAMILY-INCOME | Renda familiar declarada | [BENEFIC.ddm:78](legacy-sifap/adabas-ddms/BENEFIC.ddm#L78) | Valor total em decimal compactado, distinto do campo per capita | CONFIRMADO |
| 10 | IND-PERCAP-INCOME | Renda per capita calculada | [BENEFIC.ddm:79-80](legacy-sifap/adabas-ddms/BENEFIC.ddm#L79) | O DDM distingue membros da família, renda total e renda per capita | CONFIRMADO |
| 11 | COD-REGION | Código de região | [BENEFIC.ddm:66](legacy-sifap/adabas-ddms/BENEFIC.ddm#L66), [LDASIFAP.NSL:34-46](legacy-sifap/natural-programs/LDASIFAP.NSL#L34) | DDM e tabelas locais têm domínios distintos; revisão de paula nas áreas batch e dados | HIPÓTESE |
| 12 | IND-DOCS-OK | Indicador de documentação regular | [BENEFIC.ddm:83](legacy-sifap/adabas-ddms/BENEFIC.ddm#L83), [VALELEG.NSN:196-200](legacy-sifap/natural-programs/VALELEG.NSN#L196) | Valores S/N; responsabilidade de preenchimento ainda em aberto | HIPÓTESE |
| 13 | AMT-BASE-INDIVIDUAL | Base mensal por pessoa | [SOCPROG.ddm:41](legacy-sifap/adabas-ddms/SOCPROG.ddm#L41) | Campo P7,2 usado no cálculo; o cadastro aplica ajuste antes de gravá-lo | CONFIRMADO |
| 14 | FACTOR-ADJUST | Fator de ajuste sobre a base | [SOCPROG.ddm:52](legacy-sifap/adabas-ddms/SOCPROG.ddm#L52) | Campo BH, distinto de BG FACTOR-K | CONFIRMADO |
| 15 | FACTOR-K | Fator especial de correção | [SOCPROG.ddm:47-51](legacy-sifap/adabas-ddms/SOCPROG.ddm#L47) | Significado indicado como não documentado; validar com a coordenação de negócio | HIPÓTESE |
| 16 | GRP-CALC-BAND | Faixas de cálculo | [SOCPROG.ddm:69-74](legacy-sifap/adabas-ddms/SOCPROG.ddm#L69) | Cinco ocorrências com limites, multiplicador, adicional e acumulação | CONFIRMADO |
| 17 | YEAR-MONTH-REF | Competência do pagamento | [PAYMENT.ddm:38](legacy-sifap/adabas-ddms/PAYMENT.ddm#L38) | N6 em formato YYYYMM; não é a data de execução | CONFIRMADO |
| 18 | NUM-PAYMENT | Número de pagamento | [PAYMENT.ddm:34](legacy-sifap/adabas-ddms/PAYMENT.ddm#L34) | N15 único; distinto do ISN físico | CONFIRMADO |
| 19 | AMT-GROSS | Valor bruto | [PAYMENT.ddm:43](legacy-sifap/adabas-ddms/PAYMENT.ddm#L43) | Campo P9,2 | CONFIRMADO |
| 20 | AMT-DISC-TOTAL | Total de descontos | [PAYMENT.ddm:45](legacy-sifap/adabas-ddms/PAYMENT.ddm#L45) | Campo P7,2; possui precisão diferente do bruto | CONFIRMADO |
| 21 | AMT-NET | Valor líquido | [PAYMENT.ddm:44](legacy-sifap/adabas-ddms/PAYMENT.ddm#L44) | Descrito como bruto menos desconto; não é cálculo automático demonstrado pelo DDM | CONFIRMADO |
| 22 | AMT-BONUS | Valor adicional/abono | [PAYMENT.ddm:46](legacy-sifap/adabas-ddms/PAYMENT.ddm#L46) | Campo de valor, separado do tipo do pagamento | CONFIRMADO |
| 23 | TYPE-PAYMENT | Tipo de pagamento | [PAYMENT.ddm:79-80](legacy-sifap/adabas-ddms/PAYMENT.ddm#L79), [PDACALC.NSA:75](legacy-sifap/natural-programs/PDACALC.NSA#L75) | N/R/A/C no DDM e N/D/T na PDA; revisão de paula nas áreas de pagamentos e dados | HIPÓTESE |
| 24 | GRP-DISC | Descontos discriminados | [PAYMENT.ddm:50-56](legacy-sifap/adabas-ddms/PAYMENT.ddm#L50) | PE de oito itens com tipo, valor, percentual, processo e vigência | CONFIRMADO |
| 25 | COD-BANK-RETURN | Código de retorno bancário | [PAYMENT.ddm:98](legacy-sifap/adabas-ddms/PAYMENT.ddm#L98) | A2, descrito como retorno CNAB 240 | CONFIRMADO |
| 26 | IND-CORR | Indicador de correção | [PAYMENT.ddm:105](legacy-sifap/adabas-ddms/PAYMENT.ddm#L105), [CALCCORR.NSP:186-188](legacy-sifap/natural-programs/CALCCORR.NSP#L186) | S/N; o caminho de correção ignora registros já marcados S | CONFIRMADO |
| 27 | NUM-AUDIT | Número de evento de auditoria | [AUDIT.ddm:31](legacy-sifap/adabas-ddms/AUDIT.ddm#L31) | Sequência N15 única | CONFIRMADO |
| 28 | COD-ACTION | Natureza do evento | [AUDIT.ddm:39-49](legacy-sifap/adabas-ddms/AUDIT.ddm#L39), [RELAUDIT.NSP:163-182](legacy-sifap/natural-programs/RELAUDIT.NSP#L163) | CO/CN/DV têm usos divergentes; revisão de paula nas áreas de conciliação e relatórios | HIPÓTESE |
| 29 | COD-PROFILE | Perfil do usuário | [AUDIT.ddm:76](legacy-sifap/adabas-ddms/AUDIT.ddm#L76) | ADM/OPR/CON/AUD/SUP; existência não comprova preenchimento | CONFIRMADO |
| 30 | GRP-BEFORE / GRP-AFTER | Grupos de valores anterior e posterior | [AUDIT.ddm:61-70](legacy-sifap/adabas-ddms/AUDIT.ddm#L61) | Grupos simples com listas MU; valores escalares coexistem | CONFIRMADO |
| 31 | DDM | Data Definition Module | [BENEFIC.ddm:31-34](legacy-sifap/adabas-ddms/BENEFIC.ddm#L31) | Visão lógica com nomes longos usada por Natural | CONFIRMADO |
| 32 | FDT | Field Definition Table | [FDT-150-BENEFICIARY.txt:8-14](legacy-sifap/adabas-ddms/FDT-150-BENEFICIARY.txt#L8) | Estrutura física do arquivo, com nomes curtos | CONFIRMADO |
| 33 | PE | Grupo periódico | [FDT-150-BENEFICIARY.txt:99-102](legacy-sifap/adabas-ddms/FDT-150-BENEFICIARY.txt#L99) | Conjunto repetido de campos relacionados | CONFIRMADO |
| 34 | MU | Campo multivalorado | [FDT-150-BENEFICIARY.txt:99-102](legacy-sifap/adabas-ddms/FDT-150-BENEFICIARY.txt#L99) | Várias ocorrências de um campo, distinto de PE | CONFIRMADO |
| 35 | SUPER-CPF-PERIOD | Superdescritor CPF + competência | [PAYMENT.ddm:127-128](legacy-sifap/adabas-ddms/PAYMENT.ddm#L127) | A17 composto por AB e AE; usado para consultar geração existente | CONFIRMADO |
| 36 | PDA | Área de dados de parâmetros | [PDAVALID.NSA:43-57](legacy-sifap/natural-programs/PDAVALID.NSA#L43) | Contrato compartilhado de entradas e saídas, não uma rotina executável | CONFIRMADO |

> [!NOTE]
> Nesta tabela, CONFIRMADO significa apenas significado literal sustentado pelo acervo. Não aprova uma regra de negócio nem encerra um mistério. paula é responsável pela revisão de todas as HIPÓTESES; trabalhar individualmente não transforma uma hipótese em fato.

---

## Definição de pronto

- [x] 36 termos registrados, superando o mínimo do agente e a meta deste modelo.
- [x] Todo termo tem fonte e linha de origem.
- [x] Todo termo tem status CONFIRMADO ou HIPÓTESE.
- [x] As hipóteses estão explicitamente encaminhadas à validação humana.
- [ ] paula aprovou o vocabulário necessário ao recorte do Estágio 2.

---

### Continue lendo

| Anterior | Próximo |
|---|---|
| [GUIDE do Estágio 1](GUIDE.md)<br/><sub>Cronograma passo a passo.</sub> | [Relatório de Descoberta](discovery-report.md)<br/><sub>Consolidação final do estágio.</sub> |

<sub>[Voltar ao índice do kit](../README.md)</sub>
