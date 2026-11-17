---
id: SYNESIS_E082
title: "SYNESIS_E082"
category: diagnostic
summary: "TYPE divergente entre campos da mesma entidade no link step. (erro 82)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E082 — Erro

## Descrição

TYPE divergente entre campos da mesma entidade no link step. (erro 82)

## Mensagem do compilador

```text
The fields taking part in the entity `exemplo` have diverging `TYPE`:
  `exemplo` declares `TYPE exemplo`; `exemplo` declares `TYPE exemplo`.
  Fields of the same entity (the `IDENTIFIES` and every `REFERS TO`) must have
  the same `TYPE` — the divergence means the two sides do not model the
  same thing. Align the types in the template.
```

## Onde aparece

- **TypeMismatchInLinkage**: `entity`, `member_a`, `type_a`, `member_b`, `type_b`
