---
id: BLOCK_PHASE
title: "PHASE"
category: block
summary: "Plano de produção: quais campos o synesis-coder gera em cada fase, e a partir de quê."
syntax: "PHASE <ANNOTATIONS|ONTOLOGY> <nome> FIELDS <campos> [INPUT <campos>] [RULES <campos>] [OUTPUT \"<arquivo.syno>\"] END PHASE"
file: ".synp"
see_also: [BLOCK_PROJECT, MOD_ROLE, BLOCK_QUESTIONS, ECO_CODER, SYNESIS_E133, SYNESIS_E137, SYNESIS_E139, SYNESIS_E141, SYNESIS_E142]
source: authored
order: 76
requires_synesis: ">=0.15.0"
---

# PHASE

## Descrição

Um bloco `PHASE` divide a produção do princípio organizador em etapas, cada
uma com seus campos. Definições primeiro, depois sinônimos, depois a
taxonomia: cada fase lê o que as anteriores produziram.

O compilador valida o plano contra o template (campos que existem, ordem das
fases, campos obrigatórios cobertos). O `synesis-coder` executa cada fase.
O tipo da fase sai dos papéis dos campos (`ROLE`): campos `HIERARCHY` fazem
uma fase de **taxonomia**, campos `LABEL ALTERNATIVE`/`HIDDEN` uma fase de
**sinônimos**, e os demais uma fase **descritiva**.

## Sintaxe

```synesis
PHASE <ANNOTATIONS|ONTOLOGY> <nome>
    FIELDS <campo>[, <campo>]
    [INPUT <campo>[, <campo>]]
    [RULES <campo>[, <campo>]]
    [OUTPUT "<arquivo.syno>"]
END PHASE
```

`[ ]` opcional · `<>` valor a substituir

`FIELDS` são os campos que a fase produz; `INPUT`, o que ela lê; `OUTPUT`
(só em `ONTOLOGY`), o `.syno` onde grava.

## Exemplo

```synesis
PHASE ONTOLOGY definicoes
    FIELDS definicao, aspecto, topico
    INPUT trecho, chain
END PHASE

PHASE ONTOLOGY sinonimos
    FIELDS usado_por, nome_antigo
    INPUT definicao, topico
END PHASE

PHASE ONTOLOGY taxonomia
    FIELDS tipo_de, parte_de
    INPUT definicao, topico, chain
END PHASE
```

## Execução

```bash
synesis-coder phase projeto.synp --list          # o plano, com conexão por fase
synesis-coder phase projeto.synp definicoes      # executa uma fase
synesis-coder review projeto.synp taxonomia --sample 100   # amostra para julgamento
synesis-coder review projeto.synp taxonomia --score amostra.csv
synesis-coder consolidate projeto.synp voice_phishing --into vishing   # USE, reversível
```

Cada execução grava um manifesto (`<destino>.<fase>.manifest.json`) com o
que foi proposto, aplicado ou rejeitado. Rodar de novo sem mudança nas
entradas não chama o modelo. Modelo e conexão podem variar por fase:
`SYNESIS_CODER_PHASE_<NOME>_MODEL`, `_BACKEND`, `_API_URL`, `_API_KEY`.

## Regras

- Propriedades aceitas: `FIELDS`, `INPUT`, `RULES` e `OUTPUT`
  (`SYNESIS_E133`).
- Um campo é produzido por uma só fase (`SYNESIS_E137`).
- Uma fase só lê o que fases anteriores produzem (`SYNESIS_E139`).
- Com blocos `PHASE`, todo campo `REQUIRED` precisa de uma fase que o produza
  (`SYNESIS_E141`).
- Sem `OUTPUT`, o projeto precisa ter exatamente um `.syno` local
  (`SYNESIS_E142`).

## Ver também

`MOD_ROLE`, `BLOCK_QUESTIONS`, `BLOCK_PROJECT`, `ECO_CODER`
