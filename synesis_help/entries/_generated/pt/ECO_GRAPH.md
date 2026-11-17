---
id: ECO_GRAPH
title: "synesis-graph"
category: ecosystem
summary: "Converte projetos compilados em bancos de grafo e visualizacoes."
see_also: [ECO_SYNESIS, ECO_LSP, ECO_CODER, GUIDE_ECOSYSTEM]
source: generated
order: 40
version: "0.13.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_ecosystem.py. Nao edite. -->

# synesis-graph

## Descricao

Papel no ecossistema: **exportacao para grafos** · versao 0.13.0

Consome o artefato do `synesis compile`, nao os `.syn` diretamente.

**O grafo exportado se descreve.** Ao sincronizar com um banco (ArcadeDB ou Neo4j), o `synesis-graph` grava um vertice `ProjectContext` com o contexto do proprio projeto: a `DESCRIPTION` do `.synp`, e o template inteiro como documento legivel — cada campo com tipo, escopo, descricao, escala de valores e **GUIDELINES**, mais as arestas do grafo com sua direcao.

Isso importa porque o schema de um banco e sintaxe sem semantica: ele diz que existe um vertice `Aspect` com a propriedade `name`, mas nao que `Aspect` e uma escala ordenada nem o que cada valor significa. As `GUIDELINES` que voce escreveu sao o seu protocolo de codificacao — as regras de decisao que dizem o que conta como instancia valida de um campo. Sem elas no grafo, quem consulta precisa inferir seu criterio a partir dos dados; com elas, passa a conhece-lo.

O contexto viaja com os dados, nao com a ferramenta: qualquer consumidor do grafo o recebe — o Claude Desktop, qualquer cliente MCP, o studio do proprio banco, ou um colega que receba uma copia. E e derivado do seu template, entao dois projetos diferentes produzem contextos diferentes.

Para ler: `MATCH (p:ProjectContext) RETURN p.description, p.template_doc`.

## Uso

```text
SYNESIS GRAPH (v0.13.0)

Universal pipeline from Synesis projects to graph databases and visualizations.

Usage: synesis-graph [OPTIONS] COMMAND [ARGUMENTS]...

Global Options:
  -v, --verbose        Increase log verbosity (DEBUG). Repeatable.
  -q, --quiet          Decrease log verbosity (-q WARNING, -qq ERROR). Repeatable.
  --version            Show version and exit
  --help               Show this message and exit

Commands:

  Graph Backends
    neo4j                Sync project to a Neo4j database (bolt://)
    arcadedb             Sync project to an ArcadeDB database (http://)
    arcadedb-embedded    Sync project to a local ArcadeDB database (no server)
    html                 Render an interactive HTML graph visualization

  Local Database
    serve                Keep a local database running for chat clients

Run 'synesis-graph COMMAND --help' for options and examples of each backend.
```

Para os parametros de um subcomando: `synesis-graph <comando> --help`.
