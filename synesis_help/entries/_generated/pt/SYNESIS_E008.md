---
id: SYNESIS_E008
title: "SYNESIS_E008"
category: diagnostic
summary: "Chain qualificada usada mas template nao define RELATIONS. (erro 8)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.11.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Nao edite. Conteudo autoral vai em entries/authored/. -->

# SYNESIS_E008 — Erro

## Descricao

Chain qualificada usada mas template nao define RELATIONS. (erro 8)

## Mensagem do compilador

```text
Esta cadeia usa relacoes nomeadas (ex: `Conceito -> RELACAO -> Conceito`),
  mas o template nao define nenhum bloco `RELATIONS` para o campo
  `nome_do_campo`.
  Se o template usa cadeias simples, reescreva a cadeia sem relacoes:
  `Conceito -> Conceito`. Se deseja usar relacoes nomeadas, peca ao
  coordenador do projeto que adicione um bloco `RELATIONS` ao template.
```

## Onde aparece

- **QualifiedChainWithoutRelations**: `field_name`
