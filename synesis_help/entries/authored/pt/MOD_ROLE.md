---
id: MOD_ROLE
title: "ROLE"
category: modifier
summary: "Declara a função de um campo de ONTOLOGY no princípio organizador: rótulo, nota, hierarquia ou consolidação."
syntax: "ROLE <LABEL|NOTE|HIERARCHY> <espécie> | ROLE USE"
see_also: [BLOCK_ONTOLOGY, BLOCK_FIELD, BLOCK_EXPORT, BLOCK_PHASE, SYNESIS_E104, SYNESIS_E107, SYNESIS_E110, SYNESIS_E118, SYNESIS_E145, SYNESIS_E148]
source: authored
order: 90
requires_synesis: ">=0.15.0"
---

# ROLE

## Descrição

O **tipo** de um campo diz a forma do valor (`TEXT`, `CODE`...). A linha
`ROLE` diz a **função** desse campo no princípio organizador do projeto —
o que ele é para o conceito: um nome, uma definição, a posição numa
hierarquia.

Com a função declarada, o compilador valida a estrutura (rótulos que não se
repetem, hierarquias sem ciclo) e cada ferramenta lê o campo pelo papel, não
pelo nome: a exportação SKOS, as fases do `synesis-coder`, o grafo e o LSP.
O nome do campo continua livre (`definicao`, `definition`, `tipo_de`...).

## Sintaxe

```synesis
FIELD <nome> TYPE <tipo>
    SCOPE ONTOLOGY
    ROLE <FAMÍLIA> [<ESPÉCIE>]
END FIELD
```

`[ ]` opcional · `<>` valor a substituir

## Catálogo

| Papel | Tipo | Significado | SKOS |
|---|---|---|---|
| `LABEL PREFERRED` | TEXT | rótulo de exibição (um por conceito) | `prefLabel` |
| `LABEL ALTERNATIVE` | TEXT | sinônimos e variantes | `altLabel` |
| `LABEL HIDDEN` | TEXT | grafias antigas ou erradas, só para busca | `hiddenLabel` |
| `NOTE DEFINITION` | TEXT | a definição do conceito | `definition` |
| `NOTE USAGE` | TEXT | quando aplicar o código | `scopeNote` |
| `NOTE EXAMPLE` | TEXT | caso típico | `example` |
| `NOTE COUNTEREXAMPLE` | TEXT | caso parecido ao qual não se aplica | — |
| `HIERARCHY KIND` | CODE | é um tipo de (genérica) | `broader` |
| `HIERARCHY PART` | CODE | é parte de (partitiva) | `broader` |
| `HIERARCHY INSTANCE` | CODE | é um caso de (instancial) | `broader` |
| `USE` | CODE | este nome é preterido; vale o conceito indicado | rótulo do alvo |

## Exemplo

```synesis
FIELD definicao TYPE TEXT
    SCOPE ONTOLOGY
    ROLE NOTE DEFINITION
END FIELD

FIELD usado_por TYPE TEXT
    SCOPE ONTOLOGY
    ROLE LABEL ALTERNATIVE
END FIELD

FIELD tipo_de TYPE CODE
    SCOPE ONTOLOGY
    ROLE HIERARCHY KIND
END FIELD
```

```synesis
ONTOLOGY smishing
    definicao: Phishing conduzido por mensagens SMS.
    usado_por: phishing por SMS, SMS phishing
    tipo_de: phishing
END ONTOLOGY
```

## USE: consolidar dois nomes

Quando dois blocos nomeiam o mesmo conceito, o preterido fica só com o campo
`USE`, apontando o conceito que vale:

```synesis
ONTOLOGY voice_phishing
    usar: vishing
END ONTOLOGY
```

As anotações (`.syn`) não mudam. As contagens, a hierarquia, o grafo e o SKOS
passam a somar o preterido ao alvo, e o nome preterido vira rótulo do alvo.
`synesis-coder consolidate` faz essa edição com manifesto e é reversível
(`--revert`).

## Regras

- Só em campos com `SCOPE ONTOLOGY` (`SYNESIS_E108`); papel fora do catálogo
  é erro (`SYNESIS_E104`); `LABEL`, `NOTE` e `HIERARCHY` exigem espécie
  (`SYNESIS_E106`).
- O tipo precisa casar com o papel: `LABEL`/`NOTE` em TEXT, `HIERARCHY`/`USE`
  em CODE (`SYNESIS_E107`).
- No máximo um campo `NOTE DEFINITION`, um `LABEL PREFERRED` e um `USE` por
  template (`SYNESIS_E110`).
- Um termo de rótulo pertence a um só conceito (`SYNESIS_E115`,
  `SYNESIS_E116`).
- Hierarquia aponta sempre para o conceito mais amplo, aceita vários pais e
  não pode ter ciclo (`SYNESIS_E117`, `SYNESIS_E118`).
- `USE` aponta para um conceito que vale, nunca para si nem para outro
  preterido, e o bloco preterido não tem outros campos (`SYNESIS_E145` a
  `SYNESIS_E149`).

## Ver também

`BLOCK_ONTOLOGY`, `BLOCK_EXPORT`, `BLOCK_PHASE`, `BLOCK_FIELD`
