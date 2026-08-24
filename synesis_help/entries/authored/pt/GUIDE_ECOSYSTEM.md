---
id: GUIDE_ECOSYSTEM
title: "O ecossistema"
category: overview
summary: "As ferramentas ao redor da linguagem e quando usar cada uma."
see_also: [ECO_SYNESIS, ECO_LSP, ECO_CODER, ECO_GRAPH, GUIDE_START, GUIDE_REVIEW]
source: authored
order: 60
---

# O ecossistema

## Descrição

A linguagem é uma só; as ferramentas são várias. Todas dependem do
compilador, e **nenhuma reimplementa suas regras** — é o que impede que
duas ferramentas discordem sobre o que é um projeto válido.

| Ferramenta | Papel | Quando usar |
|---|---|---|
| `synesis` | compilador | sempre — valida e compila |
| `synesis-lsp` | language server | ao escrever no editor |
| `synesis-coder` | anotação assistida | ao anotar corpus grande |
| `synesis-graph` | exportação | ao analisar em grafo |
| `synesis-help` | este guia | ao consultar a linguagem |

## O fluxo de trabalho

1. **Escrever.** O editor mostra erro enquanto você digita — é o
   `synesis-lsp` trabalhando, iniciado pela extensão do VS Code.
2. **Anotar.** Em corpus grande, o `synesis-coder` gera blocos a partir do
   texto, guiado pelo seu template.
3. **Revisar.** O que a máquina anotou não é dado pronto: o `synesis-coder`
   traz um pipeline de revisão (`critique` → `normalize` → `incorporate`)
   que separa *propor* de *aceitar*. Veja `GUIDE_REVIEW`.
4. **Compilar.** `synesis compile` valida o projeto inteiro e gera os
   artefatos (JSON, CSV, XLS).
5. **Analisar.** O `synesis-graph` converte o artefato compilado em grafo.

Os passos 2, 3 e 5 são opcionais. Os passos 1 e 4 são o mínimo — mas quem
usa o passo 2 deveria usar o 3: anotação de LLM incorporada sem revisão
entra no corpus com o mesmo peso da que você escreveu à mão.

## O que cada um consome

O `synesis-graph` lê o **artefato compilado**, não os `.syn` diretamente —
por isso `compile` vem antes. O `synesis-coder` lê o **template**, porque é
dele que saem os campos e as restrições que o modelo deve respeitar.

## O que o grafo leva junto

Ao exportar para um banco, o `synesis-graph` não grava só os dados: grava
também o **contexto do projeto**, num vértice `ProjectContext`. Vai ali a
`DESCRIPTION` do seu `.synp` e o template inteiro como documento legível —
campos, escalas de valores e as `GUIDELINES` que você escreveu.

A razão é que o schema de um banco é sintaxe sem semântica: ele diz que
existe um vértice `Aspect` com a propriedade `name`, mas não que aquilo é
uma escala ordenada nem o que cada valor significa. Sem isso, quem consulta
o grafo — uma IA por MCP, um colega que recebeu uma cópia — precisa
adivinhar o seu critério de codificação. Com isso, passa a lê-lo.

É por isso que escrever boas `GUIDELINES` rende duas vezes: elas guiam o
`synesis-coder` na anotação e viajam com o grafo depois. Veja `ECO_GRAPH`.

## Instalação

Cada módulo é um pacote próprio:

```text
pip install synesis          # compilador (obrigatório)
pip install synesis-lsp      # servidor para o editor
pip install synesis-coder    # anotação assistida
pip install synesis-graph    # exportação para grafos
```

A extensão do VS Code encontra o `synesis-lsp` sozinha, desde que ele esteja
instalado no mesmo ambiente.

## Ver também

`ECO_SYNESIS`, `ECO_LSP`, `ECO_CODER`, `ECO_GRAPH`, `GUIDE_REVIEW`
