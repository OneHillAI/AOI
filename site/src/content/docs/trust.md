---
title: Why trust this index
description: Who stewards the AI Ownership Index, how every rating is grounded, and the public standards it is built to.
---

You are right to distrust ratings you cannot check. This page explains why this index is different:
every rating traces to a document you can read, the method is public, and the score is built to
recognised standards rather than to opinion.

## The one rule everything rests on

Every claim in an entry must trace to a **primary document that was actually read**, not a marketing
page. Each piece of evidence carries two auditable fields: what kind of document it is, and whether
its text was actually read (`retrieved`). A strong rating cannot rest on a marketing page or an
unread document. Where a document is missing, we record that as a finding rather than leave it
unstated. You can see this on any entry: the **Sources** section lists each document, whether it was
read, and a link.

This is also why the Runware entry says its data terms are weak: we read the binding Terms and
Privacy Policy, and they contradicted the marketing. We report the document, not the brochure.

## Independence

The Index is stewarded by the OneHill Foundation. Ratings are **not for sale** and entries are **not
pay-to-play**. Where a provider or model publisher disputes a rating, they are invited to point at
the primary document that supports their position, and the entry is updated from the read text. See
[GOVERNANCE](https://github.com/OneHillAI/AOI/blob/main/GOVERNANCE.md).

## Standards it is built to

The scoring is grounded on public standards and frameworks, linked below. We follow the same rule we
apply to entries: link the canonical source, and keep a short dated extract where a standard defines
something we use, rather than copying the whole document.

- **[Model Openness Framework](https://arxiv.org/abs/2403.13784)** - the openness-tier taxonomy
  (fully open vs open weights) our tiers mirror.
- **[OSI Open Source AI Definition](https://opensource.org/ai/open-source-ai-definition)** - the bar
  for what counts as open source AI (usable data information, code, and weights).
- **[Stanford Foundation Model Transparency Index](https://crfm.stanford.edu/fmti/)** - transparency
  indicators behind the openness and provenance dimensions.
- **[EU AI Act (Regulation (EU) 2024/1689)](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)** -
  Articles 53 and 55 duties and the systemic-risk compute threshold, shown on each model's EU AI Act
  fact.
- **[NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)** - the
  risk framing behind the safety and governance dimensions.
- **[OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/)** - the deployment risks
  behind the safe-deployment and security guidance.
- **[MITRE ATLAS](https://atlas.mitre.org/)** - the adversarial-ML threat taxonomy behind supply-chain
  and safety.
- **[OpenSSF](https://openssf.org/) and [SLSA](https://slsa.dev/)** - supply-chain integrity and
  build-provenance behind the provenance dimension and format-safety checks.

## Keeping it current

Each entry carries a `last_verified` date and a freshness target. A weekly review ingests newly
gathered primary documents, re-grounds the affected entries, re-runs validation, and reports what
changed and what is still outstanding. The data is validated in continuous integration on every
change, so an entry that does not meet the grounding rule does not ship.

## ownershipindex.ai and GitHub

The reader-facing site is published at **ownershipindex.ai** (the AI Ownership Index). The full source,
the calculations, the methodology, and the primary-source extracts live in the public GitHub
repository, [OneHillAI/AOI](https://github.com/OneHillAI/AOI), which anyone
can inspect or contribute to. The published site is a projection of that repository, so what you read
and what you can audit are the same thing.

Questions or corrections: dev@onehill.org.
