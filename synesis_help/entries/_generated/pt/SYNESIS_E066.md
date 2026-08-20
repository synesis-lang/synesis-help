---
id: SYNESIS_E066
title: "SYNESIS_E066"
category: diagnostic
summary: "Dois blocos PROJECT no mesmo arquivo .synp. (erro 66)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.12.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E066 — Erro

## Descrição

Dois blocos PROJECT no mesmo arquivo .synp. (erro 66)

## Mensagem do compilador

```text
Este arquivo de projeto contem dois blocos PROJECT. Apenas um bloco
  PROJECT e permitido por arquivo — o compilador nao saberia qual dos
  dois usar como ponto de entrada.
  Remova o bloco duplicado ou separe os projetos em arquivos `.synp` distintos.
```

## Onde aparece

- **DuplicateProjectBlock**: —
