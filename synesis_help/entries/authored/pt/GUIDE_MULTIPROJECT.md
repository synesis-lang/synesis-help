---
id: GUIDE_MULTIPROJECT
title: "Projetos conectados"
category: overview
summary: "Como vários projetos independentes se ligam por entidades compartilhadas."
see_also: [MOD_IDENTIFIES, LINKAGE_SCOPES, BLOCK_SOURCE, GUIDE_PRIMITIVES, SYNESIS_W083, SYNESIS_I080]
source: authored
order: 50
---

# Projetos conectados

## O problema

Uma pesquisa raramente cabe num projeto so. Fontes heterogéneas — currículos,
perfis públicos, publicações, registros institucionais — tem estruturas
diferentes, campos diferentes e ritmos de coleta diferentes.

Juntar tudo num projeto único produz um template inchado, cheio de campos
opcionais que so valem para uma parte dos dados. Mante-los separados, sem
ligação, impede qualquer analise cruzada.

## A solução: entidades compartilhadas

Cada projeto permanece independente — template próprio, compilação própria.
O que os une são **entidades**: um projeto declara `IDENTIFIES` de uma
entidade, os outros apontam para ela com `REFERS TO`.

O modelo e o do linker de C: cada unidade compila sozinha; as referencias
externas so são resolvidas quando você compila o conjunto.

## Topologia de exemplo

Um agregado com três entidades e seis projetos:

| Projeto | Entidade que possui | Entidades que referencia |
|---|---|---|
| `perfis` | `profile` | `researcher`, `company` |
| `curriculos` | `researcher` | — |
| `empresas` | `company` | — |
| `publicacoes` | — | `researcher` |
| `posts` | — | `profile` |
| `repositorios` | — | `profile` |

Três donos, três referenciadores. Cada entidade tem **um** dono
(`SYNESIS_E081`).

## Duas decisões de projeto

**1. Quem possui cada entidade.** O dono deve ser o projeto com maior
cobertura da chave. Se o identificador esta em 100% dos perfis e em 62% dos
currículos, o projeto de perfis e o dono natural.

**2. Por onde a ligação passa.** No exemplo, `posts` e `repositorios`
referenciam `profile`, não `researcher` — mesmo que o interesse final seja o
pesquisador. A razão e semântica: um post e evidencia do **perfil publico**,
não do currículo académico. A cadeia perfil → currículo e responsabilidade de
quem detém as duas chaves.

Ligação direta funcionaria tecnicamente e mentiria sobre a proveniência.

## Compilação

```bash
synesis compile perfis/                 # isolado: I080 nas referencias externas
synesis compile perfis/ curriculos/     # link step: resolve as referencias
```

Compilado sozinho, um projeto com `REFERS TO` reporta `SYNESIS_I080` —
informação, não erro. Referencias externas não são resolvíveis isoladamente,
e isso e esperado.

## Órfãos

No link step, um `REFERS TO` sem correspondente vira `SYNESIS_W083` — aviso.

Em corpus reais, ausência e normal: nem todo profissional tem currículo, nem
toda empresa citada consta na lista de referencia. Trate o aviso como
inventario de cobertura, não como fila de defeitos.

## Ver também

`MOD_IDENTIFIES`, `LINKAGE_SCOPES`, `SYNESIS_W083`, `SYNESIS_E081`
