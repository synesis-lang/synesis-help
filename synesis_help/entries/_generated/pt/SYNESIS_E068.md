---
id: SYNESIS_E068
title: "SYNESIS_E068"
category: diagnostic
summary: "Dois blocos ONTOLOGY com o mesmo nome de conceito. (erro 68)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.11.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Nao edite. Conteudo autoral vai em entries/authored/. -->

# SYNESIS_E068 — Erro

## Descricao

Dois blocos ONTOLOGY com o mesmo nome de conceito. (erro 68)

## Mensagem do compilador

```text
O conceito `exemplo` esta definido mais de uma vez na
  ontologia do projeto:
  - exemplo
  - exemplo
  Cada conceito deve ter um nome unico em todo o projeto. Verifique
  se os dois blocos representam o mesmo conceito — se sim, unifique-os.
  Se nao, renomeie um deles para que os nomes sejam distintos.
```

## Onde aparece

- **DuplicateOntologyConcept**: `concept_name`, `file_a`, `file_b`
