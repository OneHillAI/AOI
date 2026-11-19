---
title: Methodology
description: The public, versioned method behind every score, badge, and completeness meter in the library.
---

Every rating is an analytical judgement with its sources shown. The full method is in the
[GitHub repository](https://github.com/OneHillAI/AOI/tree/main/methodology); this page summarises it.

## The AI Ownership Index (AOI)

Each model is scored on seven weighted dimensions, each 0 to 5, rolled into a 0 to 100 headline and an A to F grade. Inference providers use a parallel set of seven dimensions. Trust dimensions outweigh raw capability: a model that benchmarks well but cannot be trusted, licensed or run safely still scores low.

| Dimension | Weight |
|---|---|
| Openness & Transparency | 0.18 |
| Provenance & Supply-chain Integrity | 0.16 |
| Legal & Regulatory Readiness | 0.16 |
| Safety & Alignment | 0.16 |
| Technical Performance | 0.14 |
| Operational Readiness | 0.12 |
| Maintenance & Governance | 0.08 |

Hard flags, such as a systemic-risk model with no EU AI Act Article 55 documentation, cap a grade whatever the computed score.

## Documentation meter

Each documentation domain shows a completeness meter: the coverage of the expected items for that domain. A documented gap counts as addressed and adds nothing to coverage. Entries also record originality, the share of a domain's items OneHill produced itself. It is 0 in every entry today.

## Grounded in accepted standards

Scoring and risk: the Model Openness Framework, OSI's Open Source AI Definition, Stanford's
Foundation Model Transparency Index, the EU AI Act (GPAI obligations), NIST AI RMF, OWASP
LLM Top 10, MITRE ATLAS, and OpenSSF model-signing. Documentation structure: Diátaxis,
ISO/IEC/IEEE 26514, and the Good Docs Project. See
[Documentation taxonomy](/methodology/taxonomy/) and
[How we source it](/methodology/provenance/).
