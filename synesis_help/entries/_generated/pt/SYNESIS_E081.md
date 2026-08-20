---
id: SYNESIS_E081
title: "SYNESIS_E081"
category: diagnostic
summary: "Dois membros declaram IDENTIFIES do mesmo rotulo no link step. (erro 81)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.12.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E081 — Erro

## Descrição

Dois membros declaram IDENTIFIES do mesmo rotulo no link step. (erro 81)

## Mensagem do compilador

```text
A entidade `exemplo` e declarada com `IDENTIFIES` por dois projetos:
  `exemplo` e `exemplo`.
  Um rotulo de entidade tem um unico corpus proprietario (a chave primaria).
  Se sao esquemas de ID distintos da mesma pessoa (Lattes vs ORCID), o hub
  deve `REFERS TO` a periferia — nao declarar dois `IDENTIFIES` do mesmo rotulo.
```

## Onde aparece

- **DuplicateEntityOwner**: `entity`, `first_member`, `duplicate_member`
