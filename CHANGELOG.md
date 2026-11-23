# Changelog

All notable changes to this project will be documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

**Language:** [English](CHANGELOG.md) | [Português](CHANGELOG.pt.md)

---

## [Unreleased]

## [0.4.0] — 2026-11-23

The guide is now **English-only** — 204 entries — and answers agents as well
as people.

### Changed — one language, always in sync

- All entries moved from the `pt` locale to `en`. The 26 authored entries were
  rewritten in English (and extended); the generators write English labels,
  summaries and placeholders. Diagnostic summaries now come from the compiler's
  own one-line message (`to_cli_line()`), so they are English and never drift.
- The severity shown for a diagnostic comes from the class (`DEFAULT_SEVERITY`),
  not from the letter of its code; diagnostics local to an `EXPORT` block say so.
- `tools/validate_entries.py` refuses Portuguese section headings and locale
  folders other than `en`. `tools/fix_accents.py` and the `pyspellchecker`
  dependency were removed.
- The TUI title reads "Synesis Guide"; long summaries are wrapped to the panel.
- Compiler floor `synesis>=0.16.0`; the generated entries were derived from
  synesis 0.16.0 (they record `requires_synesis: ">=0.16.0"`).

### Added — agents

- `synesis-help search <words> --format=json`: full-text search.
- `synesis-help list [--category <name>] --format=json`: what exists.
- `synesis-help lookup` accepts short forms (`E047` → `SYNESIS_E047`, `chain` →
  `TYPE_CHAIN`), reports how it matched (`id`, `title`, `prefix`, `search`) and
  suggests entries when nothing matches.
- Every JSON answer carries `help_version`, `synesis_version` (the compiler the
  generated entries were derived from) and `locale`. Exit codes: 0 found,
  1 not found, 2 usage error.
- New ecosystem entry `ECO_HELP` documents the contract.

### Added — case studies

- New category `case_study`, with nine complete projects adapted from real
  research (names, sources and excerpts fictitious): literature review of
  mechanisms, factors with signs and conditions, one term across passages,
  framing in news, assessment across linked projects, open-ended survey answers,
  a topical index as a SKOS vocabulary, participatory diagnosis, causation coding.
- `GUIDE_CASE_STUDIES` picks a case by research design or by pattern.
- `tools/check_examples.py` now **compiles each case study as a project**: the
  code blocks named after a file (`# review.synt`, `# records/s1.toml`) are
  written to a temporary folder, a `references.bib` is generated, and every
  `.synp` must compile without errors.

### Added — EXPORT ALPACA with declared composition (synesis 0.16.0)

- `BLOCK_EXPORT` documents `MAP <fields> TO INSTRUCTION|INPUT|OUTPUT` and its
  rules; generated entries for `SYNESIS_E158`–`SYNESIS_E165` and
  `SYNESIS_I166`–`SYNESIS_I167`.

### Fixed

- The frontmatter parser undoes `\"` and `\\`: syntaxes such as
  `OUTPUT "<file>"` reached the index and the JSON with the backslashes.
- SPDX license identifier (L-1): `LicenseRef-Synesis-AGPL-3.0-with-Data-Output-Exception`
  instead of `AGPL-3.0-only AND LicenseRef-Synesis-data-output-exception` (in
  SPDX, `AND` means two cumulative licenses). The license did not change;
  `CITATION.cff` keeps `AGPL-3.0-only`.

## [0.3.0] — 2026-11-17

The guide now ships in Portuguese — 183 entries — covering
synesis 0.15.

### Added

- **`MOD_ROLE`**: the function of an ONTOLOGY field in the organizing model
  (`LABEL`, `NOTE`, `HIERARCHY`, `USE`), with the SKOS property each one maps to.
- **`BLOCK_QUESTIONS`, `BLOCK_PHASE`, `BLOCK_EXPORT`**: the `.synp` blocks for
  competency questions, the production plan run by `synesis-coder phase`, and
  the project's artifacts (SKOS with `MAP RELATIONS`, `ALIAS_LABEL`,
  `REGISTRY` and `synesis export --publish`; IRIs from the project `NAMESPACE`).
- Generated entries for diagnostics `SYNESIS_E089`–`SYNESIS_E157`.

### Changed

- **`BLOCK_ONTOLOGY` explains ONTOLOGY blocks as organizing principles**: the
  same mechanism serves a flat list, a thesaurus, a taxonomy or a lightweight
  ontology, and the compiler reports each project's profile.
- **The tool's own output is in English** (help, `docs`, `credits`, TUI
  labels). Entries stay in the `pt` locale; diagnostic entries quote the
  compiler's messages, which are now in English.

### Fixed

- `tools/generate_entries.py` no longer escapes quotes twice in summaries that
  contain `:` (`SYNESIS_E091`, `SYNESIS_E092`).

## [0.2.1] — 2026-08-24

### Changed

- **The `synesis-graph` entry now covers `ProjectContext`.** Since
  `synesis-graph` 0.8.0, exporting to a database also writes the project's own
  context into the graph: the `.synp` `DESCRIPTION` and the whole template as a
  readable document — every field with its type, scope, description, value scale
  and **GUIDELINES**, plus the graph's edges with their direction.

  The guide had to say so, because it changes what writing a good template is
  worth. A database schema is syntax without semantics: it states that a vertex
  `Aspect` has a property `name`, but not that `Aspect` is an ordered scale nor
  what each value means. The `GUIDELINES` a researcher writes are their coding
  protocol — the decision rules that say what counts as a valid instance of a
  field. Without them in the graph, whoever queries it has to infer that
  criterion from the data.

  `ECO_GRAPH` is generated from the tool's `--help`, so the explanation lives in
  the generator's authored `note` field, where regeneration preserves it.

- **`GUIDE_ECOSYSTEM` gained the section "O que o grafo leva junto"**, with the
  point that matters most to whoever writes a template: good `GUIDELINES` pay
  twice — they guide `synesis-coder` while annotating, and they travel with the
  graph afterwards.

- Regenerating the ecosystem entries also refreshed the recorded versions of
  `ECO_CODER`, `ECO_LSP` and `ECO_SYNESIS`, which had fallen behind.

## [0.2.0] — 2026-08-20

The guide now ships in Portuguese — 110 entries — with the two new compiler
diagnostics below. Requires `synesis>=0.12.0`, which introduces them.

### Added

- **`SYNESIS_E087` and `SYNESIS_E088`**, regenerated from the compiler. They
  govern the two sides of the index/label distinction in closed vocabularies:
  `E087` rejects an index prefix `[N]` in an `ENUMERATED` block (no order, so
  no index), and `E088` rejects writing the label where an `ORDERED` field
  expects the index.

- **"Valor na anotação" section** in `TYPE_ORDERED` and `TYPE_ENUMERATED`.
  The generated entries described how each type is *declared* but never what
  is actually *written* in the annotation — the distinction the two new
  diagnostics enforce. Both entries now also link to their diagnostic.

### Fixed

- **The `ENUMERATED` example taught invalid syntax.** The `VALUES` snippet was
  shared by both closed-vocabulary types and carried `[1]`/`[2]`, which is now
  `SYNESIS_E087` for `ENUMERATED`. The snippet is type-aware: `ORDERED` keeps
  the indexed form (which it requires), `ENUMERATED` drops it.

  `tools/check_examples.py` catches this class of drift — it compiles every
  `FIELD` example and reported the offending block by code.

---

## [0.1.0] — 2026-08-18

First release: content, index and TUI.

The guide ships with 108 entries in Portuguese. 86 of them are **derived** —
82 by probing the compiler (`synesis.language_info`, `synesis.ast.results`)
and 4 from the `--help` of each installed module — so the documentation
cannot drift from what the tools actually do. The remaining 22 are authored,
and cover what requires methodological judgement: what each construct is for,
when to use it, and worked examples.

### Added

**Content — 108 entries in Portuguese**

- 71 diagnostics, 10 field types and 1 linkage entry **derived from the
  compiler** by probing `synesis.language_info` and `synesis.ast.results`.
  Never hand-written: a rule change in the compiler is reflected by
  regeneration.
- 20 authored entries: language blocks (`PROJECT`, `TEMPLATE`, `FIELD`,
  `SOURCE`, `ITEM`, `ONTOLOGY`, `<SCOPE> FIELDS`), modifiers (`SCOPE`,
  `GUIDELINES`, `DESCRIPTION`, `INCLUDE`, `BUNDLE`, `METADATA`,
  `IDENTIFIES`/`REFERS TO`, `ON BIBLIOGRAPHY`/`ON DATASET`) and seven overviews
  (`GUIDE_START`, `GUIDE_FILES`, `GUIDE_PRIMITIVES`, `GUIDE_CHAINS`,
  `GUIDE_MULTIPROJECT`, `GUIDE_ECOSYSTEM`, `GUIDE_REVIEW`).
- **`GUIDE_REVIEW`** documents the `synesis-coder` review pipeline
  (`anchor` → `critique` → `normalize` → `incorporate`). It is the step a
  researcher is most likely to skip and least able to skip: annotation
  produced by an LLM compiles cleanly and still asserts what the source does
  not sustain. The guide states what each phase reads and writes, which of
  them calls an LLM, and why `incorporate` rejects an ambiguous correction
  instead of guessing its target.
- **`.synr` added to the file-extension table** in `GUIDE_FILES`, with the
  reason it is the one extension that never appears in an `INCLUDE`: it is a
  `synesis-coder` work artifact, not part of the project.
- Every reference entry states its **full syntax** — required parts bare,
  optional parts in `[ ]`, alternatives with `|` — in the classic reference
  guide convention. No `...` standing in for structure.

**Tooling**

- `tools/generate_entries.py` — generates derived entries; `--check` fails on
  drift (CI gate).
- `tools/generate_index.py` — builds `INDEX.md`, the master index.
- `tools/validate_entries.py` — frontmatter, unique `id`, cross-reference
  graph integrity, and presence of a syntax section on reference entries.
- `tools/check_examples.py` — compiles every example against the installed
  `synesis`, and enforces code-block style (72 columns, 4-space indent, no
  tabs, no trailing space).
- `tools/generate_ecosystem.py` — generates the `ECO_*` entries from the
  `--help` of each installed module, so a new subcommand reaches the guide by
  regeneration rather than transcription. `--check` fails on drift.
  - **Values resolved from the environment are redacted.** `synesis-coder
    --help` prints `(Current: <model>)`, which is the model configured on the
    machine that generated the entry — not a property of the package. It is
    replaced by `(Current: set by SYNESIS_CODER_MODEL)`: the entry documents
    *how* the value is set instead of publishing one developer's `.env`, and
    stops changing on every regeneration elsewhere.
  - **`generate_entries.py --check` no longer reports the `ECO_*` entries as
    orphans.** Both generators write to `entries/_generated/pt/` and each only
    knows its own output, so the check was permanently red — and a check that
    is always red is a check that gets ignored, which is exactly what would
    have hidden a real orphan.

**Continuous integration**

- `.github/workflows/ci.yml` — tests on 3 Python versions x 3 operating
  systems, lint, dependency audit, secret scan, build and PyPI publish on
  `v*` tags. GitHub Actions pinned by commit SHA.
- **`content` job** — the check this package needs and the others do not: 86
  of its 108 entries are *derived* from the compiler and from the `--help` of
  the sibling modules. An entry that disagrees with the tool is worse than no
  entry at all, because the researcher trusts what they read. It runs
  `validate_entries`, `check_examples`, `generate_entries --check` and
  `generate_index --check`.
  - `generate_ecosystem.py --check` is deliberately **not** in CI: it reads
    the `--help` of the sibling modules, which are not installed on the
    runner, so it would compare an entry against the absence of the tool and
    fail every time.
- **`tools/check_wheel.py`** — asserts the entries are inside the built wheel.
  A wheel without them installs cleanly, the command runs, and the guide
  answers "not found" for everything: silent failure, the worst kind.
- `.github/workflows/cla.yml` — CLA Assistant, signatures held centrally in
  `synesis-lang/cla-signatures`.
- `.github/dependabot.yml` — version PRs off, matching the rest of the
  ecosystem; security updates stay on.
- **Ruff configured** with the ecosystem baseline (`select = ["F", "I"]`).
  Running ruff with no configuration reported 23 findings, none of them a bug
  — and a CI that is red on the first commit teaches people to ignore CI.

**Package**

- `synesis_help.index` — compiles the Markdown entries into SQLite + FTS5.
- `synesis_help.render` — renders entry bodies with role-based colouring.
- `synesis_help.app` — Textual TUI: title bar, two panes, key bar.
- `synesis_help.cli` — `build`, `lookup`, `lookup --format=json`, and the TUI
  as the default command.
- Keys: `↑`/`↓` move, `Enter` opens, `F2` opens cross-references, `F3` (or `/`)
  incremental search, `Backspace` goes back, `Tab` switches pane, `Esc` exits.

### Navigation (revised after the first usability pass)

It was hard to tell which pane was active: the highlighted item was cyan
whether the pane had focus or not. Three redundant focus cues, using what
modern terminals offer and DOS did not:

- **Lit frame.** Each pane has its own border and title; the active one lights
  up. It is the cue the eye finds before reading anything.
- **Selection bar only in the active pane.** In the inactive pane the selection
  is merely marked, with no bar — it shows "where you were", not
  "where you are".
- **Contextual footer.** The key bar now lists what works in the focused pane.

Also: `Enter` on a category now advances to the entry list (previously it did
nothing, stalling keyboard navigation), the content pane became a focusable
scrollable region, and body tables now respect the pane width instead of
wrapping.

### Actionable cross-references

"See also" was inert text — precisely the gesture that defined Norton Guides.
Each reference is now navigable three ways: **mouse click** (in the "see also"
list or on any `` `REF` `` cited mid-text), **keys `1`–`9`** by the number shown
to its left, and **`F2`**, which brings them all into the side list.
`Backspace` goes back in every case.

> The inertia had two causes: Textual 3.x drops `meta` when converting
> `rich.Text` into `Content`, and the action needed the `app.` namespace to
> resolve on the App rather than on the clicked widget.

### "Retro-Editorial" palette

The silhouette is from the 80s; the colours are not. Out go CGA's pure blue and
yellow — vivid, but harsh on an LCD — and in comes a palette where every colour
carries a **role in the information hierarchy**, never decoration: midnight
blue background, silver body text, bright cyan headings, golden keywords, mint
green *italic* placeholders, coral diagnostics, sky blue references (no
underline, inverted on focus), and dimmed grey for structural symbols.

The **keyword × placeholder** distinction is the central gain: gold says "this
belongs to the system", mint italic says "this you replace".

Constants are named by role (`C_KEYWORD`, `C_PLACEHOLDER`), not by colour, so
swapping the palette touches neither the CSS nor the renderer. A test locks the
hierarchy in place.

### Syntax highlighting in code blocks

Code blocks no longer render as a single-colour block; they now distinguish the
same roles an editor does: golden keywords, silver user identifiers, dimmed
italic comments, soft pink strings, sky blue italic bibrefs, mint placeholders
and coral diagnostics.

The **42 keywords are read from the installed compiler's grammar**
(`synesis.lark`), not from a parallel list — a new word in the language gets
highlighted without anyone editing the guide.

### Accents and field names

- **Authored prose is now correctly accented** (333 words across the 20
  hand-written entries). `tools/fix_accents.py` uses `pyspellchecker`'s
  Portuguese dictionary and only accepts a suggestion when it is **the same
  word, accented** — never a swap for a different word. Code blocks, inline
  code and technical frontmatter fields are left untouched: an accent inside
  an example would make it invalid.
- **The 82 generated entries stay unaccented**, deliberately: they reproduce
  `to_diagnostic()`, which is itself unaccented today. Fixing them here would
  create a second source of truth and regeneration would undo the work.
  Accenting `results.py` is the compiler's project.
- **Field names get their own colour.** In `papel: mediador` the name belongs
  to the template and the value is the researcher's data. This also fixes a
  subtle error: a field named `code` was painted as the language keyword.

### Ecosystem entries

Five new entries covering the tools around the language: `synesis`,
`synesis-lsp`, `synesis-coder`, `synesis-graph`, plus an overview with the
workflow and what each tool consumes.

Content is **captured from each installed module's `--help`**, not
transcribed (`tools/generate_ecosystem.py`). Local interpreter paths, Python
versions and log lines are filtered out: the language server prints its own
executable path, which would make the guide differ per machine.

### Presentation order

Entries were listed alphabetically, which put "Por onde começar" in 4th place
and `DATE` before `CODE`. Order is now editorial, via an `order` frontmatter
field (lower first; 100 is the default; ties fall back to alphabetical), and
applies to both the TUI and `INDEX.md`.

### Typographic finish

- **`♦` on the active category** and **`►` on the selected entry**. CSS could
  not do it — `border-left` paints every item, not just the highlighted one —
  so the marker goes into the label text itself.
- **"See also" as a diamond grid**, gloss aligned in a fixed column, no
  underline.
- **Typographic bullets** (`•`) replacing the Markdown hyphen.

### Visual finish

- **Rounded frames** (`╭─╮`) on all three panes — the modern touch over the
  vintage base.
- **Position counter** in the frame title (`Verbetes 2/10`), with the title
  reflecting where the list came from (category, search, or references).

### Fixed during testing

- **Tables truncated their text.** Columns had fixed widths, so
  "ponto de entrada; amarra tudo" became "…amarra tud…" even with free space
  to the right. Tables are now measured as a block, and the measurement uses
  the **already rendered** text — counting markup characters misaligned the
  next column.
- **Ordered lists collapsed into one paragraph.** `1.` `2.` `3.` were not
  recognised as list items, so paragraph re-joining merged them into a single
  line. Each item now opens its own paragraph, with continuations aligned
  under the text rather than the number.
- **`F10 Credits` was missing from the footer.** The key bar had been edited
  after the shortcut was added. The footer now separates active-pane keys from
  global ones and fits in 80 columns — it had grown to 102, hiding `Esc`.
- **Duplicated "See also".** The section appeared twice: once from the
  Markdown body, once built from `see_also`. The renderer now suppresses the
  body one and keeps only the actionable version.
- **Search (F3) showed a double frame and hid the status line.** Textual's
  `Input` already draws its own border and another was wrapped around it;
  the field was also declared before the status bar, so `dock: bottom` put it
  underneath. It is now a single line above the footer.
- **`**bold**` rendered literally.** Two causes: bold could wrap `` `code` ``
  (the two-pass scan broke the pair) and could straddle a line break in the
  source. Markup is now resolved in a single pass, paragraphs are joined
  before rendering, and wrapping happens *after* styling.

- **Entries were not shipped with the package.** They lived in `entries/` at
  the repository root, outside `synesis_help/`, so the wheel had no content: a
  `pip` install would give you the command without the guide. Moved to
  `synesis_help/entries/` and declared in `package-data`. Verified by
  installing the wheel into a clean environment.
- **Search favoured the longest text.** Looking up "chain" returned
  `SYNESIS_E056` before `TYPE_CHAIN`, because FTS5 scores by term frequency.
  Ordering now puts title matches ahead of the relevance rank.
- **HTML comment leaked into the body.** The "GENERATED AUTOMATICALLY" notice
  showed up in the TUI and in `lookup --format=json`. Stripped at index time.
- **Duplicate IDs when switching categories.** `ListView.clear()` is async in
  Textual and the next batch was inserted before removal completed. Entry ids
  are now tracked in an array parallel to the widget index.

### Notes

- **Portuguese only.** Translation is *blocked* by the compiler, not merely
  postponed: diagnostic prose comes from `results.py` in Portuguese, and
  translating it here would create a second source of truth. The structure is
  ready (per-locale directories, `(id, locale)` key, label catalog, locale
  selection chain) so adding a language later is translation, not refactoring.
- Entries about `VALUES` outside `ORDERED`/`ENUMERATED` and about
  `CONTEXT FROM DATASET` are deliberately absent, pending a product decision in
  the compiler.

### Findings reported upstream

Recorded in `synesis-planning/synesis-help/achados_geracao_2026-08-08.md`:

- `SYNESIS_E064` is shared by three distinct error classes — the only code that
  is not 1:1 among the 71.
- The official reference guide (Appendix A of `guia_referencia.qmd`) shows
  template metadata on its own line, which **does not compile**; the grammar
  requires it inline on the `TEMPLATE` header.

---

[0.3.0.dev0]: https://github.com/synesis-lang/synesis-help/compare/v0.2.1...HEAD
[0.4.0]: https://github.com/synesis-lang/synesis-help/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/synesis-lang/synesis-help/compare/v0.2.1...v0.3.0
[0.2.1]: https://github.com/synesis-lang/synesis-help/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/synesis-lang/synesis-help/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/synesis-lang/synesis-help/releases/tag/v0.1.0
