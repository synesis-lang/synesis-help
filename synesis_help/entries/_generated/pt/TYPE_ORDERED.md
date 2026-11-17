---
id: TYPE_ORDERED
title: "ORDERED"
category: field_type
summary: "Valor escolhido de uma lista fechada, com ordem."
syntax: FIELD <nome> TYPE ORDERED SCOPE <escopo> VALUES ... END VALUES [...] END FIELD
see_also: [SYNESIS_E049, SYNESIS_E054, SYNESIS_E055, SYNESIS_E056, SYNESIS_E088, TYPE_QUOTATION, TYPE_MEMO, TYPE_CODE]
source: generated
order: 80
requires_synesis: ">=0.15.0"
---

<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. Não edite. Conteúdo autoral vai em entries/authored/. -->

# ORDERED

## Sintaxe

```synesis
FIELD <nome> TYPE ORDERED
    SCOPE <escopo>
    VALUES ... END VALUES
    [DESCRIPTION <texto>]
    [GUIDELINES ... END GUIDELINES]
    [CONTEXT FROM DATASET <campo>]
END FIELD
```

`[ ]` opcional · `<>` valor a substituir

## Exemplo

```synesis
FIELD exemplo_ordered TYPE ORDERED
    SCOPE ITEM
    VALUES
        [1] baixo: intensidade baixa
        [2] alto: intensidade alta
    END VALUES
END FIELD
```

## Valor na anotação

O valor gravado é o **índice**, não o rótulo:

```synesis
aspect: 11
```

O rótulo (`Econômico`) pertence à declaração do template e é exibido pelo editor ao lado do índice — não se repete na anotação, porque admite variantes de grafia (`Economico`, `ECONOMICO`) que fragmentariam o corpus. Escrever o rótulo é `SYNESIS_E088`.

## Propriedades

| Propriedade | Situação | Erro se violada |
|---|---|---|
| `CONTEXT FROM DATASET` | Permitido | - |
| `DESCRIPTION` | Permitido | - |
| `GUIDELINES` | Permitido | - |
| `ARITY` | Proibido | SYNESIS_E055 |
| `FORMAT` | Proibido | SYNESIS_E054 |
| `RELATIONS` | Proibido | SYNESIS_E056 |
| `VALUES` | Obrigatório | SYNESIS_E049 |

## Regras

- **`VALUES` é obrigatório.** The field 'nome_do_campo' is of type ORDERED, but does not define a

## Ver também

`SYNESIS_E049`, `SYNESIS_E054`, `SYNESIS_E055`, `SYNESIS_E056`, `SYNESIS_E088`, `TYPE_QUOTATION`, `TYPE_MEMO`, `TYPE_CODE`
