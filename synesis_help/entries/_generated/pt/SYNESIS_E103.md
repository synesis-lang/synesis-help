---
id: SYNESIS_E103
title: "SYNESIS_E103"
category: diagnostic
summary: "Dois blocos com nomes que so coincidem pela forma Unicode (NFC)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E103 — Erro

## Descrição

Dois blocos com nomes que so coincidem pela forma Unicode (NFC).

## Mensagem do compilador

```text
The concept `exemplo` has the same identity as `exemplo`
  (in `exemplo`): the names look equal, but one of them uses accented
  letters in decomposed form (letter + combining accent). Synesis treats
  them as the same concept. Rewrite one of the names, or merge the two blocks.
```

## Onde aparece

- **IdentityCollision**: `first_name`, `second_name`, `first_file`
