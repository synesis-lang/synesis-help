---
id: SYNESIS_W067
title: "SYNESIS_W067"
category: diagnostic
summary: "Data MODIFIED anterior a data CREATED no bloco METADATA. (erro 67)."
severity: Aviso
see_also: []
source: generated
requires_synesis: ">=0.12.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_W067 — Aviso

## Descrição

Data MODIFIED anterior a data CREATED no bloco METADATA. (erro 67)

## Mensagem do compilador

```text
A data de modificacao `exemplo` e anterior a data de criacao
  `exemplo` declarada no bloco METADATA do projeto. Um projeto nao
  pode ter sido modificado antes de existir.
  Verifique as datas e corrija a que estiver incorreta. O formato esperado
  e `AAAA-MM-DD`.
```

## Onde aparece

- **ModifiedBeforeCreated**: `modified`, `created`
