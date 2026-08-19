---
id: MOD_IDENTIFIES
title: "IDENTIFIES / REFERS TO"
category: modifier
summary: "Liga projetos independentes: chave primaria e chave estrangeira."
syntax: "IDENTIFIES <entidade> | REFERS TO <entidade>"
see_also: [LINKAGE_SCOPES, GUIDE_MULTIPROJECT, BLOCK_SOURCE, SYNESIS_E077, SYNESIS_E078, SYNESIS_E081, SYNESIS_W083]
source: authored
order: 80
---

# IDENTIFIES / REFERS TO

## Descrição

O par que permite **ligar projetos independentes** sem fundi-los.

Um projeto declara `IDENTIFIES` num campo: aquele campo passa a ser a chave
que identifica uma entidade — o projeto e o **dono** dela. Outro projeto
declara `REFERS TO` no mesmo rotulo: passa a apontar para ela.

Cada projeto continua compilando sozinho. A ligação so e resolvida quando
você compila os dois juntos (o *link step*).

## Sintaxe

```synesis
FIELD <nome> TYPE <tipo>
    SCOPE SOURCE
    <IDENTIFIES|REFERS TO> <entidade>
END FIELD
```

`<>` valor a substituir · `|` alternativa

## Exemplo

```synesis
# projeto A — dono da entidade
FIELD matricula TYPE TEXT
    SCOPE SOURCE
    IDENTIFIES pesquisador
END FIELD

# projeto B — aponta para ela
FIELD matricula_autor TYPE TEXT
    SCOPE SOURCE
    REFERS TO pesquisador
END FIELD
```

## Quem deve ser o dono

Escolha como dono o projeto com **maior cobertura** da chave.

Se um identificador aparece em 100% dos registros de um projeto e em 60% de
outro, o primeiro e o dono natural. A regra evita o efeito colateral inverso:
eleger como dono a fonte incompleta transforma ausência normal em ruído
constante.

## Órfãos são normais

Um `REFERS TO` cujo valor não casa com nenhum `IDENTIFIES` gera **aviso**
(`SYNESIS_W083`), não erro. E deliberado: em corpus reais, nem toda ocorrência
tem correspondente — nem todo perfil profissional tem currículo académico, nem
toda empresa citada consta na lista de referencia.

Omita o campo quando o valor não existir. Nunca infira a chave por homonimia
de nome.

## Regras

- So valem em `SCOPE SOURCE` (`SYNESIS_E078`).
- Valores de `IDENTIFIES` são únicos entre os `SOURCE` (`SYNESIS_E077`).
- Dois projetos não podem declarar `IDENTIFIES` do mesmo rotulo
  (`SYNESIS_E081`) — uma entidade tem um dono so.
- Tipos devem coincidir entre os lados (`SYNESIS_E082`).
- Compilado isoladamente, o lado `REFERS TO` reporta informação
  (`SYNESIS_I080`), não erro — a referencia externa so e resolvida no link
  step.

## Ver também

`GUIDE_MULTIPROJECT`, `LINKAGE_SCOPES`, `BLOCK_SOURCE`, `SYNESIS_W083`
