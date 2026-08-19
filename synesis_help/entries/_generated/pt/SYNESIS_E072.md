---
id: SYNESIS_E072
title: "SYNESIS_E072"
category: diagnostic
summary: "Entrada em arquivo .bib nao esta em formato BibTeX valido. (erro 72)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.11.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Nao edite. Conteudo autoral vai em entries/authored/. -->

# SYNESIS_E072 — Erro

## Descricao

Entrada em arquivo .bib nao esta em formato BibTeX valido. (erro 72)

## Mensagem do compilador

```text
A entrada `@exemplo` no arquivo de referencias `arquivo.syn`
  nao esta em formato BibTeX valido e foi ignorada pelo compilador. Por
  isso, qualquer `@bibref` que aponte para ela sera reportada como nao
  encontrada.
  Uma entrada BibTeX valida tem tres partes: um tipo, a chave de citacao
  entre chaves, e campos separados por virgula usando `=`:
    @book{exemplo,
        title = {Titulo da obra},
        year = {2024}
    }
  Verifique se a entrada comeca com um tipo (@book, @article, @misc...),
  se a chave vem entre chaves `{ }`, e se cada campo usa `=` (e nao `:`).
```

## Onde aparece

- **MalformedBibliographyEntry**: `filename`, `entry_key`
