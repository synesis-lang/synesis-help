---
id: SYNESIS_E084
title: "SYNESIS_E084"
category: diagnostic
summary: "INCLUDE SHARED usado com tipo diferente de ONTOLOGY. (erro 84)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.12.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E084 — Erro

## Descrição

INCLUDE SHARED usado com tipo diferente de ONTOLOGY. (erro 84)

## Mensagem do compilador

```text
`INCLUDE SHARED` so e valido para `ONTOLOGY`, mas foi usado com
  `exemplo` (`exemplo`).
  A palavra `SHARED` autoriza um alvo FORA da pasta do projeto — existe
  para compartilhar o vocabulario conceitual (a ontologia) entre projetos
  do mesmo estudo. Os demais includes devem permanecer contidos no projeto.
  Remova o `SHARED`, ou mova o arquivo para dentro da pasta do projeto.
```

## Onde aparece

- **SharedOnlyForOntology**: `include_type`, `path`
