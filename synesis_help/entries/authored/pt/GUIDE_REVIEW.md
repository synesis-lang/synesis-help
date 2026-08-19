---
id: GUIDE_REVIEW
title: "Revisar anotação de IA"
category: overview
summary: "O pipeline ACT: propor, canonizar e aceitar correções sem perder dados."
see_also: [ECO_CODER, GUIDE_ECOSYSTEM, MOD_GUIDELINES, GUIDE_FILES, TYPE_CHAIN]
source: authored
order: 70
---

# Revisar anotação de IA

## O problema

Anotação gerada por LLM não é dado pronto. O modelo produz blocos
sintaticamente válidos — o compilador os aceita — e ainda assim afirma
coisas que a fonte não sustenta. Compilar sem erro diz que a **forma** está
certa, não que a **leitura** está.

O pipeline de revisão existe para separar duas coisas que a extração
mistura: **propor** uma correção e **aceitar** uma correção. Quem aceita é
o pesquisador.

## As três fases

| Fase | Comando | Lê | Escreve | LLM |
|---|---|---|---|---|
| 1 | `critique` | `.syn` | `.synr` | sim |
| 2 | `normalize` | `.synr` | `.synr` | sim |
| 3 | `incorporate` | `.synr` | `.syn` | **não** |

Nenhuma fase altera o `.syn` original. A revisão vive num arquivo próprio,
o `.synr`, e só vira anotação no passo final — que é determinístico.

```text
annotations/corpus.syn
        │  critique
        ▼
revisions/corpus.synr        ← propostas, em blocos # REVISION
        │  normalize
        ▼
revisions/corpus.synr        ← códigos canonizados no corpus
        │  incorporate
        ▼
annotations/corpus_final.syn ← aceito, sem LLM
```

## 1. `critique` — propor

Relê cada `ITEM` contra o trecho da fonte que ele anota e emite blocos
`# REVISION` com o que julga defeituoso.

```text
synesis-coder critique --project projeto.synp annotations/corpus.syn
```

O que regula o volume é `--sensitivity`:

| Valor | Quando usar |
|---|---|
| `lenient` | corpus exploratório; só o que é claramente errado |
| `standard` | padrão |
| `strict` | corpus final, revisão manual completa |

Um número de `0.0` a `1.0` também é aceito. Sensibilidade **alta gera mais
falso positivo**, não mais verdade: o modelo passa a marcar leituras que o
template admite.

## 2. `normalize` — canonizar

O `critique` olha um `ITEM` por vez e não sabe que `Aceitação_Social`,
`aceitacao_social` e `Social_Acceptance` são o mesmo conceito. O
`normalize` olha o corpus inteiro e unifica.

```text
synesis-coder normalize --project projeto.synp \
    --output-dir revisions/ revisions/*.synr
```

`--confidence` (padrão `0.65`) é o piso para aceitar uma unificação.

## 3. `incorporate` — aceitar

Aplica o `.synr` e grava o `.syn` final. **Não chama LLM** — é a fase que
você pode repetir, auditar e versionar.

```text
synesis-coder incorporate --backup revisions/corpus.synr
```

Correção ambígua é **rejeitada, não adivinhada**. Quando várias cadeias
compartilham o nó-fonte, uma correção que não identifica seu alvo de forma
única seria aplicada à primeira ocorrência — apagando um valor que ela não
endereçava. O comando prefere não aplicar e dizer que não aplicou.

Use `--backup` sempre que o destino já existir.

## `anchor` — a verificação que não custa nada

Antes de gastar token com `critique`, rode o `anchor`. Ele confere, sem
LLM, se o trecho anotado **existe de fato** na fonte:

```text
synesis-coder anchor annotations/corpus.syn --project projeto.synp
```

É determinístico, gratuito e pega a classe de defeito mais grave — trecho
que o modelo reescreveu em vez de citar. Complementa o compilador, que já
valida enums, faixas, campos obrigatórios, `BUNDLE` e relações de cadeia,
mas não verifica se o trecho citado ocorre no texto de origem.

Em integração contínua, `--strict` faz o comando sair com código 1.

## `refine` — opcional

`refine` re-extrai os `ITEM` marcados, usando a crítica como contexto. É
opt-in e consome LLM. Diferente do `incorporate`, ele **reescreve** em vez
de aplicar correções pontuais — use quando o problema for a leitura
inteira do item, não um campo.

## Ordem recomendada

```text
1. anchor       # grátis, offline — corrija o que ele apontar antes de seguir
2. critique     # --sensitivity standard
3. (leia o .synr)
4. normalize    # só faz sentido com o corpus inteiro
5. incorporate  # --backup
6. synesis compile
```

O passo 3 não é decorativo. O `.synr` é texto legível, feito para ser lido:
é onde você decide o que entra no seu dado.

## Ver também

`ECO_CODER`, `GUIDE_ECOSYSTEM`, `MOD_GUIDELINES`, `GUIDE_FILES`
