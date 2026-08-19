---
id: ECO_GRAPH
title: "synesis-graph"
category: ecosystem
summary: "Converte projetos compilados em bancos de grafo e visualizacoes."
see_also: [ECO_SYNESIS, ECO_LSP, ECO_CODER, GUIDE_ECOSYSTEM]
source: generated
order: 40
version: "0.7.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_ecosystem.py. Nao edite. -->

# synesis-graph

## Descricao

Papel no ecossistema: **exportacao para grafos** · versao 0.7.0

Consome o artefato do `synesis compile`, nao os `.syn` diretamente.

## Uso

```text
SYNESIS GRAPH (v0.7.0)

Universal pipeline from Synesis projects to graph databases and visualizations.

Usage: synesis-graph [OPTIONS] COMMAND [ARGUMENTS]...

Global Options:
  -v, --verbose    Increase log verbosity (DEBUG). Repeatable.
  -q, --quiet      Decrease log verbosity (-q WARNING, -qq ERROR). Repeatable.
  --version        Show version and exit
  --help           Show this message and exit

Commands:

  Graph Backends
    neo4j            Sync project to a Neo4j database (bolt://)
    arcadedb         Sync project to an ArcadeDB database (http://)
    html             Render an interactive HTML graph visualization

Run 'synesis-graph COMMAND --help' for options and examples of each backend.
```

Para os parametros de um subcomando: `synesis-graph <comando> --help`.
