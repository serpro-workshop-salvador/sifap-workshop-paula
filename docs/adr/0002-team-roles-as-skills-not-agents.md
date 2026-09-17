# ADR-0002: Papéis da equipe são skills; somente os estágios e o ciclo de vida dos dados são agentes

> **Trilha:** [Kit do Time](../../README.md) › [Documentação](../README.md) › [ADRs](README.md) › **ADR-0002**

| Campo | Valor |
|---|---|
| **Status** | accepted |
| **Data** | 2026-09-15 |
| **Autores** | Pessoas mantenedoras do kit |
| **Substitui** | N/A |

---

## Contexto

O kit entregava **17 agentes**: 4 agentes de estágio, 10 agentes de persona e 3
especialistas em profundidade. Dois desses grupos faziam trabalhos diferentes sob
uma mesma primitiva.

Um **estágio** é uma fase em que toda a equipe entra e da qual toda a equipe sai em
conjunto. Ele tem um início, uma definição de pronto e uma passagem de bastão para o
estágio seguinte. Selecioná-lo deliberadamente é o ponto: a seleção *é* o ritual.

Um **papel** é uma responsabilidade que uma pessoa carrega por todos os estágios. O
Responsável pelo Produto não deixa de ser o Responsável pelo Produto quando o Estágio 3
começa. Ainda assim, o desenho por agentes de persona exigia que essa pessoa
selecionasse `@product-owner` novamente em cada conversa e, depois, voltasse a
selecionar o agente de estágio para recuperar o contexto do estágio. As duas camadas
disputavam um único seletor em vez de se compor.

Disso decorreram três custos concretos:

1. **Carga no seletor.** Dezessete entradas para uma imersão de cinco pessoas e oito horas.
2. **Carga de ensino.** Existiam três documentos separados apenas para explicar por que duas camadas "não são duplicadas" — um sinal confiável de que o problema estava na abstração, não na documentação.
3. **Peso morto.** Os três agentes especialistas possuíam **zero** prompts. Já eram conhecimento puro, vestindo o frontmatter de um agente.

As skills resolvem diretamente a metade referente ao papel: elas carregam a partir da
sua `description`, por correspondência semântica, de modo que o conhecimento chega sem
uma etapa de seleção e se compõe com o agente que estiver ativo.

Um papel não se encaixa na regra. O **DBA** é responsável pelo ciclo de vida dos dados,
que a matriz de personas marca como `Líder de dados` nos **quatro** estágios e que
possui prompts com escopo de ferramentas (`persona-dba-migration`,
`persona-dba-query-audit`, `postgresql-code-review`, `postgresql-optimization`). Ele é
transversal por definição, então não cabe dentro de um agente de estágio, e seus
prompts precisam de um alvo de vínculo que somente um agente oferece.

## Decisão

Manter **cinco agentes**: os quatro agentes de estágio (`archaeologist`, `architect`,
`builder`, `evolution`) mais `dba`.

Converter os nove agentes de persona restantes e os três especialistas em skills sob
`.github/skills/`. Revincular cada prompt órfão ao agente de estágio que é dono do
momento em que aquele prompt é usado, e abrir o corpo de cada prompt revinculado
carregando a skill do papel que carrega sua fronteira, seu procedimento e seu critério
de qualidade.

A regra que governa as primitivas futuras: **uma nova fase é um agente; um novo papel
é uma skill.**

## Alternativas consideradas

| Alternativa | Por que foi rejeitada |
|---|---|
| Manter os 17 agentes | Preserva todos os custos acima e mantém duas primitivas disputando um único seletor. |
| Ocultar as personas com `user-invocable: false` | Barato e reversível, e de fato limpa o seletor — mas o conhecimento continua sem se compor com o agente ativo, que é o defeito real. Serve como experimento, não como destino. |
| Converter também o DBA e eliminar seu agente | O ciclo de vida dos dados atravessa os quatro estágios e possui quatro prompts com escopo de ferramentas. Dobrá-lo dentro de um agente de estágio representaria mal o momento em que o trabalho acontece. |
| Fundir os prompts de persona no corpo dos agentes de estágio | Destrói os comandos de barra, que são justamente a parte que as pessoas participantes usam. |

## Consequências

- **Mais fácil:** cinco entradas no seletor; o conhecimento do papel chega sem ser solicitado; o modelo de duas camadas precisa de uma tabela em vez de três documentos; doze primitivas a menos para manter em sincronia.
- **Mais difícil:** quem quiser o contexto completo de um papel sob demanda precisa nomeá-lo (`persona-qa-engineer`) em vez de mencioná-lo com `@`. A correspondência de skills é semântica, então uma `description` que se desvia em silêncio degrada o carregamento — as descrições agora pesam mais e são revisadas com esse cuidado.
- **Riscos:** 37 prompts mudaram seu vínculo `agent:` em um único commit. Uma aplicação parcial falharia no gate `copilot-primitives`, que é a rede de proteção pretendida.
- **Mitigações:** o gate valida a integridade `prompt -> agente` e a igualdade entre o `name` da skill e seu diretório em cada PR; [`.github/agents/README.md`](../../.github/agents/README.md) traz o mapeamento de agente anterior para skill, de modo que uma referência desatualizada continua rastreável.

## Relacionados

- REQ-IDs: N/A
- ADRs: [ADR-0001](0001-agent-instructions-single-source-of-truth.md)
- Arquivos de instruções: [`.github/PRIMITIVE-STANDARD.md`](../../.github/PRIMITIVE-STANDARD.md), [`.github/instructions/agent-skills.instructions.md`](../../.github/instructions/agent-skills.instructions.md)

## Referências

- GitHub Docs — Sobre a personalização das respostas do GitHub Copilot: <https://docs.github.com/en/copilot/concepts/response-customization>
- GitHub Docs — Compatibilidade com diferentes tipos de instruções personalizadas: <https://docs.github.com/en/copilot/reference/custom-instructions-support>

---

### Continue lendo

| Anterior | Próximo |
|---|---|
| [ADR-0001](0001-agent-instructions-single-source-of-truth.md)<br/><sub>Fonte única de verdade para instruções de agentes.</sub> | [ADRs — Índice](README.md)<br/><sub>Índice das decisões registradas.</sub> |

<sub>[Voltar ao índice do kit](../../README.md)</sub>
