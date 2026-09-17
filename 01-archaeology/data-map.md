# Mapa de dados do legado SIFAP

> **Trilha:** [Kit do Time](../README.md) > [Estágio 1](README.md) > **Mapa de dados**

**Leitura dos quatro DDMs e da listagem FDT, com estruturas e relações rastreáveis.** Este documento descreve evidências do acervo, não um schema de destino nem uma inspeção do banco em execução.

| Campo | Valor |
|---|---|
| Público-alvo | DBA, QA e Arquitetura |
| Data da leitura | 2026-09-17 |
| Escopo | DBID 057; quatro DDMs publicados e FDT do arquivo 150 |
| Validação humana | Pendente |

## Como ler as evidências

`A` e `N` nos DDMs indicam formatos lógicos; `P` é decimal compactado. A listagem física usa `U` para decimal não compactado. Não confunda o `U` da coluna de descritor do DDM, que indica unicidade, com o `U` da coluna FORMAT da FDT. Preserve escala e precisão dos valores monetários; qualquer futura tradução deverá usar decimal exato, não ponto flutuante.

As observações de domínio em `Remark` documentam intenção, mas não comprovam validação de todos os valores pelo Adabas. `D/U/S/H/P` identificam descritores; `N` em armazenamento corresponde à supressão de nulos. Uma view declarada em um programa não comprova leitura nem gravação: essas operações estão em [dependency-map.md](dependency-map.md).

## Arquivos e chaves

| DDM | Identificação | Chaves e descritores de busca | Evidência |
|---|---|---|---|
| BENEFIC | FNR 150, sequência AA | AA matrícula `N11` e AB CPF `A11` únicos; AM NIS `N11` e AN benefício `N13` únicos com supressão de nulos | [BENEFIC.ddm:31-53](legacy-sifap/adabas-ddms/BENEFIC.ddm#L31) |
| SOCPROG | FNR 151, sequência AA | AA programa `A4` único; tipo, situação e código de elegibilidade pesquisáveis | [SOCPROG.ddm:20-37](legacy-sifap/adabas-ddms/SOCPROG.ddm#L20), [SOCPROG.ddm:65](legacy-sifap/adabas-ddms/SOCPROG.ddm#L65) |
| PAYMENT | FNR 152, sequência AA | AA pagamento `N15` único; AB CPF `A11`, AD programa `A4`, AE competência `N6` e AF ciclo `N6` descritores | [PAYMENT.ddm:26-39](legacy-sifap/adabas-ddms/PAYMENT.ddm#L26) |
| AUDIT | FNR 153, sequência AA | AA evento `N15` único; data, ação, entidade, chave da entidade, CPF, usuário e terminal pesquisáveis | [AUDIT.ddm:23-57](legacy-sifap/adabas-ddms/AUDIT.ddm#L23), [AUDIT.ddm:74-81](legacy-sifap/adabas-ddms/AUDIT.ddm#L74) |

ISN é identificação física do registro, não sinônimo automático de CPF, matrícula ou número de pagamento. A observação de não usar ISN como identificador externo está em [PAYMENT.ddm:162-163](legacy-sifap/adabas-ddms/PAYMENT.ddm#L162).

## Estruturas de BENEFIC

| Grupo ou família | Campos e formatos relevantes | Multiplicidade/domínio declarado | Evidência |
|---|---|---|---|
| Identificação AA-AN | Matrícula `N11`, CPF `A11`, nomes `A60`, nascimento `N8`, sexo `A1`, documentos RG, NIS `N11`, benefício `N13` | Sexo M/F/I; nomes de mãe/pai e dados do RG têm supressão de nulos conforme a coluna S | [BENEFIC.ddm:39-53](legacy-sifap/adabas-ddms/BENEFIC.ddm#L39) |
| Endereço BA-BJ | Rua `A60`, número `A10`, complemento `A30`, bairro/cidade `A40`, UF/região `A2`, CEP `N8`, IBGE `N7` | Grupo simples; região anotada como 01-05 ou 99 | [BENEFIC.ddm:57-66](legacy-sifap/adabas-ddms/BENEFIC.ddm#L57) |
| Benefício CA-CL | Programa `A4`, datas `N8`, situação `A1`, renda familiar `P9,2`, membros/dependentes `N2`, per capita `P7,2`, documentos `A1` | Situação A/S/C/I/D; documentos S/N; renda total e per capita são campos distintos | [BENEFIC.ddm:70-83](legacy-sifap/adabas-ddms/BENEFIC.ddm#L70) |
| Dependentes DA-DG | CPF `A11`, nome `A60`, nascimento `N8`, parentesco `A2`, situação/deficiência `A1` | PE de 10; parentesco FI/CJ/NT/TU; situação A/I/D; deficiência S/N | [BENEFIC.ddm:87-94](legacy-sifap/adabas-ddms/BENEFIC.ddm#L87) |
| Contato EA-ED | Telefones `A14/A15`, email `A80`, telefone adicional `A15` | ED é MU de cinco valores | [BENEFIC.ddm:98-101](legacy-sifap/adabas-ddms/BENEFIC.ddm#L98) |
| Biometria FA-FD | Indicador `A1`, data `N8`, estação `A6`, hash `A64` | S/N/P; o hash é anotado como não implementado, sem prova de operação de biometria | [BENEFIC.ddm:105-108](legacy-sifap/adabas-ddms/BENEFIC.ddm#L105) |
| Controle GA-GG | Datas `N8`, horas `N6`, usuários `A8`, versão `N5` | Campo de versão não prova que todos os escritores implementem controle de concorrência | [BENEFIC.ddm:112-118](legacy-sifap/adabas-ddms/BENEFIC.ddm#L112) |
| Banco HA-HE | Banco `A3`, agência `A6`, conta `A13`, tipo/portabilidade `A1` | Tipo C/P/S e portabilidade S/N | [BENEFIC.ddm:122-126](legacy-sifap/adabas-ddms/BENEFIC.ddm#L122) |
| Óbito/bloqueio IA-IG | Indicadores `A1`, data `N8`, razão `A2`, processo `A20`, órgão pagador `N5` | SISOBI e bloqueio judicial aparecem como anotações, não como integração executável comprovada | [BENEFIC.ddm:130-135](legacy-sifap/adabas-ddms/BENEFIC.ddm#L130) |
| Representante JA-JB | Indicador `A1`, CPF `A11` descritor | JA/JB não aparecem nas linhas de campos da FDT fornecida | [BENEFIC.ddm:139-140](legacy-sifap/adabas-ddms/BENEFIC.ddm#L139) |

Descritores derivados: PN fonético de AC; SA ano por AF(1-4); S2 UF + situação; S3 programa + situação; H1 AF + CJ por HYPEREXIT 03. A implementação dessa saída não está no acervo: [BENEFIC.ddm:144-153](legacy-sifap/adabas-ddms/BENEFIC.ddm#L144).

## Estruturas de SOCPROG

| Grupo ou família | Campos e formatos relevantes | Multiplicidade/domínio declarado | Evidência |
|---|---|---|---|
| Identificação AA-AI | Código `A4`, nome `A60`, sigla/órgão `A10`, lei `A20`, datas `N8`, tipo/situação `A1` | Tipo A/T/P; situação A/I/E | [SOCPROG.ddm:28-37](legacy-sifap/adabas-ddms/SOCPROG.ddm#L28) |
| Valores BA-BH | Bases individual/familiar e piso `P7,2`, teto `P9,2`, percentual `P3,2`, data `N8`, K `P5,4`, ajuste `P3,4` | K e ajuste são campos distintos; K possui anotação de significado não documentado | [SOCPROG.ddm:41-52](legacy-sifap/adabas-ddms/SOCPROG.ddm#L41) |
| Elegibilidade CA-CJ | Teto per capita `P7,2`, idades `N3`, quantidades `N2`, indicadores `A1`, código `A5` | Zero nos limites de idade significa ausência de limite no comentário; indicadores S/N | [SOCPROG.ddm:56-65](legacy-sifap/adabas-ddms/SOCPROG.ddm#L56) |
| Faixas DA-DF | Início/fim `P7,2`, multiplicador `P3,4`, adicional `P7,2`, acumulação `A1` | PE de cinco faixas; acumulação S indica faixa acumulada | [SOCPROG.ddm:69-74](legacy-sifap/adabas-ddms/SOCPROG.ddm#L69) |
| Descontos EA | Tipo `A3` | MU de oito: IR/JD/CS/PA/EM/TX/OU/EX | [SOCPROG.ddm:78-82](legacy-sifap/adabas-ddms/SOCPROG.ddm#L78) |
| Região FA-FE | Código `A2`, fator `P3,4`, complemento `P7,2`, ativo `A1` | PE de seis: cinco regiões e especial; códigos 01-05 ou 99 | [SOCPROG.ddm:86-91](legacy-sifap/adabas-ddms/SOCPROG.ddm#L86) |
| Controle GA-GD | Datas `N8`, usuários `A8` | Campos simples | [SOCPROG.ddm:95-98](legacy-sifap/adabas-ddms/SOCPROG.ddm#L95) |

S2 concatena tipo AD e situação AI: [SOCPROG.ddm:102-103](legacy-sifap/adabas-ddms/SOCPROG.ddm#L102).

## Estruturas de PAYMENT

| Grupo ou família | Campos e formatos relevantes | Multiplicidade/domínio declarado | Evidência |
|---|---|---|---|
| Chaves AA-AF | Pagamento `N15`, CPF `A11`, matrícula `N11`, programa `A4`, competência/ciclo `N6` | CPF e programa sugerem relações lógicas com 150/151; não são FKs declaradas | [PAYMENT.ddm:34-39](legacy-sifap/adabas-ddms/PAYMENT.ddm#L34) |
| Valores BA-BD | Bruto/líquido/bônus `P9,2`, desconto total `P7,2` | A relação líquido = bruto - desconto é anotada, não um campo calculado automaticamente | [PAYMENT.ddm:43-46](legacy-sifap/adabas-ddms/PAYMENT.ddm#L43) |
| Descontos CA-CG | Tipo `A3`, valor `P7,2`, percentual `P3,2`, processo `A20`, datas `N8` | PE de oito; IR/JD/CS/PA/EM/TX/OU/EX | [PAYMENT.ddm:50-56](legacy-sifap/adabas-ddms/PAYMENT.ddm#L50) |
| Situação DA-DG | Situação `A1`, datas `N8`, hora `N6`, motivo `A3` | P=pendente, G=gerado, E=emitido, C=confirmado, D=devolvido, X=cancelado, R=reprocessado | [PAYMENT.ddm:60-68](legacy-sifap/adabas-ddms/PAYMENT.ddm#L60) |
| Banco EA-EG | Banco `A3`, agência `A6`, conta `A13`, tipo `A1`, operação `A3`, crédito `N8` | Tipo de pagamento N/R/A/C, distinto do N/D/T da PDA e dos relatórios | [PAYMENT.ddm:72-80](legacy-sifap/adabas-ddms/PAYMENT.ddm#L72) |
| SIAFI FA-FG | OB/NE `A12`, unidade `A6`, gestão `A5`, situação `A1`, lote `N8`, sequência `N6` | Integração I/P/E; presença de campos não comprova troca externa | [PAYMENT.ddm:84-90](legacy-sifap/adabas-ddms/PAYMENT.ddm#L84) |
| Conciliação GA-GK | Datas `N8`, situação/indicadores `A1`, valores `P9,2`, retorno `A2`, descrição `A40`, origem `N15` | Situação C/D/P/N; origem é referência lógica ao pagamento anterior | [PAYMENT.ddm:94-105](legacy-sifap/adabas-ddms/PAYMENT.ddm#L94) |
| Arquivos HA-HC | Hashes `A64`, ocorrências bancárias `A3` | HC é MU de dez | [PAYMENT.ddm:109-112](legacy-sifap/adabas-ddms/PAYMENT.ddm#L109) |
| Controle IA-IF | Datas `N8`, horas `N6`, usuários `A8` | Campos simples | [PAYMENT.ddm:116-121](legacy-sifap/adabas-ddms/PAYMENT.ddm#L116) |

SA é ano da competência; S1 concatena CPF + competência; S2 programa + competência + situação; S3 ciclo + situação. S1 é usado na consulta de geração existente, não declarado único: [PAYMENT.ddm:125-132](legacy-sifap/adabas-ddms/PAYMENT.ddm#L125), [BATCHPGT.NSP:294](legacy-sifap/natural-programs/BATCHPGT.NSP#L294).

## Estruturas de AUDIT

| Grupo ou família | Campos e formatos relevantes | Multiplicidade/domínio declarado | Evidência |
|---|---|---|---|
| Evento AA-AE | Sequência `N15`, data `N8`, hora `N6`, timestamp `N14`, transação `A8` | Hora/timestamp têm precisão declarada de segundos | [AUDIT.ddm:31-35](legacy-sifap/adabas-ddms/AUDIT.ddm#L31) |
| Ação BA-BC | Ação `A2`, módulo `A8`, descrição `A80` | IN/AL/EX/CO/LG/LO/BT/ER/AU/RE; CN/DV não constam dessa lista | [AUDIT.ddm:39-51](legacy-sifap/adabas-ddms/AUDIT.ddm#L39) |
| Entidade CA-CC | Tipo `A4`, chave `A15`, CPF `A11` | BENF/PGTO/PROG/ADMN/SIST; o conteúdo da chave depende do escritor | [AUDIT.ddm:55-57](legacy-sifap/adabas-ddms/AUDIT.ddm#L55) |
| Antes/depois DA-DH | Nomes de campo `A30` e valores `A80` em MU; valores escalares `A60` | Dois grupos simples, com MU de 20 em cada lista; não são PE. DG/DH coexistem com as listas | [AUDIT.ddm:61-70](legacy-sifap/adabas-ddms/AUDIT.ddm#L61) |
| Origem EA-EH | Usuário `A8`, nome `A40`, perfil `A3`, lotação `A10`, IP `A15`, sessão `A20`, terminal/LU `A8` | Perfil ADM/OPR/CON/AUD/SUP | [AUDIT.ddm:74-81](legacy-sifap/adabas-ddms/AUDIT.ddm#L74) |
| Batch FA-FE | Ciclo `N6`, sequência `N10`, job `A16`, situação `A1`, erro `A120` | S/E/W | [AUDIT.ddm:85-89](legacy-sifap/adabas-ddms/AUDIT.ddm#L85) |
| Correlação GA-GB | Identificador `A36`, sequência `N3` | Campo anotado como UUID; nenhuma geração de UUID foi encontrada nos escritores lidos | [AUDIT.ddm:93-94](legacy-sifap/adabas-ddms/AUDIT.ddm#L93) |

SA deriva ano/mês da data; S1 combina data + ação; S2 entidade + chave + data; S3 usuário + data: [AUDIT.ddm:98-105](legacy-sifap/adabas-ddms/AUDIT.ddm#L98). O rodapé cita arquivos históricos 154/155/156 sem DDM publicado no acervo: [AUDIT.ddm:143-146](legacy-sifap/adabas-ddms/AUDIT.ddm#L143).

## Relações observadas

| Origem e destino | Ligação | Natureza e evidência |
|---|---|---|
| BENEFIC para SOCPROG | CA programa para AA programa | Busca efetiva de programa pelo código do beneficiário: [BATCHPGT.NSP:302](legacy-sifap/natural-programs/BATCHPGT.NSP#L302) |
| PAYMENT para BENEFIC | AB CPF para AB CPF | Busca efetiva do beneficiário pelo CPF do pagamento: [RELPGT.NSP:154](legacy-sifap/natural-programs/RELPGT.NSP#L154) |
| PAYMENT para SOCPROG | AD programa para AA programa | Código copiado do beneficiário ao gravar: [BATCHPGT.NSP:477](legacy-sifap/natural-programs/BATCHPGT.NSP#L477); integridade referencial não demonstrada |
| PAYMENT para PAYMENT | GH origem para AA pagamento | Relação indicada no dicionário, sem travessia desse campo nos membros lidos: [PAYMENT.ddm:102](legacy-sifap/adabas-ddms/PAYMENT.ddm#L102) |
| AUDIT para entidades | CA tipo + CB chave; CC CPF auxiliar | Polimórfica e dependente do chamador; conciliação usa número de pagamento: [BATCHCON.NSP:311-343](legacy-sifap/natural-programs/BATCHCON.NSP#L311) |

Não há declaração de chave estrangeira nesses DDMs. Cardinalidades e comportamento de registros órfãos permanecem sujeitos à validação da equipe.

## Confronto com a FDT 150

| Aspecto | Evidência física e confronto |
|---|---|
| Data da observação | A listagem distingue execução, carga e última alteração estrutural em [FDT-150-BENEFICIARY.txt:5-6](legacy-sifap/adabas-ddms/FDT-150-BENEFICIARY.txt#L5). Consulte a [cronologia](legacy-sifap/CHRONOLOGY.md); não é medição atual. |
| Unicidade | AA/AB têm DE,UQ; AA também FI. A FDT não identifica ISN como um desses nomes de negócio: [FDT-150-BENEFICIARY.txt:13-14](legacy-sifap/adabas-ddms/FDT-150-BENEFICIARY.txt#L13). |
| Repetições | DA é PE e ED é MU; estatísticas indicam máximos 10 e 5, e limite Adabas 191. Não confundir capacidade física, ocorrências observadas e limite de negócio: [FDT-150-BENEFICIARY.txt:55-65](legacy-sifap/adabas-ddms/FDT-150-BENEFICIARY.txt#L55), [FDT-150-BENEFICIARY.txt:119-121](legacy-sifap/adabas-ddms/FDT-150-BENEFICIARY.txt#L119). |
| Nulos e índices | O aviso diz que campos NU vazios não entram no índice. Isso importa para buscas por NIS vazio: [FDT-150-BENEFICIARY.txt:148-150](legacy-sifap/adabas-ddms/FDT-150-BENEFICIARY.txt#L148). |
| Decimais | CH e CJ aparecem com 5 e 4 bytes físicos; DDM e fontes expressam precisão/escala logicamente. Qual correspondência de capacidade deve ser validada na extração? [FDT-150-BENEFICIARY.txt:44-46](legacy-sifap/adabas-ddms/FDT-150-BENEFICIARY.txt#L44), [BENEFIC.ddm:78-80](legacy-sifap/adabas-ddms/BENEFIC.ddm#L78). |
| Campos não listados | JA/JB existem no DDM; a lista física termina em IG antes dos derivados. Como reconciliar as representações fornecidas? [BENEFIC.ddm:139-140](legacy-sifap/adabas-ddms/BENEFIC.ddm#L139), [FDT-150-BENEFICIARY.txt:76-95](legacy-sifap/adabas-ddms/FDT-150-BENEFICIARY.txt#L76). |
| Derivados | PN, SA, S2, S3 e H1 aparecem em ambas as representações; HYPEREXIT 03 não tem implementação local: [FDT-150-BENEFICIARY.txt:91-95](legacy-sifap/adabas-ddms/FDT-150-BENEFICIARY.txt#L91). |

Os números de registros, bytes, compressão e duração de unload são estimativas/anotações da listagem histórica, não metas de desempenho, medições atuais ou autorização de operação. Os totais declarados nos rodapés não foram usados como contagem validada de campos ou da população atual.

## Limites da conclusão

- [x] Quatro DDMs e a FDT fornecida foram lidos, incluindo os rodapés.
- [x] Chaves, tipos, grupos, MU/PE e descritores foram relacionados às origens.
- [x] Relações observadas foram separadas de vínculos apenas anotados.
- [ ] A equipe validou domínios divergentes e representações física/lógica.
- [ ] O DBA mediu a população atual e verificou as definições do ambiente de origem.

### Continue lendo

| Anterior | Próximo |
|---|---|
| [Inventário](inventory.md) | [Mapa de dependências](dependency-map.md) |
