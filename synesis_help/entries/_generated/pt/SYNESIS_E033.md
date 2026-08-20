---
id: SYNESIS_E033
title: "SYNESIS_E033"
category: diagnostic
summary: "Nome de codigo ou conceito com caracteres invalidos. (erro 33)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.12.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E033 — Erro

## Descrição

Nome de codigo ou conceito com caracteres invalidos. (erro 33)

## Mensagem do compilador

```text
O nome `exemplo` contem o caractere invalido `exemplo`,
  que nao e permitido em identificadores Synesis. Identificadores aceitam
  apenas letras, numeros, underscore e hifen, e devem comecar com uma letra.
  Por exemplo: use `_` em vez de `exemplo`.
```

## Onde aparece

- **InvalidIdentifierCharacter**: `name`, `invalid_char`
