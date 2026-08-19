---
id: GUIDE_FILES
title: "Arquivos e extensões"
category: overview
summary: "Que arquivo guarda o que, e como eles se referenciam."
see_also: [GUIDE_START, BLOCK_PROJECT, MOD_INCLUDE, SYNESIS_E061, SYNESIS_E062, GUIDE_REVIEW]
source: authored
order: 20
---

# Arquivos e extensões

## Tabela de referencia

| Extensão | Conteúdo | Quantos |
|---|---|---|
| `.synp` | projeto: template, inclusões, metadados | exatamente 1 |
| `.synt` | template: campos, tipos, escopos | 1 por projeto |
| `.syno` | ontologia: conceitos/códigos | 0 ou mais |
| `.syn` | anotações: `SOURCE` e `ITEM` | 0 ou mais |
| `.bib` | bibliografia BibTeX | 1 ou mais |
| `.synr` | revisões propostas (`# REVISION`) | 0 ou mais |

O `.synr` é o único da lista que **não** entra num `INCLUDE`: ele não é
parte do projeto, e sim um artefato de trabalho do `synesis-coder`, lido e
consumido pelo `incorporate`. Ver `GUIDE_REVIEW`.

## Como se referenciam

```
projeto.synp
├── TEMPLATE "modelo.synt"
├── INCLUDE BIBLIOGRAPHY "refs.bib"
├── INCLUDE ANNOTATIONS "dados.syn"
└── INCLUDE ONTOLOGY "codigos.syno"
```

O `.synp` e o único arquivo que o compilador procura sozinho — todos os outros
precisam estar declarados nele.

## Regra que pega todo mundo

Um `.syn` ou `.syno` que existe na pasta mas **não** foi declarado num
`INCLUDE` gera erro (`SYNESIS_E061`, `SYNESIS_E062`). O `.synr` está fora
dessa regra — por isso convém mantê-lo em pasta separada (`revisions/`).

Isso e deliberado: arquivo de dados silenciosamente ignorado e pior que
arquivo ausente — a analise fica incompleta sem ninguém notar.

## Ver também

`GUIDE_START`, `BLOCK_PROJECT`, `MOD_INCLUDE`
