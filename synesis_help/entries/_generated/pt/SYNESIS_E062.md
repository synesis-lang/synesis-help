---
id: SYNESIS_E062
title: "SYNESIS_E062"
category: diagnostic
summary: "Arquivo .syno no diretorio do projeto nao referenciado em INCLUDE ONTOLOGY. (erro 62)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.11.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Nao edite. Conteudo autoral vai em entries/authored/. -->

# SYNESIS_E062 — Erro

## Descricao

Arquivo .syno no diretorio do projeto nao referenciado em INCLUDE ONTOLOGY. (erro 62)

## Mensagem do compilador

```text
O arquivo `arquivo.syn` (extensao `.syno`) existe no diretorio do projeto
  mas nao esta referenciado em nenhum bloco INCLUDE ONTOLOGY no `.synp`.
  Sem essa declaracao, a ontologia nao sera carregada e os codigos definidos
  nela nao poderao ser validados.
  Adicione ao arquivo de projeto:
    INCLUDE ONTOLOGY "arquivo.syn"
```

## Onde aparece

- **MissingOntologyInclude**: `filename`
