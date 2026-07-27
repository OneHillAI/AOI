# Documentation Taxonomy (the library's spine)

**Status: recommendation for sign-off**, grounded in a survey of established
documentation frameworks (see sources at the bottom). This defines how every Library
Entry is organised.

---

## The principle: two levels

- **Top level = the adopter's journey** (4 domains). This is what a decision-maker
  navigates: *should we adopt it → how do we deploy it → how do we use it → how do we
  keep it running.* It matches OneHill's stated goal - "complete documentation needed to
  make an informed decision to implement."
- **Inside each domain = the standard, named document types** from the accepted
  frameworks (Diátaxis, ISO/IEC/IEEE 26514, the Good Docs Project). So we get
  decision-journey navigation on top and standards-conformant writing underneath.

## Why not just use Diátaxis at the top?

Diátaxis (tutorial / how-to / reference / explanation) is the de-facto industry standard
and we **do** use it - as the doc-type layer. But its top level is *author/learning*
oriented and, like the GitLab/Kubernetes "CTRT" sites, it has **no "should I adopt this"
category** - it assumes you already chose the tool. For a library whose whole purpose is
the adopt/no-adopt decision, that has to be a first-class domain. The AI/ML **Model Card**
tradition already treats intended-use / limitations / evaluation as first-class for
exactly this reason, so promoting **Assess** to a top-level domain is well-precedented for
models - we just state the divergence explicitly rather than implying it's universal.

## The four domains

| # | Domain | The adopter's question | Standard doc types it contains |
|---|---|---|---|
| 1 | **Assess** | *Should we adopt this - is it trustworthy, legal, safe, capable enough?* | Explanation/concept (what it is), **Model Card** intended-use & limitations, evaluation/benchmarks, openness & license analysis, provenance/supply-chain, EU AI Act posture, **AOI** score. |
| 2 | **Implement** | *How do we actually deploy and run it?* | **Quickstart**, **installation/deployment** how-tos (HF/Ollama/vLLM/llama.cpp/cloud), hardware & quantization **reference**, **tutorial**, fine-tuning & integration how-tos, safe-deployment controls & Deployment Ceiling. |
| 3 | **Use** | *What can it do and how do we use its capabilities well?* | Capabilities & modalities **reference**, context/languages/tool-calling/structured-output **reference**, **prompt & chat-template reference**, task **how-to guides**, concept/explanation of reasoning modes, strengths & limits per task. |
| 4 | **Support** | *How do we keep it running and get help over time?* | **Troubleshooting**/FAQ, **release notes**/changelog & versioning, security-disclosure process, support & community channels, migration/upgrade guides, deprecation policy, known issues. |

> **Naming note:** domain 3 was "Feature" in the first draft. "Feature docs" isn't a
> recognised doc-category name; the accepted equivalent is Reference + How-to + Concept
> about *what it does and how to use it*, so it's renamed **Use**. (If you prefer the
> label "Features," we can keep it as the domain's display name - it's cosmetic.)

## The document types (the standards layer, used inside every domain)

Every page is written as one of these accepted types (Diátaxis + ISO/IEC/IEEE 26514 +
Good Docs), so contributors and readers know what they're getting:

| Type | Orientation | Standard basis |
|---|---|---|
| **Explanation / Concept** | Understand *why/what* | Diátaxis *Explanation*; ISO 26514 *Conceptual* |
| **Tutorial** | Learn by doing | Diátaxis *Tutorial*; Good Docs *Tutorial* |
| **How-to guide** | Accomplish a task | Diátaxis *How-to*; ISO 26514 *Instructional* |
| **Reference** | Look up facts | Diátaxis *Reference*; ISO 26514 *Reference* |
| **Troubleshooting** | Fix a problem | ISO 26514 & GitLab first-class type |
| **Release notes / Changelog** | Track change | Good Docs; Keep a Changelog; SemVer |
| **Glossary** | Define terms | ISO 26514 & GitLab first-class type (cross-cutting) |

## Model-specific documentation folded in

For models (vs generic software), these accepted model-doc standards populate the domains:

- **Model Cards** (Mitchell et al.; Hugging Face) → Assess (intended/out-of-scope use,
  limitations, evaluation) + Use (prompt/chat template, how-to-get-started).
- **Datasheets for Datasets / Data Cards** → Assess (training-data provenance).
- **Model Openness Framework** documentation components (model card, data card, technical
  report, eval results, metadata, sample outputs) → Assess.
- **EU AI Act** Annex XI/XII + training-content summary → Assess (regulatory).

## How this maps to the aggregation model

Each domain's pages carry per-field source labels (`aggregated` / `onehill_generated` /
`gap`) and a completeness meter, so "use what exists, complement with our own testing,
and mark what can't be provided" is visible at the domain level. See
[`library-blueprint.md`](library-blueprint.md) §4.

## Cross-framework grounding (summary of the research)

Near-universal doc types across **Diátaxis, the Good Docs Project, ISO/IEC/IEEE
26511-26515, IEC/IEEE 82079-1, GitLab (CTRT), Kubernetes, GitHub, Microsoft Learn,
Google, Write the Docs**: Concept/Explanation, Task/How-to, Reference, Tutorial - with
Troubleshooting, Release notes, and Glossary added as first-class by the formal
standards. The four **domains** above are the Diátaxis core (understand / get-started /
use) *extended* with (a) an **Assess-to-adopt** domain from the Model-Card tradition and
(b) an **operate/Support** domain promoted to top level as ISO 26514, GitLab, and GitHub
do. The one deliberate divergence from classic software-doc taxonomies - treating
"assess whether to adopt" as a peer domain - is appropriate and increasingly expected in
an AI/model context.

**Sources:** Diátaxis (diataxis.fr); The Good Docs Project (thegooddocsproject.dev);
ISO/IEC/IEEE 26514:2022 (iso.org/standard/77451.html); IEC/IEEE 82079-1:2019
(iso.org/standard/71620.html); GitLab CTRT (docs.gitlab.com); Kubernetes page content
types; GitHub content model; Microsoft Learn content types; Write the Docs guide; Model
Cards (arXiv 1810.03993); Hugging Face model cards; Model Openness Framework
(arXiv 2403.13784).
