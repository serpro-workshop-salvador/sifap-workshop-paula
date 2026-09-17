# Decisões de escopo — Estágio 2

> **Trilha:** [Kit do Time](../README.md) › [Estágio 2](README.md) › **Decisões de escopo**

**Decisões de paula sobre a consulta de programa por código e os quatro contextos do destino, mantendo explícitos os adiamentos e as questões abertas.**

| Campo | Valor |
|---|---|
| **Público-alvo** | paula, acumulando os papéis de requisitos, arquitetura e implementação |
| **Finalidade** | Apoiar a conversa do estágio; não substitui os artefatos formais do Spec-Kit |
| **Feature relacionada** | `001-program-query`: consulta de programa por código |
| **Registro** | 2026-09-17; elaboração autorizada para o caminho com programa encontrado, sem conclusão do H2 |

> [!NOTE]
> Os entregáveis formais permanecem em `specs/<NNN>-<feature>/spec.md`, `plan.md` e `tasks.md`. Não registre requisitos EARS completos aqui. Este arquivo registra somente decisões de escopo e questões em aberto.

## Entrada da especificação EARS

**Correção após a solicitação de paula em 2026-09-17:** em resposta à proposta de `001-program-query` e à confirmação do comportamento para programa encontrado, paula solicitou "faça as correcoes". Essa autorização permite elaborar o recorte apresentado, não responder às demais questões nem aprovar a especificação completa.

| Entrada | Evidência atual | Pendência |
|---|---|---|
| Regra selecionada | Item 49 do [catálogo](../01-archaeology/business-rules-catalog.md#regras-de-cadprognsp), restrito ao programa encontrado e aos seis campos apresentados. A autorização humana para especificar esse recorte é distinta da corroboração documental usada na classificação histórica. | Revisar a redação EARS produzida. O item 55 permanece Mistério; os itens de cadastro 2, 4 e 7 continuam fora da funcionalidade. |
| Identificador da feature | `001-program-query`, adotado no contexto da solicitação de correção. | Sem pendência de identificação para este rascunho. |
| Branch de especificação | A branch observada é `portugues-br`; o fluxo formal prevê `spec/001-program-query` criada de `develop`. | Regularizar o fluxo conforme [00-GIT-WORKFLOW.md](../00-GIT-WORKFLOW.md) antes da integração. A edição PT-BR não é integrada em `develop` ou `main`, que permanecem em inglês. A preparação documental local não comprova a execução do fluxo Git. |

A [origem do item 49](../01-archaeology/legacy-sifap/natural-programs/CADPROG.NSP#L156) foi conferida: para um programa encontrado, a rotina apresenta código, nome, tipo, valor-base armazenado, código de elegibilidade e situação, sem recalcular o valor-base. Esse é o limite da elaboração autorizada. Normalização da entrada, representação da saída e programa ausente continuam nas questões abaixo; ausência permanece no recorte aprovado, com comportamento pendente de validação.

A especificação permanece parcial enquanto essas questões não forem validadas. Não foi fornecida justificativa confirmada para capacidade `[GREENFIELD]`. Nenhuma branch, fonte legada ou política de negócio foi alterada nesta correção.

---

## Decisões de escopo

| Decisão | Evidência ou justificativa | Impacto nos artefatos formais |
|---|---|---|
| Manter a consulta de programa por código como fatia atual | [Aceite H1](../01-archaeology/discovery-report.md#revisão-h1-guiada) e ramo C de [CADPROG](../01-archaeology/legacy-sifap/natural-programs/CADPROG.NSP#L89) | Especificar consulta, projeção e ausência; não ampliar para cadastro ou processamento financeiro |
| Adotar Beneficiários, Programas Sociais, Pagamentos e Auditoria no Monólito Modular | paula respondeu "sim" à recomendação em 2026-09-17; [avaliação das hipóteses](bounded-contexts.md#avaliação-das-hipóteses) e [ADR-0003](../docs/adr/0003-sifap-bounded-contexts.md) | Posicionar a consulta em Programas Sociais; um proprietário lógico por DDM no destino; demais contextos orientam capacidades futuras |
| Usar interfaces em processo para comunicação entre módulos | [Comunicação documentada](bounded-contexts.md#comunicação-entre-contextos) | Não criar HTTP entre módulos nem acesso a repositórios alheios; detalhar os contratos executáveis na especificação da capacidade correspondente |
| Preservar os seis campos apresentados pela consulta legada, sem recalcular o valor-base | [QUERY-PROG](../01-archaeology/legacy-sifap/natural-programs/CADPROG.NSP#L156) e recorte aprovado | A projeção contém código, nome, tipo, valor-base armazenado, código de elegibilidade e situação; parâmetros adicionais não entram automaticamente na resposta |
| Manter inclusão/alteração, regras financeiras, folha, conciliação, migração física e mudanças de política de auditoria adiadas | [Adiamentos do H1](../01-archaeology/discovery-report.md#4-hipóteses-de-fatiamento-recomendadas) | Não gerar tarefas de implementação dessas capacidades por constarem no mapa de destino |
| Separar aceite arquitetural de aprovação de requisitos e de H2 | Limites aceitos; regras controversas e contratos executáveis ainda pendentes | Preparar os artefatos formais e sua revisão antes de iniciar implementação; não encerrar questões por inferência |

---

## Questões em aberto

| Questão | Fonte consultada | Próxima pessoa responsável |
|---|---|---|
| Como normalizar e validar o código recebido pela consulta moderna, preservando a conversão N4 para A4? | [CADPROG: formatação EM=9999](../01-archaeology/legacy-sifap/natural-programs/CADPROG.NSP#L157) | paula, antes da implementação da consulta |
| Qual contrato testável representa programa não encontrado e erros de entrada? | [CADPROG: teste do contador após a busca](../01-archaeology/legacy-sifap/natural-programs/CADPROG.NSP#L166); item 55 do [catálogo](../01-archaeology/business-rules-catalog.md#regras-de-cadprognsp) | paula, na especificação da fatia; a semântica Natural ainda requer caracterização |
| Como representar tipo, situação e valor-base na resposta sem acrescentar interpretação ou fórmula? | [Campos apresentados](../01-archaeology/legacy-sifap/natural-programs/CADPROG.NSP#L159) e [estrutura de SOCPROG](../01-archaeology/data-map.md#estruturas-de-socprog) | paula, na definição e revisão do contrato da consulta |
| Quem numera e persiste pagamentos, qual algoritmo prevalece e qual atomicidade é necessária? | [Questões financeiras do relatório](../01-archaeology/discovery-report.md#31-questões-em-aberto-aguardando-validação-humana) | paula, antes de incluir capacidades financeiras no escopo |
| Qual política de auditoria rege ações, consultas, filtros e confirmação transacional? | [Registro de questões](../01-archaeology/mysteries-found.md) e [limites de Auditoria](bounded-contexts.md#auditoria) | paula, antes de modificar essas capacidades; o mapa não decide a política |

O aceite dos contextos não resolve as perguntas acima nem associa os IDs canônicos dos mistérios. As pendências financeiras e de auditoria não ampliam a fatia atual; permanecem vinculadas às capacidades adiadas.

---

### Continue lendo

| Anterior | Próximo |
|---|---|
| [Guia do Estágio 2](GUIDE.md)<br/><sub>Especificação moderna passo a passo.</sub> | [Template de ADR](ADR-TEMPLATE.md)<br/><sub>Registre a decisão de escopo como uma ADR.</sub> |

<sub>[Voltar ao índice do kit](../README.md)</sub>
