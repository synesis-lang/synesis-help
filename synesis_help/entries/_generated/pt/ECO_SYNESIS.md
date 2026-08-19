---
id: ECO_SYNESIS
title: "synesis"
category: ecosystem
summary: "Compilador da linguagem: valida, compila e exporta."
see_also: [ECO_LSP, ECO_CODER, ECO_GRAPH, GUIDE_ECOSYSTEM]
source: generated
order: 10
version: "0.11.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_ecosystem.py. Nao edite. -->

# synesis

## Descricao

Papel no ecossistema: **compilador** · versao 0.11.0

E o nucleo do ecossistema. Todos os outros modulos dependem dele, e nenhum reimplementa suas regras.

## Uso

```text
SYNESIS COMPILER (v0.11.0)

Semantic compiler for knowledge engineering.

Usage: synesis [COMMAND] [OPTIONS]

Global Options:
  -v, --verbose        Increase log verbosity (DEBUG). Repeatable.
  -q, --quiet          Decrease log verbosity (-q WARNING, -qq ERROR). Repeatable.
  --version            Show version and exit
  --credits            Show intellectual genealogy and prior works
  --help               Show this message and exit

Commands:

  Project Management
    init                 Creates the minimal structure for a new project

  Compilation & Export
    compile              Compiles one project (or links several) and generates artifacts (JSON, CSV, XLS, Alpaca)

  Validation & Debugging
    check                Validates the syntax and integrity of a single file
    validate-template    Verifies the structure and consistency of a template file

  Language Reference
    help-field           Shows which properties a field type accepts, requires or forbids
    export-snippets      Generates editor snippets (VS Code) from the language rules

Run 'synesis COMMAND --help' for specific parameters, output formats, and examples.
```

Para os parametros de um subcomando: `synesis <comando> --help`.
