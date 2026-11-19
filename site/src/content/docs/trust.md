---
title: Why trust this index
description: Who stewards the AI Ownership Index, how every rating is grounded, and the public standards it is built to.
---

Every rating traces to a document you can read, the method is public, and the score follows published standards.

## The one rule

Every claim in an entry traces to a primary document that was read, not a marketing page. Each piece of evidence records what kind of document it is and whether its text was read (`retrieved`). A strong rating cannot rest on a marketing page or an unread document, and a missing document is recorded as a finding. The Sources section of every entry lists each document, whether it was read, and a link.

Nebius shows the effect. Its Legal Quick Guide says it does not train on customer content. Its binding Token Factory Supplemental Terms allow it to train smaller speculative-decoding models on inputs and outputs by default, with an opt-out. The entry reports the Terms.

## Independence

The index is stewarded by the OneHill Foundation. Ratings are not for sale and entries are not pay-to-play. A provider or publisher that disputes a rating can point to the primary document that supports its position, and the entry is updated from that text. See [GOVERNANCE](https://github.com/OneHillAI/AOI/blob/main/GOVERNANCE.md).

## Standards it is built to

The scoring is grounded on the public standards and frameworks linked below. Each is linked to its canonical source, with a short dated extract kept where a standard defines something the index uses.

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

Each entry carries a `last_verified` date. An entry past its freshness limit fails validation, and validation runs on every change, so an entry that breaks the grounding rule does not ship. Entries are re-checked against their primary documents on a recurring cycle.

## ownershipindex.ai and GitHub

The site at ownershipindex.ai is generated from the public repository [OneHillAI/AOI](https://github.com/OneHillAI/AOI), which holds the methodology, the calculations and the primary-source extracts. What you read and what you can audit are the same thing.

Questions or corrections: dev@onehill.org.
