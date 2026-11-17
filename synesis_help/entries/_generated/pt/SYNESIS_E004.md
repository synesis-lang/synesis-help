---
id: SYNESIS_E004
title: "SYNESIS_E004"
category: diagnostic
summary: "Codigo usado em ITEM/CHAIN sem definicao em ONTOLOGY."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E004 — Erro

## Descrição

Codigo usado em ITEM/CHAIN sem definicao em ONTOLOGY.

## Mensagem do compilador

```text
The code `CODIGO_A` is not defined in the project's organizing model. Every
  code used in the annotations needs a matching concept
  declared in an ONTOLOGY block.
  To create the concept, add to a `.syno` file:
      ONTOLOGY CODIGO_A
          description: ...
      END ONTOLOGY
```

## Onde aparece

- **UndefinedCode**: `code`, `context`, `suggestions`
