---
id: SYNESIS_E054
title: "SYNESIS_E054"
category: diagnostic
summary: "FORMAT declarado em campo que nao e TYPE SCALE. (erro 54)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.12.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E054 — Erro

## Descrição

FORMAT declarado em campo que nao e TYPE SCALE. (erro 54)

## Mensagem do compilador

```text
O campo 'nome_do_campo' declara `FORMAT`, mas seu tipo e `TEXT`.
  A declaracao `FORMAT [min..max]` e exclusiva de campos do tipo SCALE.
  Este problema esta na definicao do template.
  Remova a declaracao `FORMAT` ou altere o tipo do campo para `SCALE`.
```

## Onde aparece

- **FormatOnNonScale**: `field_name`, `field_type`
