---
id: SYNESIS_E082
title: "SYNESIS_E082"
category: diagnostic
summary: "TYPE divergente entre campos da mesma entidade no link step. (erro 82)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.12.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E082 — Erro

## Descrição

TYPE divergente entre campos da mesma entidade no link step. (erro 82)

## Mensagem do compilador

```text
Os campos que participam da entidade `exemplo` tem `TYPE` divergente:
  `exemplo` declara `TYPE exemplo`; `exemplo` declara `TYPE exemplo`.
  Campos da mesma entidade (o `IDENTIFIES` e todos os `REFERS TO`) devem ter
  o mesmo `TYPE` — a divergencia indica que os dois lados nao modelam a
  mesma coisa. Alinhe os tipos no template.
```

## Onde aparece

- **TypeMismatchInLinkage**: `entity`, `member_a`, `type_a`, `member_b`, `type_b`
