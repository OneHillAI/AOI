# Governance

The AI Ownership Index is stewarded by the OneHill Foundation. Contact: dev@onehill.org.

## Principles

The Index is a public-interest reference. It favours evidence over opinion, records its
sources, and treats a missing document as a finding rather than a gap to paper over. Ratings
are reproducible: anyone with the cited primary documents should be able to reach the same
verdict.

**Verification over self-report.** A rating may not rest on a vendor's own marketing where a
binding document or an independent attestation can be obtained. A dimension scored 5, and any
transparency or data-control factor rated strong, must trace to a retrieved binding document or
a third-party attestation, not a product page. The grounding gate in CI enforces this.

**Versioned method.** The scoring methodology is semantically versioned and every entry stamps
the version it was scored under, so a rating is always readable against the exact rules that
produced it (see [methodology/versioning.md](methodology/versioning.md)).

## Roles

- Maintainers: review contributions, run the grounding gate, and publish entries. Maintainers
  are appointed by the OneHill Foundation.
- Contributors: anyone who gathers primary documents, drafts or corrects entries, or improves
  tooling, via pull request.
- Stewards: the OneHill Foundation holds final responsibility for the standard, the release
  process, and conflict resolution.

## Decision process

Every change lands through a pull request; nothing is pushed straight to `main`. A merge needs
a green CI run and at least one maintainer approval, with code-owner review required on the
load-bearing paths (see [.github/CODEOWNERS](.github/CODEOWNERS) and the review rules in
[CONTRIBUTING.md](CONTRIBUTING.md)). Routine changes (new entries, new evidence, corrections)
proceed by maintainer review and merge. Changes to the standard itself (dimensions, doc_type
vocabulary, the grounding gate) are proposed as a pull request against STANDARD.md, open for
comment for at least two weeks, and require maintainer consensus. The version is incremented
per STANDARD.md.

## Changes and disputes

Corrections are welcome by pull request or by email to dev@onehill.org. Where a provider or
model publisher disputes a rating, they are invited to point at the primary document that
supports their position; the entry is updated from the read text.

## Review cadence

A weekly review ingests newly gathered primary documents, re-grounds the affected entries,
re-runs validation, and reports what changed and what is still outstanding.
