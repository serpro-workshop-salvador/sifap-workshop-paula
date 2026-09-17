# Registro de Questões em Aberto — Estágio 1

> **Trilha:** [Kit do Time](../README.md) › [Estágio 1](README.md) › **Questões em Aberto**

**Registro rastreável das incertezas do Estágio 1.** Cada entrada documenta uma pergunta sem resposta, com evidência, hipótese marcada como não confirmada e responsável pela validação.

| Campo | Valor |
|---|---|
| **Público-alvo** | Todas as duplas |
| **Pré-requisitos** | Ler os programas atribuídos |
| **Estágio** | Estágio 1 — Arqueologia |
| **Resultado esperado** | Perguntas sem conclusão, com evidência e responsável identificado |

> [!IMPORTANT]
> Uma pergunta só vira regra de negócio, requisito ou conclusão depois de validação humana explícita e com a evidência preservada como `path:line`. Este registro não é uma resposta e não substitui essa validação.

---

## Registro

Use uma linha por mistério. Preencha com o **ID canônico** da sua dupla (`SIFAP-M-01` … `SIFAP-M-20` — veja o [checklist](mysteries-checklist.md)) ou `BONUS` para achados fora da lista.

| ID | Questão em aberto | Evidência (`path:line`) | Impacto | Hipótese (não confirmada) | Pessoa/área responsável | Status |
|---|---|---|---|---|---|---|
| `SIFAP-M-01` | Qual das três implementações de validação de CPF é a regra oficial do SIFAP? | `CADBENEF.NSP:344-413`, `CCVALCPF.NSC:39-130`, `VALBENEF.NSN:196-282` | O mesmo CPF pode ser aceito ou recusado conforme o caminho; a migração precisa de uma única regra e da decisão sobre o acervo já gravado | Não confirmada: o copycode `CCVALCPF` seria o padrão, e as cópias inline sobreviveram ao chamado 6620/2011, que segue aberto | SUPDE/DESIF | aberta |
| `SIFAP-M-02` | Por que um CPF com todos os dígitos iguais é aceito quando começa com `000`? | `VALBENEF.NSN:237-243` | Define se a base contém CPFs sintéticos e se o sistema novo deve reproduzir a exceção ou migrar esses registros | Não confirmada: o comentário do código diz tratar-se de CPF de teste do governo | SENARC/CGPB | aberta |
| `SIFAP-M-03` | Por que um beneficiário com mais de 75 anos recebe a situação `S`, que o dicionário de dados define como **suspenso**? | `CADBENEF.NSP:250-252`, `BENEFIC.ddm:74-75` | A regra suspende automaticamente a população idosa; se a leitura estiver correta, a migração reproduziria uma suspensão em massa | Não confirmada: `S` significaria algo diferente de suspensão neste contexto, ou a atribuição seria um defeito introduzido em 10/01/2011 | SENARC/CGPB | aberta |
| `SIFAP-M-04` | Um beneficiário com NIS inválido pode ser gravado no cadastro? | `CADBENEF.NSP:199-201`, `SUBVALNI.NSN:83` | `SUBVALNI` distingue NIS ausente, inválido e não numérico, mas o cadastro apenas avisa e grava; define se a migração herda dados inválidos | Não confirmada: o modo aviso seria temporário, pendente de revisão desde o chamado 6621/2011 | SUPDE/DESIF | aberta |

> [!WARNING]
> A associação entre cada achado e o ID canônico `SIFAP-M-01` a `SIFAP-M-04` ainda **não foi confirmada**. O [checklist](mysteries-checklist.md) define que o rótulo indica a área do mistério, nunca o achado. Confirme a correspondência com a facilitação antes do handoff H1.

### Achados adicionais (bônus)

Achados legítimos fora dos 20 mistérios canônicos. Contam no debrief, **não** mudam o denominador e **não** substituem um mistério canônico que ficou faltando.

| ID | Questão em aberto | Evidência (`path:line`) | Impacto | Hipótese (não confirmada) | Pessoa/área responsável | Status |
|---|---|---|---|---|---|---|
| `BONUS` | O resultado de `CALLNAT 'SUBVALCP'` é calculado e descartado pelo cadastro? | `CADBENEF.NSP:161-168` | A decisão usa `#CPF-VALID`, da rotina interna, e não `#PV-COD-RETURN` | Não confirmada: a chamada corporativa seria inócua no fluxo atual | SUPDE/DESIF | aberta |
| `BONUS` | Por que o código de retorno 1003 nunca é emitido? | `PDAVALID.NSA:35`, `SUBVALCP.NSN:75` | Um CPF com dígitos iguais é diagnosticado como erro de dígito verificador, o que distorce relatórios de erro | Não confirmada: a verificação migrou para `CCVALCPF` e o mapeamento do código não acompanhou | SUPDE/DESIF | aberta |
| `BONUS` | Por que `#CPF-EQUAL` é declarado em `SUBVALCP` e nunca usado? | `SUBVALCP.NSN:41` | Indício de verificação removida ou nunca concluída | Não confirmada: resíduo da refatoração de 07/06/2011 | SUPDE/DESIF | aberta |
| `BONUS` | O indicador `#PV-IND-SPECIAL` tem alguma finalidade viva? | `PDAVALID.NSA:55`, `SUBVALCP.NSN:45`, `SUBVALNI.NSN:53` | O contrato prevê `S` para documento especial, e os dois subprogramas gravam `N` fixo | Não confirmada: recurso previsto em 2003 e nunca implementado | SENARC/CGPB | aberta |
| `BONUS` | Fevereiro deve mesmo aceitar 29 dias em qualquer ano? | `VALBENEF.NSN:104` | Datas de nascimento inexistentes passam na validação | Não confirmada: simplificação deliberada, conforme o comentário do próprio código | SUPDE/DESIF | aberta |
| `BONUS` | Por que a view de `BENEFIC` em `VALBENEF` nunca é lida desde 1998? | `VALBENEF.NSN:29` | A validação não confronta a base; só examina o que recebe por parâmetro | Não confirmada: verificação planejada e nunca implementada, chamado 4471/2003 | SUPDE/DESIF | aberta |
| `BONUS` | A UF em branco deve escapar da validação? | `VALBENEF.NSN:156` | Registros sem UF atravessam sem erro | Não confirmada: campo seria opcional no cadastro | SENARC/CGPB | aberta |
| `BONUS` | A semente da sequência de auditoria suporta execuções concorrentes? | `CCAUDIT.NSC:65-72` | O máximo é lido uma vez por execução e incrementado em memória; sessões simultâneas podem colidir | Não confirmada: a chave `NUM-AUDIT` poderia receber valores repetidos | CGTI | aberta |
| `BONUS` | A perda da fração de segundo na hora do evento é aceitável? | `CCAUDIT.NSC:75-77` | `*TIMN` devolve `N7` e o campo do DDM é `N6`; eventos no mesmo segundo ficam indistinguíveis | Não confirmada: limitação herdada do formato do DDM | CGTI | aberta |
| `BONUS` | Quem deveria preencher `COD-PROFILE` na trilha de auditoria? | `CCAUDIT.NSC:50-51` | Campo previsto no DDM e nunca populado; chamado 7742 em aberto | Não confirmada: responsabilidade nunca atribuída | CGTI | aberta |
| `BONUS` | Quem bloqueia o registro da ação `CO` exigido desde 2010? | `CCAUDIT.NSC:45-48` | A rotina transfere a responsabilidade ao chamador; nenhum bloqueio foi localizado em `CADBENEF` | Não confirmada: a Portaria CGTI 213/2010 não teria sido implementada | CGTI | aberta |
| `BONUS` | O endereço perde os 20 últimos caracteres na gravação? | `CADBENEF.NSP:277-279`, `CADBENEF.NSP:308` | Campo de tela `A80` gravado em campo `A60`; afeta a migração dos dados históricos | Não confirmada: perda declarada no chamado 4471/2003 e nunca corrigida | SUPDE/DESIF | aberta |
| `BONUS` | `#FOUND` pode terminar verdadeiro sem registro encontrado? | `CADBENEF.NSP:206-211` | Se puder, as regras de duplicidade e de alteração se invertem | Não confirmada: depende da semântica de `END-NOREC` no corpo do `FIND` | SUPDE/DESIF | aberta |
| `BONUS` | Qual é o conjunto válido de códigos de parentesco? | `CADDEPEN.NSP:152-153`, `BENEFIC.ddm:91-92` | O programa aceita `FI`, `CO`, `IR` e `OU`; o dicionário define `FI`, `CJ`, `NT` e `TU`. Três dos quatro códigos gravados não existem no dicionário | Não confirmada: o dicionário teria sido revisado sem atualizar o programa | SUPDE/DESIF | aberta |
| `BONUS` | O código de região identifica macrorregião ou unidade federativa? | `BENEFIC.ddm:66`, `SOCPROG.ddm:87` | Os dois DDMs indicam cinco macrorregiões mais o valor 99, e o levantamento de 2012 afirma 27 estados; o domínio muda o modelo de dados do sistema novo | Não confirmada: o levantamento de 2012 estaria errado | SENARC/CGPB | aberta |
| `BONUS` | Qual é o limite real de dependentes por beneficiário? | `CADDEPEN.NSP:117-120`, `BENEFIC.ddm:87` | O programa aceita a sexta ocorrência, o grupo periódico comporta dez e o levantamento de 2012 declara três | Não confirmada: o limite teria sido ampliado sem atualizar a documentação | SENARC/CGPB | aberta |
| `BONUS` | Por que a auditoria em nível de campo nunca é preenchida? | `AUDIT.ddm:61-66`, `CCAUDIT.NSC:60-100` | O dicionário prevê valor anterior e posterior com vinte ocorrências, e a rotina grava apenas texto livre; a RN-010 descreve o recurso como existente | Não confirmada: recurso criado em 2005 e nunca conectado à rotina padrão | CGTI | aberta |
| `BONUS` | O cadastro de programas usa o arquivo 151 ou o 155? | `CADPROG.NSP:10`, `CADPROG.NSP:109`, `SOCPROG.ddm:21` | O cabeçalho e o corpo do mesmo programa se contradizem; o dicionário indica 151 | Não confirmada: o cabeçalho estaria desatualizado desde 1997 | SUPDE/DESIF | aberta |
| `BONUS` | De onde vem a constante 0,347215 e por que `FACTOR-K` não é gravado? | `CADPROG.NSP:124-125`, `SOCPROG.ddm:47-51` | O campo existe no dicionário, marcado como não documentado, e o programa calcula um fator local que nunca persiste | Não confirmada: seriam dois fatores distintos com o mesmo nome | SENARC/CGPB | aberta |
| `BONUS` | O código de ação `DV` pertence ao domínio da auditoria? | `AUDIT.ddm:39-48`, `AUDIT.ddm:128` | O rodapé contabiliza volume para `DV`, que não consta da lista de ações válidas | Não confirmada: código criado em campo e nunca documentado | CGTI | aberta |
| `BONUS` | Por que há registro de consulta entre 2014 e 2018 se a Portaria 213/2010 o vedou? | `AUDIT.ddm:128`, `CCAUDIT.NSC:45-48` | O rodapé atribui 193,8 milhões de registros ao par `CO`/`DV` no período; define se a vedação é cumprida | Não confirmada: a conciliação bancária teria reintroduzido o registro sob outro código | CGTI | aberta |
| `BONUS` | Um dependente gravado sem situação é considerado ativo? | `CADDEPEN.NSP:25-26`, `BENEFIC.ddm:93` | O programa nunca atribui `STAT-DEPEND`, e branco não pertence ao domínio `A`/`I`/`D` do dicionário | Não confirmada: a contagem `QTY-DEPEND` substituiria a situação individual | SUPDE/DESIF | aberta |
| `BONUS` | Programas alterados pela última vez em 2012 podem referenciar um campo criado em 2013? | `BENEFIC.ddm:20`, `CADBENEF.NSP:1-12`, `CADDEPEN.NSP:1-11` | `QTY-DEPEND` consta como acrescentado em 05/04/2013, e os dois programas que o usam não registram alteração posterior a 12/09/2012 | Não confirmada: um dos cabeçalhos não teria sido atualizado na alteração | SUPDE/DESIF | aberta |

---

## Regras de integridade

- Registre apenas questões em aberto; não escreva uma resposta no catálogo.
- Mantenha a evidência no formato `path:line` para preservar a rastreabilidade.
- Marque toda hipótese explicitamente como **não confirmada**.
- Só a pessoa responsável pode dar a validação humana e mudar o status.
- Sem evidência humana, a questão continua em aberto.

---

### Continue lendo

| Anterior | Próximo |
|---|---|
| [Checklist de Questões em Aberto](mysteries-checklist.md)<br/><sub>Verificação de rastreabilidade.</sub> | [Relatório de Descoberta](discovery-report.md)<br/><sub>Consolidação final do estágio.</sub> |

<sub>[Voltar ao índice do kit](../README.md)</sub>
