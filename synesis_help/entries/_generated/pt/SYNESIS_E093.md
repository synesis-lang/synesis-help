---
id: SYNESIS_E093
title: "SYNESIS_E093"
category: diagnostic
summary: "Identificador de questao repetido no projeto."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E093 — Erro

## Descrição

Identificador de questao repetido no projeto.

## Mensagem do compilador

```text
The question identifier `exemplo` was already used on line 2.
  Each question needs a unique identifier in the project (case does not
  matter: `Q1` and `q1` are the same). Rename one of the two.
```

## Onde aparece

- **DuplicateQuestionId**: `question_id`, `first_line`
