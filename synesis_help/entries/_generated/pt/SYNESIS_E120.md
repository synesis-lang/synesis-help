---
id: SYNESIS_E120
title: "SYNESIS_E120"
category: diagnostic
summary: "Bloco sem mencao em ITEM (CODE ou CHAIN) e sem descendente mencionado."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E120 — Erro

## Descrição

Bloco sem mencao em ITEM (CODE ou CHAIN) e sem descendente mencionado.

## Mensagem do compilador

```text
The concept `exemplo` is not mentioned in any ITEM (CODE or CHAIN) and has
  no mentioned descendant. A broad term without direct use is legitimate when
  it completes the hierarchy (Z39.19 §11.1.8); without descendants, nothing supports it.
```

## Onde aparece

- **UngroundedConcept**: `concept`
