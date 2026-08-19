---
id: MOD_BUNDLE
title: "BUNDLE"
category: modifier
summary: "Campos que representam informação composta e so valem juntos."
syntax: "BUNDLE <campo>, <campo> [, ...]"
see_also: [BLOCK_FIELDS_SPEC, SYNESIS_E016, SYNESIS_E017, SYNESIS_E018]
source: authored
order: 40
---

# BUNDLE

## Descrição

`BUNDLE` declara campos que formam um **pacote indivisível**: ou todos
aparecem, ou nenhum.

O caso clássico e evidencia + localização. Uma citação sem a pagina de onde
veio e meia evidencia; a pagina sozinha não diz nada. `BUNDLE` transforma esse
pareamento numa regra que o compilador cobra.

## Sintaxe

```synesis
ITEM FIELDS
    BUNDLE citacao, pagina
END ITEM FIELDS
```

## Regras

- Faltando um membro do pacote: `SYNESIS_E016`.
- Membros com quantidades diferentes de ocorrência: `SYNESIS_E017`.
- `BUNDLE` com um único campo não faz sentido e e erro (`SYNESIS_E018`).

## Ver também

`BLOCK_FIELDS_SPEC`, `SYNESIS_E016`, `SYNESIS_E017`
