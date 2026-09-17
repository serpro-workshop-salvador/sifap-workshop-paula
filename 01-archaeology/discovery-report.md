# Relatório de Descoberta — Estágio 1: Arqueologia Digital

> **Trilha:** [Kit do Time](../README.md) › [Estágio 1](README.md) › **Relatório de Descoberta**

**Artefato preenchido pelo time ao fim do Estágio 1.** Consolida os achados da arqueologia e é a entrada principal do Estágio 2.

| Campo | Valor |
|---|---|
| **Público-alvo** | Todas as duplas — consolidação ao fim do Estágio 1 |
| **Pré-requisitos** | Catálogo de regras, mapa de dependências e glossário preenchidos |
| **Estágio** | Estágio 1 — Arqueologia |
| **Resultado esperado** | Documento de até 3 páginas com resumo, hipóteses de fatiamento e artefatos de origem |

> [!IMPORTANT]
> Os artefatos da investigação estática estão preenchidos, mas a passagem H1 não está aprovada. IDs canônicos, hipóteses de negócio, leitura humana e escopo final precisam de confirmação da equipe. Nenhuma pergunta foi encerrada pelo assistente.

> [!NOTE]
> Guia passo a passo: [`GUIDE.md`](GUIDE.md).

**Time:** a informar pela equipe. **Data da síntese:** 2026-09-17.
**Edição:** português do Brasil. **Participantes/revisores humanos:** a informar.

---

## 1. Resumo executivo

O acervo do SIFAP, Sistema de Fiscalização e Administração de Pagamentos, teve leitura assistida dos 15 programas atribuídos, nove membros de apoio, quatro DDMs e da FDT fornecida, conforme o [inventário](inventory.md).
O [catálogo](business-rules-catalog.md) registra candidatos e confrontos com origem, dos quais apenas três itens possuem corroboração documental restrita, sem aprovação de regras de negócio.
O [mapa](dependency-map.md) registra 28 nós e 80 arestas estáticas, incluindo nove chamadas externas e acesso compartilhado aos arquivos Adabas.
O principal risco para a especificação é tomar contratos divergentes de validação, cálculo e persistência como uma única regra já decidida, como mostram as [questões abertas](mysteries-found.md).
A confiança e a aprovação da equipe ainda não foram fornecidas, e não houve execução Natural, inspeção do banco atual nem validação dos vinte mistérios canônicos.

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

Três perguntas do [registro completo](mysteries-found.md) destacadas para a conversa de transição, sem substituir as demais:

| Questão em aberto | Evidência (`path:line`) | Impacto | Hipótese (não confirmada) | Pessoa/área responsável | Status |
|---|---|---|---|---|---|
| Qual implementação de validação de CPF deve servir de referência para o cadastro e seus chamadores? | [CADBENEF.NSP:344-413](legacy-sifap/natural-programs/CADBENEF.NSP#L344), [CCVALCPF.NSC:39-130](legacy-sifap/natural-programs/CCVALCPF.NSC#L39), [VALBENEF.NSN:196-281](legacy-sifap/natural-programs/VALBENEF.NSN#L196) | Equivalência das entradas aceitas | Não confirmada; não fornecida pela equipe | A designar: Duplas 1 e 4 | aberta |
| Quem deve numerar e persistir o pagamento na cadeia BATCHPGT/CALCBENF? | [CALCBENF.NSN:308-320](legacy-sifap/natural-programs/CALCBENF.NSN#L308), [BATCHPGT.NSP:473-489](legacy-sifap/natural-programs/BATCHPGT.NSP#L473), [PAYMENT.ddm:34](legacy-sifap/adabas-ddms/PAYMENT.ddm#L34) | Unicidade e atomicidade da geração | Não confirmada; não fornecida pela equipe | A designar: Duplas 2, 3 e 4 | aberta |
| Eventos EX devem ser omitidos mesmo quando a pessoa pede explicitamente esse filtro? | [RELAUDIT.NSP:130-141](legacy-sifap/natural-programs/RELAUDIT.NSP#L130), [AUDIT.ddm:42](legacy-sifap/adabas-ddms/AUDIT.ddm#L42) | Completude da consulta de auditoria | Não confirmada; não fornecida pela equipe | A designar: Dupla 5 | aberta |

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

**Fatia sugerida, não aprovada:** consulta de programa por código, ramo C de CADPROG, usando os campos de SOCPROG já apresentados pelo legado ([itens 49 e 55](business-rules-catalog.md#regras-de-cadprognsp)). **Adiado nessa hipótese:** inclusão/alteração, regras financeiras, folha, conciliação, migração física e mudanças de política de auditoria. O PO confirma ou substitui essa proposta no H1.

---

## 5. Artefatos de origem

| Artefato | Caminho | Status |
|---|---|---|
| Inventário e catálogo de membros | [inventory.md](inventory.md) | Leitura estática 24/24 membros e 5/5 artefatos Adabas |
| Regras e tipos | [business-rules-catalog.md](business-rules-catalog.md), [reading-notes.md](reading-notes.md) | Extração registrada; validação de negócio pendente |
| Dependências | [dependency-map.md](dependency-map.md), [dependency-map.mmd](dependency-map.mmd) | Origens e destinos conferidos; renderização visual pendente |
| Dados | [data-map.md](data-map.md) | DDMs/FDT documentados; medição de origem não realizada |
| Questões e placar | [mysteries-found.md](mysteries-found.md), [mysteries-checklist.md](mysteries-checklist.md) | Perguntas abertas; IDs e hipóteses humanas pendentes |
| Glossário | [glossary.md](glossary.md) | 36 termos, com evidência e status |

---

## 6. Aprovação do time

- Revisado por: a informar pela equipe.
- Data de aprovação: pendente.
- Confiança da equipe: a informar, alta/média/baixa.
- Decisão de escopo e conversa H1: pendentes.
- Verificação disponível: diagnósticos do editor e conferência estática de fontes/referências. Compilação Natural, testes de equivalência, CI e renderização Mermaid/impressão não foram executados nesta sessão.

---

## Definição de pronto

- [x] Resumo executivo com cinco frases.
- [x] Quatro hipóteses documentadas, sem decisões de arquitetura.
- [x] Artefatos de origem preenchidos e com status explícito.
- [ ] Equipe validou leitura, IDs canônicos, perguntas e escopo.
- [ ] Paginação impressa menor que três páginas e renderização Mermaid conferidas pela equipe.

---

### Continue lendo

| Anterior | Próximo |
|---|---|
| [GUIDE do Estágio 1](GUIDE.md)<br/><sub>Cronograma passo a passo.</sub> | [Estágio 2 — Especificação moderna](../02-modern-spec/README.md)<br/><sub>Handoff H1 e início do EARS.</sub> |

<sub>[Voltar ao índice do kit](../README.md)</sub>
