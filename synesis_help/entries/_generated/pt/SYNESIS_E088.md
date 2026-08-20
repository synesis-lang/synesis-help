---
id: SYNESIS_E088
title: "SYNESIS_E088"
category: diagnostic
summary: "Campo ORDERED escrito com o rotulo em vez do indice. (erro 88)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.12.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E088 — Erro

## Descrição

Campo ORDERED escrito com o rotulo em vez do indice. (erro 88)

## Mensagem do compilador

```text
O campo 'nome_do_campo' foi escrito com o rotulo `exemplo`,
  mas em campos `ORDERED` o dado gravado e o INDICE. O indice define a
  ordem dos valores e nao admite variantes de grafia; o rotulo e
  declarado no template e exibido pelo editor ao lado do indice.
  Escreva `nome_do_campo: 2`.
```

## Onde aparece

- **OrderedValueAsLabel**: `field_name`, `label`, `index`
