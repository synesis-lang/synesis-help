---
id: SYNESIS_E074
title: "SYNESIS_E074"
category: diagnostic
summary: "Arquivo .syno declarado em INCLUDE ONTOLOGY nao encontrado. (erro 74)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.11.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Nao edite. Conteudo autoral vai em entries/authored/. -->

# SYNESIS_E074 — Erro

## Descricao

Arquivo .syno declarado em INCLUDE ONTOLOGY nao encontrado. (erro 74)

## Mensagem do compilador

```text
O arquivo de ontologia `arquivo.syn` esta declarado em INCLUDE ONTOLOGY
  mas nao foi encontrado. Sem ele, os codigos usados nas anotacoes nao podem
  ser validados contra a ontologia.
  Verifique se o nome esta correto e se o arquivo existe. O caminho deve ser
  relativo a pasta onde esta o arquivo de projeto (`.synp`).
```

## Onde aparece

- **MissingOntologyFile**: `filename`
