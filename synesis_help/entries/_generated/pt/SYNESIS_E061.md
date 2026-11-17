---
id: SYNESIS_E061
title: "SYNESIS_E061"
category: diagnostic
summary: "Arquivo .syn no diretorio do projeto nao referenciado em INCLUDE ANNOTATIONS. (erro 61)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E061 — Erro

## Descrição

Arquivo .syn no diretorio do projeto nao referenciado em INCLUDE ANNOTATIONS. (erro 61)

## Mensagem do compilador

```text
The file `arquivo.syn` (`.syn` extension) exists in the project folder
  but is not referenced by any INCLUDE ANNOTATIONS in the `.synp`.
  Without that declaration, the compiler ignores the file and the annotations
  in it are neither loaded nor validated.
  Add to the project file:
    INCLUDE ANNOTATIONS "arquivo.syn"
```

## Onde aparece

- **MissingAnnotationsInclude**: `filename`
