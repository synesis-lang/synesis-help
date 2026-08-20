---
id: SYNESIS_E058
title: "SYNESIS_E058"
category: diagnostic
summary: "Valor em bloco VALUES com espaco no inicio ou fim. (erro 58)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.12.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E058 — Erro

## Descrição

Valor em bloco VALUES com espaco no inicio ou fim. (erro 58)

## Mensagem do compilador

```text
O valor `"valor"` declarado no campo 'nome_do_campo' contem
  espaco em branco no inicio ou no final. Esses espacos invisiveis fariam
  com que o valor nao fosse reconhecido quando usado nas anotacoes.
  Remova os espacos extras ao redor do valor na declaracao do template.
```

## Onde aparece

- **ValueWithWhitespace**: `field_name`, `value`
