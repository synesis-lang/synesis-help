---
id: BLOCK_PROJECT
title: "PROJECT"
category: block
summary: "Ponto de entrada do projeto. Declara template, fontes e inclusões."
syntax: "PROJECT <nome> TEMPLATE \"<arquivo>\" [INCLUDE ...] END PROJECT"
file: ".synp"
see_also: [BLOCK_TEMPLATE, MOD_INCLUDE, MOD_METADATA, SYNESIS_E064, SYNESIS_E065, SYNESIS_E066]
source: authored
order: 10
---

# PROJECT

## Descrição

Todo projeto Synesis começa aqui. O arquivo `.synp` e o único ponto de entrada:
declara qual template governa os dados, quais arquivos de anotação e ontologia
fazem parte do projeto, e onde esta a bibliografia.

Existe **um** bloco `PROJECT` por projeto, na raiz do workspace.

## Sintaxe

```synesis
PROJECT <nome>

TEMPLATE "<arquivo.synt>"

[INCLUDE BIBLIOGRAPHY "<arquivo.bib>"]
[INCLUDE ANNOTATIONS "<arquivo.syn>"]
[INCLUDE ONTOLOGY "<arquivo.syno>"]
[INCLUDE SHARED ONTOLOGY "<caminho.syno>"]
[INCLUDE DATASET "<arquivo.toml>"]

[METADATA
    version: <n>
    author: <texto>
    [created: <data>]
    [modified: <data>]
END METADATA]

[DESCRIPTION
    <texto livre>
END DESCRIPTION]

END PROJECT
```

`[ ]` opcional · `<>` valor a substituir

## Regras

- `TEMPLATE` e obrigatório — sem ele não ha o que validar (`SYNESIS_E065`).
- Um único bloco `PROJECT` por arquivo (`SYNESIS_E066`).
- Todo `.syn` e `.syno` na pasta do projeto precisa ser declarado num `INCLUDE`
  (`SYNESIS_E061`, `SYNESIS_E062`). Arquivo esquecido e dado invisível.
- Caminhos não podem escapar da pasta do projeto (`SYNESIS_E075`), exceto
  `INCLUDE SHARED ONTOLOGY`.

## Exemplo

```synesis
PROJECT resiliencia_comunitaria

TEMPLATE "template.synt"

INCLUDE BIBLIOGRAPHY "biblio.bib"
INCLUDE ANNOTATIONS "entrevistas.syn"
INCLUDE ONTOLOGY "codigos.syno"

METADATA
    version: 1.0
    author: Equipe de Pesquisa
END METADATA

END PROJECT
```

## Ver também

`BLOCK_TEMPLATE`, `MOD_INCLUDE`, `MOD_METADATA`, `SYNESIS_E065`, `SYNESIS_E066`
