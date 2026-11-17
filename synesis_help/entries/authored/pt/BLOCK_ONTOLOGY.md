---
id: BLOCK_ONTOLOGY
title: "ONTOLOGY"
category: block
summary: "Princípio organizador: o sistema conceitual que organiza as ocorrências."
syntax: "ONTOLOGY <conceito> <campo>: <valor> [...] END ONTOLOGY"
file: ".syno"
see_also: [BLOCK_ITEM, GUIDE_PRIMITIVES, MOD_ROLE, BLOCK_EXPORT, TYPE_CODE, SYNESIS_E004, SYNESIS_E068, SYNESIS_W071]
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

## Princípios organizadores

Os blocos `ONTOLOGY` são os **princípios organizadores** do projeto. Não são
uma ontologia formal no sentido da lógica descritiva: são as entradas do
**modelo organizador** — o que o compilador chama de *model entries*.

O nível de organização é decisão da pesquisa, não do formato. O mesmo
mecanismo serve a vários graus:

- **Lista plana** — só nomes e definições: um vocabulário controlado que
  impede a deriva silenciosa da codificação. Sem ele, `REDE_APOIO`,
  `rede_apoio` e `RedeDeApoio` viram três conceitos para a mesma ideia.
- **Tesauro** — com rótulos alternativos e preteridos (`ROLE LABEL`, `USE`).
- **Taxonomia** — com hierarquia declarada (`ROLE HIERARCHY`).
- **Taxonomia multirrelacional** — hierarquia com mais de uma espécie (tipo,
  parte, caso) e relações associativas, exportável em SKOS (`EXPORT SKOS`).
  Nenhum grau se chama "ontologia": SKOS é um sistema de organização do
  conhecimento, não uma ontologia formal em OWL.

O compilador informa o perfil de cada projeto ao final da compilação
(`Organizing model: Terminological: ... | Conceptual: ...`).

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

**Hierarquia e rótulos.** Com a linha `ROLE` no template, um campo comum
ganha função no princípio organizador, e o compilador a valida:

```synesis
ONTOLOGY smishing
    definicao: Phishing conduzido por mensagens SMS.
    usado_por: phishing por SMS
    tipo_de: phishing
END ONTOLOGY
```

Aqui `tipo_de` (`ROLE HIERARCHY KIND`) põe o conceito sob `phishing` — o
compilador recusa ciclos e pais sem bloco — e `usado_por`
(`ROLE LABEL ALTERNATIVE`) registra um sinônimo. Ver `MOD_ROLE`.

Nada disso e sintaxe especial: são campos comuns declarados com
`SCOPE ONTOLOGY` no template.

## Ver também

`GUIDE_PRIMITIVES`, `BLOCK_ITEM`, `MOD_ROLE`, `BLOCK_EXPORT`, `TYPE_CODE`, `TYPE_CHAIN`, `SYNESIS_E004`
