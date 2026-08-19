---
id: MOD_INCLUDE
title: "INCLUDE"
category: modifier
summary: "Declara os arquivos que compõem o projeto."
syntax: "INCLUDE [SHARED] <BIBLIOGRAPHY|ANNOTATIONS|ONTOLOGY|DATASET> \"<arquivo>\""
see_also: [BLOCK_PROJECT, GUIDE_FILES, SYNESIS_E061, SYNESIS_E062, SYNESIS_E075, SYNESIS_E084]
source: authored
order: 60
---

# INCLUDE

## Descrição

Declara, no `.synp`, quais arquivos fazem parte do projeto. Nada e carregado
por descoberta automática: o que não esta declarado não entra na analise.

## Sintaxe

```synesis
INCLUDE <BIBLIOGRAPHY|ANNOTATIONS|ONTOLOGY|DATASET> "<arquivo>"
INCLUDE SHARED ONTOLOGY "<caminho>"
```

`<>` valor a substituir · `|` alternativa

## Exemplo

```synesis
INCLUDE BIBLIOGRAPHY "referencias.bib"
INCLUDE ANNOTATIONS  "entrevistas.syn"
INCLUDE ONTOLOGY     "codigos.syno"
INCLUDE DATASET      "metadados.toml"

INCLUDE SHARED ONTOLOGY "../comum/conceitos.syno"
```

## Tipos

| Tipo | Arquivo | Para que |
|---|---|---|
| `BIBLIOGRAPHY` | `.bib` | referencias das fontes |
| `ANNOTATIONS` | `.syn` | blocos `SOURCE` e `ITEM` |
| `ONTOLOGY` | `.syno` | blocos `ONTOLOGY` |
| `DATASET` | `.toml` | metadados externos por fonte |

## SHARED

`INCLUDE SHARED ONTOLOGY` permite apontar para uma ontologia **fora** da pasta
do projeto — útil quando vários projetos compartilham o mesmo vocabulário.

E o único caso em que o caminho pode escapar da pasta (`SYNESIS_E075`), e so
vale para `ONTOLOGY` (`SYNESIS_E084`).

## Regras

- Arquivo declarado que não existe: `SYNESIS_E073`, `SYNESIS_E074`, `SYNESIS_E063`.
- Arquivo que existe mas não foi declarado: `SYNESIS_E061`, `SYNESIS_E062`.

## Ver também

`BLOCK_PROJECT`, `GUIDE_FILES`, `SYNESIS_E075`, `SYNESIS_E084`
