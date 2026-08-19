---
id: SYNESIS_E004
title: "SYNESIS_E004"
category: diagnostic
summary: "Codigo usado em ITEM/CHAIN sem definicao em ONTOLOGY."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.11.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Nao edite. Conteudo autoral vai em entries/authored/. -->

# SYNESIS_E004 — Erro

## Descricao

Codigo usado em ITEM/CHAIN sem definicao em ONTOLOGY.

## Mensagem do compilador

```text
O codigo `CODIGO_A` nao esta definido na ontologia do projeto. Todos os
  codigos usados nas anotacoes precisam ter um conceito correspondente
  declarado em um bloco ONTOLOGY.
  Para criar o conceito, adicione em um arquivo `.syno`:
      ONTOLOGY CODIGO_A
          description: ...
      END ONTOLOGY
```

## Onde aparece

- **UndefinedCode**: `code`, `context`, `suggestions`
