---
id: SYNESIS_E157
title: "SYNESIS_E157"
category: diagnostic
summary: "REGISTRY e OUTPUT apontam para o mesmo arquivo: um sobrescreveria o outro."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E157 — Erro

## Descrição

REGISTRY e OUTPUT apontam para o mesmo arquivo: um sobrescreveria o outro.

## Mensagem do compilador

```text
`exemplo`: OUTPUT and REGISTRY are the same file (`exemplo`); nothing was written.
  The SKOS would overwrite the registry of published IRIs, or the registry the SKOS.
  Give REGISTRY its own file, for example "saida/published-iris.txt".
```

## Onde aparece

- **RegistryIsOutput**: `block`, `path`
