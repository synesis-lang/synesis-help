---
id: SYNESIS_E064
title: "SYNESIS_E064"
category: diagnostic
summary: "Nenhum arquivo .synp encontrado na raiz do workspace."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.12.0"
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
Nenhum arquivo .synp encontrado na raiz do workspace: exemplo
  Validacao semantica desativada.
  Para ativar validacao completa, crie um arquivo PROJECT na raiz do workspace.
  Exemplo: projeto.synp
```

**MissingTemplateFile**

```text
Template 'exemplo' especificado em 'exemplo' nao encontrado.
  Verifique se o caminho esta correto e relativo ao diretorio do projeto.
  Ou crie o arquivo de template no local especificado.
```

**InvalidProjectFile**

```text
Arquivo de projeto 'exemplo' contem erros de sintaxe:
  exemplo
  Validacao semantica desativada ate que o arquivo seja corrigido.
```

## Onde aparece

- **MissingProjectFile**: `workspace_root`
- **MissingTemplateFile**: `template_path`, `project_file`
- **InvalidProjectFile**: `project_file`, `parse_error`
