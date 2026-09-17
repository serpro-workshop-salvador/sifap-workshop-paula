# Cronologia do SIFAP — Evidência canônica das fontes

> **Trilha:** [Kit do Time](../../README.md) › [Estágio 1](../README.md) › [Legado SIFAP](README.md) › **Cronologia**

**Este arquivo é a fonte única de verdade para toda data, autoria e versão que o kit afirma sobre o SIFAP.** Cada entrada abaixo é transcrita de uma linha de cabeçalho dentro de uma fonte legada somente leitura. Nada aqui é inferido, arredondado ou narrado.

| Campo | Valor |
|---|---|
| **Público-alvo** | Quem escreve ou revisa um documento do kit que cite uma data do SIFAP |
| **Pré-requisitos** | Nenhum |
| **Tempo estimado** | 5 min para consultar; leia uma vez antes de citar qualquer data |
| **Estágio** | Estágio 1 — Arqueologia (consultado em todos os estágios) |
| **Resultado esperado** | Você cita uma data que confere com a fonte ou registra uma divergência |

---

## 1. Por que este arquivo existe

O acervo contém dois tipos de documento, e confundi-los é a falha mais comum
em um exercício de modernização.

| Camada | Pode divergir do código? | Arquivos |
|---|---|---|
| **Evidência** — as próprias fontes | É a referência. Os cabeçalhos são a verdade de base. | `natural-programs/*`, `adabas-ddms/*` |
| **Narrativa** — documentos de época escritos *sobre* o sistema | **Sim, de propósito.** O desvio da documentação é o exercício. Toda divergência conhecida está registrada na [divergência declarada](DECLARED-DRIFT.md). | `legacy-docs/*`, [`README.md`](README.md) |
| **Verdade do kit** — os guias que orientam seu trabalho | **Nunca.** Um guia que atribui um membro à pessoa errada quebra o exercício em vez de ensiná-lo. | Este arquivo, [`natural-programs/README.md`](natural-programs/README.md), guias de estágio |

Um documento de época que contradiz o cabeçalho de uma fonte é um achado a
registrar, não um defeito a reportar. Um guia do kit que contradiz o cabeçalho
de uma fonte é um defeito.

---

## 2. Ano de referência e aritmética

| Âncora | Valor | O que estabelece |
|---|---|---|
| Fonte datada mais antiga | `BENEFIC.ddm`, 12/05/1997 | O acervo começa em 1997 |
| Fonte datada mais recente | `CONSBENF.NSP`, `RELAUDIT.NSP`, `RELPGT.NSP`, 30/05/2018 | A última manutenção registrada |
| Ano de referência da imersão | 2026 | O ano em que a equipe realiza o exercício |
| Intervalo decorrido | 1997 a 2026 = **29 anos civis** | "Aproximadamente 30 anos" é linguagem arredondada do cenário |

> [!IMPORTANT]
> Escreva "aproximadamente 30 anos" ou "aproximadamente três décadas" em prosa e
> **29 anos** sempre que um número for apresentado como medição. Nunca altere a
> data de uma fonte para deixar a aritmética mais redonda. Consulte a
> [política de cronologia](../../README.md).

---

## 3. Cronologia canônica dos membros

Transcrita das linhas de cabeçalho `* AUTHOR:` e `* DATE:` de cada membro. A
coluna "Última alteração registrada" traz a última linha `* CHANGED:` do mesmo cabeçalho.

### 3.1. Os 15 membros atribuídos

| Membro | Tipo | Autor no cabeçalho | Criado | Última alteração registrada |
|---|---|---|---|---|
| `CADBENEF.NSP` | Programa | CARLOS ROBERTO DA SILVA | 15/03/1997 | 12/09/2012 |
| `CALCBENF.NSN` | Subprograma | CARLOS ROBERTO DA SILVA | 18/04/1997 | 14/06/2016 |
| `BATCHPGT.NSP` | Programa | CARLOS ROBERTO DA SILVA | 22/06/1997 | 18/03/2016 |
| `CADPROG.NSP` | Programa | MARCOS ANTONIO RIBEIRO | 10/09/1997 | 18/11/2012 |
| `VALBENEF.NSN` | Subprograma | MARCIA HELENA OLIVEIRA | 08/01/1998 | 18/08/2011 |
| `VALDOCS.NSP` | Programa | ANA LUCIA PEREIRA | 14/05/1998 | 18/08/2011 |
| `CADDEPEN.NSP` | Programa | ANA LUCIA PEREIRA | 20/06/1998 | 12/09/2012 |
| `CONSBENF.NSP` | Programa | MARCIA HELENA OLIVEIRA | 28/09/1998 | 30/05/2018 |
| `VALELEG.NSN` | Subprograma | JOSE FERREIRA DOS SANTOS | 03/02/1999 | 05/04/2013 |
| `CALCDSCT.NSP` | Programa | ROBERTO MENDES JUNIOR | 25/08/1999 | 14/06/2016 |
| `BATCHREL.NSP` | Programa | PATRICIA GOMES DE SOUZA | 10/11/1999 | 05/06/2014 |
| `RELPGT.NSP` | Programa | ANA LUCIA PEREIRA | 17/12/1999 | 30/05/2018 |
| `BATCHCON.NSP` | Programa | MARCOS ANTONIO RIBEIRO | 05/03/2000 | 11/05/2017 |
| `CALCCORR.NSP` | Programa | PATRICIA GOMES DE SOUZA | 12/07/2001 | 14/06/2016 |
| `RELAUDIT.NSP` | Programa | ROBERTO MENDES JUNIOR | 20/08/2002 | 30/05/2018 |

### 3.2. Os nove membros de apoio

| Membro | Tipo | Autor no cabeçalho | Criado | Última alteração registrada |
|---|---|---|---|---|
| `CCVALCPF.NSC` | Copycode | CARLOS ROBERTO DA SILVA | 15/03/1997 | 07/06/2011 |
| `PDACALC.NSA` | PDA | CARLOS ROBERTO DA SILVA | 22/06/1997 | 30/09/2015 |
| `SIFAPJ01.jcl` | JCL | CARLOS ROBERTO DA SILVA | 22/06/1997 | 10/07/2015 |
| `LDASIFAP.NSL` | LDA | CARLOS ROBERTO DA SILVA | 10/09/1997 | 30/09/2015 |
| `PDAVALID.NSA` | PDA | MARCIA HELENA OLIVEIRA | 12/03/1998 | 07/06/2011 |
| `SUBVALCP.NSN` | Subprograma | MARCIA HELENA OLIVEIRA | 12/03/1998 | 07/06/2011 |
| `SIFAPJ02.jcl` | JCL | PATRICIA GOMES DE SOUZA | 10/11/1999 | 14/02/2013 |
| `CCAUDIT.NSC` | Copycode | ADILSON BATISTA | 15/04/2005 | 10/07/2015 |
| `SUBVALNI.NSN` | Subprograma | ROBERTO MENDES JUNIOR | 07/06/2011 | 30/09/2015 |

---

## 4. Cronologia canônica da camada de dados

| Artefato | Arquivo Adabas | Autor no cabeçalho | Criado | Última alteração registrada |
|---|---|---|---|---|
| `BENEFIC.ddm` | FNR 150 | ROBERTO CARLOS FERREIRA — ADABAS DBA | 12/05/1997 | veja o cabeçalho |
| `SOCPROG.ddm` | FNR 151 | ROBERTO CARLOS FERREIRA — ADABAS DBA | 12/05/1997 | veja o cabeçalho |
| `PAYMENT.ddm` | FNR 152 | ROBERTO CARLOS FERREIRA — ADABAS DBA | 15/05/1997 | veja o cabeçalho |
| `AUDIT.ddm` | FNR 153 | ROBERTO CARLOS FERREIRA — ADABAS DBA | 20/05/1997 | veja o cabeçalho |

`FDT-150-BENEFICIARY.txt` é uma listagem ADAREP, não uma definição. Ele declara três
datas distintas, e confundi-las é uma armadilha documentada:

| Data na listagem | O que significa |
|---|---|
| `ADACMP FDT AS LOADED 1997-05-12` | Quando a tabela de definição de campos foi carregada pela primeira vez |
| `LAST FDT CHANGE 2015-11-19` | A última alteração estrutural na tabela |
| `RUN DATE 2018-03-14` | Quando alguém imprimiu este relatório |

> [!WARNING]
> A data de execução indica quando o relatório foi produzido. Não é uma medição do
> banco de dados hoje e não autoriza nenhuma afirmação sobre contagem de registros
> em 2026. O DBA mede a população atual durante as verificações de prontidão da fonte.

---

## 5. Cronologia canônica das versões

Derivada estritamente da seção 3. Cada linha cita a evidência que a data.

| Ano | O que as fontes mostram | Evidência |
|---|---|---|
| 1997 | Quatro DDMs definidos (maio); primeiros membros de cadastro, cálculo e batch criados (mar–set) | `BENEFIC.ddm`, `CADBENEF.NSP`, `CALCBENF.NSN`, `BATCHPGT.NSP`, `CADPROG.NSP` |
| 1998 | Membros de validação e consulta criados; janela de século Y2K introduzida em 12/08/1998 | `VALBENEF.NSN`, `VALDOCS.NSP`, `CADDEPEN.NSP`, `CONSBENF.NSP`, linha de alteração de `BATCHPGT.NSP` |
| 1999 | Membros de elegibilidade, dedução e relatórios, além do job de relatórios | `VALELEG.NSN`, `CALCDSCT.NSP`, `BATCHREL.NSP`, `RELPGT.NSP`, `SIFAPJ02.jcl` |
| 2000 | Conciliação de retorno bancário criada | `BATCHCON.NSP` |
| 2001 | Correção retroativa criada; alteração do 13º salário no cálculo do benefício | `CALCCORR.NSP`, linha de alteração de `CALCBENF.NSN` |
| 2002 | Relatório da trilha de auditoria criado | `RELAUDIT.NSP` |
| 2005 | Copycode compartilhado de auditoria criado; validação de CPF ajustada em vários membros | `CCAUDIT.NSC`, linhas de alteração de `CCVALCPF.NSC` e `VALBENEF.NSN` |
| 2011 | Refatoração `CALLNAT` — validação e cálculo convertidos em subprogramas; subprograma de NIS criado | Linhas de alteração do chamado 6210, `SUBVALNI.NSN` |
| 2016 | Chamado 7210 — padronização de DDM na família de cálculo | Linhas de alteração de `CALCBENF.NSN`, `CALCCORR.NSP`, `CALCDSCT.NSP` |
| 2018 | Última manutenção registrada — views alinhadas aos DDMs em 30/05/2018 | Linhas de alteração de `CONSBENF.NSP`, `RELAUDIT.NSP`, `RELPGT.NSP` |

> [!NOTE]
> Uma data de criação não é uma data de entrada em produção, e uma linha de alteração
> não é um registro de implantação. O acervo não contém evidência de implantação.
> Qualquer afirmação sobre quando uma alteração chegou à produção é uma hipótese que
> a equipe deve marcar como tal.

---

## 6. Índice canônico de nomes

As linhas `* AUTHOR:` do cabeçalho usam nomes completos; as linhas `* CHANGED:` usam
formas abreviadas. Portanto, a mesma pessoa aparece com duas grafias, e duas pessoas
diferentes podem compartilhar um primeiro nome. Resolva um nome aqui antes de atribuir
uma regra a alguém.

| Nome completo como autor | Forma abreviada nas linhas de alteração | Evidência mais antiga | Evidência mais recente |
|---|---|---|---|
| CARLOS ROBERTO DA SILVA | `CARLOS SILVA` | 15/03/1997 | 30/11/2001 |
| ROBERTO CARLOS FERREIRA | `ROBERTO C. FERREIRA` | 12/05/1997 | 11/08/2003 |
| MARCOS ANTONIO RIBEIRO | `MARCOS RIBEIRO` | 10/09/1997 | 18/09/2005 |
| MARCIA HELENA OLIVEIRA | `MARCIA HELENA` | 08/01/1998 | 12/04/2007 |
| ANA LUCIA PEREIRA | `ANA LUCIA` | 14/05/1998 | 25/03/2004 |
| (somente linhas de alteração) | `R.SOUZA` | 12/08/1998 | 12/08/1998 |
| (somente linhas de alteração) | `MARCIA A. SOUZA` | 10/01/1999 | 08/03/2001 |
| JOSE FERREIRA DOS SANTOS | `JOSE FERREIRA` | 03/02/1999 | 10/01/2011 |
| ROBERTO MENDES JUNIOR | `ROBERTO MENDES` | 25/08/1999 | 09/04/2013 |
| PATRICIA GOMES DE SOUZA | `PATRICIA GOMES` | 10/11/1999 | 30/05/2018 |
| ADILSON BATISTA | `ADILSON BATISTA` | 15/04/2005 | 22/06/2010 |
| (somente linhas de alteração) | `FERNANDA OLIVEIRA` | 09/02/2012 | 09/02/2012 |
| (somente linhas de alteração) | `FERNANDA COSTA` | 11/10/2009 | 15/09/2014 |
| (somente linhas de alteração) | `ANDERSON LIMA` | 30/04/2011 | 22/07/2016 |
| (coletivo) | `SUPDE TEAM`, `SIFAP TEAM` | 09/05/2011 | 11/05/2017 |

> [!TIP]
> Três armadilhas de nome já são visíveis nesta tabela. `CARLOS ROBERTO DA SILVA`
> e `ROBERTO CARLOS FERREIRA` invertem os mesmos dois prenomes. `MARCIA HELENA
> OLIVEIRA` e `MARCIA A. SOUZA` são pessoas distintas. `FERNANDA OLIVEIRA` e
> `FERNANDA COSTA` são pessoas distintas que tocaram em código relacionado a auditoria.
> Confirme o membro e a data antes de atribuir uma alteração a alguém.

---

## 7. Como citar uma data

- [ ] **Cite o artefato, não um resumo.** Cite `CADBENEF.NSP#L5`, nunca "a documentação diz 1997".
- [ ] **Diga qual representação você leu.** Uma exportação em Word e uma exportação em Markdown do mesmo documento são uma fonte, não duas.
- [ ] **Separe criação, alteração e observação.** A data do cabeçalho, a linha de alteração e a data de execução do relatório respondem a três perguntas diferentes.
- [ ] **Registre a divergência em vez de resolvê-la em silêncio.** Acrescente-a a [`mysteries-found.md`](../mysteries-found.md) com evidência e pessoa responsável.
- [ ] **Nunca edite uma fonte legada para corrigir uma inconsistência.** O acervo é somente leitura.

---

## 8. Como este arquivo é imposto

O job `chronology` em [`spec-quality.yml`](../../.github/workflows/spec-quality.yml)
executa [`validate-chronology.py`](../../.github/scripts/validate-chronology.py), que:

1. Extrai `* AUTHOR:` e `* DATE:` de cada membro e DDM do acervo.
2. Compara-os com as tabelas deste arquivo e de [`natural-programs/README.md`](natural-programs/README.md).
3. Falha quando um documento do kit atribui um membro ao autor ou ao ano errado.
4. Ignora divergências registradas na [divergência declarada](DECLARED-DRIFT.md), porque essas são o exercício.

Acrescentar uma contradição não declarada a um guia do kit quebra a compilação. Esse
é justamente o ponto: a coerência é imposta, não prometida.

---

### Continue lendo

| Anterior | Próximo |
|---|---|
| [Legado SIFAP — visão geral](README.md)<br/><sub>Contexto e história do sistema.</sub> | [Divergência declarada](DECLARED-DRIFT.md)<br/><sub>As contradições que são deliberadas.</sub> |

<sub>[Voltar ao índice do kit](../../README.md)</sub>
