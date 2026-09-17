# Checklist de Exploração do Legado

> **Trilha:** [Kit do Time](../README.md) › [Estágio 1](README.md) › **Checklist de Exploração**

**Gate obrigatório antes do Estágio 2.** Nesta execução individual, paula cobre todos os programas e mantém a rastreabilidade das regras candidatas até o código legado.

| Campo | Valor |
|---|---|
| **Público-alvo** | paula, responsável pelo escopo completo |
| **Pré-requisitos** | Acesso a `legacy-sifap/natural-programs/` e `adabas-ddms/` |
| **Tempo estimado** | Preenchido ao longo dos 90 minutos |
| **Estágio** | Estágio 1 — Arqueologia |
| **Resultado esperado** | Cobertura individual de todas as áreas e critérios de conclusão verificáveis |

**Aplicação individual:** as cinco duplas da tabela representam somente a distribuição original dos assuntos. paula acumula os papéis; o H1 é uma revisão guiada entre paula e o agente, com registro da decisão antes de mudar de estágio. Isso não dispensa evidências, não confirma hipóteses e não autoriza o agente a aprovar o estágio em nome da participante.

> [!IMPORTANT]
> **Gate obrigatório antes do Estágio 2.** Nenhum requisito EARS é aceito sem referência a um programa Natural ou arquivo DDM. Requisitos greenfield (sem equivalente no legado) precisam ser marcados com `[GREENFIELD]` e justificados por escrito na spec.

> [!WARNING]
> Na edição anterior da imersão, vários times pularam a exploração do legado e escreveram specs baseadas apenas no briefing de modernização. O resultado foram especificações que não preservavam as regras de negócio reais dos 29 anos do SIFAP como Sistema de Fiscalização e Administração de Pagamentos. Este gate é obrigatório.

---

## 1. A regra de rastreabilidade

Todo `REQ-ID` em `specs/<NNN>-<feature>/spec.md` precisa ter uma linha `source_legacy:` apontando para uma destas opções:

- um membro Natural, como `.NSP` ou `.NSN`, em `01-archaeology/legacy-sifap/natural-programs/` (de preferência com intervalo de linhas);
- um arquivo `.ddm` específico em `01-archaeology/legacy-sifap/adabas-ddms/`;
- `[GREENFIELD]` com uma justificativa de uma linha.

O CI rejeita PRs para `develop` se algum `REQ-ID` estiver sem a linha `source_legacy:`. Os facilitadores fazem verificações por amostragem durante o handoff H2, às 15:00.

---

## 2. Os 15 programas Natural — quem lê o quê

paula cobre os 15 programas, organizados nos cinco grupos originais. O [inventário](inventory.md) registra a leitura assistida integral, e as [notas de tipos](reading-notes.md) documentam os respectivos DEFINE DATA.

| Área original | Programas a ler | Mistérios | Por quê |
|---|---|---|---|
| **1 · Visão** (PO + RE) | `CADBENEF.NSP`, `CADDEPEN.NSP`, `CADPROG.NSP` | `SIFAP-M-01` … `M-04` | Lógica de cadastro — entidades centrais que viram sujeitos EARS. |
| **2 · Arquitetura** (EA + SA) | `BATCHPGT.NSP`, `BATCHREL.NSP`, `BATCHCON.NSP` | `SIFAP-M-05` … `M-08` | Fluxos batch revelam fronteiras de módulo (bounded contexts). |
| **3 · Implementação** (TL + Dev) | `CALCBENF.NSN`, `CALCCORR.NSP`, `CALCDSCT.NSP`\* | `SIFAP-M-09` … `M-12` | Os cálculos são onde o código moderno vai viver; o time precisa reproduzi-los. |
| **4 · Qualidade** (DBA + QA) | `VALBENEF.NSN`, `VALDOCS.NSP`, `VALELEG.NSN` | `SIFAP-M-13` … `M-16` | Validações viram testes; o DBA também mapeia os campos dos DDMs. |
| **5 · Operações** (DevOps + TW) | `CONSBENF.NSP`, `RELPGT.NSP`, `RELAUDIT.NSP` | `SIFAP-M-17` … `M-20` | Caminhos de leitura alimentam o glossário e o runbook. |

\* `CALCDSCT.NSP` é **leitura de apoio** para a Dupla 3: nenhum mistério canônico mora nele. Ainda assim vale perguntar por que ele existe e quem o chama.

> [!IMPORTANT]
> **São 20 mistérios canônicos, 4 por dupla** — essa é a única meta numérica do Estágio 1. Os IDs e as áreas estão em [`mysteries-checklist.md`](mysteries-checklist.md); registre-os em [`mysteries-found.md`](mysteries-found.md). Achados fora da lista contam como bônus e **não** mudam o denominador.

### Conferência documental por programa

As fontes e seus cabeçalhos permanecem somente para leitura. Para cada programa, os artefatos de apoio são:

- [x] **Identificação e leitura:** os 24 membros estão no [inventário](inventory.md); autoria e datas são consultadas na [cronologia](legacy-sifap/CHRONOLOGY.md), sem atribuições inferidas pelo primeiro nome.
- [x] **Entradas e saídas:** o [mapa de dependências](dependency-map.md) distingue as operações efetivas por DDM das views apenas declaradas.
- [x] **Chamadas:** o mapa registra `CALLNAT`, `INCLUDE`, `USING`, rotinas internas e JCLs com suas origens.
- [x] **Regras candidatas:** o [catálogo](business-rules-catalog.md) contém as quinze seções de programas com evidência e classificação.
- [ ] **Aceite da leitura:** paula confirmou a revisão das evidências necessárias ao recorte escolhido.

> [!WARNING]
> Uma linha sem `Programa de origem` não sustenta um requisito EARS.

---

## 3. Os 4 DDMs — mapeamento de campos

paula responde pela leitura dos dados e pelo confronto com os programas. O planejamento do destino continua pertencendo aos estágios seguintes.

| DDM | Responsável | Evidência do Estágio 1 |
|---|---|---|
| BENEFIC | paula | [Mapa de dados](data-map.md#estruturas-de-benefic), incluindo confronto com a FDT |
| PAYMENT | paula | [Mapa de dados](data-map.md#estruturas-de-payment) |
| SOCPROG | paula | [Mapa de dados](data-map.md#estruturas-de-socprog) |
| AUDIT | paula | [Mapa de dados](data-map.md#estruturas-de-audit) |

Revise os DDMs necessários à feature selecionada. O mapeamento completo para PostgreSQL pertence ao planejamento e à implementação; não é pré-requisito para começar a spec.

---

## 4. Registro de questões em aberto

Use [`mysteries-checklist.md`](mysteries-checklist.md) para registrar questões em aberto sem antecipar respostas. O registro é um catálogo de incertezas, não um gabarito nem uma fonte de regras.

Registre em `mysteries-found.md` apenas as questões que afetam o escopo. Cada registro precisa conter:

| Campo | Descrição |
|---|---|
| Questão em aberto | Texto da pergunta, sem conclusão |
| Evidência | `path:line` |
| Impacto | Efeito sobre o escopo |
| Hipótese | Explicitamente marcada como não confirmada |
| Responsável | Pessoa ou área que pode validar |
| Status | `aberta` / `aguardando validação humana` / `fechada após validação humana` |

Uma questão só pode ser fechada ou usada como base para uma regra depois de validação humana explícita, apoiada na evidência registrada.

---

## 5. Verificação antes de abrir o Estágio 2

Na revisão H1 individual, paula confere esta matriz com o apoio do agente. A inexistência de grupo não é um bloqueio; ausência de evidência ou aprovação não recebida continua registrada como tal.

| Verificação | Evidência atual | Aceite |
|---|---|---|
| Leitura | Acervo completo coberto no inventário e nas notas | Confirmação individual de paula pendente |
| Cronologia | Cronologia canônica vinculada; divergências mantidas no registro | Não foram criadas datas ou autorias para preencher lacunas |
| Regras | Quinze seções com origens e classificações no catálogo | Conteúdo documental entregue; regras não aprovadas automaticamente |
| Escopo | Consulta de programa por código selecionada, com adiamentos explícitos | Aceite de paula em 2026-09-17, registrado no [relatório](discovery-report.md#revisão-h1-guiada) |
| Questões | Perguntas, evidências e responsável individual registrados | Não é necessário resolver todas para documentar a descoberta; os IDs não podem ser inventados |

Verificações de execução Natural, medidas da população atual e desenho PostgreSQL não fazem parte da conclusão documental desta arqueologia. A renderização Mermaid e a paginação impressa continuam como verificações técnicas não realizadas, sem substituir o conteúdo já conferido por leitura.

---

## 6. Formato obrigatório do Estágio 2

Escreva EARS apenas em `specs/<NNN>-<feature>/spec.md`, usando o Spec-Kit. Todo `REQ-ID` precisa de um padrão EARS, critérios Given/When/Then e `source_legacy:`. Não conclua nenhum requisito até o time confirmar a fonte ou a justificativa greenfield.

---

### Continue lendo

| Anterior | Próximo |
|---|---|
| [GUIDE do Estágio 1](GUIDE.md)<br/><sub>Cronograma cronometrado.</sub> | [Templates](templates/)<br/><sub>Modelos preenchíveis para os artefatos do estágio.</sub> |

<sub>[Voltar ao índice do kit](../README.md)</sub>
