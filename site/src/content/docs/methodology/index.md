---
title: Methodology
description: The public, versioned method behind every score, badge, and completeness meter in the library.
---

Every rating here is an **opinion with receipts**. The full method lives in the
[GitHub repository](https://github.com/OneHillAI/AOI/tree/main/methodology); this
page summarises it.

## The AI Ownership Index (AOI)

Each model is scored on **seven weighted dimensions**, each 0-5, rolled into a 0-100
headline and an A-F grade. Trust dimensions deliberately outweigh raw capability - a model
that benchmarks well but can't be trusted, licensed, or run safely is the failure this
library exists to catch.

| Dimension | Weight |
|---|---|
| Openness & Transparency | 0.18 |
| Provenance & Supply-chain Integrity | 0.16 |
| Legal & Regulatory Readiness | 0.16 |
| Safety & Alignment | 0.16 |
| Technical Performance | 0.14 |
| Operational Readiness | 0.12 |
| Maintenance & Governance | 0.08 |

**Hard flags** (e.g. a systemic-risk model with no EU AI Act Article 55 documentation) can
cap a grade regardless of the computed score.

## Two documentation meters

Beyond the trust score, each documentation domain shows:

- **Completeness** - coverage of the expected items for that domain (grounded in accepted
  standards). A documented *gap* counts as addressed-but-empty, not as coverage.
- **OneHill-tested (originality)** - the share of a domain's items OneHill generated or
  verified itself, rather than aggregating from the publisher's own docs.

## Grounded in accepted standards

Scoring and risk: the Model Openness Framework, OSI's Open Source AI Definition, Stanford's
Foundation Model Transparency Index, the EU AI Act (GPAI obligations), NIST AI RMF, OWASP
LLM Top 10, MITRE ATLAS, and OpenSSF model-signing. Documentation structure: Diátaxis,
ISO/IEC/IEEE 26514, and the Good Docs Project. See
[Documentation taxonomy](/methodology/taxonomy/) and
[How we source it](/methodology/provenance/).
