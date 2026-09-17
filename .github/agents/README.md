# Índice de agentes

Este diretório contém os agentes personalizados do GitHub Copilot da imersão: **5** no total, cada um em seu próprio `<name>.agent.md`.

> [!NOTE]
> O Copilot descobre arquivos `*.agent.md` em `.github/agents/`. Chame um agente pelo seu `name` com `@<name>` (por exemplo, `@archaeologist`). O `name` também vincula prompts: um arquivo `*.prompt.md` seleciona seu agente pela chave `agent:` do frontmatter, então o identificador de um agente é um contrato, não um rótulo.

## O modelo de duas camadas

O kit separa **quando** você está trabalhando de **qual papel** você exerce.

| Camada | Primitiva | Como carrega | Para que serve |
|---|---|---|---|
| **Estágio** — a fase em que toda a equipe está | Agente, chamado com `@name` | Você seleciona deliberadamente, uma vez por estágio | Um estágio é um ritual compartilhado, com início, definição de pronto e passagem de bastão |
| **Papel** — a responsabilidade que é sua | Habilidade (skill), em [`../skills/`](../skills/) | Carrega sozinha, a partir da sua `description` | Você leva seu papel para todos os estágios; ninguém deveria precisar lembrar de reselecioná-lo |

Uma exceção continua sendo agente: o **`dba`**. O ciclo de vida dos dados atravessa
os quatro estágios em vez de morar dentro de um só, então não pode ser um agente de
estágio, e ele possui prompts com escopo de ferramentas que uma habilidade não
consegue vincular. Todos os demais papéis da equipe são habilidades.

> [!TIP]
> Mantenha o agente do estágio selecionado o dia inteiro e deixe a habilidade do seu
> papel se compor com ele. Selecionar `@builder` e pedir lacunas de cobertura carrega
> o papel de QA sozinho.

## Agentes de estágio

Quatro agentes sequenciais, um por estágio da imersão. Eles se encadeiam pela chave `handoffs:` do frontmatter: `archaeologist -> architect -> builder` passam o bastão para o próximo; o agente terminal do Estágio 4 (`evolution`) não tem sucessor.

| Estágio | Agente | Chamada | Prompts vinculados | Descrição |
| --- | --- | --- | --- | --- |
| Estágio 1 | [`archaeologist`](archaeologist.agent.md) | `@archaeologist` | 5 | Lê código Natural/Adabas legado, extrai regras de negócio, mapeia dependências e registra perguntas em aberto |
| Estágio 2 | [`architect`](architect.agent.md) | `@architect` | 16 | Define contextos delimitados, escreve especificações EARS, gera ADRs e projeta uma arquitetura de Monólito Modular |
| Estágio 3 | [`builder`](builder.agent.md) | `@builder` | 19 | Traduz Natural para Java, gera JPA a partir de FDTs, escreve testes de equivalência e cria REST + Next.js |
| Estágio 4 | [`evolution`](evolution.agent.md) | `@evolution` | 16 | Escreve GitHub Issues para o agente de codificação, revisa PRs geradas por IA, fecha o arco com uma capacidade greenfield e valida CI/IaC |

## Agente transversal

| Agente | Chamada | Prompts vinculados | Descrição |
| --- | --- | --- | --- |
| [`dba`](dba.agent.md) | `@dba` | 4 | Descoberta de dados no Adabas, prontidão da origem, migração e conciliação para PostgreSQL, evolução segura de esquema e auditoria de consultas baseada em evidência |

## Habilidades que substituíram os agentes de persona

Nove agentes de persona e três especialistas foram convertidos em habilidades. Os
comandos de barra não mudaram; mudou apenas o agente que os hospeda.

| Agente anterior | Agora esta habilidade | Prompts migraram para |
| --- | --- | --- |
| `product-owner` | [`persona-product-owner`](../skills/persona-product-owner/SKILL.md) | `@architect` e `@evolution` para aceitação |
| `requirements-engineer` | [`persona-requirements-engineer`](../skills/persona-requirements-engineer/SKILL.md) | `@architect` |
| `enterprise-architect` | [`persona-enterprise-architect`](../skills/persona-enterprise-architect/SKILL.md) | `@architect` |
| `software-architect` | [`persona-software-architect`](../skills/persona-software-architect/SKILL.md) | `@architect` |
| `tech-lead` | [`persona-technical-lead`](../skills/persona-technical-lead/SKILL.md) | `@builder` |
| `implementer` | [`persona-developer`](../skills/persona-developer/SKILL.md) | `@builder` |
| `qa-engineer` | [`persona-qa-engineer`](../skills/persona-qa-engineer/SKILL.md) | `@builder` |
| `devops-engineer` | [`persona-devops-engineer`](../skills/persona-devops-engineer/SKILL.md) | `@evolution` |
| `tech-writer` | [`persona-tech-writer`](../skills/persona-tech-writer/SKILL.md) | `@evolution` |
| `se-ux-ui-designer` | [`ux-research-design`](../skills/ux-research-design/SKILL.md) | não possuía prompts |
| `expert-react-frontend-engineer` | [`react-nextjs-frontend`](../skills/react-nextjs-frontend/SKILL.md) | não possuía prompts |
| `java-mcp-expert` | [`java-mcp-server-generator`](../skills/java-mcp-server-generator/SKILL.md) | não possuía prompts |

A justificativa e os compromissos assumidos estão registrados no [ADR-0002](../../docs/adr/0002-team-roles-as-skills-not-agents.md).

## Propriedade dos prompts

Os 60 prompts em [`../prompts/`](../prompts/) se vinculam a um agente pela chave `agent:`:

- Todos os **60** apontam para um dos **5** agentes acima; nenhum prompt ficou no agente embutido genérico `agent: "agent"`. As contagens por agente estão nas colunas **Prompts vinculados**.
- Um prompt cujo trabalho pertence a um papel da equipe abre seu corpo carregando a habilidade daquele papel, de modo que o conhecimento do papel viaja junto com a tarefa.

Recalcule as contagens com `grep -h '^agent:' ../prompts/*.prompt.md | sort | uniq -c`.

## Regra de manutenção

- Renomear um agente quebra silenciosamente **todos** os prompts vinculados a ele por `agent:`; renomeie o agente e todas as vinculações juntos e depois execute o validador novamente.
- `description` é a única chave de frontmatter exigida com rigor pelo gate; `handoffs` é exclusiva dos agentes de estágio e apenas quando existe um estágio seguinte.
- Acrescentar um agente novo exige um motivo que o modelo de duas camadas ainda não cubra. Um **papel** novo é uma habilidade; uma **fase** nova é um agente.
- As seções obrigatórias do corpo e o esquema completo estão definidos em [`../PRIMITIVE-STANDARD.md`](../PRIMITIVE-STANDARD.md) e são verificados por [`../scripts/validate-copilot-primitives.py`](../scripts/validate-copilot-primitives.py).
- Ao acrescentar um agente, inclua a linha dele na camada correta acima e, se um prompt deve chamá-lo, defina o `agent:` desse prompt com este `name`.
