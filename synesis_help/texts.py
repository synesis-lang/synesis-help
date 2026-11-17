# Copyright (c) 2026 Christian Maciel De Britto
# SPDX-License-Identifier: AGPL-3.0-only AND LicenseRef-Synesis-data-output-exception
"""Textos longos da CLI: ajuda de escrita e creditos.

Ficam separados de `cli.py` para que a logica de comandos permaneca legivel.
A saida da CLI e em ingles (idioma oficial das saidas, 2026-11-17); o
conteudo dos verbetes continua no locale `pt`.
"""

from __future__ import annotations

__version__ = "0.3.0"

AUTHOR = "Christian Maciel De Britto"
YEAR = "2026"
ORCID = "https://orcid.org/0000-0003-1431-3924"
REPO = "https://github.com/synesis-lang/synesis-help"
DOCS = "https://synesis-lang.github.io/synesis-docs"

EPILOG = """\
examples:
  synesis-help                      open the guide (TUI)
  synesis-help lookup CHAIN         look up an entry in the terminal
  synesis-help lookup E047 --format=json
  synesis-help docs                 how to write and fix entries
  synesis-help credits              authorship, license and how to cite

in the guide:
  arrows  move / scroll            F2   cross-references
  Enter   go forward               F3   incremental search
  Tab     switch panel             Esc  quit
"""

WRITING_GUIDE = f"""\
WRITING IN THE GUIDE
====================

Where the content lives
-----------------------
  synesis_help/entries/
  ├── _generated/pt/   generated from the compiler — NEVER edit by hand
  └── authored/pt/     human content — this is where you write

What the compiler knows about itself (type x property matrix, error codes,
messages) is derived by probing, never copied. That way the guide cannot
drift from the compiler. What takes methodological judgement — what each type
is for, when to use it, examples — is authored, and lives apart.

The entries are written in Portuguese (locale `pt`); this tool's own output
is in English.


Fixing an existing text
-----------------------
1. Find the file: its name is the entry's `id`.
       synesis-help lookup TYPE_CHAIN --format=json

2. If the path contains `_generated/`, do NOT edit it — see the section below.

3. Edit the .md in synesis_help/entries/authored/pt/

4. Rebuild and check:
       python tools/validate_entries.py   links, ids, frontmatter
       python tools/check_examples.py     examples still compile
       synesis-help build                 rewrites the index

   The guide reads the compiled index, not the .md files.
   WITHOUT `build`, YOUR EDIT DOES NOT SHOW.


Adding an entry
---------------
Create synesis_help/entries/authored/pt/<ID>.md — the file name IS the `id`:

    ---
    id: MOD_EXAMPLE
    title: "EXAMPLE"
    category: modifier
    summary: "One sentence. It is what the index shows."
    syntax: "EXAMPLE <value> [OPTIONAL <n>]"
    see_also: [BLOCK_FIELD, SYNESIS_E020]
    source: authored
    order: 50
    ---

    # EXAMPLE

    ## Descrição
    What it is and what it is for.

    ## Sintaxe
    (code block with the complete form)

    ## Regras
    - One rule per line, citing the error code.

    ## Exemplo
    (code block that compiles)

Then:  python tools/generate_index.py && synesis-help build

`order` sets the position inside the category: lower comes first, 100 is the
default, ties fall back to alphabetical. The order is DIDACTIC — from the
overview to the detail — not alphabetical: "Por onde começar" must open the
guide.

Valid categories:
  overview · block · field_type · modifier · linkage
  ecosystem · glossary

The block, field_type, modifier and linkage categories REQUIRE `syntax` in the
frontmatter and a "## Sintaxe" section in the body — the validator checks it.

`id` convention:
  BLOCK_    block               BLOCK_ONTOLOGY
  TYPE_     field type          TYPE_CHAIN
  MOD_      modifier            MOD_SCOPE
  GUIDE_    overview            GUIDE_START
  GLOS_     glossary            GLOS_BIBREF
  (a diagnostic uses its own code: SYNESIS_E047)

The `id` is the key to everything — cross-references, links and the JSON
contract. Choose it and do not change it; the title may change freely.


Fixing a generated entry
------------------------
The entries in _generated/ come from the compiler. Editing them is useless: the
next regeneration overwrites them, and CI flags it.

  The rule itself ............ in the compiler (synesis/)
  The error message .......... synesis/ast/results.py, in to_diagnostic()
  Type summary ............... tools/generate_entries.py, TYPE_SUMMARY dict
  A module's help ............ the tool's own --help
                               (tools/generate_ecosystem.py only captures it)
  Section labels ............. tools/generate_entries.py, L dict

To ADD prose to a generated entry, create a file with the SAME `id` in
authored/pt/. The build merges both, and the authored one wins.


Writing rules
-------------
Accents      Write with accents. If you forget:
                 python tools/fix_accents.py --check   reports
                 python tools/fix_accents.py           fixes
             Only prose is touched — code and technical fields stay intact.

Code         At most 72 columns, 4-space indent, no TAB. Every example that
             starts with TEMPLATE or FIELD is really COMPILED against the
             installed synesis. A wrong example in the guide is worse than a
             missing one.

Register     This is a REFERENCE guide (Diataxis): it describes the machine,
             briefly and in order. Tutorials, methodological discussion and
             case studies belong in synesis-docs.

see_also     Existing `id`s only — a broken link fails the build.

Full documentation: {REPO}
"""

CREDITS = f"""\
  synesis-help {__version__}

  Quick reference guide to the Synesis language

  Copyright (c) {YEAR} {AUTHOR}
  {ORCID}

  LICENSE
  -------
  AGPL-3.0-only AND LicenseRef-Synesis-data-output-exception

  This program is free software: you can redistribute it and/or modify it
  under the terms of the GNU Affero General Public License, version 3, as
  published by the Free Software Foundation.

  Distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
  without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
  PARTICULAR PURPOSE. See the GNU AGPL for more details.

  Data output exception: the data produced by this software is NOT covered
  by the AGPL. See LICENSE.exception.

  Full text: LICENSE and LICENSE.exception, at the repository root.

  INSPIRATION
  -----------
  Norton Guides (1985), by Warren Woodford — a resident help system that set
  the standard for quick reference among programmers, whose ergonomics this
  guide tries to revive: offline, instant, keyboard-navigable.

  CONTENT
  -------
  The diagnostic and field-type entries are derived by probing the Synesis
  compiler — the documentation cannot drift from what the compiler does. The
  others are authored.

  HOW TO CITE
  -----------
  De Britto, C. M. ({YEAR}). synesis-help: reference guide to the Synesis
  language (version {__version__}) [Software]. {REPO}

  ECOSYSTEM
  ---------
  synesis          language compiler
  synesis-lsp      language server
  synesis-graph    export to graph databases
  synesis-coder    AI-assisted annotation
  synesis-vscode   editor extension
  synesis-help     this guide

  {DOCS}
"""
