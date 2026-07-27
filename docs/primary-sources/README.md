# Primary sources - where gathered documents go

This folder holds the real primary documents (licences, Terms, Privacy Policies, DPAs) that ground
the AI Ownership Index entries. A coworker saves them here; the build automation reads them. See
[`../primary-doc-handover.md`](../primary-doc-handover.md) for the full task, the priority order,
and the exact document + URL to fetch for each entity.

## How to add a document

Create a subfolder named exactly the entity id and save one file per document:

```
docs/primary-sources/<entity-id>/<doc_type>__<detail?>__<YYYY-MM-DD>.<ext>
```

- `<entity-id>` - one of the 15 ids below.
- `<doc_type>` - one of: `terms · privacy_policy · dpa · subprocessors · security · sla ·
  model_card · license · technical_report · docs · marketing · third_party` (maps 1:1 to the
  evidence `doc_type`).
- Paste the **governing clauses as text** (`.md`/`.txt`) plus the source URL and date, rather than
  committing large third-party PDFs. Add a `_sources.md` per entity, one line per document:
  `doc_type | URL | date | exists(yes/no) | notes`.
- A missing document is a finding - record `exists: no`.

The weekly review (Routine `AI Ownership Index - weekly primary-doc review`) reads this folder and
re-grounds each affected entry: it rewrites the four-domain items from the real text, sets the
evidence `retrieved: true` with citations, recomputes the ownership verdict, validates, and pushes.

## Entities (`entity-id`)

Models: `ai2-olmo` · `meta-llama` · `deepseek` · `qwen` · `mistral` · `gpt-oss` · `glm` · `kimi` ·
`soofi` · `eurollm`
Inference providers: `together-ai` · `groq` · `deepinfra` · `berget` · `infercom`

Status: the five inference providers were re-grounded on 2026-07-25 against their real Terms /
Privacy / DPA, and each now has a scaffolded folder here (`berget/`, `infercom/`, `groq/`,
`deepinfra/`, `together-ai/`) whose `_sources.md` is the outstanding-document checklist - drop the
verbatim clause files alongside it. See the per-entity grounded-vs-outstanding lists in
[`../primary-doc-handover.md`](../primary-doc-handover.md). Work order: **the nine un-grounded
models first** (licences + model cards + technical reports - Hugging Face is proxy-blocked, so a
human is needed), then the remaining provider gaps - **Berget's DPA → Infercom's DPA (v1.3 PDF,
proxy-blocked) → Groq's sub-processor list + AUP → DeepInfra's trust/compliance page → Together
pricing**.
