# Nebius (Token Factory) - OneHill Inference-Provider Dossier

> **Score: computed by scripts/score.py** · HQ: Netherlands (Nasdaq-listed) · EU residency: yes, 2 public self-serve regions (shared endpoints not pinned) · Trains on inputs: by default, opt-out available
> Last verified: 2026-09-21
>
> _An independent Cowork browser session (2026-09-21) CONFIRMED VERBATIM this entry's central finding - the binding Terms of Service contradict the marketing claim of "no training on your content." That same session corrected three overstatements (EU-region count, a claimed SLA, and a "dedicated-only" catalogue claim) and strengthened the compliance finding (named SOC 2 auditor)._

**Hard flags:** none

---

## 1. What it serves & how it's priced

Nebius Token Factory (formerly "Nebius AI Studio") serves a ~90-model-variant catalogue -
DeepSeek V4-generation, Kimi K2/K3, Qwen3-235B, Llama 3.x, gpt-oss, GLM-4.5/5.x, NVIDIA Nemotron 3
- over shared per-token endpoints and dedicated single-tenant endpoints. **Correction:** a prior
claim that several flagship models are dedicated-endpoint-only with no public price did not hold
up on re-check - they are publicly served per-token, simply superseded by newer catalogue
entries.

## 2. Data governance - where your prompts go

**The central finding of this entry, confirmed verbatim by an independent Cowork browser session:**
marketing copy claims no training on customer content, but the binding Terms of Service Sec 7
states Inputs/Outputs train Nebius' own "Speculative Decoding" models by default, opt-out
required. This finding survives independent human-grade verification. Zero Data Retention is an
account-level opt-in, not the default.

## 3. Compliance & certifications

SOC 2 Type II - now confirmed with a **named auditor, Deloitte** - covering HIPAA; the ISO 27001
scope statement explicitly names AI Studio (Token Factory itself). A GDPR DPA and CSA STAR
Level 1 are also documented at a published Trust Center - one of the stronger compliance postures
in this library, and now more precisely grounded.

## 4. Residency & sovereignty

**Correction:** only two named EU regions are public/self-serve - Finland and France. Spain and
Iceland are private, existing-deployment-only - a prior draft counted all four as public.
DPA-documented region pinning applies to dedicated/AI-Cloud workloads; shared/public endpoint
processing location "may vary." A US sub-processor entity creates plausible CLOUD Act exposure
alongside the Netherlands-domiciled parent.

## 5. Reliability & lock-in

**Correction: there is no committed inference SLA at all.** A prior draft claimed a real
contractual SLA existed with only the number unconfirmed - this overstated it; the sla-levels
index lists exactly seven non-inference services. The marketed 99.9% figure is marketing-only.
An OpenAI-compatible API over a predominantly open-weight catalogue keeps workloads portable.

## 6. Sources & evidence

See [`entry.yaml`](entry.yaml) for the full evidence list, and
[`docs/primary-sources/nebius/browser-verified/`](../../docs/primary-sources/nebius/browser-verified/)
for the independent Cowork verification pass this dossier is now grounded on.

---

_Scored against [provider rubric v1.2](../../methodology/provider-scoring-rubric.md).
Data: [`entry.yaml`](entry.yaml)._
