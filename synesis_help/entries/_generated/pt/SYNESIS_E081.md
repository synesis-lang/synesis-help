---
id: SYNESIS_E081
title: "SYNESIS_E081"
category: diagnostic
summary: "Dois membros declaram IDENTIFIES do mesmo rotulo no link step. (erro 81)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E081 — Erro

## Descrição

Dois membros declaram IDENTIFIES do mesmo rotulo no link step. (erro 81)

## Mensagem do compilador

```text
The entity `exemplo` is declared with `IDENTIFIES` by two projects:
  `exemplo` and `exemplo`.
  An entity label has a single owning corpus (the primary key).
  If they are distinct ID schemes of the same person (Lattes vs ORCID), the hub
  should `REFERS TO` the periphery — not declare two `IDENTIFIES` of the same label.
```

## Onde aparece

- **DuplicateEntityOwner**: `entity`, `first_member`, `duplicate_member`
