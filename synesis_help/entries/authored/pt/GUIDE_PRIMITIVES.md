---
id: GUIDE_PRIMITIVES
title: "Os três primitivos"
category: overview
summary: "SOURCE, ITEM e ONTOLOGY: proveniência, ocorrência, conceituacao."
see_also: [BLOCK_SOURCE, BLOCK_ITEM, BLOCK_ONTOLOGY, GUIDE_START, MOD_SCOPE]
source: authored
order: 30
---

# Os três primitivos

## A tríade

Synesis tem três blocos de dados. Eles não são etapas sucessivas de
codificação: são **primitivos** — estruturas elementares a partir das quais
metodologias diferentes podem ser expressas.

| Primitivo | Função | Pergunta que responde |
|---|---|---|
| `SOURCE` | proveniência | De onde procede a informação? |
| `ITEM` | ocorrência | Qual e a unidade concreta que registro? |
| `ONTOLOGY` | conceituacao | Segundo qual sistema conceitual a compreendo? |

Em linguagem epistemológica:

> `SOURCE` diz **de onde sabemos**.
> `ITEM` diz **o que observamos**.
> `ONTOLOGY` diz **como conceitualizamos** o que encontramos.

## Por que isso importa

A leitura estreita — documento → trecho → tema — descreve bem a analise
temática e mal todo o resto. A leitura funcional permite que a **mesma
gramática** sustente metodologias distintas sem introduzir blocos novos para
cada uma.

## O mesmo esqueleto, muitas metodologias

| Metodologia | `SOURCE` | `ITEM` | `ONTOLOGY` |
|---|---|---|---|
| Análise temática | documento | trecho codificado | tema/categoria |
| Grounded Theory | entrevista | incidente | conceito/categoria |
| Análise de conteúdo | documento | unidade de registro | categoria |
| Análise narrativa | narrativa | evento/episódio | tipo de evento |
| Análise argumentativa | discurso | argumento/premissa | classe argumentativa |
| Análise do discurso | discurso | enunciado | formação discursiva |
| Análise causal | caso | evidencia causal | mecanismo/condição |
| Process tracing | fonte documental | observação | mecanismo causal |
| Análise de frames | discurso | enquadramento | frame |
| Análise axiológica | documento | enunciado valorativo | valor/norma |
| Análise de atores | caso | acao/interação | ator/papel |
| Análise de processos | registro | evento/transição | estado/fase |
| Extração de conhecimento | documento | proposição | conceito/entidade |
| Knowledge graph | doc. de proveniência | relação extraída | entidade |
| Revisão sistemática | artigo | achado/resultado | construto/fator |
| Análise de requisitos | documento técnico | requisito | domínio/componente |
| Análise jurídica | legislação/julgado | norma/argumento | instituto jurídico |
| Análise teológica | texto | proposição/exegese | conceito teológico |

O template e o que faz essa escolha: ao nomear os campos de cada escopo, você
declara qual metodologia esta usando.

## Simetria e assimetria

Os três escopos aceitam **os mesmos tipos de campo**. Um `CHAIN` funciona em
`SOURCE`, `ITEM` ou `ONTOLOGY` — a escolha e sua.

Ha uma única assimetria deliberada: `IDENTIFIES` e `REFERS TO` so existem em
`SCOPE SOURCE` (`SYNESIS_E078`). O que se liga entre projetos e a
**proveniência**, não a ocorrência nem o conceito.

## Consequência pratica

Antes de escrever o template, responda as três perguntas para a **sua**
pesquisa. O vocabulário do seu campo entra nos nomes dos campos; os três
blocos permanecem os mesmos.

## Ver também

`BLOCK_SOURCE`, `BLOCK_ITEM`, `BLOCK_ONTOLOGY`, `GUIDE_START`
