---
id: MOD_DESCRIPTION
title: "DESCRIPTION"
category: modifier
summary: "Texto curto explicando o que um campo registra."
syntax: "DESCRIPTION <texto>"
see_also: [BLOCK_FIELD, MOD_GUIDELINES]
source: authored
order: 20
---

# DESCRIPTION

## Descrição

Explica **o que** o campo registra. Aceito em qualquer tipo de campo.

Aparece no autocomplete e no hover do editor — e a frase que a equipe le ao
preencher. Uma linha boa aqui economiza duvida recorrente.

## Sintaxe

```synesis
FIELD quote TYPE QUOTATION
    SCOPE ITEM
    DESCRIPTION trecho literal transcrito da fonte
END FIELD
```

## DESCRIPTION ou GUIDELINES?

| | Responde |
|---|---|
| `DESCRIPTION` | o que este campo e |
| `GUIDELINES` | como preenche-lo bem |

Use os dois quando o campo exigir critério.

## Ver também

`BLOCK_FIELD`, `MOD_GUIDELINES`
