---
id: BLOCK_ITEM
title: "ITEM"
category: block
summary: "Unidade de ocorrência: o que foi observado ou registrado."
syntax: "ITEM @<bibref> <campo>: <valor> [...] END ITEM"
file: ".syn"
see_also: [BLOCK_SOURCE, BLOCK_ONTOLOGY, GUIDE_PRIMITIVES, TYPE_CODE, TYPE_CHAIN, SYNESIS_E002, SYNESIS_E023]
source: authored
order: 60
---

# ITEM

## Descrição

`ITEM` e a **unidade de ocorrência**. Responde:

> Qual e a unidade concreta que estou registrando?

E o mais flexível dos três primitivos. Conforme a metodologia, um `ITEM` pode
ser um excerto codificado, um incidente, uma unidade de registro, um episódio
narrativo, um argumento, uma evidencia causal, um enunciado, um achado de
revisão, um requisito, uma proposição extraída ou uma relação.

O que não muda: um `ITEM` sempre pertence a um `SOURCE`. Ocorrência sem
procedência não e evidencia.

## Sintaxe

```synesis
ITEM @<bibref>
    <campo>: <valor>
    [<campo>: <valor>]
END ITEM
```

`[ ]` opcional · `<>` valor a substituir

Um `ITEM` não pode ser vazio (`SYNESIS_E023`). Quais campos são aceitos vem de
`ITEM FIELDS` no template.

## Regras

- Todo `ITEM` precisa de um `SOURCE` com o mesmo `@bibref` (`SYNESIS_E002`).
- `ITEM` vazio e erro (`SYNESIS_E023`).
- Códigos usados precisam estar definidos na ontologia (`SYNESIS_E004`).
- Campos obrigatórios pelo template devem estar presentes (`SYNESIS_E020`);
  campos proibidos, ausentes (`SYNESIS_E021`).

## Exemplo

```synesis
ITEM @silva2024
    quote: "quando o rio subiu, foi o vizinho que avisou"
    code: REDE_APOIO, ALERTA_INFORMAL
    chain: ALERTA_INFORMAL -> PRECEDE -> REDE_APOIO
END ITEM
```

## Ver também

`GUIDE_PRIMITIVES`, `BLOCK_SOURCE`, `BLOCK_ONTOLOGY`, `TYPE_CODE`, `SYNESIS_E002`
