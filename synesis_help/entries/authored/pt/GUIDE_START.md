---
id: GUIDE_START
title: "Por onde começar"
category: overview
summary: "Os quatro arquivos de um projeto Synesis e a ordem de escrita."
see_also: [BLOCK_PROJECT, BLOCK_TEMPLATE, GUIDE_PRIMITIVES, GUIDE_FILES, BLOCK_ITEM]
source: authored
order: 10
---

# Por onde começar

## A ideia em uma frase

Synesis torna a analise **verificável**: você declara as regras da sua
codificação uma vez, e o compilador as cobra em cada unidade analisada.

## Os quatro arquivos

| Arquivo | Papel | Bloco principal |
|---|---|---|
| `.synp` | ponto de entrada; amarra tudo | `PROJECT` |
| `.synt` | as regras: que campos existem | `TEMPLATE`, `FIELD` |
| `.syno` | o sistema conceitual | `ONTOLOGY` |
| `.syn` | os dados: proveniência e ocorrências | `SOURCE`, `ITEM` |

Some-se a esses um `.bib` BibTeX com as referencias — a ancora bibliográfica
das fontes.

Antes de escrever, vale conhecer os três primitivos e o que cada um significa
na **sua** metodologia: `GUIDE_PRIMITIVES`.

## Ordem de escrita

1. **`.synt` primeiro.** Decidir os campos antes dos dados evita retrabalho.
   Comece mínimo: um campo de citação, um de código.
2. **`.syno` em seguida.** Os conceitos que você ja sabe que vai usar. A lista
   cresce durante a analise — e normal.
3. **`.synp`** amarrando os arquivos.
4. **`.syn`** por ultimo: proveniência e ocorrências.

## Fluxo mínimo

```synesis
# template.synt
TEMPLATE minimo
ITEM FIELDS
    REQUIRED quote, code
END ITEM FIELDS
FIELD quote TYPE QUOTATION
    SCOPE ITEM
END FIELD
FIELD code TYPE CODE
    SCOPE ITEM
END FIELD
```

```synesis
# dados.syn
SOURCE @silva2024
END SOURCE

ITEM @silva2024
    quote: "o rio subiu sem aviso"
    code: EVENTO_EXTREMO
END ITEM
```

## Próximo passo

Rode `synesis compile` na pasta do projeto. Cada erro reportado tem um código
(`SYNESIS_E0NN`) com entry própria neste guia.

## Ver também

`BLOCK_TEMPLATE`, `BLOCK_ITEM`, `GUIDE_FILES`
