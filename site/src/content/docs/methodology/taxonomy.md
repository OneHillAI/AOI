---
title: Documentation taxonomy
description: The two-level structure behind every entry - adopter-journey domains, composed of standards-conformant document types.
---

Every entry is organised in **two levels**: the top level follows the adopter's journey;
inside each domain, content is written as the **standard document types** from Diátaxis,
ISO/IEC/IEEE 26514, and the Good Docs Project.

## The four domains

| Domain | The question it answers | Typical document types |
|---|---|---|
| **Assess** | Should we adopt this? | Explanation, Model-Card intended-use & limitations, evaluation/benchmarks, license & openness, provenance, EU AI Act |
| **Implement** | How do we deploy it? | Quickstart, install/deploy how-tos, hardware/quantization reference, tutorial, fine-tuning |
| **Use** | What can it do and how? | Capabilities & prompt-template reference, task how-tos, concepts |
| **Support** | How do we keep it running? | Troubleshooting, release notes, security disclosure, community |

## Why "Assess" is a first-class domain

Classic software-documentation frameworks (Diátaxis and the tutorial/how-to/reference/
explanation sites) assume you've *already chosen* the tool - they have no "should I adopt
this?" category. But that decision is exactly what the AI/ML **Model Card** tradition
documents (intended use, limitations, evaluation). For a library whose purpose is the
adopt-or-not decision, Assess has to be first-class - a deliberate, well-precedented
extension for models.

The full rationale and cross-framework grounding is in the
[repository](https://github.com/OneHillAI/AOI/blob/main/docs/documentation-taxonomy.md).
