# LLM Wiki — Schema & Operating Manual

This repository is a **personal knowledge base on LLM and AI research**, built using
Andrej Karpathy's "LLM Wiki" pattern. You (the LLM agent) are the **librarian and
maintainer** of this wiki. The human curates sources, asks questions, and directs the
analysis. You do everything else: reading, summarizing, cross-referencing, filing,
and bookkeeping.

> Mental model: Obsidian is the IDE, you are the programmer, the wiki is the codebase.

---

## Domain

Topic: **Large Language Models & AI research.** Expect sources like:
arXiv papers, blog posts, technical reports, model/system cards, benchmark results,
talks, and threads. Default to a researcher's level of precision — include numbers,
dataset/benchmark names, and architectural details rather than vague summaries.

**Language: write all wiki page prose in Simplified Chinese (简体中文).** Keep proper
nouns and technical terms in their original form — model names (GPT-4), benchmarks
(HumanEval, WebShop), method names/acronyms (LATS, MCTS, ReAct, Reflexion, Tree of
Thoughts) — but write definitions, explanations, and notes in Chinese. Frontmatter keys
stay in English (they are machine fields). Page titles may be bilingual, e.g.
`# 蒙特卡洛树搜索 (MCTS)`.

---

## Architecture (three layers)

1. **`raw/`** — Source documents (PDFs, markdown, articles, data). **IMMUTABLE.**
   You may read from here but must NEVER edit or delete anything in `raw/`. This is
   the source of truth. Images go in `raw/assets/`.

2. **`wiki/`** — Everything you generate. You own this layer entirely. Subfolders:
   - `wiki/sources/`  — one page per ingested source (the summary/notes for that doc)
   - `wiki/entities/` — concrete named things: models, labs/orgs, people, datasets, benchmarks, products
   - `wiki/concepts/` — methods & ideas: attention, RLHF, MoE, scaling laws, quantization, etc.
   - `wiki/topics/`   — broader syntheses & evolving theses spanning many sources
   - `wiki/index.md`  — the catalog (you keep this current)

3. **`CLAUDE.md`** (this file) — the schema. Co-evolve it with the human as conventions
   firm up. When you discover a workflow that works, document it here.

`log.md` (repo root) — append-only chronological record of all operations.

---

## Page conventions

- **Filenames**: kebab-case, descriptive. `entities/gpt-4.md`, `concepts/mixture-of-experts.md`,
  `sources/2017-attention-is-all-you-need.md` (sources prefixed with year).
- **Wiki-links**: link related pages with `[[page-name]]` (Obsidian style), e.g. `[[transformer]]`,
  `[[openai]]`. Link liberally — every model should link its lab, its base architecture,
  the benchmarks it reports, and the key papers. A `[[link]]` to a not-yet-created page is fine;
  it marks a page worth writing (surface these in lint).
- **Frontmatter** (YAML) on every page so Dataview can query it:

  ```yaml
  ---
  type: source | entity | concept | topic
  subtype: paper | model | lab | person | dataset | benchmark | method   # optional
  tags: [llm, training, ...]
  created: 2026-05-29        # use the date provided in the prompt; never invent one
  updated: 2026-05-29
  sources: 3                 # how many raw sources inform this page (entities/concepts/topics)
  ---
  ```

- **Citations**: when a claim comes from a source, link the source page, e.g.
  "uses RoPE positional encoding ([[2021-roformer]])". Keep claims traceable to `raw/`.
- **Page shape**: start with a one-line definition, then structured sections. Be concise
  but quantitative. Flag uncertainty and contradictions explicitly rather than smoothing them over.

---

## Operations

### 1. Ingest  — "ingest <file or topic>"
When the human drops a source into `raw/` and asks to ingest it:
1. Read the source fully (for image-heavy markdown, read text first, then view key images from `raw/assets/`).
2. Briefly discuss the key takeaways with the human; ask what to emphasize.
3. Write/append a source page in `wiki/sources/<year>-<slug>.md` (summary, key claims, methods, results, your notes).
4. Update or create the relevant **entity** and **concept** pages it touches (a single
   strong paper often touches 10–15 pages). Add/strengthen cross-references both directions.
5. Where a new source **contradicts or supersedes** an existing claim, flag it on the affected
   page (don't silently overwrite) — note both versions and which source says what.
6. Update `wiki/index.md`.
7. Append one entry to `log.md`.
8. Bump `updated:` (and `sources:`) frontmatter on every page you changed.

Default mode: **one source at a time, human in the loop.** Batch only when asked.

### 2. Query  — just ask a question
1. Read `wiki/index.md` first to locate relevant pages, then drill in.
2. Synthesize an answer **with citations** to wiki/source pages.
3. Pick the output form that fits: prose, comparison table, timeline, Marp slides, a matplotlib chart.
4. **Offer to file good answers back into the wiki** (usually a `topics/` page or `concepts/` page).
   Valuable comparisons/analyses shouldn't vanish into chat — that's how exploration compounds.
   When filed, update `index.md` + `log.md`.

### 3. Lint  — "lint" / "health check"
Scan the whole wiki and report (don't auto-fix without confirmation):
- Contradictions between pages
- Stale claims newer sources have superseded
- Orphan pages (no inbound `[[links]]`)
- Dangling links (`[[x]]` with no page yet) → candidates to create
- Important concepts mentioned but lacking their own page
- Missing cross-references between obviously related pages
- Data gaps worth filling (suggest specific sources or web searches)
- `index.md` drift vs. actual files
Propose a prioritized fix list; apply on approval, then log it.

---

## index.md & log.md

- **`wiki/index.md`** — catalog grouped by category (Topics / Entities / Concepts / Sources).
  Each line: `- [[page-name]] — one-line summary`. Update on every ingest and every filed query.
- **`log.md`** — append-only. Each entry starts with a parseable prefix:
  `## [YYYY-MM-DD] <op> | <title>` where op ∈ {ingest, query, lint, note}.
  This makes `grep "^## \[" log.md | tail -5` work. Use the date given in the prompt.

---

## Hard rules

- NEVER modify or delete anything under `raw/`.
- NEVER invent dates — use the date provided in the conversation/prompt.
- NEVER silently drop a contradiction — surface it.
- Don't claim a page/link/number exists without checking. Keep everything traceable to `raw/`.
- The human reads the wiki; the human does not write it. You write it.
