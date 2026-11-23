# Copyright (c) 2026 Christian Maciel De Britto
# SPDX-License-Identifier: LicenseRef-Synesis-AGPL-3.0-with-Data-Output-Exception
"""Long texts of the CLI: writing guide and credits.

Kept apart from `cli.py` so the command logic stays readable. The guide and the
CLI are English-only (decision of 2026-11-21): one source, always in sync with
the compiler. Agents translate for the researcher when needed.
"""

from __future__ import annotations

__version__ = "0.4.0"

AUTHOR = "Christian Maciel De Britto"
YEAR = "2026"
ORCID = "https://orcid.org/0000-0003-1431-3924"
REPO = "https://github.com/synesis-lang/synesis-help"
DOCS = "https://synesis-lang.github.io/synesis-docs"

EPILOG = """\
examples:
  synesis-help                              open the guide (TUI)
  synesis-help lookup CHAIN                 one entry in the terminal
  synesis-help lookup E047 --format=json    one entry, JSON contract
  synesis-help search bundle status         full-text search
  synesis-help list --category case_study   what exists in a category
  synesis-help docs                         how to write and fix entries
  synesis-help credits                      authorship, license and how to cite

for agents:
  use --format=json; exit codes are 0 found, 1 not found, 2 usage error;
  every answer carries help_version and synesis_version.

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
  ├── _generated/en/   generated from the compiler — NEVER edit by hand
  └── authored/en/     human content — this is where you write

What the compiler knows about itself (type x property matrix, error codes,
messages) is derived by probing, never copied. That way the guide cannot
drift from the compiler. What takes methodological judgement — what each type
is for, when to use it, examples — is authored, and lives apart.

The guide is English-only. Agents that talk to researchers in another
language translate the answer; the guide itself stays in one language, so it
never lags behind the compiler.


Fixing an existing text
-----------------------
1. Find the file: its name is the entry's `id`.
       synesis-help lookup TYPE_CHAIN --format=json

2. If the path contains `_generated/`, do NOT edit it — see the section below.

3. Edit the .md in synesis_help/entries/authored/en/

4. Rebuild and check:
       python tools/validate_entries.py   links, ids, frontmatter
       python tools/check_examples.py     examples still compile
       synesis-help build                 rewrites the index

   The guide reads the compiled index, not the .md files.
   WITHOUT `build`, YOUR EDIT DOES NOT SHOW.


Adding an entry
---------------
Create synesis_help/entries/authored/en/<ID>.md — the file name IS the `id`:

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

    ## Description
    What it is and what it is for.

    ## Syntax
    (code block with the complete form)

    ## Rules
    - One rule per line, citing the error code.

    ## Example
    (code block that compiles)

Then:  python tools/generate_index.py && synesis-help build

`order` sets the position inside the category: lower comes first, 100 is the
default, ties fall back to alphabetical. The order is DIDACTIC — from the
overview to the detail — not alphabetical: "Where to start" must open the
guide.

Valid categories:
  overview · block · field_type · modifier · linkage
  case_study · ecosystem · diagnostic

The block, field_type, modifier and linkage categories REQUIRE `syntax` in the
frontmatter and a "## Syntax" section in the body — the validator checks it.
A case_study REQUIRES the sections "## Research question", "## Template",
"## Annotation", "## Design decisions" and "## Adapt it".

`id` convention:
  BLOCK_    block               BLOCK_ONTOLOGY
  TYPE_     field type          TYPE_CHAIN
  MOD_      modifier            MOD_SCOPE
  GUIDE_    overview            GUIDE_START
  CASE_     case study          CASE_LITERATURE_REVIEW
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
authored/en/. The build merges both, and the authored one wins.


Writing rules
-------------
Language     English only. Portuguese section headings are refused by the
             validator. Case studies never name real people, institutions
             or projects: describe the design, not who used it.

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
  AGPL-3.0-only with the Synesis Data-Output Exception
  (SPDX: LicenseRef-Synesis-AGPL-3.0-with-Data-Output-Exception)

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
