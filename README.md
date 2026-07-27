<div align="center">

<h1>AI Ownership Index</h1>

<p><em>How much do you actually own the open model or inference provider you build on?</em></p>

<p>
<a href="./LICENSE"><img alt="Licence" src="https://img.shields.io/badge/licence-Apache%202.0-0E7382"></a>
<a href="./STANDARD.md"><img alt="Standard" src="https://img.shields.io/badge/standard-v0.1-9A7B1E"></a>
<a href="https://ownershipindex.ai/"><img alt="Docs" src="https://img.shields.io/badge/docs-ownershipindex.ai-1B1E23"></a>
<a href="https://onehill.org"><img alt="Stewarded by OneHill Foundation" src="https://img.shields.io/badge/stewarded%20by-OneHill%20Foundation-9A7B1E"></a>
</p>

</div>

**Maintained by [OneHill](https://onehill.org). Status: v0.1, Foundation. Content baseline: July 2026.**

---

## The question

Adopting an open model, or routing your traffic through a hosted inference API, is an
ownership decision as much as a capability one. Four things decide how much of it is
actually yours:

- **Use and modify it** freely, with no gate and no field-of-use trap.
- **See what it is:** the weights, the training, the behaviour, and the binding terms.
- **Rely on it:** dependable to run and safe to deploy. How *capable* it is shapes the AOI
  score, not this factor - you can fully own a model that is not the most capable.
- **Keep your data yours:** running it does not hand your inputs or your knowledge to
  someone else.

The AI Ownership Index rates every entry on those four factors and resolves them into one
verdict: an ownership **level**, from `full` down through `substantial`, `partial` and
`limited` to `none`. The verdict is floor-weighted, so the weakest factor caps it. A black
box is never "full", however cheap the price.

## Score against verdict

The **AOI score** is a 0 to 100 headline built from seven weighted dimensions, each scored
0 to 5 against a published anchor. It is an analytical input to the ownership verdict, not
the verdict itself. The rubric is public and versioned; see
[methodology/scoring-rubric.md](methodology/scoring-rubric.md) and
[methodology/versioning.md](methodology/versioning.md).

Models are scored on Openness and Transparency, Provenance and Supply-chain Integrity,
Legal and Regulatory Readiness, Safety and Alignment, Technical Performance, Operational
Readiness, and Maintenance and Governance. Inference providers use a parallel set: data
governance, compliance, residency, security, reliability, transparency and lock-in, and
cost. Every rung 0 to 5 is defined for all fourteen dimensions; the exact anchors and the
ownership cutoffs are laid out in the
[classification matrices](https://ownershipindex.ai/classification-matrices/).

## What is in here

| Section | What it documents |
|---|---|
| [`models/`](models/) | One folder per open model: a validated `entry.yaml` plus a four-domain dossier (assess, implement, use, support). |
| [`inference-providers/`](inference-providers/) | APIs that serve open models: retention, training-on-inputs, residency, compliance, and security, read from the binding terms. |
| [`methodology/`](methodology/) | The versioned rubric, the ownership rules, the openness framework, the EU AI Act mapping, and the grounding standard. |
| [`schema/`](schema/) | JSON Schemas that every entry validates against. |
| [`scripts/`](scripts/) | Scoring, completeness, and validation tooling. Scores are derived from the anchors, never hand-typed. |
| [`templates/`](templates/) | Copy-to-start folders for contributing a new entry. |
| [`site/`](site/) | The published site: the library ledger, the entry sheets, compare, and the reference pages. |

## Evidence, not marketing

Every rating traces to a primary document, tagged with which kind it is (`doc_type`) and
whether the text was actually read (`retrieved`). A binding document, a licence, a signed
DPA, or read terms, along with an independent attestation, outranks a claim on a product
page. A dimension scored 5, and any transparency or data-control factor rated strong, must
cite a retrieved binding document or a third-party attestation; a self-reported claim is
marked, dated, and cannot reach the top anchor. CI enforces this on every change. Where a
fact may already have moved, a version, a price, a certification, the entry says so and
dates it.

## The site

The reader-facing index is at [ownershipindex.ai](https://ownershipindex.ai): a ledger of
every entry ranked by AOI, an entry sheet per model and provider that leads with the
ownership verdict, side-by-side [compare](https://ownershipindex.ai/compare/), and reference
pages for the [classification matrices](https://ownershipindex.ai/classification-matrices/)
and the [glossary](https://ownershipindex.ai/glossary/). The site is a projection of this
repository, so what a reader sees and what they can audit are the same thing.

## Contributing and governance

New entries and corrections are welcome by pull request. The rules, the evidence-first
score-change process, and the review requirements are in
[CONTRIBUTING.md](CONTRIBUTING.md); how the project is run is in
[GOVERNANCE.md](GOVERNANCE.md); the prose rules (plain hyphens, British spelling, no filler)
are in [STYLE.md](STYLE.md).

## Scope and honesty

No index can independently re-run every evaluation on every open checkpoint. Where a datum
comes from a publisher or a third party rather than from OneHill's own check, it is marked
as such (`source_type: publisher | third_party | onehill_verified`). A missing document is
recorded as a finding, not papered over. Trust the labels.

---

_This repository is licensed under the **Apache License 2.0**. See [LICENSE](LICENSE) and
[NOTICE](NOTICE). Primary-source extracts under `docs/primary-sources/` remain the property
of their respective publishers._
