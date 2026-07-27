---
title: Classification matrices
description: The exact 0-5 rungs behind every dimension score, and the rules that turn them into an ownership verdict - so any rating can be checked against the evidence.
---

Every score in this index maps to a **written rung** you can check the evidence against. Nothing
is interpolated or set by feel: pick the rung whose description the entry meets, and cite the
document that shows it. This page is the full set of matrices - the dimension anchors and the
ownership rules - so you can contest any rating by pointing at the exact criterion.

The rubric behind this page is versioned; these matrices are **rubric 1.1**. When an anchor or a
weight changes, the version bumps and every entry is re-scored.

## How a score is built

A model is scored on **seven dimensions**, each **0-5** against the anchors below. The dimension
scores combine with fixed weights into a **0-100 headline** and a **letter grade**:

```
AOI = 100 × Σ(weightᵢ × scoreᵢ / 5)
```

| # | Model dimension | Weight |
|---|---|--------|
| 1 | Openness & Transparency | 0.18 |
| 2 | Provenance & Supply-chain Integrity | 0.16 |
| 3 | Legal & Regulatory Readiness | 0.16 |
| 4 | Safety & Alignment | 0.16 |
| 5 | Technical Performance | 0.14 |
| 6 | Operational Readiness | 0.12 |
| 7 | Maintenance & Governance | 0.08 |

Trust dimensions (openness, provenance, legal, safety) carry **0.66** together - deliberately more
than raw capability (0.14). A `5` on any dimension needs independent evidence (OneHill-verified or
third-party); publisher marketing alone caps a dimension at `3`.

| Grade | Score | Meaning |
|---|---|---|
| **A** | 85-100 | Trustworthy and deployable with standard controls. |
| **B** | 70-84 | Solid; deployable with the noted mitigations. |
| **C** | 55-69 | Usable but with real gaps - read the risks first. |
| **D** | 40-54 | High-caution; significant openness, legal or safety gaps. |
| **F** | 0-39 | Not recommended without exceptional justification. |

Some findings **cap** the grade regardless of the computed score - a confirmed malicious checkpoint
(F), pickle-only weights with no safetensors option (C), a licence that bars the intended use (C
for that use), no accountable publisher (D), or a systemic-risk model with no Article 55
documentation (C).

## Model dimension anchors (0-5)

### 1 · Openness & Transparency

Graded on the openness framework, whose tier sets the ceiling (open-weights caps at 3, open-weights
+ recipe at 4, fully open at 5).

| Score | Anchor |
|---|---|
| 0 | Closed weights, or weights available but no meaningful documentation. |
| 1 | Weights downloadable but essentially undocumented and/or under no stated licence - a raw weight dump. |
| 2 | Open-washed / gated: marketed as "open" but the licence forbids common uses, a key component is undisclosed, or weights sit behind a restrictive community gate with only a basic model card. |
| 3 | Open weights + model card + licence, but training data/code not released. |
| 4 | Open weights + recipe: weights, training/eval code and thorough docs open, training data described or partially released, under a permissive licence. |
| 5 | Fully open: weights + training data (or a reproducible description) + training & eval code + thorough docs, under an OSI-approved or equally permissive licence. |

### 2 · Provenance & Supply-chain Integrity

Tracks the eight-box checkpoint trust checklist (verified org, safetensors, checksums, signature,
provenance attestation, no malicious mirror, pinned loader, malware scan).

| Score | Anchor |
|---|---|
| 0 | Anonymous/unverifiable distributor; pickle-only; no integrity metadata; tampered mirrors. (0-1 boxes.) |
| 1 | Publisher identifiable but not a verified org; pickle required or no checksums; no scanning. (~2 boxes.) |
| 2 | Canonical source identifiable and safetensors offered, but a key control missing - unverified org, no checksums, or pickle for some artifacts. (~3 boxes.) |
| 3 | Verified org on the primary host; safetensors + checksums; canonical source clear. (~4-5 boxes.) |
| 4 | All of 3 plus a scanned checkpoint and/or a documented mirror/quantization policy; short only of signing. (~6-7 boxes.) |
| 5 | Cryptographically signed weights with verifiable provenance (SLSA), safetensors-only or scanned, documented mirror policy. (8 boxes.) |

### 3 · Legal & Regulatory Readiness

| Score | Anchor |
|---|---|
| 0 | Restrictive/ambiguous licence, no data disclosure, no copyright policy, no downstream docs. |
| 1 | Licence usable for narrow cases only (research-only or heavy field-of-use), no GPAI documentation, no training-data summary. |
| 2 | Permissive-enough for some uses but with material caveats (community licence, scale thresholds, acceptable-use) and only fragmentary GPAI documentation. |
| 3 | Clear permissive-enough licence for common uses; some GPAI documentation and a training-data summary; caveats exist. |
| 4 | Broadly permissive with a near-complete GPAI package and a public training-data summary; most obligations assemblable, with one or two residual gaps (e.g. no full corpus). |
| 5 | OSI-approved/broadly permissive, complete EU AI Act GPAI package (Annex XI/XII-grade), public training-data summary, copyright policy. |

### 4 · Safety & Alignment

| Score | Anchor |
|---|---|
| 0 | No safety tuning or evaluation; trivially elicited harm; no misuse policy. |
| 1 | A misuse policy exists but no safety-tuned release and no published evaluation; harm easily elicited. |
| 2 | Safety-tuned release with an acceptable-use policy but only a thin or publisher-only evaluation; withstands trivial jailbreaks only. |
| 3 | Safety-tuned release with a published evaluation; withstands casual jailbreaks; documented residual risks. |
| 4 | All of 3 plus an independent/third-party evaluation or a companion guard model, with residual-risk disclosure across several harm domains. |
| 5 | Independent red-team results, strong jailbreak resistance, transparent evals across CBRN/cyber/child-safety, clear residual-risk disclosure, companion safety tooling. |

### 5 · Technical Performance

Scored relative to the model's own class (size / intended use), not absolutely.

| Score | Anchor |
|---|---|
| 0 | Fails basic capability checks for its class; claims not reproducible. |
| 1 | Below its class on independent evaluation; publisher claims largely fail to reproduce. |
| 2 | Roughly mid-pack for its class, with reproducibility gaps or thin independent coverage. |
| 3 | Competitive within its class on independent re-runs; publisher claims broadly reproduce. |
| 4 | Toward the top of its class on independent evaluation, reproducible, no contamination - short of class-leading or OneHill-reproduced. |
| 5 | Class-leading on independent evaluation across domains, reproducible, no contamination. |

### 6 · Operational Readiness

| Score | Anchor |
|---|---|
| 0 | No practical path to run it; unsupported by common stacks; undocumented hardware needs. |
| 1 | Runs only via bespoke/publisher code; no mainstream-runtime support; hardware needs undocumented. |
| 2 | Runs on at least one mainstream stack but with gaps - few/no quantizations, sparse hardware guidance, or day-N availability. |
| 3 | Runs on mainstream stacks (vLLM/llama.cpp/TGI/Ollama), quantizations available, hardware documented. |
| 4 | Broad ecosystem support with quantizations and hardware/scaling guidance - short of first-class day-0 support and an official quantization programme. |
| 5 | First-class support across the ecosystem, official quantizations, scaling guidance, long-context/tooling support, day-0 availability. |

### 7 · Maintenance & Governance

| Score | Anchor |
|---|---|
| 0 | Abandoned; no security contact; no update history; unaccountable publisher. |
| 1 | Identifiable publisher but no update track record and no way to report issues. |
| 2 | Some release history but irregular, with a limited/informal issue path and no security process. |
| 3 | Active publisher with a track record; occasional updates; a way to report issues. |
| 4 | Reputable, accountable publisher with a predictable cadence and a documented issue/security path - short of a formal signed disclosure process or deprecation policy. |
| 5 | Reputable publisher; predictable cadence; documented security-response/disclosure process; deprecation policy. |

## Inference-provider dimension anchors (0-5)

Providers are services you route data through, so they are scored on an adapted rubric that
weights data governance and lock-in over raw capability.

| # | Provider dimension | Weight |
|---|---|--------|
| 1 | Data Governance & Privacy | 0.24 |
| 2 | Compliance & Certifications | 0.18 |
| 3 | Data Residency & Sovereignty | 0.16 |
| 4 | Security Posture | 0.14 |
| 5 | Reliability & SLA | 0.12 |
| 6 | Transparency & Lock-in | 0.10 |
| 7 | Cost & Value | 0.06 |

### 1 · Data Governance & Privacy

| Score | Anchor |
|---|---|
| 0 | Retains and may train on inputs by default; no ZDR; opaque sub-processors. |
| 1 | Retains inputs by default; training-on-inputs unclear; no ZDR; sub-processors undocumented. |
| 2 | No training claimed, but retention is the default with only a limited opt-out; ZDR unavailable/unclear; partial sub-processor disclosure. |
| 3 | No training by default; ZDR available; retention documented; some caveats (free-tier logs, third-party routing). |
| 4 | Contractually no training; short bounded retention or ZDR by default on paid tiers; sub-processors disclosed; routing clear - short of zero-retention-by-default. |
| 5 | Zero retention by default, contractually no training, ZDR verifiable, sub-processors disclosed, routing leakage flagged. |

### 2 · Compliance & Certifications

| Score | Anchor |
|---|---|
| 0 | None documented / no trust page. |
| 1 | Security/privacy claims on a marketing surface only; no third-party certification and no DPA. |
| 2 | A DPA is available and one certification is in progress or self-attested (e.g. SOC 2 Type I), but no completed independent audit. |
| 3 | SOC 2 Type II or ISO 27001, GDPR/DPA available. |
| 4 | Two of {SOC 2 Type II, ISO 27001, HIPAA/BAA} - or two independent attestations (e.g. ISO 27001 + CSA STAR) - plus GDPR/DPA; short of the full HIPAA + ISO 27701 + trust-centre set. |
| 5 | SOC 2 Type II and ISO 27001/27701, HIPAA/BAA where relevant, published trust centre. |

### 3 · Data Residency & Sovereignty

| Score | Anchor |
|---|---|
| 0 | Single-region (typically US), no residency options. |
| 1 | Multi-region for latency only, no residency guarantee or region pinning. |
| 2 | An EU region for some workloads but without pinning guarantees or a documented data boundary. |
| 3 | EU region available for at least some workloads. |
| 4 | EU/sovereign residency with region pinning for the main workloads and a documented data boundary - short of sovereign guarantees across all services. |
| 5 | EU/sovereign residency with region pinning and documented data-boundary guarantees; CLOUD-Act exposure disclosed. |

### 4 · Security Posture

| Score | Anchor |
|---|---|
| 0 | No documented isolation, encryption or access control; no pen-testing; unresolved incidents. |
| 1 | Basic encryption asserted, but no isolation model, access-control detail or testing disclosed. |
| 2 | Encryption in transit and at rest plus stated access controls, but no independent pen-test and a thin isolation story. |
| 3 | Documented tenant isolation, encryption, RBAC and periodic penetration testing. |
| 4 | All of 3 plus independent pen-test attestation or a bug-bounty programme, and a clean/well-handled incident history. |
| 5 | Independently audited posture, regular third-party pen-testing/bug bounty, and a transparent incident-response record. |

### 5 · Reliability & SLA

| Score | Anchor |
|---|---|
| 0 | Not yet in production; no status page, no uptime record; opaque incident communication. |
| 1 | Best-effort only; no status page and no operational track record. |
| 2 | Serving in production but with no status page or published uptime history, and no SLA. |
| 3 | An operational track record with a public status page and documented incident communication (SLA may be informal/absent). |
| 4 | Contractual SLA with credits, a solid public uptime record, documented failover/redundancy - short of a long multi-year record. |
| 5 | Strong contractual SLA with credits, a long verifiable uptime record, documented multi-region failover, transparent incident communication. |

### 6 · Transparency & Lock-in

| Score | Anchor |
|---|---|
| 0 | Proprietary API, custom silicon, no portability, opaque routing. |
| 1 | Proprietary API with some docs but no open-model portability and unclear routing. |
| 2 | OpenAI-compatible surface but a largely proprietary catalogue, or an opaque sub-processor/routing story. |
| 3 | OpenAI-compatible API, standard open models, portable. |
| 4 | OpenAI-compatible over open models with transparent routing and a documented exit path - short of full sub-processor transparency. |
| 5 | Fully portable (open models + open API), transparent routing/sub-processors, clear exit path. |

### 7 · Cost & Value

| Score | Anchor |
|---|---|
| 0 | Pricing undisclosed or quote-only; no way to estimate spend before committing. |
| 1 | Headline pricing shown but with material hidden costs (egress, minimums, opaque dedicated pricing). |
| 2 | Public per-token pricing but limited tier/quota transparency, or above-market rates for the class. |
| 3 | Clear public pricing that is broadly competitive for the class, with documented tiers. |
| 4 | Clear, competitive pricing with a transparent dedicated/serverless breakdown and no surprise fees. |
| 5 | Fully transparent, competitive pricing across serverless and dedicated, with predictable cost controls and no hidden fees. |

## The ownership verdict

The AOI grade tells you how open and well-governed a thing is; the **ownership verdict** answers a
single question - *do you really own it?* It is built from four factors, each rated **strong /
moderate / weak**, and it is **floor-weighted**: a weakness in any one factor caps the whole,
because ownership is a conjunction, not an average.

### The four factors and their rules

Each factor is set by a rule with explicit cutoffs, so two assessors reach the same rating. Where
the primary documents have been read, they override the rule - the rule is the floor, the
documents are the ceiling.

**Use & modify freely** (licence + field-of-use + trainability, checked per variant)

| Level | Rule |
|---|---|
| strong | OSI/permissive-open licence, ungated, no field-of-use limit, weights fine-tunable. |
| moderate | Community licence with restrictions (acceptable-use, scale thresholds, brand terms), or a licence-split family. |
| weak | Research-only / non-commercial / commercial-prohibited, a hard gate, or not meaningfully modifiable. |

**Transparency - you know what it is** (openness tier; for a provider, the read Terms/DPA/Privacy)

| Level | Rule |
|---|---|
| strong | Fully open or open-weights + recipe; for a provider, binding terms published and legible. |
| moderate | Open weights (data/code closed); for a provider, terms published but with gaps. |
| weak | Open-washed/closed, opaque training with no legible terms - a black box. |

**Reliability** (the operational and safety scores. Raw performance is scored elsewhere, in the AOI score; this factor asks only whether you can run the model and control its misuse)

| Level | Rule |
|---|---|
| strong | Operational ≥ 4 and safety ≥ 4 (dependable to run, and misuse genuinely controlled). |
| moderate | Operational = 3, or safety = 3 (runnable and deployable, but a safety gap you must fill: lighter alignment, unbenchmarked misuse, no guard model, censorship distortion). |
| weak | Operational ≤ 2 (cannot run it dependably) or safety ≤ 2 (unsafe as presented). A low performance score never touches this factor. |

**Doesn't extract your data** (self-hosting for a model; the read data terms for a provider)

| Level | Rule |
|---|---|
| strong | Self-hosted with no phone-home/clawback; or a provider that contractually never trains, offers zero-retention/ZDR by default and lets you keep data and IP. |
| moderate | No training by default but with retention or only opt-in ZDR, or unclear residency; or a self-hosted licence that claws back some rights. |
| weak | A provider that may use/retain inputs or trains by default; or a model that phones home. |

### From factors to a level

| Overall level | Rule |
|---|---|
| **full** | All four factors strong. |
| **substantial** | Strong on use-&-modify and data-control, no factor weak (one or two moderate). |
| **partial** | Exactly one factor weak; or use-&-modify or data-control only moderate; or transparency moderate with real unknowns. |
| **limited** | Two factors weak. |
| **none** | Three or more weak, or a closed black box you can neither see nor modify. |

A black box can never be "full" however cheap; a model that fails you, or a provider that may train
on your inputs, can never be "full". A factor rated **strong** on transparency or data-control must
trace to a **retrieved binding document**, never a marketing page - a rule the tooling enforces.

## Where the full method lives

These matrices are summarised from the versioned rubric in the
[GitHub repository](https://github.com/OneHillAI/AOI/tree/main/methodology):
the [model scoring rubric](https://github.com/OneHillAI/AOI/blob/main/methodology/scoring-rubric.md),
the [provider scoring rubric](https://github.com/OneHillAI/AOI/blob/main/methodology/provider-scoring-rubric.md)
and the [ownership method](https://github.com/OneHillAI/AOI/blob/main/methodology/ownership.md).
