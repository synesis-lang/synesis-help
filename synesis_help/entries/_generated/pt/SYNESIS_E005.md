---
id: SYNESIS_E005
title: "SYNESIS_E005"
category: diagnostic
summary: "ONTOLOGY presente mas template nao declara ONTOLOGY FIELDS. (erro 5)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.11.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Nao edite. Conteudo autoral vai em entries/authored/. -->

# SYNESIS_E005 — Erro

## Descricao

ONTOLOGY presente mas template nao declara ONTOLOGY FIELDS. (erro 5)

## Mensagem do compilador

```text
O projeto contem blocos ONTOLOGY, mas o template nao declara nenhum
  campo em `ONTOLOGY FIELDS`. Sem essa configuracao, os campos dos
  conceitos nao podem ser validados.
  Este problema esta na definicao do template. Se voce nao e o autor
  do template, avise o coordenador do projeto.
  Para corrigir, adicione ao template:
      ONTOLOGY FIELDS
          REQUIRED nome_do_campo
      END ONTOLOGY FIELDS
```

## Onde aparece

- **OntologyWithoutTemplateFields**: —
