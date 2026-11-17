---
id: SYNESIS_E006
title: "SYNESIS_E006"
category: diagnostic
summary: "Campo listado em SCOPE FIELDS cujo FIELD tem SCOPE diferente. (erro 6)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E006 — Erro

## Descrição

Campo listado em SCOPE FIELDS cujo FIELD tem SCOPE diferente. (erro 6)

## Mensagem do compilador

```text
The field 'nome_do_campo' is listed in `exemplo FIELDS`,
  but its FIELD definition declares `SCOPE exemplo`.
  Each listed field needs its own definition with the same scope.
  Fix the scope in the FIELD definition or move the field to the right block.
  This problem is in the template definition. If you are not the author
  of the template, tell the project coordinator.
```

## Onde aparece

- **FieldScopeListMismatch**: `field_name`, `listed_scope`, `actual_scope`
