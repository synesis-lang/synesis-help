---
id: SYNESIS_E154
title: "SYNESIS_E154"
category: diagnostic
summary: "SKOS gerado viola condicao de integridade (S9, S13, S14, S27, S37) ou a regra de hierarquia aciclica do Synesis."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E154 — Erro

## Descrição

SKOS gerado viola condicao de integridade (S9, S13, S14, S27, S37) ou a regra de hierarquia aciclica do Synesis.

## Mensagem do compilador

```text
`exemplo`: the generated SKOS violates the integrity condition exemplo (2 case(s)); the file was not written.

  This is an exporter or project inconsistency, not an editorial choice: report it with the project files.
```

## Onde aparece

- **SkosIntegrityViolation**: `block`, `condition`, `count`, `examples`
