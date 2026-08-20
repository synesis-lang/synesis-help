---
id: SYNESIS_E016
title: "SYNESIS_E016"
category: diagnostic
summary: "Campo de BUNDLE ausente (violacao de pareamento)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.12.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E016 — Erro

## Descrição

Campo de BUNDLE ausente (violacao de pareamento).

## Mensagem do compilador

```text
Os campos `exemplo_a, exemplo_b` formam um pacote indivisivel (bundle) neste bloco
  — eles representam informacao composta e devem sempre aparecer juntos.
  Um ou mais campos do pacote estao ausentes: `exemplo_b`.
  Adicione os campos faltantes ou remova todos os campos do pacote.
  Um bundle parcial nao e valido.
```

## Onde aparece

- **MissingBundleField**: `bundle_fields`, `present_fields`
