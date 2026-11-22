---
id: SYNESIS_E162
title: "SYNESIS_E162"
category: diagnostic
summary: "Campo do OUTPUT tambem em INPUT ou INSTRUCTION: a resposta vazaria no prompt."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E162 — Erro

## Descrição

Campo do OUTPUT tambem em INPUT ou INSTRUCTION: a resposta vazaria no prompt.

## Mensagem do compilador

```text
`exemplo`: the field `nome_do_campo` is in OUTPUT and also in exemplo.
  The answer would be in the prompt, and the model would learn to copy it.
  Instruction and input are joined into the prompt at training time.
```

## Onde aparece

- **AlpacaFieldLeak**: `block`, `field_name`, `target`
