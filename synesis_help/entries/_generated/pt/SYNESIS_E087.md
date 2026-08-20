---
id: SYNESIS_E087
title: "SYNESIS_E087"
category: diagnostic
summary: "Prefixo de indice `[N]` em VALUES de campo ENUMERATED. (erro 87)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.12.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E087 — Erro

## Descrição

Prefixo de indice `[N]` em VALUES de campo ENUMERATED. (erro 87)

## Mensagem do compilador

```text
O campo 'nome_do_campo' e do tipo `ENUMERATED`, mas seus valores usam
  prefixo de indice (`[0]`, `[1]`, ...). O indice existe para estabelecer
  ORDEM entre os valores e so tem efeito em campos `ORDERED`, onde ele e o
  dado gravado nas anotacoes. Em `ENUMERATED` nao ha ordem: o dado e o
  proprio rotulo, e o indice seria ignorado.
  Remova os prefixos `[N]` ou altere o tipo do campo para `ORDERED`.
```

## Onde aparece

- **IndexOnEnumeratedValue**: `field_name`
