# Catálogo de Regras de Negócio — SIFAP Legado

> **Trilha:** [Kit do Time](../README.md) › [Estágio 1](README.md) › **Catálogo de Regras de Negócio**

**Artefato preenchido pelo time durante o Estágio 1.** Cada dupla extrai as regras dos programas `.NSP` e `.NSN` que recebeu e as registra aqui, com rastreabilidade obrigatória até o programa de origem.

| Campo | Valor |
|---|---|
| **Público-alvo** | Todas as duplas — cada dupla preenche a seção dos seus programas |
| **Pré-requisitos** | Ler os programas `.NSP` e `.NSN` atribuídos |
| **Estágio** | Estágio 1 — Arqueologia |
| **Resultado esperado** | Catálogo com `Programa de origem` preenchido para cada regra candidata |

> [!NOTE]
> Cada regra cita o programa de origem com um intervalo de linhas (`arquivo.NSP:Linicio-Lfim` ou `arquivo.NSN:Linicio-Lfim`) e é classificada como **Confirmada** (corroborada pela documentação histórica em `legacy-sifap/legacy-docs/`), **Inferida** (só a partir do código) ou **Mistério** (questão em aberto — registre-a também em [`mysteries-found.md`](mysteries-found.md) com evidência `path:line`, hipótese não confirmada, responsável e status).

> [!IMPORTANT]
> Guia passo a passo: [`GUIDE.md`](GUIDE.md).

**Time**: <!-- preencher -->

---

## Regras de `CADBENEF.NSP`

**Dupla:** 1 · Visão (cadastro) · **Lido em:** 2026-09-17 · **Documentação confrontada:** `legacy-docs/BUSINESS-RULES-2012.md`

Cabeçalho do membro: autor CARLOS ROBERTO DA SILVA, criado em 15/03/1997, última alteração registrada em 12/09/2012 (`CADBENEF.NSP:1-12`).

| # | Enunciado da regra | Candidato EARS | Origem | Classificação | Notas |
|---|---|---|---|---|---|
| 1 | SE a operação informada não for `I` nem `A`, ENTÃO o sistema DEVE recusar a entrada e encerrar o fluxo | Indesejada | `CADBENEF.NSP:139-143` | Inferida | Sem correspondência no levantamento de 2012 |
| 2 | SE o CPF informado for zero, ENTÃO o sistema DEVE recusar o cadastro | Indesejada | `CADBENEF.NSP:145-149` | Confirmada | RN-001, §1.1, exige CPF válido |
| 3 | O sistema DEVE validar o CPF pelo algoritmo de módulo 11 com dois dígitos verificadores | Ubíqua | `CADBENEF.NSP:152`, `CADBENEF.NSP:344-413` | Confirmada | RN-001, §1.1. O documento cita o subprograma `VALCPF`; o código usa rotina interna `VALID-CPF` |
| 4 | SE o dígito verificador do CPF não conferir, ENTÃO o sistema DEVE recusar o cadastro | Indesejada | `CADBENEF.NSP:164-168` | Confirmada | RN-001, §1.1 |
| 5 | O resultado da validação corporativa de CPF não altera o fluxo | — | `CADBENEF.NSP:153-168` | Mistério | <!-- mystery: CALLNAT 'SUBVALCP' é executado, mas #PV-COD-RETURN nunca é testado; a decisão em L164 usa #CPF-VALID, que só a rotina interna atribui. Confirmar se a chamada corporativa é efetivamente inócua --> |
| 6 | SE o nome estiver em branco, ENTÃO o sistema DEVE recusar o cadastro | Indesejada | `CADBENEF.NSP:170-174` | Inferida | Sem correspondência no levantamento de 2012 |
| 7 | SE a data de nascimento for zero, ENTÃO o sistema DEVE recusar o cadastro | Indesejada | `CADBENEF.NSP:176-180` | Confirmada | RN-006, §1.1, declara a data de nascimento obrigatória |
| 8 | Não há verificação de idade mínima na inclusão | — | `CADBENEF.NSP:176-180` | Mistério | <!-- mystery: RN-006 exige recusar menores de 16 anos, mas a única verificação sobre a data de nascimento é a de preenchimento. Confirmar se a regra vive em outro membro ou nunca foi implementada --> |
| 9 | SE o sexo informado não for `M` nem `F`, ENTÃO o sistema DEVE recusar o cadastro | Indesejada | `CADBENEF.NSP:182-186` | Inferida | Sem correspondência no levantamento de 2012 |
| 10 | ONDE a validação de NIS retornar código diferente de zero, o sistema DEVE emitir aviso e prosseguir com a gravação | Opcional | `CADBENEF.NSP:188-201` | Mistério | <!-- mystery: RN-001 trata o NIS como validação obrigatória, mas o código apenas emite WRITE de aviso e não bloqueia. O comentário diz 'modo aviso pendente de revisão' desde 2011; confirmar se a revisão ocorreu --> |
| 11 | A verificação de existência marca o beneficiário como encontrado | — | `CADBENEF.NSP:206-211` | Mistério | <!-- mystery: MOVE TRUE TO #FOUND está após END-NOREC, dentro do corpo do FIND. Confirmar com pessoa especialista em Natural se #FOUND pode terminar TRUE mesmo sem registro, o que inverteria as regras 12 e 13 --> |
| 12 | SE a operação for inclusão e já existir registro com o mesmo CPF, ENTÃO o sistema DEVE recusar o cadastro | Indesejada | `CADBENEF.NSP:213-217` | Confirmada | RN-002, §1.1. Divergência: o documento restringe o bloqueio à situação ativa e permite reinclusão de excluído lógico; o código não consulta `STAT-BENEFICIARY` |
| 13 | SE a operação for alteração e não existir registro com o CPF informado, ENTÃO o sistema DEVE recusar a alteração | Indesejada | `CADBENEF.NSP:219-223` | Inferida | Sem correspondência no levantamento de 2012 |
| 14 | A expansão de ano por janela de século foi desativada no programa | — | `CADBENEF.NSP:232-236` | Mistério | <!-- mystery: o bloco de janela de século está comentado e o comentário afirma que a janela permanece em LDASIFAP para arquivos históricos. Confirmar quais fluxos ainda dependem dessa janela --> |
| 15 | O sistema DEVE calcular a idade pela diferença entre o ano corrente e o ano de nascimento | Ubíqua | `CADBENEF.NSP:241-242` | Mistério | <!-- mystery: o cálculo ignora mês e dia, então a idade muda em 1º de janeiro e não no aniversário. Confirmar se o desvio é intencional, pois alimenta a regra 17 --> |
| 16 | QUANDO a operação for inclusão, o sistema DEVE atribuir a situação `A` ao beneficiário | Orientada a evento | `CADBENEF.NSP:245-247` | Inferida | O documento cita `BN-CD-SIT = 'A'` como situação ativa em RN-002 e RN-011, sem descrever a atribuição inicial |
| 17 | ONDE a idade calculada for maior que 75 anos, o sistema DEVE atribuir a situação `S` | Opcional | `CADBENEF.NSP:250-252` | Mistério | <!-- mystery: o significado de 'S' não aparece no levantamento de 2012, que só cita 'A' e 'E'. O cabeçalho registra 'ADJUSTED ELDERLY STATUS' em 10/01/2011. Confirmar o domínio completo de STAT-BENEFICIARY no DDM BENEFIC --> |
| 18 | ONDE a validação cadastral corporativa retornar inconsistência, o sistema DEVE emitir aviso e prosseguir com a gravação | Opcional | `CADBENEF.NSP:258-268` | Mistério | <!-- mystery: CALLNAT 'VALBENEF' retorna #QTY-ERRS, mas nenhum erro bloqueia a gravação. Confirmar se o modo aviso pendente de revisão desde 2011 ainda é o comportamento desejado --> |
| 19 | QUANDO a operação for inclusão, o sistema DEVE gravar o registro no arquivo 150 com data de cadastro e data de atualização iguais à data corrente | Orientada a evento | `CADBENEF.NSP:271-295` | Inferida | Sem correspondência direta; RN-011 afirma que não há exclusão física no DDM BENEFIC |
| 20 | O endereço informado é gravado com perda dos últimos caracteres | — | `CADBENEF.NSP:277-279`, `CADBENEF.NSP:308` | Mistério | <!-- mystery: o comentário do chamado 4471/2003 declara que um endereço A80 é gravado em campo A60 e que os últimos 20 bytes se perdem. O mesmo MOVE se repete no ramo de alteração, sem o comentário. Confirmar se houve correção posterior ou se a perda persiste em produção --> |
| 21 | QUANDO um cadastro for criado ou alterado, o sistema DEVE registrar o evento na trilha de auditoria do arquivo 153 | Orientada a evento | `CADBENEF.NSP:296-303`, `CADBENEF.NSP:320-326`, `CADBENEF.NSP:418` | Confirmada | RN-010, §1.2. O documento cita o subprograma `LOGAUDIT`; o código usa o copycode `CCAUDIT` com a sub-rotina `WRITE-AUDIT` |
| 22 | QUANDO a operação for alteração, o sistema DEVE atualizar apenas parte dos campos informados na tela | Orientada a evento | `CADBENEF.NSP:306-327` | Mistério | <!-- mystery: o ramo de alteração não regrava DT-BIRTH, SEX, COD-PROGRAM, COD-REGION nem NUM-NIS, embora a tela colete todos. Confirmar se a omissão é intencional ou silenciosa --> |
| 23 | SE a operação não for reconhecida no desvio final, ENTÃO o sistema DEVE informar operação inválida | Indesejada | `CADBENEF.NSP:329-331` | Mistério | <!-- mystery: o ramo NONE parece inalcançável, pois a regra 1 já encerra o fluxo para operação diferente de I ou A. Confirmar se existe caminho que chegue ao DECIDE com outro valor --> |
| 24 | SE ocorrer erro de execução Natural, ENTÃO o sistema DEVE desfazer a transação e encerrar com código 12 | Indesejada | `CADBENEF.NSP:423-428` | Inferida | Sem correspondência no levantamento de 2012 |

### Divergências entre código e levantamento de 2012

Registradas como achado, não como correção. O levantamento é documento de época e pode divergir por projeto; consulte [`DECLARED-DRIFT.md`](legacy-sifap/DECLARED-DRIFT.md).

| Item do documento | O que o código mostra | Onde |
|---|---|---|
| RN-002 — bloqueio só para situação ativa, com reinclusão de excluído lógico | A duplicidade é bloqueada sem consultar a situação cadastral | `CADBENEF.NSP:213-217` |
| RN-006 — recusar menores de 16 anos | Nenhuma verificação de idade mínima | `CADBENEF.NSP:176-180` |
| RN-005 — região válida de 01 a 27, com 99 reservado | Nenhuma validação de região neste programa | `CADBENEF.NSP:271-295` |
| RN-007 — dados bancários obrigatórios | A view `BENEFIC` usada aqui não expõe campos bancários | `CADBENEF.NSP:16-36` |
| RN-011 — exclusão lógica de beneficiário | O programa implementa apenas inclusão e alteração | `CADBENEF.NSP:271-331` |
| Nomes de campo `BN-*` usados no documento | A view usa `NUM-CPF`, `STAT-BENEFICIARY`, `QTY-DEPEND`, `COD-REGION` | `CADBENEF.NSP:16-36` |

> [!NOTE]
> Duplique a seção acima para cada programa `.NSP` ou `.NSN` lido pela sua dupla.

---

## Leitura de dependências de `CADBENEF.NSP`

Foram lidos cinco membros de apoio e `VALBENEF.NSN`, programa atribuído à Dupla 4. `CCVALCPF.NSC` é uma dependência indireta, incluída por `SUBVALCP.NSN`. Esta leitura estática não representa validação humana das regras nem conclusão da leitura atribuída à Dupla 4.

| Membro | Como é referenciado | Linha em `CADBENEF.NSP` |
|---|---|---|
| `PDAVALID.NSA` | `LOCAL USING PDAVALID` | `CADBENEF.NSP:14` |
| `SUBVALCP.NSN` | `CALLNAT 'SUBVALCP'` | `CADBENEF.NSP:161` |
| `SUBVALNI.NSN` | `CALLNAT 'SUBVALNI'` | `CADBENEF.NSP:196` |
| `VALBENEF.NSN` | `CALLNAT 'VALBENEF'` | `CADBENEF.NSP:263` |
| `CCAUDIT.NSC` | `INCLUDE CCAUDIT` | `CADBENEF.NSP:418` |
| `CCVALCPF.NSC` | `INCLUDE CCVALCPF` dentro de `SUBVALCP` | `SUBVALCP.NSN:94` |

### O contrato da família de validação

`PDAVALID.NSA:31-41` declara dez códigos de retorno. A leitura dos dois subprogramas mostra quais são efetivamente emitidos.

| Código | Significado declarado | Emitido por | Evidência |
|---|---|---|---|
| 0000 | Documento válido | `SUBVALCP`, `SUBVALNI` | `SUBVALCP.NSN:81`, `SUBVALNI.NSN:89` |
| 1001 | CPF inválido — dígito verificador | `SUBVALCP` | `SUBVALCP.NSN:75` |
| 1002 | CPF não informado | `SUBVALCP` | `SUBVALCP.NSN:57` |
| 1003 | CPF com todos os dígitos iguais | **ninguém** | só aparece em `PDAVALID.NSA:35` |
| 1004 | Tipo de documento inválido | `SUBVALCP`, `SUBVALNI` | `SUBVALCP.NSN:51`, `SUBVALNI.NSN:59` |
| 1005 | CPF com caractere não numérico | `SUBVALCP` | `SUBVALCP.NSN:63` |
| 1010 | NIS não informado | `SUBVALNI` | `SUBVALNI.NSN:65` |
| 1011 | NIS inválido — dígito verificador | `SUBVALNI` | `SUBVALNI.NSN:83` |
| 1012 | NIS com caractere não numérico | `SUBVALNI` | `SUBVALNI.NSN:71` |
| 9999 | Erro Natural | ambos | `SUBVALCP.NSN:86`, `SUBVALNI.NSN:94` |

### Caminhos de validação de CPF consultados

O próprio copycode padrão adverte que as cópias não são equivalentes e que o chamado 6620/2011 continua aberto (`CCVALCPF.NSC:32-37`).

| Caminho | Exige apenas dígitos | Rejeita dígitos iguais | Exceção | Evidência |
|---|---|---|---|---|
| Rotina interna de `CADBENEF` | `DECIDE` aceita caracteres de 0 a 9 e rejeita `NONE VALUE` | Não contém teste de igualdade de todos os dígitos | CPF zero é barrado antes da rotina | `CADBENEF.NSP:145-149`, `CADBENEF.NSP:344-413` |
| `CCVALCPF` via `SUBVALCP` | Sim | Sim | — | `CCVALCPF.NSC:45`, `CCVALCPF.NSC:79-90` |
| `VALBENEF` | `DECIDE` aceita caracteres de 0 a 9 e rejeita `NONE VALUE` | Sim | A exceção dos três zeros só é testada dentro de `IF #ALL-EQUAL` | `VALBENEF.NSN:202-245` |
| `VALDOCS` | `DECIDE` aceita caracteres de 0 a 9 e rejeita `NONE VALUE` | Não contém teste de igualdade de todos os dígitos | Rotina posterior de prefixos especiais pode alterar resultado e contador | [VALDOCS.NSP:137-241](legacy-sifap/natural-programs/VALDOCS.NSP#L137) |

Ausência de `MASK` não significa ausência de rejeição de caracteres. Comparar essas implementações exige preservar conversões, estados e o uso do retorno pelo chamador; não foi executado teste de equivalência Natural.

### Como cada mistério mudou

| Regra | Situação após a leitura das dependências |
|---|---|
| 3 | **Agravada.** Não há uma validação de CPF, há três, com resultados diferentes para a mesma entrada |
| 5 | **Precisa.** `SUBVALCP` calcula 1001, 1002, 1005 e 9999, e `CADBENEF` descarta todos; o caminho que decide é o mais fraco dos três |
| 10 | **Precisa.** `SUBVALNI` distingue 1010, 1011 e 1012, mas `CADBENEF` só emite aviso e grava assim mesmo |
| 17 | **Parcialmente resolvida.** `S` pertence ao domínio aceito por `VALBENEF.NSN:174-175` (`A`, `S`, `C`, `I`, `D`); o significado permanece indocumentado |
| 18 | **Precisa.** `VALBENEF` verifica CPF, data, nome, UF e situação, e devolve até dez mensagens que `CADBENEF` nunca lê |
| 21 | **Confirmada com ressalvas.** `CCAUDIT.NSC:60-100` grava de fato no arquivo 153, mas com semente de sequência lida uma vez por execução |

### Achados novos trazidos pelos membros de apoio

| # | Achado | Evidência | Classificação |
|---|---|---|---|
| 25 | O código 1003 é inalcançável; um CPF com dígitos iguais retorna 1001 e é diagnosticado como erro de dígito verificador | `PDAVALID.NSA:35`, `SUBVALCP.NSN:75` | Mistério |
| 26 | `#CPF-EQUAL` é declarado em `SUBVALCP` e usado pelo `CCVALCPF` inserido por `INCLUDE`; a afirmação anterior de variável sem uso era um erro de leitura isolada. | [SUBVALCP.NSN:41](legacy-sifap/natural-programs/SUBVALCP.NSN#L41), [SUBVALCP.NSN:94](legacy-sifap/natural-programs/SUBVALCP.NSN#L94), [CCVALCPF.NSC:80-90](legacy-sifap/natural-programs/CCVALCPF.NSC#L80) | Retificada; não contar como mistério |
| 27 | `#PV-IND-SPECIAL` recebe `N` fixo nos dois subprogramas; o valor `S` previsto no contrato nunca ocorre | `PDAVALID.NSA:55`, `SUBVALCP.NSN:45`, `SUBVALNI.NSN:53` | Mistério |
| 28 | `VALBENEF` aceita as situações `A`, `S`, `C`, `I` e `D`, e **não** aceita `E`, que o levantamento de 2012 usa para exclusão lógica | `VALBENEF.NSN:174-175` | Mistério |
| 29 | Fevereiro é sempre validado com 29 dias | `VALBENEF.NSN:104` | Mistério |
| 30 | A view de `BENEFIC` em `VALBENEF` é declarada e nunca lida desde 1998 | `VALBENEF.NSN:29` | Mistério |
| 31 | A validação de UF é inteiramente pulada quando a UF vem em branco | `VALBENEF.NSN:156` | Inferida |
| 32 | O nome é aceito quando contém ao menos um espaço a partir da segunda posição | `VALBENEF.NSN:316-331` | Inferida |
| 33 | A semente da sequência de auditoria é lida uma vez por execução e incrementada em memória | `CCAUDIT.NSC:65-72` | Mistério |
| 34 | A hora do evento perde a fração: `*TIMN` é `N7` e o campo do DDM é `N6` | `CCAUDIT.NSC:75-77` | Mistério |
| 35 | O campo `COD-PROFILE` do DDM não é preenchido pela rotina; chamado 7742 em aberto | `CCAUDIT.NSC:50-51` | Mistério |
| 36 | A ação `CO` não pode ser registrada desde 2010, mas a rotina não bloqueia e transfere a responsabilidade ao chamador | `CCAUDIT.NSC:45-48` | Mistério |

---

## Regras de `CADDEPEN.NSP`

**Lido em:** 2026-09-17 · Cabeçalho: ANA LUCIA PEREIRA, criado em 20/06/1998, última alteração em 12/09/2012 (`CADDEPEN.NSP:1-11`).

| # | Enunciado da regra | Candidato EARS | Origem | Classificação | Notas |
|---|---|---|---|---|---|
| 37 | SE o CPF do titular não existir no arquivo 150, ENTÃO o sistema DEVE recusar o cadastro de dependente | Indesejada | `CADDEPEN.NSP:105-108` | Inferida | — |
| 38 | SE a situação do titular for `C` ou `D`, ENTÃO o sistema DEVE recusar a inclusão de dependente | Indesejada | `CADDEPEN.NSP:110-113` | Mistério | <!-- mystery: as situações `S` (suspenso) e `I` (inativo) atravessam a verificação. Confirmar se um titular suspenso pode mesmo ganhar dependentes --> |
| 39 | SE a quantidade de dependentes for maior que 5, ENTÃO o sistema DEVE recusar novas inclusões | Indesejada | `CADDEPEN.NSP:117-120` | Mistério | <!-- mystery: a verificação ocorre antes do incremento, de modo que a sexta ocorrência é aceita; o grupo periódico do DDM permite 10 e o levantamento de 2012 declara 3 --> |
| 40 | SE o nome do dependente estiver em branco, ENTÃO o sistema DEVE recusar a inclusão | Indesejada | `CADDEPEN.NSP:147-150` | Inferida | — |
| 41 | SE o grau de parentesco não for `FI`, `CO`, `IR` ou `OU`, ENTÃO o sistema DEVE recusar a inclusão | Indesejada | `CADDEPEN.NSP:152-156` | Mistério | <!-- mystery: o DDM define FI, CJ, NT e TU para o mesmo campo; três dos quatro códigos aceitos pelo programa não existem no dicionário de dados --> |
| 42 | O sistema DEVE validar o CPF do dependente pela rotina padrão do copycode | Ubíqua | `CADDEPEN.NSP:167-171`, `CADDEPEN.NSP:230` | Mistério | <!-- mystery: a mensagem de CPF inválido é movida para #MSG, que nunca aparece em um WRITE; o aviso é invisível e a inclusão prossegue --> |
| 43 | SE o CPF do dependente já constar no grupo periódico e for diferente de zero, ENTÃO o sistema DEVE recusar a inclusão | Indesejada | `CADDEPEN.NSP:174-184` | Inferida | Dependente sem CPF escapa da verificação de duplicidade |
| 44 | QUANDO um dependente for aceito, o sistema DEVE gravá-lo na próxima ocorrência do grupo periódico e incrementar a quantidade | Orientada a evento | `CADDEPEN.NSP:191-203` | Inferida | — |
| 45 | Documento e sexo do dependente são coletados na tela e não são gravados | — | `CADDEPEN.NSP:198-201` | Mistério | <!-- mystery: chamado 4471/2003 declara que os campos não existem no arquivo 150; os MOVE seguem comentados e a tela continua pedindo os dados --> |
| 46 | A situação e o indicador de deficiência do dependente nunca recebem valor | — | `CADDEPEN.NSP:25-26` | Mistério | <!-- mystery: ambos são declarados na view e nunca atribuídos; o DDM define domínios A/I/D e S/N, e branco não pertence a nenhum deles --> |
| 47 | QUANDO um dependente for incluído, o sistema DEVE registrar auditoria como alteração do titular | Orientada a evento | `CADDEPEN.NSP:204-211` | Inferida | Ação `AL` sobre a entidade `BENF`, sem identificar o dependente |

---

## Regras de `CADPROG.NSP`

**Lido em:** 2026-09-17 · Cabeçalho: MARCOS ANTONIO RIBEIRO, criado em 10/09/1997, última alteração em 18/11/2012 (`CADPROG.NSP:1-11`).

| # | Enunciado da regra | Candidato EARS | Origem | Classificação | Notas |
|---|---|---|---|---|---|
| 48 | SE a operação não for `I` nem `C`, ENTÃO o sistema DEVE recusar a entrada | Indesejada | `CADPROG.NSP:84-87` | Inferida | — |
| 49 | ONDE a operação for consulta, o sistema DEVE exibir os dados do programa e encerrar | Opcional | `CADPROG.NSP:89-92`, `CADPROG.NSP:156-171` | Inferida | A consulta não grava auditoria, o que é coerente com a vedação da ação `CO` |
| 50 | SE já existir programa com o código informado, ENTÃO o sistema DEVE recusar a inclusão | Indesejada | `CADPROG.NSP:118-121` | Inferida | — |
| 51 | O sistema DEVE calcular o valor-base aplicando o fator `1,00 + (fator de ajuste × 0,347215)` | Ubíqua | `CADPROG.NSP:124-125` | Mistério | <!-- mystery: a constante 0,347215 não aparece em nenhum documento nem no DDM; o levantamento de 2012 cita um FACTOR-K que ninguém soube explicar --> |
| 52 | QUANDO um programa for incluído, o sistema DEVE gravar o valor **já ajustado** no campo de valor-base individual | Orientada a evento | `CADPROG.NSP:130`, `CADPROG.NSP:137` | Mistério | <!-- mystery: o valor ajustado e o fator de ajuste são gravados juntos; qualquer recálculo posterior que reaplique o fator o aplicaria duas vezes --> |
| 53 | QUANDO um programa for incluído, o sistema DEVE atribuir a situação `A` | Orientada a evento | `CADPROG.NSP:134` | Inferida | Domínio do DDM: `A`, `I`, `E` |
| 54 | O programa aceita tipo, datas, idades e renda máxima sem qualquer validação | — | `CADPROG.NSP:95-105` | Mistério | <!-- mystery: nenhum campo da tela de inclusão é criticado; apenas a operação e a duplicidade de código são verificadas --> |
| 55 | A consulta detecta ausência de registro testando o contador após o laço | — | `CADPROG.NSP:166-169` | Mistério | <!-- mystery: o comentário declara estilo de 1997 não padronizado e chamado 3312/2004 em aberto --> |

---

## Confronto com os quatro DDMs

Os quatro arquivos `.ddm` foram consultados. As evidências de código e de dicionário devem ser confrontadas, mas essa comparação não encerra nenhuma pergunta nem confirma um ID canônico. A revisão integral dos DDMs e da FDT está em andamento.

### Evidências encontradas nos DDMs

| Pergunta | O que o DDM mostra | Evidência |
|---|---|---|
| Qual é o domínio de `STAT-BENEFICIARY`? | `A`=ativo, `S`=**suspenso**, `C`=cancelado, `I`=inativo, `D`=desligado | `BENEFIC.ddm:74-75` |
| `COD-PROFILE` existe mesmo? | Sim, `A3`, com domínio `ADM/OPR/CON/AUD/SUP`; confirma o chamado 7742 | `AUDIT.ddm:76` |
| A colisão de sequência de auditoria é grave? | `NUM-AUDIT` é **único** no Adabas, então uma repetição vira erro de gravação | `AUDIT.ddm:31` |
| A hora do evento perde precisão? | O campo é `N6` (`HHMMSS`), enquanto `*TIMN` devolve `N7` | `AUDIT.ddm:33` |
| `FACTOR-K` existe fora do código? | Sim, campo `BG`, marcado `>>> UNDOCUMENTED <<<`, inserido em ago/2008 "a pedido da SENARC", sem detalhes no chamado | `SOCPROG.ddm:47-51` |

### Contradições novas, todas com evidência dos dois lados

| # | Contradição | Código | Dicionário de dados ou documento |
|---|---|---|---|
| 56 | Códigos de parentesco divergentes | `FI`, `CO`, `IR`, `OU` em `CADDEPEN.NSP:152-153` | `FI`, `CJ`, `NT`, `TU` em `BENEFIC.ddm:91-92` |
| 57 | Significado do código de região | Nenhuma validação no código | `01-05 ou 99` em `BENEFIC.ddm:66` e `1=N 2=NE 3=CO 4=SE 5=S 6=ESP` em `SOCPROG.ddm:87`, contra "01 a 27, estados" em RN-005 |
| 58 | Limite de dependentes | Sexta ocorrência aceita em `CADDEPEN.NSP:117-120` | Grupo periódico `(1:10)` em `BENEFIC.ddm:87`, contra "máximo 3" em RN-004 |
| 59 | Quantidade de faixas de cálculo | — | Grupo periódico `(1:5)` em `SOCPROG.ddm:69`, contra "até 10 faixas" em RN-017 |
| 60 | Auditoria em nível de campo | `CCAUDIT` grava apenas texto livre em `DESCR-ACTION` | `GRP-BEFORE` e `GRP-AFTER`, com 20 ocorrências cada, existem e nunca são preenchidos: `AUDIT.ddm:61-66`, contra RN-010 |
| 61 | Número do arquivo do cadastro de programas | Cabeçalho diz arquivo 155 em `CADPROG.NSP:10`, corpo diz 151 em `CADPROG.NSP:109` | `FNR: 151` em `SOCPROG.ddm:21` |
| 62 | `FACTOR-K` calculado e nunca persistido | `CADPROG.NSP:124-125` calcula em variável local | O campo `BG FACTOR-K` do DDM permanece sem gravação: `SOCPROG.ddm:47` |
| 63 | Código de ação `DV` não existe no domínio | — | O rodapé cita volume de `'CO'/'DV'`, mas `COD-ACTION` não define `DV`: `AUDIT.ddm:39-48` contra `AUDIT.ddm:128` |
| 64 | Consultas continuaram sendo auditadas depois da vedação | — | O rodapé atribui 193,8 milhões de registros a `CO`/`DV` entre 01/2014 e 03/2018, embora a Portaria 213/2010 vede o registro de `CO`: `AUDIT.ddm:128` |

> [!WARNING]
> Os totais de registros dos DDMs vêm de uma execução ADAREP de **14/03/2018** e descrevem aquele momento, não a população atual. A [cronologia](legacy-sifap/CHRONOLOGY.md) trata essa confusão como armadilha documentada. A medição atual cabe ao DBA.

---

## Regras de BATCHPGT

Leitura integral do membro, incluindo `DEFINE DATA`, a sub-rotina de faixa e o tratamento de erro. São candidatas de leitura estática, não requisitos aprovados. `PDAVALID`, `PDACALC` e `LDASIFAP` ampliam o vocabulário local; os resultados `#PC-*` não devem ser confundidos com os acumuladores `#AMT-*`.

| # | Condição e comportamento observado | Padrão candidato | Origem | Classificação |
|---|---|---|---|---|
| 65 | Se o período de entrada for zero, usa ano e mês da data da execução; caso contrário, decompõe o período informado em ano e mês. | Orientada a evento | [BATCHPGT.NSP:161-176](legacy-sifap/natural-programs/BATCHPGT.NSP#L161) | Inferida |
| 66 | Na leitura ordenada por CPF, ignora CPF igual ao anterior e, em seguida, situações diferentes de `A`; ambos incrementam ignorados. | Orientada a evento | [BATCHPGT.NSP:250-266](legacy-sifap/natural-programs/BATCHPGT.NSP#L250) | Inferida |
| 67 | Se `SUBVALCP` retornar código não zero, escreve mensagem e rejeição no work file 2, incrementa erros/rejeições e passa ao próximo beneficiário. | Indesejada | [BATCHPGT.NSP:276-288](legacy-sifap/natural-programs/BATCHPGT.NSP#L276) | Inferida |
| 68 | Se houver pagamento para o superdescritor CPF + competência, ignora a geração, sem filtrar a situação do pagamento nessa consulta. Qual é a política para reprocessar pagamentos cancelados? | Não promover | [BATCHPGT.NSP:294-298](legacy-sifap/natural-programs/BATCHPGT.NSP#L294) | Mistério <!-- mystery: Qual é a política de reprocessamento por situação do pagamento? --> |
| 69 | No bloco sem programa, registra rejeição e atribui `X`; após a busca, testa `X` e depois situação diferente de `A`. Como se comporta esse caminho sem registro na execução Natural? | Não promover | [BATCHPGT.NSP:302-325](legacy-sifap/natural-programs/BATCHPGT.NSP#L302) | Mistério <!-- mystery: O marcador de ausência é preservado ao sair do FIND? --> |
| 70 | Para ano de nascimento menor que 100, expande abaixo do pivô para 2000 + ano e os demais para 1900 + ano; depois calcula idade pela diferença de anos. | Orientada a evento | [BATCHPGT.NSP:329-348](legacy-sifap/natural-programs/BATCHPGT.NSP#L329) | Inferida |
| 71 | Após `VALELEG`, retorno não zero incrementa ignorados e interrompe aquele beneficiário. `CALCBENF` é chamado depois, sem teste do seu código de retorno nesse ponto. Como devem ser tratados seus erros e resultados? | Não promover | [BATCHPGT.NSP:369-387](legacy-sifap/natural-programs/BATCHPGT.NSP#L369) | Mistério <!-- mystery: Qual resultado de cálculo deve governar a gravação da folha? --> |
| 72 | Para região entre 1 e 25, usa a posição da tabela local; fora desse intervalo, usa fator 1.0000. | Orientada a evento | [BATCHPGT.NSP:390-394](legacy-sifap/natural-programs/BATCHPGT.NSP#L390) | Inferida |
| 73 | Fator familiar: zero dependentes = 1; até dois = `1 + quantidade * 0.05`; até quatro = `1.10 + (quantidade - 2) * 0.03`; demais = `1.16 + (quantidade - 4) * 0.02`. | Orientada a evento | [BATCHPGT.NSP:397-409](legacy-sifap/natural-programs/BATCHPGT.NSP#L397) | Inferida |
| 74 | Usa a primeira faixa cujo teto comporte a renda. O fator não é reinicializado na sub-rotina quando nenhuma faixa corresponde. Qual deve ser o resultado acima do último teto? | Não promover | [BATCHPGT.NSP:586-593](legacy-sifap/natural-programs/BATCHPGT.NSP#L586) | Mistério <!-- mystery: Qual fator deve ser usado quando nenhuma faixa de renda corresponde? --> |
| 75 | Fator etário: idade >= 65 usa 1.15; de 60 a 64 usa 1.10; abaixo de 18 usa 1.05; demais usam 1.00. | Orientada a evento | [BATCHPGT.NSP:415-427](legacy-sifap/natural-programs/BATCHPGT.NSP#L415) | Inferida |
| 76 | O cálculo local multiplica base e fatores regional, familiar, renda e idade, aplica `1 + ajuste` e passa por temporário inteiro em centavos. Esses valores locais alimentam a gravação. Qual equivalência é exigida com `CALCBENF`? | Não promover | [BATCHPGT.NSP:430-439](legacy-sifap/natural-programs/BATCHPGT.NSP#L430) | Mistério <!-- mystery: A fórmula local deve permanecer equivalente à do subprograma chamado? --> |
| 77 | Em dezembro, tipo vira `D`, soma uma parcela `base * região * idade` e, para programa `A`, acrescenta 15% do benefício calculado. Fora de dezembro, mantém tipo `N` e bônus zero. | Orientada a evento | [BATCHPGT.NSP:437-454](legacy-sifap/natural-programs/BATCHPGT.NSP#L437) | Inferida |
| 78 | Se bruto > 500, calcula desconto local de 3%; caso contrário, desconto zero. Qual é a relação desse desconto com o programa `CALCDSCT` citado no cabeçalho? | Não promover | [BATCHPGT.NSP:456-462](legacy-sifap/natural-programs/BATCHPGT.NSP#L456) | Mistério <!-- mystery: O desconto simplificado substitui ou complementa o cálculo de CALCDSCT? --> |
| 79 | Líquido negativo vira zero. Grava pagamento `G` e confirma a transação antes de escrever o extrato de 240 posições. Como reconciliar falha no extrato depois do commit? | Não promover | [BATCHPGT.NSP:465-503](legacy-sifap/natural-programs/BATCHPGT.NSP#L465) | Mistério <!-- mystery: Como a reexecução recupera um extrato não escrito após um pagamento confirmado? --> |
| 80 | A cada múltiplo de 1000 pagamentos gerados escreve progresso; acumula bruto, desconto, líquido e bônus. | Orientada a evento | [BATCHPGT.NSP:505-516](legacy-sifap/natural-programs/BATCHPGT.NSP#L505) | Inferida |
| 81 | Após auditoria do ciclo e fechamento dos arquivos: zero gerados retorna 8; havendo gerados e rejeições retorna 4; demais retornam 0. | Orientada a evento | [BATCHPGT.NSP:539-566](legacy-sifap/natural-programs/BATCHPGT.NSP#L539) | Inferida |
| 82 | Em erro Natural, escreve contexto, desfaz a transação corrente, fecha os dois arquivos e retorna 12; o código não desfaz commits anteriores. | Indesejada | [BATCHPGT.NSP:572-582](legacy-sifap/natural-programs/BATCHPGT.NSP#L572) | Inferida |

## Regras de BATCHREL

`DEFINE DATA` separa valores `P13.2` regionais, totais `P15.2`, contadores `N8`, arrays de cinco posições e linha de arquivo `A132`. `AT BREAK` e `AT END OF DATA` escrevem contagens no log; não são chamadas externas.

| # | Condição e comportamento observado | Padrão candidato | Origem | Classificação |
|---|---|---|---|---|
| 83 | Período zero termina com 12. Lê pagamentos a partir da competência e interrompe ao encontrar uma diferente; quebras e fim dos dados escrevem contagens. | Orientada a evento | [BATCHREL.NSP:119-138](legacy-sifap/natural-programs/BATCHREL.NSP#L119) | Inferida |
| 84 | Região começa em zero e é obtida buscando o beneficiário por CPF. Agrupa 1-5, 6-10, 11-15 e 16-20 nas quatro primeiras posições; todos os demais vão à quinta. Como devem ser classificados ausentes e região 99? | Não promover | [BATCHREL.NSP:141-163](legacy-sifap/natural-programs/BATCHREL.NSP#L141) | Mistério <!-- mystery: Como classificar regiões ausentes, especiais ou fora da tabela? --> |
| 85 | Antes dos totais regional e geral, soma 0.005 ao bruto em variável `P13.2` e usa temporário inteiro; totais por situação recebem o bruto original. Qual é o efeito numérico efetivo dessa sequência? | Não promover | [BATCHREL.NSP:167-195](legacy-sifap/natural-programs/BATCHREL.NSP#L167) | Mistério <!-- mystery: Os totais por região e situação devem usar o mesmo arredondamento? --> |
| 86 | `G/P/C/D/E` selecionam índices 1/2/3/4/5; qualquer outro código vai ao índice 1. Os rótulos são GENERATED/PAID/CANCELED/RETURNED/REVERSED. Como alinhar esses rótulos ao DDM? | Não promover | [BATCHREL.NSP:97-101](legacy-sifap/natural-programs/BATCHREL.NSP#L97), [BATCHREL.NSP:177-190](legacy-sifap/natural-programs/BATCHREL.NSP#L177) | Mistério <!-- mystery: Qual correspondência de situação deve aparecer nos relatórios? --> |
| 87 | Se não houver pagamentos contados, escreve ausência e retorna 4. Caso contrário, imprime os subtotais e total, escreve a cópia no work file 1 e retorna 0. | Orientada a evento | [BATCHREL.NSP:203-252](legacy-sifap/natural-programs/BATCHREL.NSP#L203) | Inferida |
| 88 | Em erro Natural, escreve contexto, desfaz a transação corrente, fecha o work file 1 e retorna 12. O cabeçalho de impressão incrementa a página e reinicia a linha em 5. | Indesejada | [BATCHREL.NSP:258-278](legacy-sifap/natural-programs/BATCHREL.NSP#L258) | Inferida |

## Regras de BATCHCON

`DEFINE DATA` distingue registro CNAB `A240`, documento bancário `A10`, número de pagamento `N15`, valor textual `A15`, centavos `N15` e valores monetários `P9.2`. O nome de arquivo digitado não é usado para vincular o work file no corpo lido.

| # | Condição e comportamento observado | Padrão candidato | Origem | Classificação |
|---|---|---|---|---|
| 89 | Só processa detalhe de tipo `3`. Extrai CPF, valor, data, retorno e documento por posições fixas e divide o valor em centavos por 100. | Orientada a evento | [BATCHCON.NSP:135-166](legacy-sifap/natural-programs/BATCHCON.NSP#L135) | Inferida |
| 90 | Busca pelo número do documento convertido e aceita correspondência apenas se CPF e competência também coincidirem; ausência incrementa não encontrados e pula o detalhe. | Orientada a evento | [BATCHCON.NSP:169-185](legacy-sifap/natural-programs/BATCHCON.NSP#L169) | Inferida |
| 91 | Converte diferença negativa em positiva; diferença > 0.01 gera divergência e auditoria própria. Diferença <= 0.01 entra na conciliação. | Orientada a evento | [BATCHCON.NSP:188-202](legacy-sifap/natural-programs/BATCHCON.NSP#L188) | Inferida |
| 92 | Retorno `00` grava situação `P`, data de crédito, banco numérico 1 no campo `A3` e código de retorno. Qual semântica de situação e representação de banco é esperada? | Não promover | [BATCHCON.NSP:204-213](legacy-sifap/natural-programs/BATCHCON.NSP#L204) | Mistério <!-- mystery: O retorno 00 deve gravar P e qual representação deve ter COD-BANK? --> |
| 93 | Retornos `01` e `02` gravam respectivamente `D` e `E`, com confirmação da transação em cada ramo. | Orientada a evento | [BATCHCON.NSP:214-227](legacy-sifap/natural-programs/BATCHCON.NSP#L214) | Inferida |
| 94 | Retorno desconhecido apenas escreve mensagem; o contador de conciliados já foi incrementado e a auditoria de conciliação ainda é chamada. Como esse caso deve afetar o resultado do ciclo? | Não promover | [BATCHCON.NSP:201-235](legacy-sifap/natural-programs/BATCHCON.NSP#L201) | Mistério <!-- mystery: Retorno desconhecido deve contar como conciliado? --> |
| 95 | A auditoria de conciliação grava ação `CO`; a de divergência grava `DV` e valores anterior/novo escalares. Como esses códigos se relacionam à política e ao domínio documentados? | Não promover | [BATCHCON.NSP:311-343](legacy-sifap/natural-programs/BATCHCON.NSP#L311) | Mistério <!-- mystery: Qual é a política de auditoria para as ações CO e DV da conciliação? --> |
| 96 | Transfere a sequência local para o copycode antes da auditoria final `BT`, confirma e fecha o arquivo. Divergências ou não encontrados retornam 4; caso contrário retorna 0. | Orientada a evento | [BATCHCON.NSP:275-294](legacy-sifap/natural-programs/BATCHCON.NSP#L275) | Inferida |
| 97 | Em erro Natural, escreve contexto, desfaz a transação corrente, fecha o arquivo e retorna 12. O bloco de outro banco está comentado e não integra esse fluxo executável. | Indesejada | [BATCHCON.NSP:245-258](legacy-sifap/natural-programs/BATCHCON.NSP#L245), [BATCHCON.NSP:299-308](legacy-sifap/natural-programs/BATCHCON.NSP#L299) | Inferida |

---

## Regras de CALCBENF

O contrato é `PARAMETER USING PDACALC`, mas o programa relê beneficiário e programa. `DEFINE DATA` contém valores `P9.2`, temporário `N11`, fatores `N3.4`, tabela regional de 27 posições e cinco faixas de renda. As views e as variáveis locais não provam, sozinhas, ausência de efeitos de escrita.

| # | Condição e comportamento observado | Padrão candidato | Origem | Classificação |
|---|---|---|---|---|
| 98 | Mês fora de 1-12 retorna 2020 e mensagem, saindo da rotina. | Indesejada | [CALCBENF.NSN:154-162](legacy-sifap/natural-programs/CALCBENF.NSN#L154) | Inferida |
| 99 | Beneficiário ausente retorna 2001; situação diferente de `A` retorna 2002; programa ausente retorna 2003. Os ramos saem da rotina. | Indesejada | [CALCBENF.NSN:166-197](legacy-sifap/natural-programs/CALCBENF.NSN#L166) | Inferida |
| 100 | Usa região 1-25 na tabela, demais com fator 1. A árvore de fator familiar separa zero, até dois, até quatro e demais, com as fórmulas do item 73. | Orientada a evento | [CALCBENF.NSN:200-219](legacy-sifap/natural-programs/CALCBENF.NSN#L200) | Inferida |
| 101 | Calcula idade por diferença de anos e aplica fatores 1.15/1.10/1.05/1.00 nos mesmos intervalos do item 75. A janela de século nesta seção está comentada. | Orientada a evento | [CALCBENF.NSN:223-252](legacy-sifap/natural-programs/CALCBENF.NSN#L223) | Inferida |
| 102 | Escolhe a primeira faixa que comporte a renda; sem correspondência, a sub-rotina não atribui um fator. Qual saída é esperada acima do último teto? | Não promover | [CALCBENF.NSN:347-354](legacy-sifap/natural-programs/CALCBENF.NSN#L347) | Mistério <!-- mystery: Qual resultado deve ser devolvido para renda fora de todas as faixas? --> |
| 103 | Multiplica base pelos quatro fatores, aplica `1 + ajuste` e converte por temporário inteiro em centavos. A documentação RN-014 descreve truncamento; isso não comprova equivalência entre todas as fórmulas. | Ubíqua | [CALCBENF.NSN:259-269](legacy-sifap/natural-programs/CALCBENF.NSN#L259) | Inferida |
| 104 | Em dezembro soma `base * região * idade`; programa `A` recebe também 15% do benefício e os demais recebem bônus zero. O comentário menciona meses ativos/12, mas o corpo usa fator etário. Qual fórmula deve prevalecer? | Não promover | [CALCBENF.NSN:271-293](legacy-sifap/natural-programs/CALCBENF.NSN#L271) | Mistério <!-- mystery: A parcela adicional deve usar meses ativos ou fator etário? --> |
| 105 | Desconto simplificado é 3% se bruto > 500, zero nos demais casos; líquido negativo vira zero, com passagem por temporário inteiro. | Orientada a evento | [CALCBENF.NSN:295-306](legacy-sifap/natural-programs/CALCBENF.NSN#L295), [CALCBENF.NSN:358-366](legacy-sifap/natural-programs/CALCBENF.NSN#L358) | Inferida |
| 106 | Executa `STORE PAYMENT-V` e commit antes de devolver valores; esse bloco não atribui `NUM-PAYMENT`. O chamador também grava pagamento. Qual contrato de persistência e numeração é esperado? | Não promover | [CALCBENF.NSN:308-328](legacy-sifap/natural-programs/CALCBENF.NSN#L308), [BATCHPGT.NSP:473-489](legacy-sifap/natural-programs/BATCHPGT.NSP#L473) | Mistério <!-- mystery: Quem deve numerar e persistir o pagamento na cadeia chamada? --> |
| 107 | O tratamento de erro escreve diagnóstico, desfaz a transação corrente e termina com 12, em vez de devolver 9999 no contrato da PDA. | Indesejada | [CALCBENF.NSN:370-376](legacy-sifap/natural-programs/CALCBENF.NSN#L370) | Inferida |

## Regras de CALCCORR

`DEFINE DATA` usa competências `N6`, valores `P9.2`, total `P11.2`, índice acumulado `N5.6` e matriz `N3.6/1:10,1:12`. A área de parâmetros de documentos alimenta a chamada de CPF; não há `PARAMETER USING PDACALC` neste programa.

| # | Condição e comportamento observado | Padrão candidato | Origem | Classificação |
|---|---|---|---|---|
| 108 | Início maior que fim escreve erro e sai. CPF rejeitado por `SUBVALCP` escreve a mensagem e sai; sucesso copia o CPF formatado. | Indesejada | [CALCCORR.NSP:151-168](legacy-sifap/natural-programs/CALCCORR.NSP#L151) | Inferida |
| 109 | Lê por CPF, para ao mudar CPF, ignora competências anteriores ao início e para ao ultrapassar o fim. A ordenação por CPF garante a ordem de competência necessária a essa parada? | Não promover | [CALCCORR.NSP:174-184](legacy-sifap/natural-programs/CALCCORR.NSP#L174) | Mistério <!-- mystery: A parada pelo período é válida dentro da leitura ordenada apenas por CPF? --> |
| 110 | Pagamentos já marcados com `IND-CORR = S` são ignorados. | Orientada a estado | [CALCCORR.NSP:186-188](legacy-sifap/natural-programs/CALCCORR.NSP#L186) | Inferida |
| 111 | Inicia fator 1 e usa uma vez o índice do ano/mês do pagamento. Só três anos recebem valores na matriz; não há laço avançando até o período final. Qual acumulação era pretendida? | Não promover | [CALCCORR.NSP:87-127](legacy-sifap/natural-programs/CALCCORR.NSP#L87), [CALCCORR.NSP:191-196](legacy-sifap/natural-programs/CALCCORR.NSP#L191), [CALCCORR.NSP:229-239](legacy-sifap/natural-programs/CALCCORR.NSP#L229) | Mistério <!-- mystery: A correção deveria acumular vários meses e como tratar índices não cadastrados? --> |
| 112 | Multiplica o bruto pelo fator e calcula diferença. Somente diferença positiva grava o valor corrigido em `AMT-CORR`, data e indicador `S`, acumulando a diferença no total. | Orientada a evento | [CALCCORR.NSP:198-219](legacy-sifap/natural-programs/CALCCORR.NSP#L198) | Inferida |
| 113 | O commit do pagamento precede `WRITE-AUDIT`; o copycode não faz commit. Qual garantia de auditoria é exigida para a última correção do lote? | Não promover | [CALCCORR.NSP:204-219](legacy-sifap/natural-programs/CALCCORR.NSP#L204), [CCAUDIT.NSC:57-58](legacy-sifap/natural-programs/CCAUDIT.NSC#L57) | Mistério <!-- mystery: Como é confirmada a auditoria após o último pagamento corrigido? --> |
| 114 | Erro Natural desfaz apenas a transação corrente e termina com 12. O bloco de correção monetária histórica comentado não participa do cálculo executável. | Indesejada | [CALCCORR.NSP:129-143](legacy-sifap/natural-programs/CALCCORR.NSP#L129), [CALCCORR.NSP:247-253](legacy-sifap/natural-programs/CALCCORR.NSP#L247) | Inferida |

## Regras de CALCDSCT

`DEFINE DATA` expõe oito ocorrências de desconto, tipo do DDM `A3` e variável local de tipo `A1`, valores `P9.2`, percentuais `P3.2`, temporário `N11` e quatro faixas de contribuição. A existência de uma view não equivale a uma atualização de todos os seus campos.

| # | Condição e comportamento observado | Padrão candidato | Origem | Classificação |
|---|---|---|---|---|
| 115 | Procura pagamento por número e exige CPF correspondente; ausência sai. Depois verifica a existência do beneficiário, saindo quando o contador é zero. | Indesejada | [CALCDSCT.NSP:79-99](legacy-sifap/natural-programs/CALCDSCT.NSP#L79) | Inferida |
| 116 | A primeira faixa que comporte o bruto aplica 3%, 5%, 7% ou 9%, com tetos 500, 1000, 2000 e 9999.99. Sem faixa, a sub-rotina não acrescenta contribuição. | Orientada a evento | [CALCDSCT.NSP:62-69](legacy-sifap/natural-programs/CALCDSCT.NSP#L62), [CALCDSCT.NSP:197-205](legacy-sifap/natural-programs/CALCDSCT.NSP#L197) | Inferida |
| 117 | Desconto com fim não zero anterior a hoje é ignorado; início posterior a hoje também é ignorado. A referência usada é a data da execução, não a competência do pagamento. | Orientada a estado | [CALCDSCT.NSP:117-123](legacy-sifap/natural-programs/CALCDSCT.NSP#L117) | Inferida |
| 118 | Para tipo local `J`, valor fixo positivo prevalece; caso contrário usa percentual do bruto, acrescentando ao acumulado sem aplicar teto nessa iteração. | Orientada a evento | [CALCDSCT.NSP:127-137](legacy-sifap/natural-programs/CALCDSCT.NSP#L127) | Inferida |
| 119 | Para `P`, valor fixo positivo prevalece; caso contrário usa percentual, acrescentando ao acumulado. | Orientada a evento | [CALCDSCT.NSP:138-146](legacy-sifap/natural-programs/CALCDSCT.NSP#L138) | Inferida |
| 120 | Para `I`, usa percentual cadastrado; para `S`, usa 1% do bruto. | Orientada a evento | [CALCDSCT.NSP:147-155](legacy-sifap/natural-programs/CALCDSCT.NSP#L147) | Inferida |
| 121 | Para `A`, usa valor fixo positivo ou percentual; o ramo `NONE` não acrescenta item. | Orientada a evento | [CALCDSCT.NSP:156-167](legacy-sifap/natural-programs/CALCDSCT.NSP#L156) | Inferida |
| 122 | Após cada ocorrência diferente de `J`, limita o acumulado inteiro a 30% do bruto. Uma ocorrência posterior pode limitar valor judicial já acumulado. Qual resultado é esperado para diferentes ordens do PE? | Não promover | [CALCDSCT.NSP:106-110](legacy-sifap/natural-programs/CALCDSCT.NSP#L106), [CALCDSCT.NSP:170-174](legacy-sifap/natural-programs/CALCDSCT.NSP#L170) | Mistério <!-- mystery: A exceção judicial deve depender da ordem dos descontos no grupo periódico? --> |
| 123 | O tipo `A3` é movido para `A1` antes do `DECIDE`. Como interpretar os códigos de duas letras do DDM nesse despacho de uma letra? | Não promover | [CALCDSCT.NSP:22-23](legacy-sifap/natural-programs/CALCDSCT.NSP#L22), [CALCDSCT.NSP:45](legacy-sifap/natural-programs/CALCDSCT.NSP#L45), [CALCDSCT.NSP:125-167](legacy-sifap/natural-programs/CALCDSCT.NSP#L125) | Mistério <!-- mystery: Qual correspondência de códigos de desconto é válida entre A3 e A1? --> |
| 124 | Trunca o total e atualiza somente `AMT-DISC-TOTAL`, com commit; esse caminho não atribui líquido nem chama auditoria. Quem deve manter esses dados consistentes? | Não promover | [CALCDSCT.NSP:179-188](legacy-sifap/natural-programs/CALCDSCT.NSP#L179) | Mistério <!-- mystery: Quem recalcula o líquido e audita a alteração do total de descontos? --> |
| 125 | Erro Natural escreve diagnóstico, desfaz a transação corrente e termina com 12. | Indesejada | [CALCDSCT.NSP:209-215](legacy-sifap/natural-programs/CALCDSCT.NSP#L209) | Inferida |

---

## Regras de VALBENEF

Os parâmetros incluem CPF `A11`, nome `A60`, nascimento/CEP `N8`, sexo/UF/situação e saídas `#RESULT A1`, `#QTY-ERRS N2`, `#MSG-ERR A60/1:10`. O corpo possui rotinas locais de CPF, data e nome; as tabelas de UF e dias são locais, apesar do `USING LDASIFAP`.

| # | Condição e comportamento observado | Padrão candidato | Origem | Classificação |
|---|---|---|---|---|
| 126 | Inicia resultado `V` e zero erros; falhas nas rotinas de CPF, data ou nome acrescentam mensagem e mudam resultado para `I`, sem interromper as validações seguintes. | Orientada a evento | [VALBENEF.NSN:116-151](legacy-sifap/natural-programs/VALBENEF.NSN#L116) | Inferida |
| 127 | Converte cada caractere de 0 a 9 em dígito; `NONE VALUE` marca CPF inválido e sai da rotina local. | Indesejada | [VALBENEF.NSN:196-227](legacy-sifap/natural-programs/VALBENEF.NSN#L196) | Inferida |
| 128 | No ramo em que todos os dígitos são iguais, o teste dos três primeiros zeros retorna válido; demais sequências iguais retornam inválido. Qual é a finalidade dessa exceção, restrita a esse ramo? | Não promover | [VALBENEF.NSN:230-245](legacy-sifap/natural-programs/VALBENEF.NSN#L230) | Mistério <!-- mystery: Qual é a finalidade da exceção dos zeros dentro do teste de todos os dígitos iguais? --> |
| 129 | Para cada dígito verificador, resto < 2 produz zero, caso contrário produz 11 menos resto; divergência invalida o CPF. Qual equivalência numérica existe entre esse `COMPUTE` do resto e o `DIVIDE ... REMAINDER` do copycode? | Não promover | [VALBENEF.NSN:247-280](legacy-sifap/natural-programs/VALBENEF.NSN#L247), [CCVALCPF.NSC:99-128](legacy-sifap/natural-programs/CCVALCPF.NSC#L99) | Mistério <!-- mystery: Os cálculos de resto são equivalentes sob os formatos numéricos Natural usados? --> |
| 130 | Rejeita ano anterior a 1900 ou posterior ao atual, mês fora de 1-12 e dia fora do tamanho tabelado; fevereiro contém 29. A janela de século comentada não é executada. | Orientada a evento | [VALBENEF.NSN:104](legacy-sifap/natural-programs/VALBENEF.NSN#L104), [VALBENEF.NSN:284-313](legacy-sifap/natural-programs/VALBENEF.NSN#L284) | Inferida |
| 131 | Nome em branco falha; nos demais, a posição do primeiro espaço precisa ser > 1. Como distinguir separação de sobrenome do preenchimento à direita do campo `A60`? | Não promover | [VALBENEF.NSN:316-331](legacy-sifap/natural-programs/VALBENEF.NSN#L316) | Mistério <!-- mystery: A validação de nome distingue sobrenome de espaços de preenchimento? --> |
| 132 | UF em branco não é testada; UF preenchida deve coincidir com uma das 27 entradas. Situação fora de `A/S/C/I/D` acrescenta erro. | Orientada a evento | [VALBENEF.NSN:156-179](legacy-sifap/natural-programs/VALBENEF.NSN#L156) | Inferida |
| 133 | Sexo e CEP são recebidos, mas não participam de testes nesse corpo; a view de beneficiário é declarada sem acesso a dados. Qual cobertura se espera desse contrato? | Não promover | [VALBENEF.NSN:15-71](legacy-sifap/natural-programs/VALBENEF.NSN#L15), [VALBENEF.NSN:126-179](legacy-sifap/natural-programs/VALBENEF.NSN#L126) | Mistério <!-- mystery: Sexo, CEP e confronto com o cadastro pertencem à responsabilidade deste validador? --> |
| 134 | Erro Natural acrescenta diagnóstico ao vetor, marca resultado `I` e sai da rotina. | Indesejada | [VALBENEF.NSN:186-193](legacy-sifap/natural-programs/VALBENEF.NSN#L186) | Inferida |

## Regras de VALDOCS

`DEFINE DATA` inclui CPF/NIS `N11`, RG/CTPS `A15`, título `A12`, cinco mensagens `A60`, oito prefixos `A3` e a PDA de documentos. O programa é de entrada e saída em tela, não uma rotina chamada por `CALLNAT` no corpus encontrado.

| # | Condição e comportamento observado | Padrão candidato | Origem | Classificação |
|---|---|---|---|---|
| 135 | CPF ou RG reprovado incrementa erros e marca resultado `I`; depois é executado o tratamento especial. | Orientada a evento | [VALDOCS.NSP:78-98](legacy-sifap/natural-programs/VALDOCS.NSP#L78) | Inferida |
| 136 | CPF zero falha; cada caractere não pertencente a 0-9 também invalida e sai da rotina de CPF. | Indesejada | [VALDOCS.NSP:137-170](legacy-sifap/natural-programs/VALDOCS.NSP#L137) | Inferida |
| 137 | Cada resto menor que 2 gera verificador zero, demais geram 11 menos resto; divergência com o dígito informado invalida o CPF. | Orientada a evento | [VALDOCS.NSP:172-204](legacy-sifap/natural-programs/VALDOCS.NSP#L172) | Inferida |
| 138 | RG em branco falha. Usa a posição anterior ao primeiro espaço, ou 15 quando não há espaço; tamanho menor que cinco falha. | Orientada a evento | [VALDOCS.NSP:207-223](legacy-sifap/natural-programs/VALDOCS.NSP#L207) | Inferida |
| 139 | Prefixo coincidente com a tabela `000/001/002/010/011/099/100/999` marca documento especial, restaura resultado `V` e zera a quantidade de erros anteriores. Qual autorização sustenta esse tratamento? | Não promover | [VALDOCS.NSP:58-65](legacy-sifap/natural-programs/VALDOCS.NSP#L58), [VALDOCS.NSP:228-241](legacy-sifap/natural-programs/VALDOCS.NSP#L228) | Mistério <!-- mystery: Quais erros podem ser desconsiderados por um prefixo especial? --> |
| 140 | A validação de NIS vem depois do tratamento especial: retorno não zero volta a marcar `I`. A mensagem de documento especial pode coexistir com resultado inválido. | Orientada a evento | [VALDOCS.NSP:106-125](legacy-sifap/natural-programs/VALDOCS.NSP#L106) | Inferida |
| 141 | Título e CTPS são coletados sem testes no corpo; a view contém `IND-DOCS-OK`, mas não há gravação. Quem mantém esse indicador consumido pela elegibilidade? | Não promover | [VALDOCS.NSP:18-24](legacy-sifap/natural-programs/VALDOCS.NSP#L18), [VALDOCS.NSP:67-125](legacy-sifap/natural-programs/VALDOCS.NSP#L67) | Mistério <!-- mystery: Quem valida os documentos adicionais e persiste IND-DOCS-OK? --> |
| 142 | Erro Natural escreve diagnóstico, marca resultado `I` e termina com 12. | Indesejada | [VALDOCS.NSP:128-134](legacy-sifap/natural-programs/VALDOCS.NSP#L128) | Inferida |

## Regras de VALELEG

`DEFINE DATA` recebe `PDACALC`, possui motivos `A60/1:10`, código específico `A5`, idades `N3` e renda `P9.2`. O limite lido do programa é `MAX-PERCAP-INCOME P7.2`; os nomes dos campos não substituem a leitura das comparações.

| # | Condição e comportamento observado | Padrão candidato | Origem | Classificação |
|---|---|---|---|---|
| 143 | Beneficiário ou programa ausente retorna 2001 ou 2003; programa não ativo retorna 2004, sempre com saída antecipada. | Indesejada | [VALELEG.NSN:84-118](legacy-sifap/natural-programs/VALELEG.NSN#L84) | Inferida |
| 144 | Relê dados do beneficiário e recalcula a idade pelo ano de execução, substituindo valores recebidos da PDA. Que data deve reger uma reexecução de competência passada? | Não promover | [VALELEG.NSN:68-97](legacy-sifap/natural-programs/VALELEG.NSN#L68) | Mistério <!-- mystery: A elegibilidade retroativa deve usar a idade atual ou a idade na competência? --> |
| 145 | Depois de verificar existência e programa ativo, região 99 retorna zero e sai antes dos demais testes. O chamador batch já filtra situações não ativas; o alcance não pode ser generalizado para toda a cadeia. | Não promover | [VALELEG.NSN:114-128](legacy-sifap/natural-programs/VALELEG.NSN#L114), [BATCHPGT.NSP:263-266](legacy-sifap/natural-programs/BATCHPGT.NSP#L263) | Mistério <!-- mystery: Qual é o alcance autorizado da exceção de região 99? --> |
| 146 | Fora da exceção, situações `S`, `C/D` e `I` acrescentam motivos próprios. Outros códigos diferentes de `A` não recebem motivo nessa árvore. Como tratar situações fora do domínio? | Não promover | [VALELEG.NSN:133-151](legacy-sifap/natural-programs/VALELEG.NSN#L133) | Mistério <!-- mystery: Como a elegibilidade deve tratar uma situação cadastral desconhecida? --> |
| 147 | Limite de idade positivo é aplicado: menor que mínimo ou maior que máximo acrescenta motivo. Limite zero não aciona o teste correspondente. | Orientada a evento | [VALELEG.NSN:156-169](legacy-sifap/natural-programs/VALELEG.NSN#L156) | Inferida |
| 148 | Se o limite de renda for positivo e a renda familiar ultrapassá-lo, acrescenta motivo. Como comparar renda familiar total a um campo descrito como teto per capita? | Não promover | [VALELEG.NSN:92](legacy-sifap/natural-programs/VALELEG.NSN#L92), [VALELEG.NSN:111](legacy-sifap/natural-programs/VALELEG.NSN#L111), [VALELEG.NSN:174-180](legacy-sifap/natural-programs/VALELEG.NSN#L174) | Mistério <!-- mystery: A renda usada nesta comparação deveria ser total ou per capita? --> |
| 149 | Tipo `A`: renda > 600 combinada com menos de um dependente reprova; documentação diferente de `S` reprova independentemente desse primeiro teste. | Orientada a evento | [VALELEG.NSN:185-200](legacy-sifap/natural-programs/VALELEG.NSN#L185) | Inferida |
| 150 | Tipo `P` reprova idade < 60; tipo `T` reprova idade fora de 16-65; tipo desconhecido sempre acrescenta motivo. | Orientada a evento | [VALELEG.NSN:201-219](legacy-sifap/natural-programs/VALELEG.NSN#L201) | Inferida |
| 151 | Código específico preenchido: `R` na primeira posição verifica NIS zero na view; `D` na segunda verifica ausência de dependentes. As outras posições não têm teste nesse corpo. Como assegurar o dado da view após o `FIND`? | Não promover | [VALELEG.NSN:224-226](legacy-sifap/natural-programs/VALELEG.NSN#L224), [VALELEG.NSN:249-267](legacy-sifap/natural-programs/VALELEG.NSN#L249) | Mistério <!-- mystery: Quais posições do código de elegibilidade são significativas e como é preservado o NIS lido? --> |
| 152 | Elegível retorna zero e limpa mensagem; não elegível retorna 2010 e apenas o primeiro motivo. | Orientada a evento | [VALELEG.NSN:231-237](legacy-sifap/natural-programs/VALELEG.NSN#L231) | Inferida |
| 153 | Erro Natural devolve 9999 e diagnóstico pela PDA, saindo da rotina. | Indesejada | [VALELEG.NSN:240-246](legacy-sifap/natural-programs/VALELEG.NSN#L240) | Inferida |

---

## Regras de CONSBENF

`DEFINE DATA` diferencia pesquisas numéricas, chave CPF `A11`, máscara `A14`, endereço `A80` e arrays de histórico de 12 posições. A exibição usa diretamente o cursor de pagamentos, não esses arrays.

| # | Condição e comportamento observado | Padrão candidato | Origem | Classificação |
|---|---|---|---|---|
| 154 | PF3 encerra o laço; tipo vazio vira `C`. Em consulta por CPF, retorno não zero de `SUBVALCP` causa `REINPUT` no campo. | Orientada a evento | [CONSBENF.NSP:119-144](legacy-sifap/natural-programs/CONSBENF.NSP#L119) | Inferida |
| 155 | `C` busca pelo CPF formatado; `N` busca por NIS. Ausência causa `REINPUT`; tipo diferente dos dois causa erro de tipo. O caminho NIS não chama `SUBVALNI`. | Orientada a evento | [CONSBENF.NSP:147-166](legacy-sifap/natural-programs/CONSBENF.NSP#L147) | Inferida |
| 156 | Situações `A/S/C/I/D` recebem as descrições ACTIVE/SUSPENDED/CANCELED/INACTIVE/TERMINATED; demais recebem UNKNOWN. | Orientada a evento | [CONSBENF.NSP:228-241](legacy-sifap/natural-programs/CONSBENF.NSP#L228) | Inferida |
| 157 | CPF numérico abaixo de 10000000000 mostra o primeiro grupo de três caracteres; demais mostram os grupos finais. Qual máscara é autorizada em cada superfície? | Não promover | [CONSBENF.NSP:298-311](legacy-sifap/natural-programs/CONSBENF.NSP#L298) | Mistério <!-- mystery: A máscara deve variar conforme o valor numérico do CPF? --> |
| 158 | Interrompe histórico ao mudar CPF ou quando o contador ultrapassa 12; zero registros produz mensagem. A leitura por CPF não declara ordenação temporal decrescente. São os últimos 12 ou os primeiros 12 do cursor? | Não promover | [CONSBENF.NSP:270-288](legacy-sifap/natural-programs/CONSBENF.NSP#L270) | Mistério <!-- mystery: Qual ordenação deve definir os doze pagamentos exibidos? --> |
| 159 | Após a consulta, grava auditoria `CO/BENF` e commit; o CPF da entidade é copiado dentro da exibição. Como se aplica a política de consultas descrita no copycode? | Não promover | [CONSBENF.NSP:172-179](legacy-sifap/natural-programs/CONSBENF.NSP#L172), [CONSBENF.NSP:202-205](legacy-sifap/natural-programs/CONSBENF.NSP#L202) | Mistério <!-- mystery: Qual política autoriza a auditoria CO de consultas cadastrais? --> |
| 160 | O handler escreve diagnóstico e executa `ESCAPE ROUTINE`; não contém `BACKOUT TRANSACTION` nem `TERMINATE`. Qual continuidade e estado transacional devem ser garantidos? | Não promover | [CONSBENF.NSP:188-193](legacy-sifap/natural-programs/CONSBENF.NSP#L188) | Mistério <!-- mystery: Qual deve ser o comportamento da consulta após um erro Natural? --> |
| 161 | Compõe endereço de rua, número e bairro em `A80`, exibindo com `AL=60`. Qual parcela do endereço precisa permanecer visível? | Não promover | [CONSBENF.NSP:207-210](legacy-sifap/natural-programs/CONSBENF.NSP#L207), [CONSBENF.NSP:244-263](legacy-sifap/natural-programs/CONSBENF.NSP#L244) | Mistério <!-- mystery: Qual limite de apresentação de endereço é aceito pela equipe? --> |

## Regras de RELPGT

`DEFINE DATA` contém competências `N6`, filtro numérico `N4` convertido para `A4`, acumuladores `P13.2`, nome de apresentação `A30`, máscaras `A14` e paginação `N2/N4`.

| # | Condição e comportamento observado | Padrão candidato | Origem | Classificação |
|---|---|---|---|---|
| 162 | Lê o intervalo de competência; filtro de programa zero aceita todos, e filtro não zero exclui códigos diferentes. | Orientada a evento | [RELPGT.NSP:123-138](legacy-sifap/natural-programs/RELPGT.NSP#L123) | Inferida |
| 163 | Ao mudar código de programa, se havia anterior, imprime e reinicia subtotal. A leitura é ordenada por competência, não por programa. O subtotal deve representar grupos contíguos ou o programa no período inteiro? | Não promover | [RELPGT.NSP:123-149](legacy-sifap/natural-programs/RELPGT.NSP#L123) | Mistério <!-- mystery: Qual ordenação sustenta o subtotal por programa? --> |
| 164 | Zera nome/UF antes da busca de beneficiário e usa `IGNORE` no bloco sem registros; o nome exibido é limitado a 30 caracteres. Qual saída é esperada para pagamento sem beneficiário correspondente? | Não promover | [RELPGT.NSP:151-161](legacy-sifap/natural-programs/RELPGT.NSP#L151) | Mistério <!-- mystery: Como apresentar pagamentos sem beneficiário correspondente? --> |
| 165 | A máscara esconde apenas os três primeiros caracteres e mantém os grupos seguintes. Como conciliá-la com a máscara de consulta cadastral? | Não promover | [RELPGT.NSP:163-167](legacy-sifap/natural-programs/RELPGT.NSP#L163) | Mistério <!-- mystery: As máscaras de CPF dos relatórios e da consulta devem ser iguais? --> |
| 166 | Tipos `N/D/T` são NORMAL/13TH/THIRD e demais OTHER; situações `G/P/C/D/E` são CREATED/PAID/CANCELED/RETURNED/REVERSED e demais OTHER. Qual domínio deve reger esses rótulos? | Não promover | [RELPGT.NSP:170-195](legacy-sifap/natural-programs/RELPGT.NSP#L170) | Mistério <!-- mystery: Como alinhar descrições de tipo e situação aos DDMs? --> |
| 167 | Reinicia totais no início dos dados, pagina quando linha >= máximo - 5 e imprime último subtotal quando há programa anterior; no fim dos dados imprime total geral. | Orientada a evento | [RELPGT.NSP:115-129](legacy-sifap/natural-programs/RELPGT.NSP#L115), [RELPGT.NSP:198-230](legacy-sifap/natural-programs/RELPGT.NSP#L198), [RELPGT.NSP:246-271](legacy-sifap/natural-programs/RELPGT.NSP#L246) | Inferida |
| 168 | Erro Natural escreve na impressora lógica 1, desfaz a transação corrente e termina com 12. | Indesejada | [RELPGT.NSP:237-243](legacy-sifap/natural-programs/RELPGT.NSP#L237) | Inferida |

## Regras de RELAUDIT

`DEFINE DATA` contém datas `N8`, ação `A2`, usuário `A8`, entidade `A4`, modo `A1`, contadores `N8` e hora formatada `A8`. A view expõe valores anterior/novo escalares `A60`, mas o detalhe não os imprime.

| # | Condição e comportamento observado | Padrão candidato | Origem | Classificação |
|---|---|---|---|---|
| 169 | Modo vazio vira `T`; início zero vira o literal 19970101; fim zero vira a data de execução. | Orientada a evento | [RELAUDIT.NSP:99-108](legacy-sifap/natural-programs/RELAUDIT.NSP#L99) | Inferida |
| 170 | Lê por data no intervalo, reinicia contadores no início, ignora datas anteriores e para após o fim. Cada filtro preenchido de ação, usuário ou entidade exclui valores diferentes. | Orientada a evento | [RELAUDIT.NSP:111-157](legacy-sifap/natural-programs/RELAUDIT.NSP#L111) | Inferida |
| 171 | Ação `EX` é excluída antes do filtro solicitado, inclusive quando esse filtro pede `EX`. Qual autorização sustenta a exclusão desses eventos da apresentação? | Não promover | [RELAUDIT.NSP:130-141](legacy-sifap/natural-programs/RELAUDIT.NSP#L130) | Mistério <!-- mystery: Eventos EX devem ser omitidos mesmo em uma consulta explícita por exclusões? --> |
| 172 | `IN/AL/CO/CN/DV` alimentam contadores e rótulos distintos; `CO` é chamado de conciliação e `CN` de consulta. Como esse vocabulário se relaciona ao domínio do DDM? | Não promover | [RELAUDIT.NSP:163-182](legacy-sifap/natural-programs/RELAUDIT.NSP#L163) | Mistério <!-- mystery: Qual vocabulário de ações é válido entre escritores e relatório? --> |
| 173 | Pagina pelo limite de linhas. `T` escreve em tela e qualquer outro modo escreve na impressora, com descrição adicional; o cabeçalho reinicia a linha em 7. | Orientada a evento | [RELAUDIT.NSP:190-211](legacy-sifap/natural-programs/RELAUDIT.NSP#L190), [RELAUDIT.NSP:279-303](legacy-sifap/natural-programs/RELAUDIT.NSP#L279) | Inferida |
| 174 | Na quebra por dia, imprime subtotal somente fora do modo `T` e zera o contador diário. No fim dos dados, imprime total também somente fora de `T`. | Orientada a evento | [RELAUDIT.NSP:215-230](legacy-sifap/natural-programs/RELAUDIT.NSP#L215) | Inferida |
| 175 | O histograma para impressão usa apenas o intervalo de datas; os filtros de ação/usuário/entidade e a exclusão de `EX` não são reaplicados. Que universo deve representar o histograma? | Não promover | [RELAUDIT.NSP:256-266](legacy-sifap/natural-programs/RELAUDIT.NSP#L256) | Mistério <!-- mystery: O histograma deve contar todos os eventos ou somente os eventos exibidos? --> |
| 176 | Erro Natural escreve diagnóstico e termina com 12. | Indesejada | [RELAUDIT.NSP:271-276](legacy-sifap/natural-programs/RELAUDIT.NSP#L271) | Inferida |

## Contratos dos membros Natural de apoio

Estes registros complementam as regras dos chamadores. Uma diretiva `INCLUDE` incorpora os testes no objeto que a utiliza; não é uma chamada externa.

| # | Membro e ramos examinados | Origem | Classificação |
|---|---|---|---|
| 177 | `SUBVALCP`: tipo diferente de C retorna 1004; CPF vazio/zero retorna 1002; não numérico retorna 1005; copycode reprovado retorna 1001; sucesso retorna zero; erro Natural retorna 9999. Todos saem pela PDA. | [SUBVALCP.NSN:44-96](legacy-sifap/natural-programs/SUBVALCP.NSN#L44) | Inferida |
| 178 | `SUBVALNI`: tipo diferente de N retorna 1004; vazio/zero retorna 1010; não numérico retorna 1012; divergência do verificador retorna 1011; sucesso zero; erro 9999. O cálculo usa pesos 3,2,9,8,7,6,5,4,3,2, resto por divisão, zero se resto < 2, senão 11 menos resto. O `DECIDE` converte 0-9 e tem alternativa zero, precedida pelo teste numérico. | [SUBVALNI.NSN:52-152](legacy-sifap/natural-programs/SUBVALNI.NSN#L52) | Inferida |
| 179 | `CCVALCPF`: reprova máscara não numérica, caractere não reconhecido, todos os dígitos iguais e divergência de qualquer verificador. Nos dois verificadores, resto < 2 produz zero; demais produzem 11 menos resto. `#CPF-EQUAL` é efetivamente usado. | [CCVALCPF.NSC:39-130](legacy-sifap/natural-programs/CCVALCPF.NSC#L39) | Inferida |
| 180 | `CCAUDIT`: quando a semente é zero, lê o maior número; incrementa, atribui identificação/data/hora e grava. Apenas ação `BT` preenche os campos específicos de batch. Não há filtro de `CO`, handler nem commit no copycode. | [CCAUDIT.NSC:60-100](legacy-sifap/natural-programs/CCAUDIT.NSC#L60) | Inferida |
| 181 | `PDACALC`: define nove entradas e sete saídas, incluindo CPF `A11`, programa `A4`, competência `N6`, região `A2`, valores `P9.2`, código `N4` e mensagem `A60`. Os nomes de uma cadeia no comentário não comprovam chamadas. | [PDACALC.NSA:49-79](legacy-sifap/natural-programs/PDACALC.NSA#L49) | Inferida |
| 182 | `LDASIFAP`: define e inicializa tabelas locais de fatores, UF, rendas, contribuições, dias e pivô de século 50; não executa validação por si só. A adoção dos campos `#L-*` precisa ser distinguida das cópias locais. | [LDASIFAP.NSL:32-107](legacy-sifap/natural-programs/LDASIFAP.NSL#L32) | Inferida |
| 183 | `PDAVALID`: três entradas (`A1`, `A11`, `A11`) e três saídas (`N4`, `A60`, `A1`). A lista de códigos documentada não prova que cada chamador os trate nem que todos sejam emitidos. | [PDAVALID.NSA:31-57](legacy-sifap/natural-programs/PDAVALID.NSA#L31) | Inferida |

---

## Resumo geral

| Métrica | Valor |
|---|---:|
| Programas atribuídos lidos | 4 de 15: três cadastros e `VALBENEF`, lido como dependência |
| Membros de apoio lidos | 5 de 9: `PDAVALID`, `SUBVALCP`, `SUBVALNI`, `CCAUDIT`, `CCVALCPF` |
| DDMs consultados | 4 de 4; revisão integral e confronto com a FDT pendentes |
| Itens catalogados | 64 |
| Classificações dos itens | Em revisão; não equivalem ao placar dos 20 mistérios canônicos |
| Validação humana | Pendente; nenhuma pergunta foi encerrada |

---

## Definição de pronto

- [ ] Todo bloco condicional dos programas atribuídos foi examinado.
- [ ] Toda regra cita `arquivo:linha`.
- [ ] Toda questão em aberto está registrada em `mysteries-found.md` sem conclusão.

---

### Continue lendo

| Anterior | Próximo |
|---|---|
| [Inventário](inventory.md)<br/><sub>Passo 1 — varredura de arquivos.</sub> | [Mapa de Dependências](dependency-map.md)<br/><sub>Passo 3 — grafo de chamadas e acessos.</sub> |

<sub>[Voltar ao índice do kit](../README.md)</sub>
