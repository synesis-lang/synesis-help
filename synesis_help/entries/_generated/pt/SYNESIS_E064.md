---
id: SYNESIS_E064
title: "SYNESIS_E064"
category: diagnostic
summary: "Nenhum arquivo .synp encontrado na raiz do workspace."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E064 — Erro

## Descrição

Este código cobre 3 situações distintas:

- **MissingProjectFile** — Nenhum arquivo .synp encontrado na raiz do workspace.
- **MissingTemplateFile** — Template especificado no .synp nao existe no filesystem.
- **InvalidProjectFile** — Arquivo .synp contem erros de sintaxe e nao pode ser parseado.

## Mensagem do compilador

**MissingProjectFile**

```text
No .synp file found at the workspace root: exemplo
  Semantic validation disabled.
  To enable full validation, create a PROJECT file at the workspace root.
  Example: project.synp
```

**MissingTemplateFile**

```text
Template 'exemplo' given in 'exemplo' was not found.
  Check that the path is correct and relative to the project folder.
  Or create the template file at the given location.
```

**InvalidProjectFile**

```text
Project file 'exemplo' has syntax errors:
  exemplo
  Semantic validation is disabled until the file is fixed.
```

## Onde aparece

- **MissingProjectFile**: `workspace_root`
- **MissingTemplateFile**: `template_path`, `project_file`
- **InvalidProjectFile**: `project_file`, `parse_error`
