---
id: SYNESIS_E079
title: "SYNESIS_E079"
category: diagnostic
summary: "Campo REQUIRED ... ON BIBLIOGRAPHY sem valor no .bib do SOURCE. (erro 79)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.11.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Nao edite. Conteudo autoral vai em entries/authored/. -->

# SYNESIS_E079 — Erro

## Descricao

Campo REQUIRED ... ON BIBLIOGRAPHY sem valor no .bib do SOURCE. (erro 79)

## Mensagem do compilador

```text
O campo `nome_do_campo` foi declarado `REQUIRED ... ON BIBLIOGRAPHY`,
  ou seja, seu valor deve vir da entrada `.bib` do SOURCE — nao do texto.
  Mas a entrada `@autor2024` nao tem o campo `nome_do_campo`.
  Adicione `nome_do_campo = {...}` a entrada `@autor2024` no arquivo
  `.bib`, ou remova a exigencia `ON BIBLIOGRAPHY` do template.
```

## Onde aparece

- **MissingBibliographyValue**: `field_name`, `bibref`
