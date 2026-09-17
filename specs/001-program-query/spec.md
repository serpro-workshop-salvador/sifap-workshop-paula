# Especificação: consulta de programa por código

> **Trilha:** [Kit do Time](../../README.md) > [Especificações](../README.md) > **001-program-query**

**Especificação parcial da consulta de um programa social encontrado pelo código, preservando os seis campos apresentados pelo legado.**

| Campo | Valor |
|---|---|
| Feature | `001-program-query` |
| Responsável | paula, em execução individual |
| Data | 2026-09-17 |
| Estágio | Estágio 2: especificação |
| Status | Rascunho parcial; requisito proposto para revisão, sem autorização de implementação |
| Contexto | Programas Sociais, conforme [ADR-0003](../../docs/adr/0003-sifap-bounded-contexts.md) |
| Edição e fluxo Git | PT-BR em `portugues-br`; preparação da branch formal `spec/001-program-query` a partir de `develop` ainda não realizada |

## Escopo e confirmação do recorte

A [decisão H1](../../01-archaeology/discovery-report.md#revisão-h1-guiada) seleciona consulta de programa por código, incluindo o caminho de ausência. Este rascunho especifica o caminho com programa encontrado; não retira programa ausente da funcionalidade, mas mantém seu comportamento pendente de validação.

Após a proposta do identificador e do comportamento do caminho encontrado, paula solicitou "faça as correcoes". O [registro de escopo](../../02-modern-spec/scope-decisions.md#entrada-da-especificação-ears) delimita a autorização de elaboração aos seis campos, sem recálculo do valor-base. Isso não aprova regras financeiras, normalização, respostas de erro ou a redação final desta especificação.

O item 49 do [catálogo](../../01-archaeology/business-rules-catalog.md#regras-de-cadprognsp) conserva sua classificação documental Inferida. A confirmação humana restrita para especificação está [registrada separadamente](../../01-archaeology/business-rules-catalog.md#validação-do-recorte-para-especificação); não foi inventada corroboração histórica. O item 55 permanece Mistério.

| Incluído neste rascunho | Adiado ou ainda não definido |
|---|---|
| Consulta de um programa encontrado pelo código | Normalização e validação da entrada |
| Projeção dos seis valores lidos, sem novo cálculo do valor-base | Programa ausente, erros e representação externa dos valores |
| Rastreabilidade do comportamento até a origem legada | Inclusão/alteração, fórmulas, folha, conciliação, migração física e mudanças de política de auditoria |

Não há capacidade `[GREENFIELD]` neste rascunho. Nenhum endpoint, status HTTP, prazo de resposta ou dependência tecnológica é definido por suposição.

## Evidência revisada

O [ramo C](../../01-archaeology/legacy-sifap/natural-programs/CADPROG.NSP#L89) chama `QUERY-PROG` e sai antes da inclusão. A [rotina](../../01-archaeology/legacy-sifap/natural-programs/CADPROG.NSP#L156) busca o programa pelo código e apresenta os campos abaixo a partir do registro encontrado.

| Dado apresentado | Campo de origem em SOCPROG | Uso nesta especificação |
|---|---|---|
| Código do programa | `COD-PROGRAM` | Identifica o programa encontrado |
| Nome | `NAME-PROGRAM` | Apresenta o nome armazenado |
| Tipo | `TYPE-PROGRAM` | Preserva o valor do campo, sem atribuir uma nova descrição |
| Valor-base | `AMT-BASE-INDIVIDUAL` | Apresenta o valor armazenado, sem aplicar ajuste na consulta |
| Código de elegibilidade | `COD-ELIGIBILITY` | Apresenta o código, sem executar avaliação de elegibilidade |
| Situação | `STAT-PROGRAM` | Preserva o valor do campo, sem reinterpretar seu domínio |

Os formatos da entrada e da resposta moderna não decorrem automaticamente dos formatos Natural. O requisito trata os valores apresentados; a representação desses valores permanece uma questão de contrato.

## Requisito EARS

### REQ-001: Apresentar o programa encontrado

QUANDO uma pessoa consultar pelo código um programa social existente, o SIFAP DEVE apresentar os dados desse programa: código, nome, tipo, valor-base armazenado sem recálculo, código de elegibilidade e situação.

source_legacy: 01-archaeology/legacy-sifap/natural-programs/CADPROG.NSP#L156-L165

- Padrão EARS: orientado a evento.
- Regra de origem: item 49, restrito ao caminho com programa encontrado, com autorização humana de elaboração registrada no catálogo e no escopo.
- Status: proposed; a revisão deste texto permanece pendente.

**Critérios de aceitação (Dado/Quando/Então):**

- **AC-001.1:** Dado um programa social existente com código e seis campos conhecidos, Quando uma pessoa consultar o programa por esse código, Então a apresentação conterá o código, o nome, o tipo, o valor-base, o código de elegibilidade e a situação correspondentes ao registro encontrado.
- **AC-001.2:** Dado um programa social existente com valor-base armazenado conhecido, Quando uma pessoa consultar esse programa pelo código, Então o valor-base apresentado será igual ao armazenado, sem aplicação de fator ou novo cálculo durante a consulta.

Esses critérios não pressupõem entradas inválidas aceitas, normalização específica, um formato JSON ou uma resposta para ausência. O segundo critério verifica a preservação do valor-base, não a correção da fórmula que o produziu.

## Matriz de rastreabilidade

| REQ-ID | Padrão EARS | source_legacy | Regra de origem | Arquivo de origem |
|---|---|---|---|---|
| REQ-001 | Orientado a evento | [CADPROG.NSP](../../01-archaeology/legacy-sifap/natural-programs/CADPROG.NSP#L156), intervalo 156 a 165 | Item 49, recorte encontrado; registro de autorização humana para elaboração | [business-rules-catalog.md](../../01-archaeology/business-rules-catalog.md#validação-do-recorte-para-especificação) |

## Questões em aberto

Nenhuma pergunta desta seção é requisito ou critério de aceitação. Não foi alterado o status dos registros de origem nem atribuída correspondência a IDs canônicos.

### Pendências da consulta

Estas perguntas vêm das [decisões de escopo](../../02-modern-spec/scope-decisions.md#questões-em-aberto), não representam questões já resolvidas pelo aceite arquitetural.

| Questão em aberto | Evidência (`path:line`) | Impacto | Hipótese (não confirmada) | Pessoa responsável | Status |
|---|---|---|---|---|---|
| Como normalizar e validar o código recebido pela consulta moderna, preservando a conversão N4 para A4? | [CADPROG.NSP:157](../../01-archaeology/legacy-sifap/natural-programs/CADPROG.NSP#L157) | Formatos de entrada aceitos e correspondência com a chave pesquisada | Não confirmada; sem hipótese registrada | paula | aberta |
| Qual contrato testável representa programa não encontrado e erros de entrada? | [CADPROG.NSP:166](../../01-archaeology/legacy-sifap/natural-programs/CADPROG.NSP#L166), item 55 do catálogo | Completude da consulta e seus critérios de erro; programa ausente continua no recorte | Não confirmada; sem hipótese registrada | paula | aberta |
| Como representar tipo, situação e valor-base na resposta sem acrescentar interpretação ou fórmula? | [CADPROG.NSP:159](../../01-archaeology/legacy-sifap/natural-programs/CADPROG.NSP#L159) e [estrutura de SOCPROG](../../01-archaeology/data-map.md#estruturas-de-socprog) | Contrato externo e testes de representação dos valores | Não confirmada; sem hipótese registrada | paula | aberta |

### Questões preservadas do Estágio 1

Os registros abaixo foram copiados do [registro de questões](../../01-archaeology/mysteries-found.md#cadastro), preservando pergunta, evidência, impacto, hipótese, responsável e status. Os caminhos relativos foram ajustados à localização desta especificação.

| ID | Questão em aberto | Evidência (`path:line`) | Impacto | Hipótese (não confirmada) | Pessoa/área responsável | Status |
|---|---|---|---|---|---|---|
| A atribuir | Qual relação existe entre a constante 0.347215, o fator local e o campo persistido FACTOR-K? | [CADPROG.NSP:124-138](../../01-archaeology/legacy-sifap/natural-programs/CADPROG.NSP#L124), [SOCPROG.ddm:47-52](../../01-archaeology/legacy-sifap/adabas-ddms/SOCPROG.ddm#L47) | Interpretação do valor-base | Não confirmada; sem hipótese registrada | paula | aberta |
| A atribuir | Quais ajustes devem ocorrer na inclusão do programa e no cálculo posterior do benefício? | [CADPROG.NSP:124-138](../../01-archaeology/legacy-sifap/natural-programs/CADPROG.NSP#L124), [CALCBENF.NSN:259-266](../../01-archaeology/legacy-sifap/natural-programs/CALCBENF.NSN#L259) | Equivalência financeira | Não confirmada; sem hipótese registrada | paula | aberta |

Essas duas perguntas contextualizam o valor-base armazenado. Não justificam recalculá-lo na consulta nem ampliar a fatia para inclusão ou cálculo de benefício. As demais questões do acervo permanecem no registro de origem, fora desta especificação.

## Verificação e próximos passos

- [x] Identificador da feature e recorte de elaboração registrados.
- [x] Um requisito proposto com padrão EARS, fonte legada existente e critérios observáveis.
- [x] Matriz relaciona o requisito ao item e ao registro de autorização de elaboração.
- [x] Questões não validadas preservadas fora dos requisitos, sem mudança de status.
- [ ] paula revisou a redação do requisito e dos critérios de aceitação.
- [ ] Normalização, programa ausente e representação externa esclarecidos para completar a consulta.
- [ ] Fluxo formal de branches e destino de idioma regularizados antes da integração.
- [ ] Validação de rastreabilidade na CI e caracterização do comportamento executadas.

Este arquivo segue o formato de `/write-ears-spec` no diretório da feature. Não foram executados a CLI do Spec-Kit, programas Natural ou CI, nem criados plano, tarefas ou código. A preparação documental em PT-BR não comprova que a branch de especificação foi criada de `develop`; esta edição não será integrada em `develop` ou `main`, que permanecem em inglês.

### Continue lendo

| Anterior | Próximo |
|---|---|
| [Decisões de escopo](../../02-modern-spec/scope-decisions.md) | [Fluxo do Spec-Kit](../../09-cheat-sheets/spec-kit-workflow.md) |

<sub>[Voltar ao índice do kit](../../README.md)</sub>
