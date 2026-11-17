---
id: SYNESIS_E065
title: "SYNESIS_E065"
category: diagnostic
summary: "Bloco PROJECT sem declaracao TEMPLATE. (erro 65)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E065 — Erro

## Descrição

Bloco PROJECT sem declaracao TEMPLATE. (erro 65)

## Mensagem do compilador

```text
The project file declares no template. The template is required
  — it defines the validation rules for every annotation in the project.
  Without it, the compiler cannot check whether the annotations are correct.
  Add to the PROJECT block:
    TEMPLATE "file_name.synt"
```

## Onde aparece

- **MissingTemplateDeclaration**: —
