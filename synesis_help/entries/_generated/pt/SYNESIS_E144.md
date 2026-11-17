---
id: SYNESIS_E144
title: "SYNESIS_E144"
category: diagnostic
summary: "Fases com o mesmo nome, ou nomes que viram a mesma variavel de ambiente."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E144 — Erro

## Descrição

Fases com o mesmo nome, ou nomes que viram a mesma variavel de ambiente.

## Mensagem do compilador

```text
`exemplo` collides with `exemplo`: both names become the same
  coder environment variable (SYNESIS_CODER_PHASE_<NAME>_*). Rename one of the phases.
```

## Onde aparece

- **PhaseNameCollision**: `phase`, `other`
