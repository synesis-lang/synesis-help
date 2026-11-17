---
id: LINKAGE_SCOPES
title: "Escopos e ligacao entre projetos"
category: linkage
summary: "Onde IDENTIFIES e REFERS TO podem ser declarados."
syntax: FIELD <nome> TYPE <tipo> SCOPE SOURCE <IDENTIFIES|REFERS TO> <entidade> END FIELD
see_also: [SYNESIS_E078]
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# Escopos e ligacao

## Descrição

Os modificadores `IDENTIFIES` e `REFERS TO` ligam projetos independentes.
Nem todo escopo os aceita.

## Sintaxe

```synesis
FIELD <nome> TYPE <tipo>
    SCOPE SOURCE
    [IDENTIFIES <entidade>]
    [REFERS TO <entidade>]
END FIELD
```

`[ ]` opcional · `<>` valor a substituir

## Regras

| Escopo | `IDENTIFIES` | `REFERS TO` |
|---|---|---|
| `SOURCE` | Permitido | Permitido |
| `ITEM` | Proibido (SYNESIS_E078) | Proibido (SYNESIS_E078) |
| `ONTOLOGY` | Proibido (SYNESIS_E078) | Proibido (SYNESIS_E078) |

## Ver também

`SYNESIS_E078`
