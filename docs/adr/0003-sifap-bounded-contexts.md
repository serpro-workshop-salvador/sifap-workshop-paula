# ADR-0003: Definir quatro contextos no Monólito Modular do SIFAP

> **Trilha:** [Kit do Time](../../README.md) > [Documentação](../README.md) > [ADRs](README.md) > **ADR-0003**

**Organizamos o destino do SIFAP em quatro contextos delimitados, preservando a consulta de programa por código como fatia atual.**

| Campo | Valor |
|---|---|
| Status | accepted |
| Data | 2026-09-17 |
| Responsável pela decisão | paula, em execução individual |
| Apoio à redação | GitHub Copilot, agente architect |
| Substitui | N/A |

## Contexto

O [relatório de descoberta](../../01-archaeology/discovery-report.md#4-hipóteses-de-fatiamento-recomendadas) apresenta quatro hipóteses de agrupamento, ainda sem propriedade exclusiva dos dados. O [mapa de dependências](../../01-archaeology/dependency-map.md) evidencia chamadas e acessos compartilhados; ele não demonstra módulos já desacoplados. Um contexto delimitado reúne termos, regras e dados com responsabilidades coerentes, e não corresponde automaticamente a um prefixo de programa ou arquivo Adabas.

A hipótese de cadastro reúne beneficiários e programas sociais, enquanto a de consultas reúne apresentações de domínios distintos. A separação entre cálculo e ciclo financeiro também divide uma responsabilidade ainda controversa: [CALCBENF](../../01-archaeology/legacy-sifap/natural-programs/CALCBENF.NSN#L319) e [BATCHPGT](../../01-archaeology/legacy-sifap/natural-programs/BATCHPGT.NSP#L488) contêm escrita de PAYMENT. Nenhuma escolha de limite resolve, por si só, as divergências de fórmulas, numeração ou transações.

O aceite H1 seleciona a consulta de programa por código, ramo C de CADPROG. A [rotina de consulta](../../01-archaeology/legacy-sifap/natural-programs/CADPROG.NSP#L156) lê SOCPROG e apresenta código, nome, tipo, valor-base, código de elegibilidade e situação. A modernização das demais capacidades continua adiada.

## Decisão

Adotamos quatro contextos em um único Monólito Modular: **Beneficiários**, proprietário lógico de BENEFIC/150; **Programas Sociais**, de SOCPROG/151; **Pagamentos**, de PAYMENT/152; e **Auditoria**, de AUDIT/153. Os limites derivam das responsabilidades e dos contratos observados; os DDMs identificam os dados sob cada responsabilidade, não uma regra geral de um contexto por tabela.

A validação cadastral fica em Beneficiários. A elegibilidade para pagamento, o cálculo, o ciclo financeiro e seus relatórios ficam em Pagamentos, consumindo os dados publicados por Beneficiários e Programas Sociais. Auditoria responde pelo registro e pela consulta da trilha, sem assumir as regras de negócio das entidades auditadas. Consultas que combinam cadastro e histórico financeiro usam composição na aplicação, sem criar um quinto contexto ou dependência circular entre os domínios.

A comunicação é em processo por interfaces públicas e DTOs, sem HTTP entre módulos nem acesso a entidades ou repositórios internos alheios. A [definição detalhada dos contextos](../../02-modern-spec/bounded-contexts.md) é a referência para responsabilidades, avaliação das hipóteses, interfaces de desenho e diagrama. Essas interfaces ainda precisam de especificação testável; este ADR não é um contrato executável.

**Aceite:** paula respondeu "sim", em 2026-09-17, à recomendação dos quatro contextos e à manutenção do recorte. O status accepted registra essa decisão individual. Não declara aprovação de regras controversas, revisão por pares de PR, integração de branch ou conclusão do H2.

## Alternativas consideradas

| Alternativa | Benefício | Motivo da rejeição |
|---|---|---|
| Manter as quatro hipóteses originais sem ajustes | Preserva a organização inicial da descoberta | Mistura capacidades por prefixo ou apresentação e mantém a escrita de PAYMENT dividida entre cálculo e ciclo financeiro |
| Manter cadastro de beneficiários e programas em um contexto único | Reduz o número de interfaces | Agrupa identificação de pessoas e parâmetros de programas sem evidência de uma responsabilidade única; a consulta atual não depende de BENEFIC |
| Isolar toda validação e determinação de valores em um contexto | Concentra rotinas com nomes e contratos técnicos semelhantes | Une diagnóstico cadastral e decisão financeira; não resolve a persistência de CALCBENF nem a necessidade de dados dos outros proprietários |
| Criar um contexto genérico para consultas e relatórios | Centraliza formatos de saída | Separa a apresentação das regras dos respectivos domínios e incentiva acesso direto a dados de vários proprietários |

## Consequências

- **Mais fácil:** localizar a consulta atual em Programas Sociais, identificar um proprietário lógico para cada conjunto de dados e manter a responsabilidade financeira próxima dos escritores de PAYMENT.
- **Mais difícil:** substituir acessos cruzados do legado por interfaces explícitas e compor consultas de mais de um domínio. Pagamentos concentra várias capacidades, que precisarão de organização interna quando entrarem no escopo.
- **Riscos:** confundir propriedade lógica com schema físico pronto, interpretar proximidade estrutural como frequência histórica medida ou tratar uma interface de desenho como aprovação de seu comportamento.
- **Mitigações:** especificar e testar uma fatia por vez; manter as questões abertas rastreáveis; revisar assinaturas, projeções e garantias transacionais antes da implementação correspondente.

Não adicionamos dependências, tabelas, migrações ou código. A consulta não recalcula valores nem altera política de auditoria. Os dados fora do recorte continuam no legado; não se presume integração executável com um ambiente legado disponível.

## Acompanhamentos

- [ ] Especificar a consulta por código com REQ-IDs, EARS, fontes e critérios de aceitação nos artefatos Spec-Kit.
- [ ] Validar normalização do código, projeção dos seis campos e comportamento para programa ausente antes de implementar a consulta.
- [ ] Detalhar os contratos executáveis e os testes de fronteira da fatia atual no plano e nas tarefas.
- [ ] Antes de ampliar o escopo financeiro ou de auditoria, decidir as respectivas questões de algoritmo, numeração, consistência e transação.
- [ ] Conferir a renderização do diagrama e os gates de documentação antes da integração por PR.

## Relacionados

- REQ-IDs: ainda não atribuídos para esta fatia; este documento não cria requisitos formais.
- Escopo: [decisões do Estágio 2](../../02-modern-spec/scope-decisions.md).
- Descobertas: [catálogo de regras](../../01-archaeology/business-rules-catalog.md), [mapa de dados](../../01-archaeology/data-map.md) e [questões abertas](../../01-archaeology/mysteries-found.md).
- Os ADRs 0001 e 0002 tratam das primitivas do kit, não dos limites de negócio desta decisão; não são substituídos.

## Referências

- [Mapa de contextos delimitados](../../02-modern-spec/bounded-contexts.md).
- [Guia de arquitetura de Monólito Modular](../../.github/instructions/modular-monolith.instructions.md).
- [Fluxo Git e revisão para integração](../../00-GIT-WORKFLOW.md).

### Continue lendo

| Anterior | Próximo |
|---|---|
| [ADRs: índice](README.md) | [Mapa de contextos delimitados](../../02-modern-spec/bounded-contexts.md) |

<sub>[Voltar ao índice do kit](../../README.md)</sub>
