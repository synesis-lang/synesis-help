---
id: GUIDE_ECOSYSTEM
title: "The ecosystem"
category: overview
summary: "The tools around the language, when to use each, and how agents reach them."
see_also: [ECO_SYNESIS, ECO_LSP, ECO_CODER, ECO_GRAPH, ECO_HELP, GUIDE_START, GUIDE_REVIEW]
source: authored
order: 60
---

# The ecosystem

## Description

The language is one; the tools are several. All of them depend on the
compiler, and **none reimplements its rules**, which keeps two tools from
disagreeing about what a valid project is.

| Tool | Role | When to use |
|---|---|---|
| `synesis` | compiler | always: validates, compiles, exports |
| `synesis-lsp` | language server | while writing in the editor |
| `synesis-coder` | assisted annotation | to annotate a large corpus |
| `synesis-graph` | graph export | to analyse as a graph, serve it to AI clients |
| `synesis-help` | this guide | to look up the language (people and agents) |

## The workflow

1. **Write.** The editor shows errors as you type: that is `synesis-lsp`,
   started by the VS Code extension.
2. **Annotate.** For a large corpus, `synesis-coder` writes blocks from the
   text, guided by your template and its `GUIDELINES`.
3. **Review.** What the machine annotated is not finished data:
   `synesis-coder` has a review pipeline (`critique` → `normalize` →
   `incorporate`) that separates *proposing* from *accepting*. See
   `GUIDE_REVIEW`.
4. **Compile.** `synesis compile` validates the whole project;
   `synesis export` writes the artifacts declared in `EXPORT` blocks (JSON,
   CSV, XLS, Alpaca, OKF, SKOS).
5. **Analyse.** `synesis-graph` turns the compiled artifact into a graph.

Steps 2, 3 and 5 are optional; 1 and 4 are the minimum. Whoever uses step 2
should use step 3: LLM annotation incorporated without review enters the
corpus with the same weight as what you wrote by hand.

## What each one consumes

`synesis-graph` reads the **compiled artifact**, not the `.syn` files, so
`compile` comes first. `synesis-coder` reads the **template**, because the
fields and constraints the model must respect come from it.

## What the graph carries along

When exporting to a database, `synesis-graph` writes the **project context**
too, in a `ProjectContext` vertex: the `DESCRIPTION` of your `.synp` and the
whole template as a readable document (fields, value scales and the
`GUIDELINES` you wrote). A database schema is syntax without semantics;
without the context, whoever queries the graph (an AI over MCP, a colleague
with a copy) has to guess your coding criteria. Good `GUIDELINES` pay twice:
they guide the coder and travel with the graph. See `ECO_GRAPH`.

## Agents

Synesis works as middleware between research material and AI agents. An
agent with a shell reaches everything through the command line:

```text
synesis compile project.synp --diagnostics-json diag.json
synesis-help search "bundle status" --format=json
synesis-help lookup SYNESIS_E047 --format=json
```

`synesis-help` answers in a stable JSON contract with the version of the
compiler its entries were derived from. See `ECO_HELP`.

## Installation

Each module is its own package:

```text
pip install synesis          # compiler (required)
pip install synesis-lsp      # editor server
pip install synesis-coder    # assisted annotation
pip install synesis-graph    # graph export
pip install synesis-help     # this guide
```

The VS Code extension finds `synesis-lsp` by itself when it is installed in
the same environment.

## See also

`ECO_SYNESIS`, `ECO_LSP`, `ECO_CODER`, `ECO_GRAPH`, `ECO_HELP`,
`GUIDE_REVIEW`
