---
id: GUIDE_CHAINS
title: "Cadeias na pratica"
category: overview
summary: "Como desenhar RELATIONS e ARITY para cadeias que dizem algo."
see_also: [TYPE_CHAIN, BLOCK_ONTOLOGY, MOD_GUIDELINES, SYNESIS_E007, SYNESIS_E010, SYNESIS_E048]
source: authored
order: 40
---

# Cadeias na pratica

## O que uma cadeia registra

`CHAIN` liga conceitos por relações nomeadas:

```
Timidez -> CAUSA -> Medo_De_Falar -> RESTRINGE -> Fala_Em_Publico
```

A leitura e direta: a timidez causa medo de falar, que restringe a fala em
publico. O que era prosa vira estrutura verificável.

## Desenhar as RELATIONS

O conjunto de relações e uma decisão teórica, não de vocabulário. Poucas e
bem distintas valem mais que muitas e sobrepostas.

```synesis
FIELD chain TYPE CHAIN
    SCOPE ITEM
    ARITY >= 3
    RELATIONS
        CAUSA: um fator produz diretamente outro
        HABILITA: um fator cria condicoes para outro se desenvolver
        AMPLIFICA: um fator reforca outro ja presente
        RESTRINGE: um fator limita ou reduz outro
    END RELATIONS
END FIELD
```

Note a diferença entre `CAUSA`, `HABILITA` e `AMPLIFICA`: produção direta,
criação de condição, e intensificação do que ja existe. Se duas relações não
podem ser distinguidas numa frase, são a mesma relação.

## ARITY define a forma do argumento

`ARITY` não e so um mínimo técnico — expressa o desenho analítico.

`ARITY >= 3` exige três conceitos, isto e, uma cadeia com **mediador**:
antecedente → mediador → resultado. Isso forca o anotador a explicitar *por
onde* a causa passa, em vez de registrar pares soltos.

Se o template declara `RELATIONS`, o numero de relações precisa ser
compatível com a aridade (`SYNESIS_E048`).

## Combinar com a ontologia

Cadeias ficam mais fortes quando os conceitos declaram seu papel:

```synesis
ONTOLOGY Timidez
    papel: antecedente
END ONTOLOGY

ONTOLOGY Medo_De_Falar
    papel: mediador
END ONTOLOGY
```

Com `papel` declarado, um leitor sabe se a cadeia respeita o desenho teórico
sem reconstruir a analise inteira.

## Erros frequentes

| Situação | Código |
|---|---|
| menos conceitos que a aridade exige | `SYNESIS_E007` |
| relação não declarada no template | `SYNESIS_E010` |
| falta o operador `->` | `SYNESIS_E013` |
| conceito com espaços | `SYNESIS_E015` |
| conceito com nome igual ao de uma relação | `SYNESIS_E014` |

## Ver também

`TYPE_CHAIN`, `BLOCK_ONTOLOGY`, `SYNESIS_E007`, `SYNESIS_E048`
