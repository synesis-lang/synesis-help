---
id: SYNESIS_E032
title: "SYNESIS_E032"
category: diagnostic
summary: "Campo TOPIC recebendo valor com espacos. (erro 32)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.11.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Nao edite. Conteudo autoral vai em entries/authored/. -->

# SYNESIS_E032 — Erro

## Descricao

Campo TOPIC recebendo valor com espacos. (erro 32)

## Mensagem do compilador

```text
O valor `valor` do campo `nome_do_campo` contem espacos, o que
  nao e permitido para campos do tipo TOPIC. Espacos sao interpretados como
  separadores e causariam ambiguidade na hierarquia ontologica.
  Use underscore no lugar de espacos. Por exemplo: `valor`.
```

## Onde aparece

- **TopicWithSpaces**: `field_name`, `value`
