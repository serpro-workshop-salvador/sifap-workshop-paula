---
name: "audit-context"
description: "Audite a superfície de contexto do Copilot no repositório (AGENTS.md, CODEMAP.md, instruções, prompts e agentes) e retorne correções priorizadas."
argument-hint: "scope=.github"
agent: "builder"
tools: ["read", "search"]
---
# /audit-context

## Objetivo

Auditar `AGENTS.md`, `CODEMAP.md`, instruções, prompts e agentes e listar correções reais por gravidade.

## Quando usar

Periodicamente, antes de transições ou após mudanças em primitives.

## Pré-condições

- `.github/` existe; os índices de instruções e [prompts](README.md) são referência

## Entradas que a equipe deve fornecer

- Escopo opcional

## O que farei

- Inventariarei arquivos e linhas; verificarei `applyTo`, frescor do CODEMAP, frontmatter, agentes, ferramentas, modelos, paths e links
- Aplicarei [`context-audit`](../skills/context-audit/SKILL.md)

## O que não farei

- Criar falso positivo, editar, sugerir modelo/provedor fixo ou reescrever primitives

## Formato da saída

Tabela `Arquivo | Problema | Gravidade | Correção` e três principais.

## Definição de pronto

- [ ] Todo High tem correção concreta
- [ ] Frescor, todos os `applyTo` e links foram verificados
- [ ] Sem falso positivo ou sugestão sobre aplicação

## Corpo do prompt

Você é `@builder`. Inventarie `.github/instructions/`, `.github/prompts/` e `.github/agents/`. `applyTo: "**"` ou ausente é High. CODEMAP com mais de 30 dias ou arquivos apagados está desatualizado. Verifique descriptions, resolução de agent, ferramentas mínimas e ausência de modelo fixo. Pesquise paths e links quebrados. Ordene High, Medium, Low e termine com três correções.

Carregue a skill [`persona-technical-lead`](../skills/persona-technical-lead/SKILL.md) antes de começar: a skill `persona-technical-lead` define a fronteira, o procedimento e o critério de qualidade do papel, e este prompt define a tarefa.

## Exemplo de chamada

```
/audit-context scope=.github
```
