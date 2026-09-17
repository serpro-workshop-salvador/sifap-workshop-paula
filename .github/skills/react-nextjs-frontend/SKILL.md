---
name: "react-nextjs-frontend"
description: "Use para trabalho com foco em frontend na UI modernizada do SIFAP — React 19 e Next.js 15 App Router, limites entre Server e Client Component, Server Actions, busca de dados, UI otimista, acessibilidade e desempenho de renderização. Os gatilhos incluem \"Server Component\", \"use client\", \"Server Action\", \"App Router\", \"hidratação\" e \"a página está lenta\"."
---
# Profundidade de frontend com React e Next.js

## Quando usar

- "Isto deve ser um Server Component ou um Client Component?"
- "Conecte esta mutação com uma Server Action."
- "Esta página renderiza de novo vezes demais."
- "Deixe esta tabela acessível e rápida."

## Limite do papel

| Esta habilidade cobre | Use outra habilidade para |
|---|---|
| Estrutura e desempenho com foco em frontend | Um único item rastreável do `tasks.md` — habilidade developer |
| Limites Server/Client e fluxo de dados | Qualquer mudança de backend — habilidade developer |
| Renderização, hidratação e custo de interação | Intenção de design e jornadas — habilidade ux-research-design |

## Procedimento

**Etapa 1 — Tenha o servidor como padrão.**

- Server Components são o padrão. Adicione `'use client'` apenas onde o componente precisa de estado, de um efeito, de uma API do navegador ou de um manipulador de eventos.
- Empurre `'use client'` **para baixo** na árvore. Um limite de cliente no nível da página arrasta toda a subárvore para o bundle.
- Nunca passe um valor não serializável através do limite.

**Etapa 2 — Busque os dados onde eles são usados.**

- Busque no Server Component que renderiza os dados. Evite passar um resultado de busca por prop através de três níveis.
- Paralelize requisições independentes; uma cadeia sequencial de awaits é a causa mais comum de página lenta.
- Use `Suspense` com um fallback significativo, para que o shell renderize enquanto os dados resolvem.

**Etapa 3 — Faça mutações com Server Actions.**

- Valide a entrada **no servidor**, dentro da action. Uma verificação no cliente é uma conveniência, nunca um controle.
- Revalide explicitamente as entradas de cache afetadas depois de uma mutação.
- Use UI otimista apenas onde o caminho de falha estiver desenhado, e sempre reconcilie com a resposta do servidor.

**Etapa 4 — Mantenha o TypeScript estrito e honesto.**

- `strict: true`. Apenas exports nomeados.
- Tipe o contrato da API no limite e faça o parse da entrada não confiável, em vez de afirmá-la.
- Um cast que silencia o compilador esconde justamente o bug que deveria revelar.

**Etapa 5 — Construa a acessibilidade desde o início.**

- Elementos semânticos primeiro; ARIA apenas onde a semântica não consegue expressar o padrão.
- Toda interação alcançável por teclado, com foco visível e ordem lógica.
- Anuncie mudanças de estado assíncronas; um spinner sem nome acessível é invisível para um leitor de tela.

**Etapa 6 — Trate os dados do SIFAP como sensíveis.**

- CPF e valores de benefício ficam mascarados por padrão em listas e detalhes.
- Nunca coloque valores sensíveis em uma URL, no `localStorage` ou em um log do lado do cliente.

## Antipadrões a rejeitar

| Padrão | Correção |
|---|---|
| `'use client'` no topo de uma página | Mova o limite para baixo, até a folha interativa. |
| Awaits sequenciais para dados independentes | Busque em paralelo. |
| Validação apenas no cliente | Valide dentro da Server Action. |
| `any` ou um cast para silenciar o compilador | Faça o parse e estreite o tipo. |
| `div` com `onClick` | Use um button, ou forneça role, tabindex e tratamento de teclas. |
| Dado sensível em uma query string | Mova-o para o corpo da requisição ou para uma consulta no servidor. |

## Modelo de saída

```markdown
## Plano de componentes — <funcionalidade>

| Componente | Server ou Client | Por quê | Fonte de dados |
|---|---|---|---|

**Limite de cliente:** <o componente mais baixo que precisa dele, e o que o obriga>

**Mutações**

| Action | Validação (servidor) | Cache revalidado | Caminho de falha |
|---|---|---|---|

**Acessibilidade**

- Dado <contexto>, quando <ação> apenas por teclado, então <resultado observável>.

**Campos sensíveis:** <campo, estado padrão, regra de revelação>
```

## Critérios de qualidade

- [ ] `'use client'` aparece apenas onde estado, efeitos, APIs do navegador ou manipuladores exigem.
- [ ] Requisições de dados independentes rodam em paralelo, com um fallback de Suspense significativo.
- [ ] Cada mutação valida no servidor e revalida o cache que invalida.
- [ ] `strict: true` se mantém, sem casts adicionados para silenciar o compilador.
- [ ] Toda interação é alcançável por teclado, com foco visível e estado anunciado.
- [ ] CPF e valores de benefício ficam mascarados por padrão e ausentes de URLs e logs do cliente.
