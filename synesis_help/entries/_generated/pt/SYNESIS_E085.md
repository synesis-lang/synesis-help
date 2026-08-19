---
id: SYNESIS_E085
title: "SYNESIS_E085"
category: diagnostic
summary: "Campo REQUIRED ... ON DATASET sem valor no registro do dataset TOML. (erro 85)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.11.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Nao edite. Conteudo autoral vai em entries/authored/. -->

# SYNESIS_E085 — Erro

## Descricao

Campo REQUIRED ... ON DATASET sem valor no registro do dataset TOML. (erro 85)

## Mensagem do compilador

```text
O campo `nome_do_campo` foi declarado `REQUIRED ... ON DATASET`,
  ou seja, seu valor deve vir do registro TOML do SOURCE — nao do texto.
  Mas o registro `@autor2024` nao tem valor no caminho
  `exemplo`.
  Verifique a secao/campo TOML, ou remova a exigencia `ON DATASET`
  do template.
```

## Onde aparece

- **MissingDatasetValue**: `field_name`, `bibref`, `dataset_path`
