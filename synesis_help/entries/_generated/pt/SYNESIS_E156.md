---
id: SYNESIS_E156
title: "SYNESIS_E156"
category: diagnostic
summary: "REGISTRY com IRIs de outro NAMESPACE: nao sao conferidos (aviso; o namespace e do pesquisador)."
severity: Erro
see_also: []
source: generated
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# SYNESIS_E156 — Erro

## Descrição

REGISTRY com IRIs de outro NAMESPACE: nao sao conferidos (aviso; o namespace e do pesquisador).

## Mensagem do compilador

```text
`exemplo`: the REGISTRY has 2 published IRI(s) outside the current
  NAMESPACE `exemplo`; they are not checked and are absent from this file.

  The NAMESPACE is the researcher's decision. If the change is intended, links to the
  old IRIs will break: keep a redirect at the old address, or a separate REGISTRY.
```

## Onde aparece

- **RegistryOutsideNamespace**: `block`, `namespace`, `count`, `examples`
