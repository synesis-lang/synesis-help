---
id: SYNESIS_E089
title: "SYNESIS_E089"
category: diagnostic
summary: "Mesma chave em dois arquivos da bibliografia ou do dataset. (erro 89)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E089 — Erro

## Descrição

Mesma chave em dois arquivos da bibliografia ou do dataset. (erro 89)

## Mensagem do compilador

```text
The key `exemplo` appears in two project files: `exemplo:2`
  and `exemplo`. Each dataset record needs a unique key
  across the whole project; the compiler used the first occurrence and ignored this one.
  If it is the same item, delete one of the two entries. If they are different
  items, give one of them another key and update the annotations that cite it.
```

## Onde aparece

- **DuplicateKeyAcrossFiles**: `kind`, `key`, `first_file`, `first_line`, `duplicate_file`
