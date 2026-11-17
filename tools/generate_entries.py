# Copyright (c) 2026 Christian Maciel De Britto
# SPDX-License-Identifier: AGPL-3.0-only AND LicenseRef-Synesis-data-output-exception
"""Gerador de entries derivadas do compilador Synesis.

Materializa em Markdown o que o compilador ja sabe sobre si mesmo:
tipos de campo (matriz tipo x propriedade) e diagnosticos (codigos estaveis).

NUNCA edite os arquivos em entries/_generated/ a mao: rode este script.
Ver estudo: synesis-planning/synesis-help/estudo_synesis_help.md (secao 4).

Uso:
    python tools/generate_entries.py            # grava
    python tools/generate_entries.py --check    # falha se houver divergencia
"""

from __future__ import annotations

import argparse
import dataclasses
import inspect
import sys
import typing
from pathlib import Path

from synesis import __version__ as SYNESIS_VERSION
from synesis.ast import results as R
from synesis.language_info import Requirement, get_language_info

OUT = Path(__file__).resolve().parent.parent / "synesis_help" / "entries" / "_generated" / "pt"

# --------------------------------------------------------------------------
# Camada FIXA: rotulos de apresentacao.
#
# Catalogo por chave (requisito 4 da porta de i18n, secao 7.4 do estudo).
# Traduzir o gerador = traduzir este dicionario. Nunca escreva um rotulo
# solto no corpo das funcoes.
# --------------------------------------------------------------------------
L = {
    "pt": {
        "required": "Obrigatório",
        "allowed": "Permitido",
        "forbidden": "Proibido",
        "sec_desc": "Descrição",
        "sec_syntax": "Sintaxe",
        "sec_props": "Propriedades",
        "sec_example": "Exemplo",
        "sec_rules": "Regras",
        "sec_seealso": "Ver também",
        "syntax_legend": "`[ ]` opcional · `<>` valor a substituir",
        "sec_message": "Mensagem do compilador",
        "sec_context": "Onde aparece",
        "sec_value": "Valor na anotação",
        "prop_header": "| Propriedade | Situação | Erro se violada |",
        "no_props": "Nenhuma propriedade obrigatória. O campo funciona apenas com `SCOPE`.",
        "gen_warning": (
            "<!-- GERADO AUTOMATICAMENTE por tools/generate_entries.py. "
            "Não edite. Conteúdo autoral vai em entries/authored/. -->"
        ),
        "severity_error": "Erro",
        "severity_warning": "Aviso",
        "severity_info": "Informação",
    }
}

REQ_LABEL = {
    Requirement.REQUIRED: "required",
    Requirement.ALLOWED: "allowed",
    Requirement.FORBIDDEN: "forbidden",
}

# --------------------------------------------------------------------------
# Camada FIXA (autoral): a linha de indice de cada tipo.
#
# O compilador sabe as REGRAS de cada tipo, mas nao sabe PARA QUE ele serve —
# isso e decisao metodologica. Fica aqui, por chave, e nao nos arquivos
# gerados: assim o gerador continua sendo dono do arquivo inteiro.
# Ver estudo, secao 5.2 (divisao derivar/declarar).
# --------------------------------------------------------------------------
#: Ordem de apresentacao dos tipos: os de uso corrente primeiro, os
#: especializados depois. Alfabetico poria DATE antes de CODE, o que nao
#: ajuda quem esta escolhendo um tipo.
TYPE_ORDER = {
    "QUOTATION": 10, "CODE": 20, "MEMO": 30, "TEXT": 40, "CHAIN": 50,
    "TOPIC": 60, "ENUMERATED": 70, "ORDERED": 80, "SCALE": 90, "DATE": 95,
}

#: Como se ESCREVE o valor do campo na anotacao (.syn/.syno) — distinto de como
#: o tipo se DECLARA no template, que a matriz de propriedades ja cobre.
#:
#: O compilador sabe validar o valor, mas a distincao "o que se declara" x "o
#: que se grava" e decisao de linguagem, nao consequencia de uma sondagem: por
#: isso mora aqui, junto de TYPE_SUMMARY. Preenchido so para os tipos em que a
#: diferenca nao e obvia e ja causou erro real em campo.
TYPE_VALUE_FORM = {
    "pt": {
        "ORDERED": (
            "O valor gravado é o **índice**, não o rótulo:\n"
            "\n"
            "```synesis\n"
            "aspect: 11\n"
            "```\n"
            "\n"
            "O rótulo (`Econômico`) pertence à declaração do template e é "
            "exibido pelo editor ao lado do índice — não se repete na anotação, "
            "porque admite variantes de grafia (`Economico`, `ECONOMICO`) que "
            "fragmentariam o corpus. Escrever o rótulo é `SYNESIS_E088`."
        ),
        "ENUMERATED": (
            "O valor gravado é o **rótulo** declarado em `VALUES`:\n"
            "\n"
            "```synesis\n"
            "zone: Method\n"
            "```\n"
            "\n"
            "Diferente de `ORDERED`, aqui não há índice: `ENUMERATED` não tem "
            "ordem, então o prefixo `[N]` no bloco `VALUES` é recusado com "
            "`SYNESIS_E087`."
        ),
    }
}

#: Diagnosticos que governam o VALOR de um tipo (nao suas propriedades de
#: declaracao). A matriz tipo x propriedade nao os alcanca, porque eles nao
#: nascem de uma propriedade do template — mas quem le sobre o tipo precisa
#: chegar neles.
TYPE_VALUE_CODES = {
    "ORDERED": ["SYNESIS_E088"],
    "ENUMERATED": ["SYNESIS_E087"],
}

TYPE_SUMMARY = {
    "pt": {
        "QUOTATION": "Trecho literal transcrito da fonte.",
        "MEMO": "Nota livre do pesquisador, sem estrutura fixa.",
        "CODE": "Um ou mais conceitos da ontologia atribuídos à unidade.",
        "CHAIN": "Cadeia de conceitos ligados por relações.",
        "TEXT": "Texto curto de uma linha.",
        "DATE": "Data.",
        "SCALE": "Valor numérico dentro de um intervalo declarado.",
        "ENUMERATED": "Valor escolhido de uma lista fechada, sem ordem.",
        "ORDERED": "Valor escolhido de uma lista fechada, com ordem.",
        "TOPIC": "Termo único, sem espaços, para agrupar unidades.",
    }
}

# Sintaxe minima por propriedade, para montar o exemplo de cada tipo.
#: Forma sintatica de cada propriedade, para a secao Sintaxe.
#: Blocos multilinha aparecem condensados — a estrutura interna fica no
#: exemplo, logo abaixo.
PROP_FORM = {
    "ARITY": "ARITY <operador> <n>",
    "FORMAT": "FORMAT [<min>..<max>]",
    "DESCRIPTION": "DESCRIPTION <texto>",
    "GUIDELINES": "GUIDELINES ... END GUIDELINES",
    "RELATIONS": "RELATIONS ... END RELATIONS",
    "VALUES": "VALUES ... END VALUES",
    "CONTEXT FROM DATASET": "CONTEXT FROM DATASET <campo>",
    "IDENTIFIES": "IDENTIFIES <entidade>",
    "REFERS TO": "REFERS TO <entidade>",
}

#: Linhas ja prontas para o corpo do FIELD, indentadas com 4 espacos.
#: Blocos multilinha fecham na mesma coluna em que abriram.
PROP_SYNTAX = {
    "ARITY": ["    ARITY >= 2"],
    "FORMAT": ["    FORMAT [0..5]"],
    "DESCRIPTION": ["    DESCRIPTION o que este campo registra"],
    "RELATIONS": [
        "    RELATIONS",
        "        CAUSA: quando um fator produz outro",
        "        REDUZ: quando um fator atenua outro",
        "    END RELATIONS",
    ],
    # Forma valida em ENUMERATED, que nao aceita o prefixo `[N]` (SYNESIS_E087).
    # ORDERED, que o exige, usa a variante em PROP_SYNTAX_BY_TYPE.
    "VALUES": [
        "    VALUES",
        "        baixo: intensidade baixa",
        "        alto: intensidade alta",
        "    END VALUES",
    ],
}

#: Trechos cuja forma depende do TIPO. `VALUES` e o unico caso: o prefixo `[N]`
#: estabelece ordem, sendo obrigatorio em ORDERED (SYNESIS_E049 sem ele) e
#: recusado em ENUMERATED (SYNESIS_E087). Um exemplo unico ensinaria uma
#: construcao invalida para um dos dois tipos.
PROP_SYNTAX_BY_TYPE = {
    "ORDERED": {
        "VALUES": [
            "    VALUES",
            "        [1] baixo: intensidade baixa",
            "        [2] alto: intensidade alta",
            "    END VALUES",
        ],
    },
}


def esc(text: str) -> str:
    """Neutraliza pipes para nao quebrar tabelas Markdown."""
    return text.replace("|", "\\|")


def frontmatter(**kw) -> str:
    lines = ["---"]
    for k, v in kw.items():
        if isinstance(v, list):
            lines.append(f"{k}: [{', '.join(v)}]")
        elif isinstance(v, str) and len(v) >= 2 and v[0] == v[-1] == '"':
            lines.append(f"{k}: {v}")  # ja vem entre aspas (summary, title)
        elif isinstance(v, str) and (":" in v or v.startswith(("<", ">", "["))):
            q = v.replace('"', '\\"')
            lines.append(f'{k}: "{q}"')
        else:
            lines.append(f"{k}: {v}")
    lines.append("---")
    return "\n".join(lines)


# --------------------------------------------------------------------------
# Gerador (a): tipos de campo
# --------------------------------------------------------------------------

def gen_field_types(lang: str = "pt") -> dict[str, str]:
    t = L[lang]
    out: dict[str, str] = {}
    info = get_language_info()

    for ft in info.field_types:
        eid = f"TYPE_{ft.name}"
        req = [p.name for p in ft.required]

        # Sintaxe: obrigatorias no corpo. Concreto e compilavel de proposito —
        # e verificado por tools/check_examples.py (secao 5.4 do estudo).
        body = [f"FIELD exemplo_{ft.name.lower()} TYPE {ft.name}", "    SCOPE ITEM"]
        by_type = PROP_SYNTAX_BY_TYPE.get(ft.name, {})
        for name in req:
            snippet = by_type.get(name) or PROP_SYNTAX.get(name, [f"    {name}"])
            body.extend(snippet)
        body.append("END FIELD")
        # Forma completa, no padrao de guia de referencia: obrigatorias sem
        # colchetes, permitidas entre colchetes. Nada de "..." no lugar da
        # estrutura — o leitor precisa ver o que pode escrever.
        allowed = [p.name for p in ft.allowed]
        syntax_lines = [f"FIELD <nome> TYPE {ft.name}", "    SCOPE <escopo>"]
        for name in req:
            syntax_lines.append(f"    {PROP_FORM.get(name, name)}")
        for name in allowed:
            syntax_lines.append(f"    [{PROP_FORM.get(name, name)}]")
        syntax_lines.append("END FIELD")
        syntax_block = "\n".join(syntax_lines)
        # Versao de uma linha, para o frontmatter e o indice.
        syntax_inline = (
            f"FIELD <nome> TYPE {ft.name} SCOPE <escopo>"
            + ("".join(f" {PROP_FORM.get(n, n)}" for n in req))
            + (" [...]" if allowed else "")
            + " END FIELD"
        )

        rows = [t["prop_header"], "|---|---|---|"]
        for p in sorted(ft.properties, key=lambda x: (x.requirement.value, x.name)):
            code = p.error_code or "-"
            rows.append(f"| `{p.name}` | {t[REQ_LABEL[p.requirement]]} | {code} |")

        # see_also: irmaos + codigos citados (propriedades + valor)
        codes = sorted(
            {p.error_code for p in ft.properties if p.error_code}
            | set(TYPE_VALUE_CODES.get(ft.name, []))
        )
        siblings = [f"TYPE_{o.name}" for o in info.field_types if o.name != ft.name][:3]
        see = codes + siblings

        # Explicacoes do compilador (prosa canonica, ja em pt).
        expl = [p for p in ft.properties if p.explanation and p.requirement is Requirement.REQUIRED]

        parts = [
            frontmatter(
                id=eid,
                title=f'"{ft.name}"',
                category="field_type",
                summary=f'"{TYPE_SUMMARY[lang].get(ft.name, f"Tipo de campo {ft.name}.")}"',
                syntax=syntax_inline,
                see_also=see,
                source="generated",
                order=TYPE_ORDER.get(ft.name, 100),
                requires_synesis=f'">={SYNESIS_VERSION}"',
            ),
            "",
            t["gen_warning"],
            "",
            f"# {ft.name}",
            "",
            f"## {t['sec_syntax']}",
            "",
            "```synesis",
            syntax_block,
            "```",
            "",
            t["syntax_legend"],
            "",
            f"## {t['sec_example']}",
            "",
            "```synesis",
            "\n".join(body),
            "```",
        ]

        # Como se escreve o VALOR — antes das propriedades de declaracao: quem
        # consulta o tipo costuma estar anotando, nao escrevendo o template.
        value_form = TYPE_VALUE_FORM.get(lang, {}).get(ft.name)
        if value_form:
            parts += ["", f"## {t['sec_value']}", "", value_form]

        parts += [
            "",
            f"## {t['sec_props']}",
            "",
            "\n".join(rows),
        ]

        if req:
            parts += ["", f"## {t['sec_rules']}", ""]
            for p in expl:
                first = (p.explanation or "").strip().split("\n")[0]
                parts.append(f"- **`{p.name}` é obrigatório.** {first}")
        else:
            parts += ["", f"## {t['sec_rules']}", "", "- " + t["no_props"]]

        parts += [
            "",
            f"## {t['sec_seealso']}",
            "",
            ", ".join(f"`{s}`" for s in see),
            "",
        ]
        out[eid] = "\n".join(parts)
    return out


# --------------------------------------------------------------------------
# Gerador (b): diagnosticos
# --------------------------------------------------------------------------

SEVERITY_BY_PREFIX = {"E": "severity_error", "W": "severity_warning", "I": "severity_info"}

#: Diagnosticos cujo to_diagnostic() falhou. Relatado ao final da execucao:
#: e achado sobre o compilador, nao ruido do gerador.
UNRENDERABLE: list[tuple[str, str, str]] = []


def _sample(name: str, ann) -> object:
    """Valor plausivel para instanciar um erro e obter to_diagnostic()."""
    origin = typing.get_origin(ann)
    if origin in (dict, typing.Dict) or name == "counts":
        return {"exemplo_a": 2, "exemplo_b": 3}
    if origin in (set, frozenset):
        return {"exemplo_a"}
    if origin in (list, tuple, typing.List, typing.Tuple):
        return ["exemplo_a", "exemplo_b"]
    if ann in (int,) or name in {"arity", "n_relations"}:
        return 2
    if ann in (float,):
        return 1.5
    return {
        "bibref": "@autor2024",
        "field_name": "nome_do_campo",
        "block_type": "ITEM",
        "scope": "ITEM",
        "field_type": "TEXT",
        "filename": "arquivo.syn",
        "value": "valor",
        "code": "CODIGO_A",
    }.get(name, "exemplo")


def _instantiate(cls):
    """Instancia um ValidationError com dados de exemplo, se possivel."""
    hints = typing.get_type_hints(cls)
    kwargs = {}
    for f in dataclasses.fields(cls):
        if f.name in ("location", "severity"):
            continue
        if f.default is not dataclasses.MISSING or f.default_factory is not dataclasses.MISSING:  # type: ignore[misc]
            continue
        kwargs[f.name] = _sample(f.name, hints.get(f.name))
    try:
        return cls(location=None, **kwargs)
    except Exception:
        try:
            return cls(**kwargs)
        except Exception:
            return None


def gen_diagnostics(lang: str = "pt") -> dict[str, str]:
    t = L[lang]
    out: dict[str, str] = {}

    classes = [
        (o.CODE, n, o)
        for n, o in vars(R).items()
        if inspect.isclass(o)
        and dataclasses.is_dataclass(o)
        and isinstance(getattr(o, "CODE", None), str)
    ]
    # CODE nao e unico: E064 e compartilhado por 3 classes. Agrupa por CODE.
    by_code: dict[str, list] = {}
    for code, name, cls in classes:
        by_code.setdefault(code, []).append((name, cls))

    for code, members in sorted(by_code.items()):
        sev_key = SEVERITY_BY_PREFIX.get(code.split("_")[1][0], "severity_error")
        docs = [(n, (c.__doc__ or "").strip().split("\n")[0]) for n, c in members]
        summary = docs[0][1].rstrip(".") or code

        parts = [
            frontmatter(
                id=code,
                title=f'"{code}"',
                category="diagnostic",
                summary=f'"{summary}."',
                severity=t[sev_key],
                see_also=[],
                source="generated",
                requires_synesis=f'">={SYNESIS_VERSION}"',
            ),
            "",
            t["gen_warning"],
            "",
            f"# {code} — {t[sev_key]}",
            "",
            f"## {t['sec_desc']}",
            "",
        ]

        if len(members) == 1:
            parts.append(docs[0][1])
        else:
            parts.append(
                f"Este código cobre {len(members)} situações distintas:"
            )
            parts.append("")
            for n, d in docs:
                parts.append(f"- **{n}** — {d}")

        parts += ["", f"## {t['sec_message']}", ""]
        for n, cls in members:
            inst = _instantiate(cls)
            msg = None
            if inst is not None:
                try:
                    msg = inst.to_diagnostic()
                except Exception as exc:  # noqa: BLE001
                    # Falha ao renderizar e sinal de defeito no compilador,
                    # nao motivo para omitir a entry em silencio.
                    UNRENDERABLE.append((code, n, f"{type(exc).__name__}: {exc}"))
            if len(members) > 1:
                parts.append(f"**{n}**")
                parts.append("")
            if msg is None:
                parts += [
                    "> Mensagem não reproduzível neste guia; consulte o compilador.",
                    "",
                ]
            else:
                parts += ["```text", msg.strip(), "```", ""]

        parts += [f"## {t['sec_context']}", ""]
        for n, cls in members:
            fields = [
                f.name
                for f in dataclasses.fields(cls)
                if f.name not in ("location", "severity")
            ]
            detail = ", ".join(f"`{x}`" for x in fields) or "—"
            parts.append(f"- **{n}**: {detail}")
        parts.append("")

        out[code] = "\n".join(parts)
    return out


# --------------------------------------------------------------------------
# Gerador (c): escopos e linkage
# --------------------------------------------------------------------------

def gen_linkage(lang: str = "pt") -> dict[str, str]:
    t = L[lang]
    info = get_language_info()
    rows = ["| Escopo | `IDENTIFIES` | `REFERS TO` |", "|---|---|---|"]
    codes: set[str] = set()
    for scope in info.scopes:
        props = {p.name: p for p in info.linkage_by_scope.get(scope, [])}
        cells = []
        for mod in ("IDENTIFIES", "REFERS TO"):
            p = props.get(mod)
            if p is None:
                cells.append("—")
            else:
                lab = t[REQ_LABEL[p.requirement]]
                if p.error_code:
                    codes.add(p.error_code)
                    lab += f" ({p.error_code})"
                cells.append(lab)
        rows.append(f"| `{scope}` | {cells[0]} | {cells[1]} |")

    see = sorted(codes)
    body = [
        frontmatter(
            id="LINKAGE_SCOPES",
            title='"Escopos e ligacao entre projetos"',
            category="linkage",
            summary='"Onde IDENTIFIES e REFERS TO podem ser declarados."',
            syntax="FIELD <nome> TYPE <tipo> SCOPE SOURCE "
            "<IDENTIFIES|REFERS TO> <entidade> END FIELD",
            see_also=see,
            source="generated",
            requires_synesis=f'">={SYNESIS_VERSION}"',
        ),
        "",
        t["gen_warning"],
        "",
        "# Escopos e ligacao",
        "",
        f"## {t['sec_desc']}",
        "",
        "Os modificadores `IDENTIFIES` e `REFERS TO` ligam projetos independentes.",
        "Nem todo escopo os aceita.",
        "",
        f"## {t['sec_syntax']}",
        "",
        "```synesis",
        "FIELD <nome> TYPE <tipo>",
        "    SCOPE SOURCE",
        "    [IDENTIFIES <entidade>]",
        "    [REFERS TO <entidade>]",
        "END FIELD",
        "```",
        "",
        t["syntax_legend"],
        "",
        f"## {t['sec_rules']}",
        "",
        "\n".join(rows),
        "",
        f"## {t['sec_seealso']}",
        "",
        ", ".join(f"`{s}`" for s in see) or "—",
        "",
    ]
    return {"LINKAGE_SCOPES": "\n".join(body)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="falha se houver divergencia")
    args = ap.parse_args()

    entries: dict[str, str] = {}
    entries.update(gen_field_types())
    entries.update(gen_diagnostics())
    entries.update(gen_linkage())

    OUT.mkdir(parents=True, exist_ok=True)

    if args.check:
        drift = []
        for eid, content in entries.items():
            p = OUT / f"{eid}.md"
            if not p.exists() or p.read_text(encoding="utf-8") != content:
                drift.append(eid)
        # `ECO_*` sai de tools/generate_ecosystem.py, que grava no mesmo
        # diretorio. Sem esta excecao elas contam como orfas e o --check
        # NUNCA fica verde — um check sempre vermelho e um check ignorado,
        # e seria justamente o que esconderia uma orfa de verdade.
        existing = {
            p.stem for p in OUT.glob("*.md") if not p.stem.startswith("ECO_")
        }
        orphans = existing - set(entries)
        if drift or orphans:
            print(f"DIVERGENCIA: {len(drift)} desatualizadas, {len(orphans)} orfas")
            for d in sorted(drift)[:10]:
                print(f"  ~ {d}")
            for o in sorted(orphans)[:10]:
                print(f"  - {o}")
            return 1
        print(f"OK: {len(entries)} entries sincronizadas (synesis {SYNESIS_VERSION})")
        return 0

    for eid, content in entries.items():
        (OUT / f"{eid}.md").write_text(content, encoding="utf-8")
    print(f"Geradas {len(entries)} entries em {OUT} (synesis {SYNESIS_VERSION})")

    if UNRENDERABLE:
        print(f"\nAVISO: {len(UNRENDERABLE)} diagnóstico(s) não renderizaram.")
        print("Isto é achado sobre o compilador, não falha do guia:")
        for code, name, err in UNRENDERABLE:
            print(f"  {code} {name}: {err}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
