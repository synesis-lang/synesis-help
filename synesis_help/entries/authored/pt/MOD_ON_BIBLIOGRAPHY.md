---
id: MOD_ON_BIBLIOGRAPHY
title: "ON BIBLIOGRAPHY / ON DATASET"
category: modifier
summary: "Campo cujo valor vem do .bib ou de um dataset externo, não do .syn."
syntax: "REQUIRED <campo> ON BIBLIOGRAPHY | ON DATASET \"<caminho.no.registro>\""
see_also: [BLOCK_SOURCE, BLOCK_FIELDS_SPEC, MOD_INCLUDE, SYNESIS_E079, SYNESIS_E085]
source: authored
order: 50
---

# ON BIBLIOGRAPHY / ON DATASET

## Descrição

Declara que o valor de um campo **não e digitado na anotação**: vem de fora.

- `ON BIBLIOGRAPHY` — o valor vem da entrada BibTeX do `SOURCE`.
- `ON DATASET` — o valor vem de um registro TOML (um arquivo por registro),
  no caminho indicado.

Evita redigitar o que ja esta registrado, e evita a divergência que a
redigitacao produz.

## Sintaxe

```synesis
SOURCE FIELDS
    REQUIRED ano ON BIBLIOGRAPHY
    REQUIRED entrevista ON DATASET "entrevista.id"
    OPTIONAL regiao ON DATASET "entrevista.regiao"
END SOURCE FIELDS

FIELD entrevista TYPE TEXT
    SCOPE SOURCE
    IDENTIFIES entrevista
END FIELD
```

```toml
# registros/s1.toml — associado ao SOURCE @s1
[entrevista]
id = "s1"
regiao = "Nordeste"
```

A string depois de `ON DATASET` e um **caminho dentro do registro** (notação
de ponto), não o nome do arquivo. Os arquivos vem de `INCLUDE DATASET
"registros/*.toml"` no `.synp`.

## Regras

- Valor ausente no `.bib`: `SYNESIS_E079`.
- Valor ausente no dataset: `SYNESIS_E085`.
- Os registros precisam estar declarados com `INCLUDE DATASET` (arquivo ou
  glob).
- Um campo de `SCOPE SOURCE` com `IDENTIFIES` e `ON DATASET` e a chave: o
  valor nesse caminho do registro deve ser igual ao bibref do `SOURCE`.
- So em cláusula de campo único: `REQUIRED a, b ON DATASET "x"` e erro.
- No JSON compilado, os valores ficam na seção `dataset`, pelo bibref.
- Para usar seções do registro como contexto na geração de um campo (sem dar
  valor a ele), veja `CONTEXT FROM DATASET` em `BLOCK_FIELD`.

## Ver também

`BLOCK_SOURCE`, `MOD_INCLUDE`, `MOD_IDENTIFIES`, `SYNESIS_E079`, `SYNESIS_E085`
