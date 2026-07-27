# Contributing

This registry is **data-first**: an entry is a validated `entry.yaml` plus a human
`README.md` dossier generated from and kept consistent with it. Contributions are how
coverage grows and how the registry stays current.

## Adding an entry

1. **Pick the type** and copy the matching template folder:
   - a model → copy [`templates/model/`](templates/model/) to `models/<id>/`
   - an inference provider → copy [`templates/inference-provider/`](templates/inference-provider/) to `inference-providers/<id>/`
   - a hosting provider → copy [`templates/hosting-provider/`](templates/hosting-provider/) to `hosting-providers/<id>/`
2. **Fill in `entry.yaml`.** Read the relevant [`methodology/`](methodology/) docs first
   - the anchors tell you how to score each dimension. Every non-trivial claim needs an
   `evidence` entry with a `source_type` and URL.
3. **Score it.** Set each dimension's `score` (0-5) with a one-line `rationale` and
   `evidence_refs`. Then compute the headline/grade:
   ```bash
   python scripts/score.py --write models/<id>/entry.yaml
   ```
4. **Write the dossier** (`README.md`) so its score block, tables, and flags match the
   data file, and add the independent prose analysis.
5. **Validate.**
   ```bash
   pip install -r requirements.txt
   python scripts/validate.py models/<id>
   ```
6. Open a PR.

## The rules that CI enforces

- **Schema.** `entry.yaml` must validate against `schema/`.
- **Evidence.** A dimension scored **5** must cite at least one `onehill_verified` or
  `third_party` evidence reference - publisher marketing alone can't justify the top
  anchor.
- **Score consistency.** The stored `headline`/`grade` must equal what `score.py`
  computes from the dimensions and hard flags.
- **Freshness.** `last_verified` must be within the entry's fast-moving SLA (default
  30 days). Stale entries fail - that's intentional.

## Changing a score, rating or level

A change to any dimension score, ownership-factor rating, or ownership level is
evidence-first, in this order:

1. Read the primary document that motivates the change and add it to the entry's `evidence`
   with its `doc_type`, `retrieved: true`, the `url`, and the `date` you read it.
2. Update the affected `dimensions.<key>.score` with a one-line `rationale` and
   `evidence_refs` pointing at that evidence.
3. Recompute the headline and grade: `python scripts/score.py --write <path>/entry.yaml`.
   Scores are derived, never hand-typed, and CI fails if a stored value disagrees.
4. If the change crosses an ownership-factor cutoff, update `ownership.factors` and the
   `ownership.verdict` to match, per [`methodology/ownership.md`](methodology/ownership.md).
5. Record the change in [`CHANGELOG.md`](CHANGELOG.md) under Unreleased.
6. Open a pull request that links the primary document. A maintainer confirms the cited text
   actually supports the new score before merge; a score change without a readable source is
   not merged.

## Verification over self-report

A rating may not rest on a vendor's own marketing where a binding document or an independent
attestation can be obtained. Read terms, a signed DPA, a licence file, or a third-party audit
outrank a claim on a product page. A dimension scored **5**, and any transparency or
data-control factor rated **strong**, must cite a **retrieved binding document** or a
**third-party** attestation; a self-reported claim is marked as such, dated, and cannot reach
the top anchor. CI enforces this (`check_grounding`); the `retrieved` flag on every evidence
item is the record of whether the document was actually read.

## Review and merge

Every change lands through a pull request; nothing is pushed straight to `main`. To merge, a
PR needs a green CI run (data validation, the no-dashes/no-slop docs lint, and the site build)
and at least one maintainer approval. The load-bearing paths (`methodology/`, `schema/`,
`scripts/`, and the entry trees) have named reviewers in
[`.github/CODEOWNERS`](.github/CODEOWNERS) whose review is required for changes there. This is
enforced by a branch-protection rule on `main` that requires a pull request, requires those
status checks, and requires review from code owners. Those are repository settings a maintainer
enables once.

## YAML gotcha (quote your yes/no)

YAML 1.1 reads bare `yes`, `no`, `on`, `off` as **booleans**. Several enum fields take
the *string* `"yes"`/`"no"`/`"unknown"` (e.g. a provider's `iso_27001`, a model's
`article_55_docs_available`). Always **quote** those values - `iso_27001: "yes"` - or
schema validation will reject the coerced boolean. `score.py --write` patches only the
computed `headline`/`grade` lines in place, so it will not touch or corrupt your other
fields.

## Sourcing standard

- Tag every datum: `onehill_verified` (we ran/observed it), `third_party` (independent
  source, cited), or `publisher` (a claim, not a fact).
- Also tag each evidence item's `doc_type` (`terms | privacy_policy | dpa | license |
  model_card | technical_report | security | docs | marketing | third_party` …) and
  whether the document was actually read (`retrieved: true|false`). A binding document
  (terms/privacy/DPA/license) beats a marketing page; `retrieved: false` may back only a
  "documented but unverified" statement - and the prose must say so.
- A dimension scored **5** (and any ownership factor rated **strong** on transparency or
  data-control) must cite a **retrieved binding document** or a **third-party** attestation -
  never marketing, never an unread doc. CI enforces this (`check_grounding`).
- Prefer primary sources (the license file, the hub page, the trust centre, the
  regulation text, the CVE) over secondary summaries.
- Where the fast-moving landscape means a fact may already have changed (a version, a
  price, a cert), say so and date it.
- The full standard, the document inventory, and the retrieval routes are in
  [`methodology/primary-source-grounding.md`](methodology/primary-source-grounding.md) and
  [`methodology/ownership.md`](methodology/ownership.md).

## Editing the methodology

The rubric is meant to be contested. Propose changes to [`methodology/`](methodology/)
via PR with a rationale. Changing an anchor, a weight, or an ownership-factor cutoff is a
**version bump** and requires re-scoring the affected entries in the same change. The
versioning scheme, and the current rubric version, are in
[`methodology/versioning.md`](methodology/versioning.md).

## Tone

Independent, sourced, and honest about uncertainty. We document what publishers don't -
risks and gaps included - but we never overstate. No claim without a receipt. Lead with the
decision, be concrete and conclusive, and cut AI/LLM filler - the full rules and the banned
phrase list are in [`STYLE.md`](STYLE.md).

## Licensing of contributions

By contributing you agree your contributions are licensed under the **Apache License 2.0**
(see [`LICENSE`](LICENSE) and [`NOTICE`](NOTICE)).
