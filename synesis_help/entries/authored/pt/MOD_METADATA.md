---
id: MOD_METADATA
title: "METADATA"
category: modifier
summary: "Bloco opcional do projeto com versão, autoria e datas."
syntax: "METADATA ... END METADATA"
see_also: [BLOCK_PROJECT, SYNESIS_W067]
source: authored
order: 70
---

# METADATA

## Descrição

Bloco opcional dentro de `PROJECT`, com dados sobre o projeto em si — não
sobre os dados analisados.

## Sintaxe

```synesis
METADATA
    version: <n>
    author: <texto>
    [created: <data>]
    [modified: <data>]
    [dataset: <texto>]
END METADATA
```

`[ ]` opcional · `<>` valor a substituir

## Exemplo

```synesis
METADATA
    version: 1.0
    author: Equipe de Pesquisa
    created: 2026-03-01
    modified: 2026-08-08
END METADATA
```

## Campos

| Campo | Obrigatório |
|---|---|
| `version` | sim |
| `author` | sim |
| `created` | não |
| `modified` | não |
| `dataset` | não |

## Regras

- `modified` anterior a `created` gera aviso (`SYNESIS_W067`).

## Ver também

`BLOCK_PROJECT`, `SYNESIS_W067`
