---
id: SYNESIS_E078
title: "SYNESIS_E078"
category: diagnostic
summary: "IDENTIFIES/REFERS TO em campo que nao e SCOPE SOURCE. (erro 78)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.11.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Nao edite. Conteudo autoral vai em entries/authored/. -->

# SYNESIS_E078 — Erro

## Descricao

IDENTIFIES/REFERS TO em campo que nao e SCOPE SOURCE. (erro 78)

## Mensagem do compilador

```text
O campo `nome_do_campo` usa `exemplo`, mas esta declarado com
  `SCOPE ITEM`. Os modificadores de ligacao (`IDENTIFIES` / `REFERS TO`)
  so fazem sentido em campos `SCOPE SOURCE` — a ligacao entre projetos
  opera sobre SOURCEs (unidades de coleta), nao sobre ITEMs ou conceitos.
  Mova o modificador para um campo SOURCE, ou remova-o deste campo.
```

## Onde aparece

- **LinkageModifierOutsideSource**: `field_name`, `modifier`, `scope`
