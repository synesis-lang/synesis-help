---
id: BLOCK_SOURCE
title: "SOURCE"
category: block
summary: "Unidade de proveniência: de onde procede a informação."
syntax: "SOURCE @<bibref> [<campo>: <valor>] END SOURCE"
file: ".syn"
see_also: [BLOCK_ITEM, GUIDE_PRIMITIVES, MOD_ON_BIBLIOGRAPHY, MOD_IDENTIFIES, SYNESIS_E001, SYNESIS_E003, SYNESIS_E070]
source: authored
order: 50
---

# SOURCE

## Descrição

`SOURCE` e a **unidade de proveniência**. Responde a uma pergunta so:

> De onde procede esta informação?

Não presuma que seja um documento. Conforme o desenho da pesquisa, um `SOURCE`
pode ser uma entrevista, um artigo, um caso, uma pessoa, uma legislação, um
experimento, um registro administrativo, uma pagina web ou um dataset.

O que todos tem em comum e a função: ancorar a evidencia numa origem citável.
E isso que torna a analise rastreavel — todo trecho analisado aponta, no fim,
para uma fonte real.

## Sintaxe

```synesis
SOURCE @<bibref>
    [<campo>: <valor>]
    [<campo>: <valor>]
END SOURCE
```

`[ ]` opcional · `<>` valor a substituir

Quais campos são aceitos — e quais são obrigatórios — vem de `SOURCE FIELDS`
no template.

## Regras

- O `@bibref` deve existir no arquivo `.bib` (`SYNESIS_E001`).
- Um `@bibref` não pode abrir dois blocos `SOURCE` no mesmo arquivo
  (`SYNESIS_E070`).
- `SOURCE` sem nenhum `ITEM` associado gera aviso (`SYNESIS_E003`) — fonte
  registrada e nunca analisada costuma ser esquecimento.
- Campos marcados `ON BIBLIOGRAPHY` no template puxam o valor do `.bib`; se
  faltar la, o compilador avisa (`SYNESIS_E079`).

## Particularidade

`SOURCE` e o único escopo que aceita `IDENTIFIES` e `REFERS TO`
(`SYNESIS_E078`). A razão e conceitual: o que se liga entre projetos e a
**procedência** — o mesmo município, o mesmo caso, a mesma instituição —, não
a ocorrência analisada nem o conceito.

## Exemplo

```synesis
SOURCE @silva2024
    tipo: entrevista
    contexto: comunidade ribeirinha, marco de 2024
END SOURCE
```

## Ver também

`GUIDE_PRIMITIVES`, `BLOCK_ITEM`, `MOD_IDENTIFIES`, `SYNESIS_E001`
