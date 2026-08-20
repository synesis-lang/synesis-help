---
id: SYNESIS_E039
title: "SYNESIS_E039"
category: diagnostic
summary: "Campo listado em SCOPE FIELDS sem FIELD correspondente. (erros 39-41)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.12.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E039 — Erro

## Descrição

Campo listado em SCOPE FIELDS sem FIELD correspondente. (erros 39-41)

## Mensagem do compilador

```text
O campo 'nome_do_campo' esta listado em `ITEM FIELDS`,
  mas nao ha uma definicao `FIELD` correspondente no template.
  Adicione ao template:
      FIELD nome_do_campo TYPE TEXT
          SCOPE ITEM
      END FIELD
  Este problema esta na definicao do template. Se voce nao e o autor
  do template, avise o coordenador do projeto.
```

## Onde aparece

- **UndefinedFieldInScopeFields**: `field_name`, `scope`
