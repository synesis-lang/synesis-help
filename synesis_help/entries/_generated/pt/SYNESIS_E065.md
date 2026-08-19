---
id: SYNESIS_E065
title: "SYNESIS_E065"
category: diagnostic
summary: "Bloco PROJECT sem declaracao TEMPLATE. (erro 65)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.11.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Nao edite. Conteudo autoral vai em entries/authored/. -->

# SYNESIS_E065 — Erro

## Descricao

Bloco PROJECT sem declaracao TEMPLATE. (erro 65)

## Mensagem do compilador

```text
O arquivo de projeto nao declara nenhum template. O template e obrigatorio
  — ele define as regras de validacao para todas as anotacoes do projeto.
  Sem ele, o compilador nao pode verificar se as anotacoes estao corretas.
  Adicione ao bloco PROJECT:
    TEMPLATE "nome_do_arquivo.synt"
```

## Onde aparece

- **MissingTemplateDeclaration**: —
