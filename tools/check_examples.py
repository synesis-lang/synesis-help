# Copyright (c) 2026 Christian Maciel De Britto
# SPDX-License-Identifier: LicenseRef-Synesis-AGPL-3.0-with-Data-Output-Exception
"""Compile the examples of the entries against the installed compiler.

This is where authored content rots: a new compiler rule silently invalidates
an example written months before.

Three checks:
  - complete templates (starting with TEMPLATE) are compiled as they are;
  - `FIELD ... END FIELD` fragments are wrapped in a minimal template;
  - **projects**: code blocks whose first line names a file
    (`# template.synt`, `# annotations.syn`, `# records/s1.toml`, ...) are
    written to a temporary folder, a `references.bib` is generated for the
    bibrefs they cite, and every `.synp` among them is compiled. Case studies
    must compile without errors.

Fragments of .synp/.syn/.syno and schematic forms (with `<placeholder>`) are
counted as not verifiable: honesty is better than a false green.

Usage:
    python tools/check_examples.py
"""

from __future__ import annotations

import re
import sys
import tempfile
from pathlib import Path

from synesis.parser.template_loader import load_template_from_string, validate_template

ROOT = Path(__file__).resolve().parent.parent / "synesis_help" / "entries"
FENCE = re.compile(r"```synesis\n(.*?)```", re.DOTALL)
FILE_FENCE = re.compile(r"```(?:synesis|toml)\n# ([\w./-]+\.(?:synp|synt|syn|syno|toml|bib))\n(.*?)```", re.DOTALL)
BIBREF = re.compile(r"^\s*(?:SOURCE|ITEM)\s+@([\w.-]+)", re.MULTILINE)

#: Maximum width of an example line: blocks are read in a terminal panel.
MAX_WIDTH = 72
INDENT = 4


def check_style(src: str) -> list[str]:
    """Presentation problems, not syntax ones."""
    issues: list[str] = []
    for n, line in enumerate(src.split("\n"), 1):
        if not line.strip():
            continue
        if "\t" in line:
            issues.append(f"line {n}: TAB (use {INDENT} spaces)")
        if len(line) > MAX_WIDTH:
            issues.append(f"line {n}: {len(line)} columns (max {MAX_WIDTH})")
        if line.rstrip() != line:
            issues.append(f"line {n}: trailing space")
        indent = len(line) - len(line.lstrip())
        if indent % INDENT:
            issues.append(f"line {n}: indent {indent} is not a multiple of {INDENT}")
    return issues


def check_project(files: dict[str, str]) -> list[str]:
    """Write the files of one entry, generate the bibliography, compile each .synp."""
    from synesis.compiler import SynesisCompiler

    problems: list[str] = []
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        for rel, content in files.items():
            path = root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        projects = sorted(root.rglob("*.synp"))
        if not projects:
            return ["files named in the entry, but no .synp to compile"]
        for synp in projects:
            folder = synp.parent
            bib = folder / "references.bib"
            if "references.bib" in synp.read_text(encoding="utf-8") and not bib.exists():
                refs = sorted({m for syn in folder.rglob("*.syn")
                               for m in BIBREF.findall(syn.read_text(encoding="utf-8"))})
                bib.write_text("".join(
                    f"@misc{{{r},\n  title = {{Fictitious source {r}}},\n"
                    f"  author = {{Author, A.}},\n  year = {{2024}}\n}}\n\n" for r in refs),
                    encoding="utf-8")
            try:
                result = SynesisCompiler(synp).compile()
            except Exception as exc:  # noqa: BLE001
                problems.append(f"{synp.relative_to(root)}: {type(exc).__name__}: {exc}")
                continue
            errors = result.validation_result.errors
            if errors or result.linked_project is None:
                codes = ", ".join(sorted({getattr(e, "CODE", type(e).__name__) for e in errors}))
                first = errors[0].to_cli_line() if errors else "no linked project"
                problems.append(f"{synp.relative_to(root)}: {codes or 'error'} — {first}")
    return problems


def main() -> int:
    checked = skipped = projects = 0
    failures: list[tuple[str, str]] = []

    for md in sorted(ROOT.rglob("*.md")):
        rel = md.relative_to(ROOT)
        text = md.read_text(encoding="utf-8")
        for block in FENCE.findall(text):
            src = block.strip()
            for issue in check_style(src):
                failures.append((str(rel), f"style — {issue}"))

            if src.startswith("# ") and re.match(r"# [\w./-]+\.\w+\n", src + "\n"):
                skipped += 1  # file of a project: compiled below, as a whole
                continue
            if "<" in src and ">" in src:
                skipped += 1  # schematic form (<name>, <TYPE>), not real code
                continue
            if src.startswith("FIELD "):
                name_match = re.match(r"FIELD\s+(\w+)", src)
                if not name_match:
                    skipped += 1
                    continue
                field = name_match.group(1)
                scope_match = re.search(r"SCOPE\s+(\w+)", src)
                scope = scope_match.group(1) if scope_match else "ITEM"
                src = (
                    f"TEMPLATE conformance\n"
                    f"{scope} FIELDS\n    REQUIRED {field}\nEND {scope} FIELDS\n"
                    f"{src}"
                )
            elif not src.startswith("TEMPLATE"):
                skipped += 1
                continue
            checked += 1
            try:
                result = validate_template(load_template_from_string(src))
                codes = [e.CODE for e in result.errors]
                if codes:
                    failures.append((str(rel), ", ".join(codes)))
            except Exception as exc:  # noqa: BLE001
                failures.append((str(rel), f"{type(exc).__name__}: {exc}"))

        files = {name: body for name, body in FILE_FENCE.findall(text)}
        if any(name.endswith(".synp") for name in files):
            projects += 1
            for problem in check_project(files):
                failures.append((str(rel), f"project — {problem}"))

    if failures:
        print(f"FAILED: {len(failures)} example(s) do not compile\n")
        for path, err in failures:
            print(f"  {path}: {err}")
        return 1

    print(f"OK: {checked} example(s) and {projects} project(s) compile cleanly "
          f"({skipped} fragments not verifiable alone)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
