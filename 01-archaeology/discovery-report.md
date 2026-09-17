# Relatório de Descoberta — Estágio 1: Arqueologia Digital

> **Trilha:** [Kit do Time](../README.md) › [Estágio 1](README.md) › **Relatório de Descoberta**

**Relatório da arqueologia individual de paula.** Consolida a investigação de todo o acervo e separa a entrega documental do aceite para o Estágio 2.

| Campo | Valor |
|---|---|
| **Público-alvo** | paula, acumulando as cinco áreas de responsabilidade |
| **Pré-requisitos** | Catálogo de regras, mapa de dependências e glossário preenchidos |
| **Estágio** | Estágio 1 — Arqueologia |
| **Resultado esperado** | Documento de até 3 páginas com resumo, hipóteses de fatiamento e artefatos de origem |

> [!IMPORTANT]
> **Aceite H1 individual do recorte registrado em 2026-09-17.** paula confirmou a consulta de programa por código como próxima fatia, com os adiamentos descritos na seção 4. Esse aceite não associa os IDs canônicos, não resolve as perguntas abertas e não comprova as verificações técnicas ainda não realizadas.

> [!NOTE]
> Guia passo a passo: [`GUIDE.md`](GUIDE.md).

**Responsável:** paula. **Modalidade:** individual. **Data da síntese:** 2026-09-17.
**Edição:** português do Brasil. **Apoio à investigação:** agente archaeologist do GitHub Copilot.

---

## 1. Resumo executivo

O acervo do SIFAP, Sistema de Fiscalização e Administração de Pagamentos, teve leitura assistida dos 15 programas atribuídos, nove membros de apoio, quatro DDMs e da FDT fornecida, conforme o [inventário](inventory.md).
O [catálogo](business-rules-catalog.md) registra candidatos e confrontos com origem, dos quais apenas três itens possuem corroboração documental restrita, sem aprovação de regras de negócio.
O [mapa](dependency-map.md) registra 28 nós e 80 arestas estáticas, incluindo nove chamadas externas e acesso compartilhado aos arquivos Adabas.
O principal risco para a especificação é tomar contratos divergentes de validação, cálculo e persistência como uma única regra já decidida, como mostram as [questões abertas](mysteries-found.md).
paula deu aceite individual ao recorte de consulta de programa por código em 2026-09-17; a associação dos vinte IDs, as decisões sobre perguntas abertas e as verificações não executadas permanecem explicitamente separadas desse aceite.

---

## 2. O que sabemos (confirmado)

### 2.1 Regras de negócio

“Confirmada” é usada no sentido documental do prompt, não como aprovação humana. As divergências de algoritmo, idade mínima e auditoria não foram promovidas.

| Item do catálogo | Candidata EARS restrita | Apoio documental |
|---|---|---|
| [2](business-rules-catalog.md#regras-de-cadbenefnsp) | SE o CPF informado for zero, ENTÃO o sistema DEVE recusar o cadastro. | RN-001, seção 1.1: obrigatoriedade de CPF válido |
| [4](business-rules-catalog.md#regras-de-cadbenefnsp) | SE a validação local sinalizar CPF inválido, ENTÃO o sistema DEVE recusar o cadastro. | RN-001, seção 1.1: não comprova a correção do algoritmo local |
| [7](business-rules-catalog.md#regras-de-cadbenefnsp) | SE a data de nascimento for zero, ENTÃO o sistema DEVE recusar o cadastro. | RN-006, seção 1.1: somente obrigatoriedade, não idade mínima |

São candidatas de descoberta, sem REQ-ID; requisitos formais pertencem ao Estágio 2 após a validação de fonte e escopo.

### 2.2 Dependências

O [mapa de dependências](dependency-map.md) contém 9 CALLNAT, 9 INCLUDE, 23 USING, 3 invocações por JCL e 36 arestas Adabas que agrupam 49 instruções. Os 36 PERFORM estão resolvidos separadamente para rotinas locais ou copycodes. Todos os destinos literais de chamada, inclusão e área existem no acervo; comentários de agendamento não foram tratados como chamadas executáveis.

### 2.3 Estruturas de dados

O [mapa de dados](data-map.md) documenta BENEFIC/150, SOCPROG/151, PAYMENT/152 e AUDIT/153, com chaves, formatos, domínios, grupos PE/MU e descritores. As relações são lógicas e apoiadas em acessos, não FKs demonstradas. A FDT de 150 foi confrontada com BENEFIC; diferenças físicas/lógicas e arquivos históricos de auditoria sem DDM local permanecem como perguntas. Estatísticas e datas das listagens não são medições atuais, conforme a [cronologia](legacy-sifap/CHRONOLOGY.md).

---

## 3. O que é arriscado

### 3.1 Questões em aberto aguardando validação humana

Três perguntas do [registro completo](mysteries-found.md) destacadas para a revisão individual, sem substituir as demais:

| Questão em aberto | Evidência (`path:line`) | Impacto | Hipótese (não confirmada) | Pessoa/área responsável | Status |
|---|---|---|---|---|---|
| Qual implementação de validação de CPF deve servir de referência para o cadastro e seus chamadores? | [CADBENEF.NSP:344-413](legacy-sifap/natural-programs/CADBENEF.NSP#L344), [CCVALCPF.NSC:39-130](legacy-sifap/natural-programs/CCVALCPF.NSC#L39), [VALBENEF.NSN:196-281](legacy-sifap/natural-programs/VALBENEF.NSN#L196) | Equivalência das entradas aceitas | Não confirmada; sem hipótese registrada | paula | aberta |
| Quem deve numerar e persistir o pagamento na cadeia BATCHPGT/CALCBENF? | [CALCBENF.NSN:308-320](legacy-sifap/natural-programs/CALCBENF.NSN#L308), [BATCHPGT.NSP:473-489](legacy-sifap/natural-programs/BATCHPGT.NSP#L473), [PAYMENT.ddm:34](legacy-sifap/adabas-ddms/PAYMENT.ddm#L34) | Unicidade e atomicidade da geração | Não confirmada; sem hipótese registrada | paula | aberta |
| Eventos EX devem ser omitidos mesmo quando a pessoa pede explicitamente esse filtro? | [RELAUDIT.NSP:130-141](legacy-sifap/natural-programs/RELAUDIT.NSP#L130), [AUDIT.ddm:42](legacy-sifap/adabas-ddms/AUDIT.ddm#L42) | Completude da consulta de auditoria | Não confirmada; sem hipótese registrada | paula | aberta |

### 3.2 Regras com evidência fraca

Os demais comportamentos inferidos do [catálogo](business-rules-catalog.md) não são requisitos aprovados. Entre os riscos registrados estão cursores sem registros, precisão de restos/decimais, ordenação de subtotais, domínios regionais e de situação, índices retroativos e commit separado de arquivo/auditoria. O [registro](mysteries-found.md) conserva essas perguntas; o [placar](mysteries-checklist.md) não tem associações canônicas validadas.

---

## 4. Hipóteses de fatiamento recomendadas

São hipóteses de agrupamento para o arquiteto avaliar, não decisões de arquitetura. O [grafo](dependency-map.md) mostra compartilhamento de dados, portanto não demonstra módulos já desacoplados.

| Hipótese | Programas | DDMs relacionados | Justificativa |
|---|---|---|---|
| 1. Cadastro e programas | CADBENEF, CADDEPEN, CADPROG | BENEFIC, SOCPROG, AUDIT | Concentram inclusão/alteração e seus vínculos com validação e auditoria |
| 2. Elegibilidade e determinação de valores | VALBENEF, VALDOCS, VALELEG, CALCBENF, SUBVALCP, SUBVALNI | BENEFIC, SOCPROG, PAYMENT | Agrupam contratos de validação/cálculo, com escrita de CALCBENF ainda a discutir |
| 3. Ciclo de pagamentos | BATCHPGT, BATCHCON, CALCDSCT, CALCCORR | PAYMENT, BENEFIC, SOCPROG, AUDIT | Compartilham competência, valores, retorno bancário e transações |
| 4. Consulta e prestação de informações | CONSBENF, BATCHREL, RELPGT, RELAUDIT | BENEFIC, PAYMENT, AUDIT | Agrupam projeções e filtros; CONSBENF também escreve auditoria |

**Fatia aprovada por paula em 2026-09-17:** consulta de programa por código, ramo C de CADPROG, usando os campos de SOCPROG já apresentados pelo legado ([itens 49 e 55](business-rules-catalog.md#regras-de-cadprognsp)). **Fora desse recorte, adiado:** inclusão/alteração, regras financeiras, folha, conciliação, migração física e mudanças de política de auditoria. O aceite foi fornecido explicitamente na conversa H1 individual.

As três regras corroboradas de cadastro da seção 2.1 não são a especificação dessa consulta. O recorte escolhido usa as evidências dos itens 49 e 55, incluindo o caminho sem programa encontrado; o aceite de escopo não promove interpretações pendentes a requisitos aprovados.

---

## 5. Artefatos de origem

| Artefato | Caminho | Status |
|---|---|---|
| Inventário e catálogo de membros | [inventory.md](inventory.md) | Leitura estática 24/24 membros e 5/5 artefatos Adabas |
| Regras e tipos | [business-rules-catalog.md](business-rules-catalog.md), [reading-notes.md](reading-notes.md) | Extração registrada; validação de negócio pendente |
| Dependências | [dependency-map.md](dependency-map.md), [dependency-map.mmd](dependency-map.mmd) | Origens e destinos conferidos; renderização visual pendente |
| Dados | [data-map.md](data-map.md) | DDMs/FDT documentados; medição de origem não realizada |
| Questões e placar | [mysteries-found.md](mysteries-found.md), [mysteries-checklist.md](mysteries-checklist.md) | Todas as perguntas têm paula como responsável; associação canônica e hipóteses não informadas |
| Glossário | [glossary.md](glossary.md) | 36 termos, com evidência e status |

---

## 6. Fechamento individual

| Entrega do agente | Estado documental | Referência |
|---|---|---|
| Glossário | 36 termos registrados com origem e status | Seção 5 |
| Catálogo de programas | 15 atribuídos e nove de apoio, com finalidade candidata e leitura | Inventário |
| Mapa de dados | Quatro DDMs e uma FDT documentados | Mapa de dados |
| Grafo de chamadas | Origens e destinos documentados; verificação visual não realizada | Mapa de dependências |
| Rascunho de regras | Todos os programas cobertos; candidatos separados de perguntas | Catálogo e notas |
| Registro de questões | Perguntas de todas as áreas com evidência, impacto, responsável e status; IDs ainda sem associação humana | Registro e placar |
| Síntese para transição | Relatório preenchido, com recorte e adiamentos aceitos por paula | Este relatório |

**Não falta investigação atribuída a outra pessoa.** A decisão de paula sobre o recorte está registrada. A associação das perguntas aos IDs canônicos ainda não foi informada; o aceite do recorte não representa validação de vinte mistérios nem resolução de todas as regras controversas do SIFAP.

### Revisão H1 guiada

1. O agente apresentou o fechamento documental, as pendências e o recorte de consulta de programa por código para confirmação individual.
2. paula respondeu: "confirmo dou o aceite", em 2026-09-17. O recorte e seus adiamentos ficam registrados como aceitos.
3. As perguntas sem validação permanecem abertas. A correspondência com os IDs canônicos e a classificação de bônus continuam sem informação fornecida por paula.
4. Este relatório registra o aceite para uso na transição ao agente de arquitetura, sem criar requisitos formais nem iniciar implementação neste estágio.

**Aceite de paula:** recebido em 2026-09-17 para o recorte do H1 individual. **Fonte do aceite:** mensagem "confirmo dou o aceite", em resposta à confirmação da consulta de programa por código. **Confiança declarada por paula:** não informada; não foi inferida a partir do aceite.

### Limites das verificações

Diagnósticos do editor e conferência estática de fontes/referências foram realizados. Compilação Natural, testes de equivalência, CI e medição de população atual não foram executados; não são substitutos da descoberta nem se tornam pendências de outra dupla. A renderização Mermaid e a paginação impressa exigidas pelos prompts continuam não verificadas porque não há ferramenta de renderização disponível nesta sessão.

---

## Definição de pronto

- [x] Resumo executivo com cinco frases.
- [x] Quatro hipóteses documentadas, sem decisões de arquitetura.
- [x] Artefatos de origem preenchidos e com status explícito.
- [x] Modalidade individual e responsabilidade de paula registradas em todo o escopo.
- [x] paula deu aceite ao recorte de consulta de programa por código no H1 individual em 2026-09-17.
- [ ] paula informou a correspondência das perguntas aos IDs canônicos.
- [ ] Paginação impressa menor que três páginas e renderização Mermaid conferidas.

---

### Continue lendo

| Anterior | Próximo |
|---|---|
| [GUIDE do Estágio 1](GUIDE.md)<br/><sub>Cronograma passo a passo.</sub> | [Estágio 2 — Especificação moderna](../02-modern-spec/README.md)<br/><sub>Handoff H1 e início do EARS.</sub> |

<sub>[Voltar ao índice do kit](../README.md)</sub>
