# Divergência declarada — contradições que são deliberadas

> **Trilha:** [Kit do Time](../../README.md) › [Estágio 1](../README.md) › [Legado SIFAP](README.md) › **Divergência declarada**

**Um registro de cada ponto em que um documento narrativo sobre o SIFAP discorda, de forma consciente, da fonte que descreve.** O desvio da documentação é a lição central do Estágio 1, por isso essas divergências são preservadas de propósito. Este arquivo registra que elas são intencionais; ele nunca registra qual lado está correto.

| Campo | Valor |
|---|---|
| **Público-alvo** | Pessoas mantenedoras do kit, facilitadoras e o gate de cronologia na integração contínua |
| **Pré-requisitos** | [Cronologia](CHRONOLOGY.md) |
| **Tempo estimado** | 5 min |
| **Estágio** | Estágio 1 — Arqueologia (artefato de manutenção) |
| **Resultado esperado** | Você distingue uma divergência projetada de um defeito do kit |

> [!IMPORTANT]
> Este registro responde a uma única pergunta: **"esta contradição é proposital?"**
> Ele não diz qual documento está certo, o que o código realmente faz ou qual
> regra de negócio se aplica. Lê-lo não elimina nenhum trabalho de descoberta,
> porque cada entrada ainda exige que a equipe abra a fonte e decida o que a
> diferença significa.

---

## 1. Por que um registro é necessário

Sem ele, três falhas ficam indistinguíveis entre si:

| Situação | Sem o registro | Com o registro |
|---|---|---|
| Um documento de época informa uma data errada | Parece um erro de digitação do kit; alguém "corrige" e apaga o exercício | Preservado e citado como achado |
| Um guia do kit informa uma data errada | Parece um enigma projetado; ninguém corrige e o mapa continua errado | Falha imediatamente na integração contínua |
| Uma equipe encontra uma inconsistência real | Não há como saber se ela já era conhecida | Achado não registrado, anotado como descoberta |

A regra que decorre da tabela:

- A **camada narrativa** (`legacy-docs/`, [`README.md`](README.md)) pode divergir, e toda divergência conhecida aparece abaixo.
- A **camada de verdade do kit** ([`CHRONOLOGY.md`](CHRONOLOGY.md), [`natural-programs/README.md`](natural-programs/README.md), guias de estágio) nunca pode divergir.

---

## 2. Registro

`Afirmação` é o que o documento narrativo declara. `Fonte` é o artefato que
registra algo diferente. Leia os dois antes de concluir qualquer coisa.

| ID | Documento narrativo | Afirmação que ele faz | Fonte que difere | Por que é preservado |
|---|---|---|---|---|
| `DRIFT-01` | [`README.md`](README.md) §2.1 | O programa de conciliação chegou com a integração SIAFI de 2002 | Cabeçalho de `BATCHCON.NSP` | Uma linha do tempo reconstruída depois agrupa um programa com o projeto que só mais tarde o justificou |
| `DRIFT-02` | [`README.md`](README.md) §2.1 | O DDM de auditoria foi criado durante a migração de plataforma de 2005 | Cabeçalho de `AUDIT.ddm` | Um arquivo pode ser definido anos antes do módulo que enfim o utiliza |
| `DRIFT-03` | [`README.md`](README.md) §2.1 | O relatório de auditoria faz parte da entrega de 2005 | Cabeçalho de `RELAUDIT.NSP` | Notas de versão escritas depois absorvem trabalho anterior |
| `DRIFT-04` | [`README.md`](README.md) §2.1 | O módulo de dedução é a "última funcionalidade relevante", de 2015 | Cabeçalho de `CALCDSCT.NSP` e suas linhas de alteração | Uma grande alteração em um programa antigo é frequentemente lembrada como um programa novo |
| `DRIFT-05` | [`README.md`](README.md) §3 | Nomeia uma equipe original | Linhas `* AUTHOR:` em todo o acervo | A memória institucional e a autoria no código divergem ao longo de três décadas |
| `DRIFT-06` | [`README.md`](README.md) §5 | Atribui autor, ano e ano da última alteração por programa | Cabeçalhos dos membros | Um inventário compilado em um esforço posterior de documentação herda os próprios erros |
| `DRIFT-07` | [`README.md`](README.md) §5.6 | Lista subprogramas e copycode compartilhados pelo nome | Os membros realmente presentes em `natural-programs/` | Um inventário parcial é o tipo mais perigoso de inventário |
| `DRIFT-08` | [`README.md`](README.md) §7.3 | Atribui a revisão de um procedimento de recuperação a um DBA nomeado | Linha `* AUTHOR:` nos quatro DDMs | A memória operacional raramente é escrita por quem é responsável pelo artefato |
| `DRIFT-09` | [`README.md`](README.md) §6 | Declara volumes de registros para uma data de referência informada | Data de execução de `FDT-150-BENEFICIARY.txt` | Um relatório impresso é uma observação histórica, nunca uma medição atual |
| `DRIFT-10` | [`legacy-docs/ORIGINAL-ARCHITECTURE-1997.md`](legacy-docs/ORIGINAL-ARCHITECTURE-1997.md) | Traz anotações que descrevem eventos posteriores à data de emissão | A própria data de abertura do documento | Documentos de vida longa acumulam anotações de margem posteriores |
| `DRIFT-11` | [`legacy-docs/TECHNICAL-MANUAL-SIFAP-2008.md`](legacy-docs/TECHNICAL-MANUAL-SIFAP-2008.md) | Descreve o comportamento na data de publicação | Linhas de alteração datadas depois dele | Um manual congela; o código não |
| `DRIFT-12` | [`legacy-docs/BUSINESS-RULES-2012.md`](legacy-docs/BUSINESS-RULES-2012.md) | Documenta regras de negócio de 2012, de forma incompleta | Linhas de alteração datadas depois dele | Um esforço de descoberta abandonado deixa um registro parcial que envelhece |

---

## 3. O que uma equipe faz com uma divergência que encontra

- [ ] **Registre-a como pergunta, não como correção.** Use [`mysteries-found.md`](../mysteries-found.md) com evidência, impacto, pessoa responsável e status.
- [ ] **Cite os dois lados.** `path#Lstart-Lend` para a fonte e a seção para a afirmação narrativa.
- [ ] **Marque a hipótese como não confirmada.** Somente validação humana explícita a encerra.
- [ ] **Nunca edite a fonte legada.** O acervo é somente leitura, inclusive os documentos que estão errados.
- [ ] **Nunca alinhe em silêncio um documento de época ao código.** Isso apaga evidência.

---

## 4. Como incluir ou remover uma entrada

- [ ] **Inclua uma entrada** quando uma nova divergência for introduzida de propósito na camada narrativa. Informe o documento, a afirmação e a fonte que difere, nunca a resolução.
- [ ] **Remova uma entrada** somente quando o documento narrativo correspondente for retirado do acervo.
- [ ] **Nunca acrescente um guia do kit a este registro.** A verdade do kit é fixa, não declarada.
- [ ] **Execute o gate novamente** com `python3 .github/scripts/validate-chronology.py` após qualquer alteração.

---

### Continue lendo

| Anterior | Próximo |
|---|---|
| [Cronologia](CHRONOLOGY.md)<br/><sub>Datas canônicas, autoria e o índice de nomes.</sub> | [Programas Natural](natural-programs/README.md)<br/><sub>Os 15 membros atribuídos e os 9 membros de apoio.</sub> |

<sub>[Voltar ao índice do kit](../../README.md)</sub>
