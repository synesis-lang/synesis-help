---
id: SYNESIS_E062
title: "SYNESIS_E062"
category: diagnostic
summary: "Arquivo .syno no diretorio do projeto nao referenciado em INCLUDE ONTOLOGY. (erro 62)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E062 — Erro

## Descrição

Arquivo .syno no diretorio do projeto nao referenciado em INCLUDE ONTOLOGY. (erro 62)

## Mensagem do compilador

```text
The file `arquivo.syn` (`.syno` extension) exists in the project folder
  but is not referenced by any INCLUDE ONTOLOGY in the `.synp`.
  Without that declaration, the organizing model is not loaded and the codes
  defined in it cannot be validated.
  Add to the project file:
    INCLUDE ONTOLOGY "arquivo.syn"
```

## Onde aparece

- **MissingOntologyInclude**: `filename`
