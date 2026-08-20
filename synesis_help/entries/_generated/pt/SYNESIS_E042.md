---
id: SYNESIS_E042
title: "SYNESIS_E042"
category: diagnostic
summary: "FIELD definido mas nao listado em nenhum SCOPE FIELDS. (erro 42)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.12.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E042 — Erro

## Descrição

FIELD definido mas nao listado em nenhum SCOPE FIELDS. (erro 42)

## Mensagem do compilador

```text
O campo 'nome_do_campo' esta definido no template, mas nao aparece
  em nenhum bloco `SOURCE FIELDS`, `ITEM FIELDS` ou `ONTOLOGY FIELDS`.
  Um campo definido mas nao listado nunca sera reconhecido nas anotacoes.
  Inclua `nome_do_campo` no bloco `ITEM FIELDS` correspondente
  ao seu escopo, ou remova a definicao se ela nao for necessaria.
```

## Onde aparece

- **OrphanFieldDefinition**: `field_name`, `scope`
