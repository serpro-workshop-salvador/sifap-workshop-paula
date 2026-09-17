---
name: "ux-research-design"
description: "Use ao estabelecer quem usa a interface modernizada do SIFAP e do que essas pessoas precisam — Jobs-to-be-Done, jornadas de usuário, arquitetura de informação e requisitos de acessibilidade que alimentam a construção do frontend. Produz documentos de pesquisa, nunca código de componente. Os gatilhos incluem \"jornada de usuário\", \"jobs to be done\", \"pesquisa de UX\", \"especificação de acessibilidade\" e \"quem usa esta tela\"."
---
# Pesquisa de UX e intenção de design

## Quando usar

- "Quem de fato usa esta tela, e para fazer o quê?"
- "Mapeie a jornada antes de desenharmos a página."
- "Quais são os requisitos de acessibilidade deste fluxo?"
- "Esta arquitetura de informação está correta?"

## Limite do papel

| Isto produz | Isto nunca produz |
|---|---|
| Documentos de pesquisa em Markdown | Arquivos `.tsx` ou classes Tailwind |
| Declarações de job e jornadas | Implementações de componentes |
| Critérios de aceitação de acessibilidade | Ativos de design visual |
| Arquitetura de informação | Escolhas de framework ou biblioteca |

Entregue a saída para a habilidade react-nextjs-frontend ou para a habilidade
developer construírem.

## Procedimento

**Etapa 1 — Estabeleça quem usa antes da tela.**

- Um wireframe sem declaração de job é rejeitado.
- No domínio do SIFAP, nomeie a pessoa que opera de verdade: quem abre isto, de onde, sob qual pressão de tempo e o que acontece se errar.
- Fundamente o papel em evidência onde ela existe. Os códigos de transação 3270 e os fluxos de tela legados descrevem trabalho real; cite-os em vez de inventar uma persona.

**Etapa 2 — Escreva o job, não a funcionalidade.**

- Formato: `Quando <situação>, quero <motivação>, para que eu possa <resultado esperado>`.
- Um job sobrevive a um redesenho. Uma funcionalidade não.

**Etapa 3 — Mapeie a jornada de ponta a ponta.**

| Etapa | O que a pessoa faz | Do que precisa | Onde falha hoje |
|---|---|---|---|

- Inclua os caminhos infelizes: não encontrado, correspondência ambígua, dado desatualizado, permissão parcial.
- Os modos de falha legados são evidência. Um design moderno que os repete em silêncio não melhorou nada.

**Etapa 4 — Faça da acessibilidade um requisito, não uma revisão.**

- Caminho por teclado para cada ação, foco visível e ordem de tabulação lógica.
- Estrutura e rótulos semânticos, não ARIA remendado sobre uma `div`.
- Contraste e tamanhos de alvo que atendam ao WCAG 2.2 AA.
- Mensagens de erro que digam o que fazer a seguir, não apenas o que falhou.
- Escreva isto como critérios de aceitação, para que possam reprovar em um teste.

**Etapa 5 — Respeite as regras de dados.**

- Dados sensíveis como CPF e valores de benefício ficam mascarados por padrão, revelados apenas por uma ação autorizada explícita.
- Uma tela que mostra tudo para todo mundo é um achado de segurança, não uma conveniência.

## Antipadrões a rejeitar

| Solicitação | Resposta |
|---|---|
| "Desenhe a tela" sem ninguém nomeado | Estabeleça o job primeiro. |
| Uma persona inventada com dor inventada | Cite o fluxo legado, ou marque como suposição. |
| Acessibilidade como passe final de revisão | Escreva-a como critérios de aceitação desde o início. |
| Apenas o caminho feliz | Mapeie os caminhos de não encontrado, ambíguo e permissão parcial. |
| Uma proposta de layout escrita como código de componente | Esta habilidade produz pesquisa; entregue para a construção. |

## Modelo de saída

```markdown
## Declarações de job

- Quando <situação>, quero <motivação>, para que eu possa <resultado esperado>.

## Jornada — <nome do fluxo>

| Etapa | Ação da pessoa | Necessidades | Modo de falha hoje | Evidência |
|---|---|---|---|---|

## Arquitetura de informação

<O que é agrupado, o que é primário, o que é divulgação progressiva.>

## Critérios de aceitação de acessibilidade

- Dado <contexto>, quando <ação> apenas por teclado, então <resultado observável>.

## Regras de exposição de dados

| Campo | Estado padrão | Revelar exige |
|---|---|---|
```

## Critérios de qualidade

- [ ] Cada tela rastreia até pelo menos uma declaração de job.
- [ ] Cada jornada inclui seus caminhos infelizes.
- [ ] A acessibilidade está escrita como critérios de aceitação testáveis, não como princípio.
- [ ] Campos sensíveis têm um estado padrão explícito e uma regra de revelação.
- [ ] Afirmações sobre o comportamento atual citam o acervo ou estão rotuladas como suposições.
- [ ] A entrega é um documento de pesquisa, não código de componente.
