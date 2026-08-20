---
id: SYNESIS_E061
title: "SYNESIS_E061"
category: diagnostic
summary: "Arquivo .syn no diretorio do projeto nao referenciado em INCLUDE ANNOTATIONS. (erro 61)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.12.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E061 — Erro

## Descrição

Arquivo .syn no diretorio do projeto nao referenciado em INCLUDE ANNOTATIONS. (erro 61)

## Mensagem do compilador

```text
O arquivo `arquivo.syn` (extensao `.syn`) existe no diretorio do projeto
  mas nao esta referenciado em nenhum bloco INCLUDE ANNOTATIONS no `.synp`.
  Sem essa declaracao, o compilador ignora o arquivo e as anotacoes nele
  contidas nao serao carregadas nem validadas.
  Adicione ao arquivo de projeto:
    INCLUDE ANNOTATIONS "arquivo.syn"
```

## Onde aparece

- **MissingAnnotationsInclude**: `filename`
