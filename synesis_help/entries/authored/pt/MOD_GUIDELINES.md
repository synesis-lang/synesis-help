---
id: MOD_GUIDELINES
title: "GUIDELINES"
category: modifier
summary: "Instruções de preenchimento do campo, para o anotador humano ou para IA."
syntax: "GUIDELINES ... END GUIDELINES"
see_also: [BLOCK_FIELD, MOD_DESCRIPTION]
source: authored
order: 30
---

# GUIDELINES

## Descrição

Texto livre com **instruções de como preencher** o campo. Aceito em qualquer
tipo.

E a diferença entre um template que so você entende e um que a equipe inteira
— ou um assistente de IA — consegue seguir. `DESCRIPTION` diz o que o campo e;
`GUIDELINES` diz como preenche-lo bem.

## Sintaxe

```synesis
FIELD code TYPE CODE
    SCOPE ITEM
    DESCRIPTION codigos atribuidos ao trecho
    GUIDELINES
        Atribua no maximo tres codigos por trecho.
        Prefira o codigo mais especifico que couber.
        Nao crie codigo novo sem registra-lo na ontologia.
    END GUIDELINES
END FIELD
```

## Uso com IA

Ferramentas de anotação assistida leem `GUIDELINES` como parte do prompt.
Instrução vaga aqui produz codificação vaga la.

## Ver também

`BLOCK_FIELD`, `MOD_DESCRIPTION`
