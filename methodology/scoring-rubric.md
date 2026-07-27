# The AI Ownership Index (AOI) - Scoring Rubric

**Rubric version:** `1.1` · **Baseline:** July 2026

This is the public, versioned rubric behind every score in the registry. It exists so
that scores are **contestable**: if you disagree with a rating, you can point at the
exact criterion and evidence.

---

## 1. Structure

A model is scored on **seven dimensions**. Each dimension is scored **0-5** against
explicit anchors (below). Dimension scores are combined with fixed weights into a
**0-100 headline score** and a **letter grade**.

```
AOI = 100 × Σ(weightᵢ × scoreᵢ / 5)
```

| # | Dimension | Weight |
|---|---|--------|
| 1 | Openness & Transparency | 0.18 |
| 2 | Provenance & Supply-chain Integrity | 0.16 |
| 3 | Legal & Regulatory Readiness | 0.16 |
| 4 | Safety & Alignment | 0.16 |
| 5 | Technical Performance | 0.14 |
| 6 | Operational Readiness | 0.12 |
| 7 | Maintenance & Governance | 0.08 |

> **Weighting rationale.** Trust dimensions (openness, provenance, legal, safety)
> together carry **0.66** - deliberately more than raw capability (0.14). A model
> that benchmarks well but can't be trusted, licensed, or run safely is the exact
> failure mode this registry exists to catch. Weights are versioned; changing them
> bumps the rubric version and triggers a re-score.

### Letter grades

| Grade | Score | Meaning |
|---|---|---|
| **A** | 85-100 | Trustworthy and deployable with standard controls. |
| **B** | 70-84 | Solid; deployable with the noted mitigations. |
| **C** | 55-69 | Usable but with real gaps - read the risks before adopting. |
| **D** | 40-54 | High-caution; significant openness, legal, or safety gaps. |
| **F** | 0-39 | Not recommended without exceptional justification. |

### Hard flags (override the grade)

Some findings are severe enough to **cap** the grade regardless of the computed score.
An entry with any active hard flag cannot exceed the stated ceiling and must display
the flag prominently:

| Flag | Ceiling |
|---|---|
| 🚩 Confirmed malicious / backdoored checkpoint from the primary distribution | **F** |
| 🚩 Weights distributed only as pickle/`.bin` with no safetensors option | **C** |
| 🚩 License prohibits the user's intended use (e.g. commercial use barred) | **C** for that use case |
| 🚩 No identifiable, accountable publisher | **D** |
| 🚩 EU AI Act systemic-risk model with no Article 55 documentation | **C** |

---

## 2. Dimension anchors

Every rung **0-5** is defined for every dimension - there is no interpolated middle;
each score maps to a written anchor a reader can check the evidence against. **Every
score in a published entry must cite evidence.** A score with no evidence is invalid.

### Dimension 1 - Openness & Transparency (weight 0.18)

Graded on the [Openness Framework](openness-framework.md), which grades six
components: weights, training data, training code, evaluation code, documentation,
and license.

| Score | Anchor |
|---|---|
| 0 | Closed weights, or weights available but no meaningful documentation. |
| 1 | Weights downloadable but essentially undocumented and/or under no stated licence - a raw weight dump you cannot safely build on. |
| 2 | **Open-washed / gated**: marketed as "open" but the licence forbids common uses, or a key component is undisclosed, or weights sit behind a restrictive community gate with only a basic model card. |
| 3 | **Open weights** + model card + license, but training data/code not released ("open weight"). |
| 4 | **Open weights + recipe**: weights, training/eval code and thorough docs are open with training data described or partially released (short of a fully reproducible dataset), under a permissive licence. |
| 5 | **Fully open**: weights + training data (or a detailed, reproducible data description) + training & eval code + thorough documentation, under an OSI-approved or equally permissive license. |

### Dimension 2 - Provenance & Supply-chain Integrity (weight 0.16)

Graded on the [Supply-chain Risk Framework](supply-chain-risk.md).

Anchors track the eight-box [checkpoint trust checklist](supply-chain-risk.md#3-checkpoint-trust-checklist).

| Score | Anchor |
|---|---|
| 0 | Anonymous or unverifiable distributor; pickle-only weights; no integrity metadata; known tampered mirrors. (0-1 of 8 boxes.) |
| 1 | Publisher identifiable but not a verified org on the primary host; pickle required or no published checksums; no scanning. (~2 boxes.) |
| 2 | Canonical source identifiable and safetensors offered, but a key control is missing - unverified org, no published checksums, or pickle still required for some artifacts. (~3 boxes.) |
| 3 | Verified publisher org on the primary host; safetensors available; checksums present; re-uploads/quants exist but the canonical source is clear. (~4-5 boxes.) |
| 4 | All of 3 **plus** a malware-scanned checkpoint and/or a documented mirror/quantization policy; safetensors-only or scanned; short only of cryptographic signing. (~6-7 boxes.) |
| 5 | Cryptographically **signed** weights (e.g. sigstore/model-signing) with verifiable provenance (SLSA), safetensors-only or scanned, clear canonical source, and a documented policy for mirrors/quantizations. (8 boxes.) |

### Dimension 3 - Legal & Regulatory Readiness (weight 0.16)

Graded on the [EU AI Act mapping](eu-ai-act-mapping.md) + license analysis.

| Score | Anchor |
|---|---|
| 0 | Restrictive/ambiguous license, no training-data disclosure, no copyright policy, no downstream documentation. Cannot support a compliant deployment. |
| 1 | Licence usable for narrow cases only (research-only or heavy field-of-use limits), with no GPAI documentation and no training-data summary. |
| 2 | Permissive-enough licence for some uses but with material caveats (community licence, scale thresholds, acceptable-use clauses) and only fragmentary GPAI documentation. |
| 3 | Clear permissive-enough license for common uses; publisher provides some GPAI documentation and a training-data summary; caveats exist (acceptable-use clauses, field-of-use limits). |
| 4 | Broadly permissive licence for common uses with a near-complete GPAI documentation package and a public training-data summary; a downstream deployer can assemble most obligations, with one or two residual gaps (e.g. no full training corpus). |
| 5 | OSI-approved or broadly permissive license, complete EU AI Act GPAI documentation package (Annex XI/XII-grade), public training-data summary, copyright policy - a downstream deployer can assemble their obligations from what's provided. |

### Dimension 4 - Safety & Alignment (weight 0.16)

Graded on the [Benchmark & Behaviour methodology](benchmark-methodology.md) safety
sections.

| Score | Anchor |
|---|---|
| 0 | No safety tuning or safety evaluation; trivially elicited harmful behaviour; no misuse policy. |
| 1 | A misuse/acceptable-use policy exists but there is no safety-tuned release and no published safety evaluation; harmful behaviour is still easily elicited. |
| 2 | Safety-tuned release with an acceptable-use policy but only a thin or publisher-only safety evaluation; withstands trivial jailbreaks only; residual risks under-documented. |
| 3 | Safety-tuned release with a published safety evaluation; withstands casual jailbreaks; documented residual risks. |
| 4 | All of 3 **plus** either an independent/third-party safety evaluation or a companion guard/classifier model, with residual-risk disclosure across several harm domains - short of a broad independent red-team. |
| 5 | Independent red-team results available, strong jailbreak resistance, transparent safety evals across CBRN/cyber/child-safety domains, clear residual-risk disclosure, and companion safety tooling (e.g. a guard/classifier model). |

> **Note:** For a base/un-tuned model, "safety" is scored on *honest disclosure of the
> absence of safety tuning* plus the availability of a safety-tuned sibling - not
> penalised to zero for being a research artifact, but never presented as deployable
> as-is.

### Dimension 5 - Technical Performance (weight 0.14)

Independent, reproducible benchmarks + behavioural analysis
([methodology](benchmark-methodology.md)). Scored **relative to the model's own class**
(size / intended use), not absolutely - a 3B model is judged against 3B peers.

| Score | Anchor |
|---|---|
| 0 | Fails basic capability checks for its class; benchmark claims not reproducible. |
| 1 | Below its class on independent evaluation; publisher claims largely fail to reproduce. |
| 2 | Roughly mid-pack for its class, with some reproducibility gaps or only thin independent coverage. |
| 3 | Competitive within its class on independent re-runs; publisher claims broadly reproduce. |
| 4 | Toward the top of its class on independent evaluation across several domains, reproducible with no contamination evidence - short of class-leading or of OneHill-reproduced results. |
| 5 | Class-leading on independent evaluation across multiple domains, with reproducible results and no evidence of benchmark contamination. |

### Dimension 6 - Operational Readiness (weight 0.12)

| Score | Anchor |
|---|---|
| 0 | No practical path to run it; unsupported by common serving stacks; undocumented hardware needs. |
| 1 | Runs only via bespoke/publisher code; no mainstream-runtime support; hardware needs largely undocumented. |
| 2 | Runs on at least one mainstream stack but with gaps - few or no quantizations, sparse hardware guidance, or day-N (not day-0) availability. |
| 3 | Runs on mainstream stacks (vLLM/llama.cpp/TGI/Ollama), quantizations available, hardware requirements documented. |
| 4 | Broad support across the serving ecosystem with community or official quantizations and documented hardware/scaling guidance - short of first-class day-0 support and an official quantization program. |
| 5 | First-class support across the serving ecosystem, official quantizations, clear scaling/hardware guidance, long-context/tooling support documented, day-0 ecosystem availability. |

### Dimension 7 - Maintenance & Governance (weight 0.08)

| Score | Anchor |
|---|---|
| 0 | Abandoned; no security contact; no update history; unaccountable publisher. |
| 1 | Identifiable publisher but no update track record and no way to report issues. |
| 2 | Some release history but irregular, with only a limited or informal issue-reporting path and no security process. |
| 3 | Active publisher with a track record; occasional updates; a way to report issues. |
| 4 | Reputable, accountable publisher with a predictable cadence and a documented issue/security-reporting path - short of a formal signed vulnerability-disclosure process or a deprecation policy. |
| 5 | Reputable, accountable publisher; predictable release cadence; documented security-response/vulnerability-disclosure process; deprecation policy. |

---

## 3. Evidence & sourcing rules

Every datum in an entry carries a `source_type`:

- `onehill_verified` - OneHill independently reproduced/observed it (ran the model,
  verified the signature, re-ran the benchmark).
- `third_party` - from an independent source (a benchmark org, a security vendor, a
  regulator), cited by URL.
- `publisher` - from the model publisher; treated as a claim, not a fact.

A dimension may not be scored **5** on `publisher`-only evidence. Independent
verification (`onehill_verified` or `third_party`) is required for the top anchor.

## 4. Re-scoring triggers

An entry is re-scored when any of these occur (all logged in the entry's changelog):

- A new checkpoint / version is released.
- The license or distribution terms change.
- A security incident, malicious-mirror finding, or CVE is reported.
- New independent benchmark or red-team results are published.
- The rubric version changes.
- `last_verified` exceeds the freshness SLA (see
  [`update-automation.md`](update-automation.md)).

## 5. Provider scoring

Inference and hosting providers use an **adapted rubric** with dimensions:
Data Governance & Privacy · Compliance & Certifications · Provenance & Integrity ·
Security Posture · Reliability & SLA · Transparency & Lock-in · Cost. Anchors are
defined in [`provider-scoring-rubric.md`](provider-scoring-rubric.md).

---

_Changelog for this rubric lives at the bottom of the file and bumps the version on
every anchor or weight change._

### Rubric changelog
- **1.1** (2026-07) - Defined every rung 0-5 for all seven dimensions (previously only
  0/3/5 were anchored and 1/2/4 interpolated). Weights and grade cutoffs unchanged, so
  headline arithmetic is identical; the added anchors make each in-between score
  checkable and trigger a re-score of every entry (§4).
- **1.0** (2026-07) - Initial public rubric.
