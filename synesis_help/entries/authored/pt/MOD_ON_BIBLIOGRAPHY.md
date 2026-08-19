---
id: MOD_ON_BIBLIOGRAPHY
title: "ON BIBLIOGRAPHY / ON DATASET"
category: modifier
summary: "Campo cujo valor vem do .bib ou de um dataset externo, não do .syn."
syntax: "REQUIRED <campo> ON BIBLIOGRAPHY | ON DATASET \"<arquivo>\""
see_also: [BLOCK_SOURCE, BLOCK_FIELDS_SPEC, MOD_INCLUDE, SYNESIS_E079, SYNESIS_E085]
source: authored
order: 50
---

# ON BIBLIOGRAPHY / ON DATASET

## Descrição

Declara que o valor de um campo **não e digitado na anotação**: vem de fora.

- `ON BIBLIOGRAPHY` — o valor vem da entrada BibTeX do `SOURCE`.
- `ON DATASET` — o valor vem de um arquivo TOML de metadados.

Evita redigitar o que ja esta registrado, e evita a divergência que a
redigitacao produz.

## Sintaxe

```synesis
SOURCE FIELDS
    REQUIRED ano ON BIBLIOGRAPHY
    REQUIRED regiao ON DATASET "metadados.toml"
END SOURCE FIELDS
```

## Regras

- Valor ausente no `.bib`: `SYNESIS_E079`.
- Valor ausente no dataset: `SYNESIS_E085`.
- O arquivo de dataset precisa estar declarado com `INCLUDE DATASET`.

## Ver também

`BLOCK_SOURCE`, `MOD_INCLUDE`, `SYNESIS_E079`, `SYNESIS_E085`
