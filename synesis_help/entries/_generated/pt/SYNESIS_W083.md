---
id: SYNESIS_W083
title: "SYNESIS_W083"
category: diagnostic
summary: "REFERS TO cujo valor nao casa com nenhum IDENTIFIES no link step. (warning 83)."
severity: Aviso
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_W083 — Aviso

## Descrição

REFERS TO cujo valor nao casa com nenhum IDENTIFIES no link step. (warning 83)

## Mensagem do compilador

```text
The value `valor` (`REFERS TO exemplo` in `exemplo`) has no
  matching `IDENTIFIES exemplo` — it is an orphan reference.
  This may be expected (e.g. an external author with no record in the corpus). No node is created.
```

## Onde aparece

- **OrphanReference**: `entity`, `value`, `member`, `near_match`
