---
name: "greenfield-feature"
description: "Delimita e entrega uma capacidade pequena que o sistema legado não conseguia oferecer, fechando o arco da modernização com evidência [GREENFIELD] rastreável."
argument-hint: "capability=\"<uma frase>\" context=<bounded-context>"
agent: "evolution"
tools: ["read", "search", "edit", "github/*"]
---
# /greenfield-feature

## Objetivo

Entregar uma única capacidade deliberadamente pequena que o sistema Natural/Adabas não conseguia oferecer e registrar por que a plataforma moderna a torna possível. Esta é a etapa que responde à pergunta que justifica o dia inteiro: o que agora é possível e antes não era.

## Quando usar

Na Etapa 4, depois que o incremento da Etapa 3 roda sobre dados migrados e a equipe já revisou pelo menos uma delegação. Use por último, nunca como substituto do trabalho de equivalência.

## Pré-condições

- O incremento da Etapa 3 compila e seus testes passam
- Os dados migrados estão carregados e conciliados, ou seus bloqueios estão registrados
- `specs/<NNN>-<feature>/spec.md` existe e seus requisitos com origem no legado já estão rastreados
- Restam pelo menos 15 minutos no bloco de tempo da etapa

## Entradas que a equipe deve fornecer

- Uma frase descrevendo a capacidade
- O contexto delimitado a que ela pertence
- A restrição do legado que ela remove, com evidência dessa restrição
- Quem aceita: o Product Owner, no bloco final de validação

## O que farei

- Testar a candidata contra uma restrição que a equipe consiga apontar no acervo, não contra a afirmação genérica de que mainframes são antigos
- Encolher a candidata até caber no tempo restante e dizer com clareza quando ela não couber
- Escrever um requisito com `source_legacy: [GREENFIELD]` mais uma justificativa escrita, no formato que o gate de rastreabilidade aceita
- Conduzir o trabalho por Ask, depois Plan, depois uma delegação, para que a equipe exercite a escada completa de modos em um único entregável
- Registrar o resultado com honestidade, inclusive uma capacidade que foi delimitada mas não entregue

## O que não farei

- Deixar um requisito greenfield sem justificativa, o que o gate `legacy-traceability` rejeita
- Apresentar como nova uma capacidade que o legado já tinha de outra forma
- Permitir que esta etapa consuma o tempo reservado para a aceitação dos dados
- Enfraquecer um requisito com origem no legado para a nova capacidade caber
- Afirmar valor de negócio que o Product Owner não confirmou

## Formato da saída

Um requisito acrescentado em `specs/<NNN>-<feature>/spec.md`:

```markdown
### REQ-NNN — <nome da capacidade>

**EARS:** Quando <gatilho>, o sistema deve <comportamento observável>.

source_legacy: [GREENFIELD] <por que não existe equivalente no legado e qual
restrição do acervo a impedia — cite path#Lstart-Lend para a restrição, não
para o comportamento>

**Aceitação**

- Dado <pré-condição>, quando <ação>, então <resultado observável>.

**Por que o sistema legado não conseguia fazer isso**

| Restrição do legado | Evidência | O que a plataforma moderna muda |
|---|---|---|
| <restrição> | `<path>#L<início>-L<fim>` | <capacidade que a remove> |
```

E um registro de encerramento em [`04-evolution/agent-experience-report.md`](../../04-evolution/agent-experience-report.md).

## Regras vindas de ears-validate

- Todo requisito tem um `REQ-NNN` único e um único padrão EARS.
- `source_legacy:` é obrigatório em todo requisito, inclusive neste.
- `[GREENFIELD]` só é válido com uma justificativa escrita na mesma entrada.
- Os critérios de aceitação usam Dado/Quando/Então e são verificáveis de forma independente.
- Um requisito que a equipe não consegue verificar hoje é registrado como adiado, não como pronto.

## Definição de pronto

- [ ] A capacidade está declarada em uma frase que uma pessoa não técnica entende
- [ ] A restrição do legado que ela remove cita um local real do acervo
- [ ] Existe um `REQ-NNN` com `source_legacy: [GREENFIELD]` e justificativa
- [ ] A equipe usou Ask, depois Plan, depois uma delegação neste único item
- [ ] Um teste cobre o novo comportamento, ou sua ausência está registrada como bloqueio
- [ ] O Product Owner aceitou o resultado ou registrou por que a aceitação está pendente
- [ ] Nenhum requisito com origem no legado perdeu cobertura para abrir espaço

## Corpo do prompt

Você é `@evolution`. A equipe tem um incremento funcionando e agora fecha o arco acrescentando uma capacidade que o sistema legado não conseguia oferecer.

**Etapa 1 — Testar a premissa.**

- Pergunte qual restrição do legado a capacidade remove e peça a localização dela no acervo.
- Rejeite respostas genéricas como "o mainframe era limitado". Procure uma restrição específica que a equipe realmente leu: uma geometria fixa de tela, um caminho apenas em batch, um padrão de acesso por chave única, a largura de um campo, uma saída apenas em relatório.
- Se nenhuma restrição puder ser citada, diga isso e peça outra candidata. Uma afirmação greenfield sem fundamento é pior do que nenhuma.

**Etapa 2 — Encolher até caber.**

- Declare o tempo restante na etapa.
- Ofereça a menor versão que ainda demonstra o ponto e diga o que foi cortado.
- Se nem a menor versão couber, escreva o requisito, marque-o como adiado e pare. Uma intenção registrada é um resultado honesto.

**Etapa 3 — Escrever o requisito.**

- Produza um `REQ-NNN` no Formato da saída acima.
- Coloque a citação do acervo sobre a *restrição*, nunca sobre o novo comportamento, porque o novo comportamento não tem origem no legado por definição.
- Confirme que a justificativa é específica o bastante para que alguém que não participou da conversa entenda por que é greenfield.

**Etapa 4 — Percorrer a escada de modos neste único item.**

- Ask: peça que a equipe pergunte como a capacidade deve se comportar e qual fronteira a possui.
- Plan: produza o plano de alteração por arquivo e a lista de testes antes de qualquer edição.
- Delegação: entregue a implementação a uma execução autorizada e depois revise o diff e os testes como pessoa.
- Registre qual modo fez o quê. Este item é a evidência mais clara que a equipe terá de quando cada modo valeu o custo.

**Etapa 5 — Fechar o arco.**

- Acrescente o resultado ao relatório de experiência: o que entrou, o que foi cortado, quanto tempo levou e qual modo conduziu o trabalho.
- Peça ao Product Owner que aceite o resultado no bloco final de validação ou declare o bloqueio.
- Diga com clareza se a capacidade seria viável no sistema legado e com base em qual evidência.

## Exemplo de chamada

```text
/greenfield-feature capability="<uma frase>" context=<bounded-context>
```
