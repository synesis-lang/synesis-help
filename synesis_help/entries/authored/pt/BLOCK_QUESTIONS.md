---
id: BLOCK_QUESTIONS
title: "QUESTIONS"
category: block
summary: "Questões de competência: o que a estrutura do projeto precisa permitir responder."
syntax: "QUESTIONS <id>: <texto> [...] END QUESTIONS"
file: ".synp"
see_also: [BLOCK_PROJECT, BLOCK_PHASE, BLOCK_EXPORT, SYNESIS_E091, SYNESIS_E092, SYNESIS_E093]
source: authored
order: 75
requires_synesis: ">=0.15.0"
---

# QUESTIONS

## Descrição

As **questões de competência** dizem o que o projeto precisa conseguir
responder quando estiver pronto. Elas orientam o template (quais campos e
papéis existem) e servem de critério de aceite do princípio organizador:
se uma questão não tem como ser respondida pelo que foi codificado, falta
estrutura.

As questões viajam com o projeto: aparecem no JSON compilado, no contexto do
grafo e nos prompts das fases do `synesis-coder`.

## Sintaxe

```synesis
QUESTIONS
    <id>: <texto>
    [<id>: <texto>]
END QUESTIONS
```

`[ ]` opcional · `<>` valor a substituir

O bloco fica dentro de `PROJECT`, no `.synp`.

## Exemplo

```synesis
QUESTIONS
    Q1: Quais evidências tratam de phishing ou de seus subtipos?
    Q2: Quais conceitos não têm evidência direta nem indireta?
    Q3: Por quais rótulos cada tipo de golpe é conhecido?
END QUESTIONS
```

## Regras

- Cada linha tem a forma `<id>: <texto>` (`SYNESIS_E091`) e texto não vazio
  (`SYNESIS_E092`).
- Identificadores não se repetem no projeto (`SYNESIS_E093`).

## Ver também

`BLOCK_PROJECT`, `BLOCK_PHASE`, `BLOCK_EXPORT`
