---
id: BLOCK_TEMPLATE
title: "TEMPLATE"
category: block
summary: "Define quais campos existem, de que tipo, e onde podem ser usados."
syntax: "TEMPLATE <nome> [version: \"<v>\"] [<ESCOPO> FIELDS ... END <ESCOPO> FIELDS] [FIELD ... END FIELD]"
file: ".synt"
see_also: [BLOCK_FIELD, BLOCK_FIELDS_SPEC, BLOCK_PROJECT, SYNESIS_E069, SYNESIS_E042]
source: authored
order: 20
---

# TEMPLATE

## Descrição

O template e a **constituição do projeto**. Ele responde três perguntas, e o
compilador cobra as respostas em todos os arquivos de dados:

1. Que campos existem? — blocos `FIELD`
2. De que tipo e cada um? — `TYPE`
3. Onde cada campo pode aparecer? — `SCOPE` e os blocos `... FIELDS`

Escrever o template primeiro e o que separa uma pesquisa auditavel de uma
planilha com nomes de coluna improvisados.

## Sintaxe

```synesis
TEMPLATE <nome> [version: "<v>"] [author: "<nome>"]

[SOURCE FIELDS
    ...
END SOURCE FIELDS]

[ITEM FIELDS
    ...
END ITEM FIELDS]

[ONTOLOGY FIELDS
    ...
END ONTOLOGY FIELDS]

FIELD <nome> TYPE <tipo>
    ...
END FIELD
```

`[ ]` opcional · `<>` valor a substituir

Os metadados (`version`, `author`) ficam **na mesma linha** do nome. Em linha
própria não compilam.

## Exemplo

```synesis
TEMPLATE entrevistas version: "1.0"

ITEM FIELDS
    REQUIRED code
    OPTIONAL note
END ITEM FIELDS

FIELD code TYPE CODE
    SCOPE ITEM
    DESCRIPTION conceitos atribuidos a unidade
END FIELD

FIELD note TYPE MEMO
    SCOPE ITEM
END FIELD
```

## Regras

- Nomes de campo são únicos no template (`SYNESIS_E069`).
- Todo `FIELD` definido precisa ser listado em algum bloco `... FIELDS`
  (`SYNESIS_E042`) — campo definido e nunca usado e ruído.
- Todo campo listado precisa ter um `FIELD` correspondente (`SYNESIS_E039`).
- O `SCOPE` do `FIELD` deve concordar com o bloco que o lista (`SYNESIS_E006`).
- Um bloco `... FIELDS` por escopo (`SYNESIS_E057`).

## Ver também

`BLOCK_FIELD`, `BLOCK_FIELDS_SPEC`, `BLOCK_PROJECT`, `SYNESIS_E069`, `SYNESIS_E042`
