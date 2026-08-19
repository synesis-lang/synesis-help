---
id: BLOCK_ONTOLOGY
title: "ONTOLOGY"
category: block
summary: "Unidade de conceituacao: o sistema conceitual que organiza as ocorrências."
syntax: "ONTOLOGY <conceito> <campo>: <valor> [...] END ONTOLOGY"
file: ".syno"
see_also: [BLOCK_ITEM, GUIDE_PRIMITIVES, TYPE_CODE, SYNESIS_E004, SYNESIS_E068, SYNESIS_W071]
source: authored
order: 70
---

# ONTOLOGY

## Descrição

`ONTOLOGY` e a **unidade de conceituacao**. Responde:

> Segundo qual sistema conceitual os itens serão compreendidos?

Não presuma que seja um tema. Conforme a metodologia, um bloco `ONTOLOGY` pode
definir um código, uma categoria, um conceito, um construto, um mecanismo
causal, um valor normativo, uma classe argumentativa, um frame, um tipo de
evento ou uma entidade de knowledge graph.

Funcionalmente, e o **vocabulário controlado** da pesquisa — o que impede a
deriva silenciosa da codificação. Sem ele, `REDE_APOIO`, `rede_apoio` e
`RedeDeApoio` viram três conceitos distintos para a mesma ideia, e ninguém
percebe ate a analise final.

## Sintaxe

```synesis
ONTOLOGY <conceito>
    <campo>: <valor>
    [<campo>: <valor>]
END ONTOLOGY
```

`[ ]` opcional · `<>` valor a substituir

O nome do conceito não aceita espaços. Quais campos são aceitos vem de
`ONTOLOGY FIELDS` no template.

## Regras

- Nome de conceito não aceita espaços (`SYNESIS_E015`) nem caracteres
  especiais (`SYNESIS_E033`).
- Dois blocos não podem definir o mesmo conceito (`SYNESIS_E068`).
- Descrições idênticas em conceitos distintos geram aviso (`SYNESIS_W071`) —
  em geral indica duplicação conceitual.
- Código usado num `ITEM` sem definição aqui e erro (`SYNESIS_E004`).
- Se ha ontologia, o template precisa declarar `ONTOLOGY FIELDS`
  (`SYNESIS_E005`).

## Exemplo mínimo

```synesis
ONTOLOGY REDE_APOIO
    definition: lacos informais mobilizados em situacao de risco
END ONTOLOGY
```

## Ontologias estruturadas

Um conceito raramente e so um nome e uma definição. O template pode dar a
`ONTOLOGY` campos que expressam a **arquitetura** do seu sistema conceitual —
e o compilador passa a valida-la.

**Papel causal.** Em desenhos que analisam mecanismos, cada conceito ocupa uma
posição na cadeia:

```synesis
ONTOLOGY Medo_De_Falar
    descricao: receio de avaliacao negativa em situacoes de fala publica
    papel: mediador
    grupo: Barreiras_Iniciais
END ONTOLOGY
```

Com `papel` como `ENUMERATED` (antecedente, mediador, resultado), o template
impede que uma cadeia comece por um resultado.

**Hierarquia.** Conceitos podem declarar seu lugar numa taxonomia:

```synesis
ONTOLOGY integridade_da_informacao
    definicao: autenticidade e manipulacao do artefato
    tipo_conceito: estrutural
    papel_hierarquico: dimensao
    conceito_pai: desinformacao
    pergunta: o artefato e autentico?
END ONTOLOGY
```

Aqui `conceito_pai` liga o conceito ao agregador, e `pergunta_operacional`
registra o critério que o anotador aplica — a definição vira instrumento, não
so glossário.

Nada disso e sintaxe especial: são campos comuns declarados com
`SCOPE ONTOLOGY` no template.

## Ver também

`GUIDE_PRIMITIVES`, `BLOCK_ITEM`, `TYPE_CODE`, `TYPE_CHAIN`, `SYNESIS_E004`
