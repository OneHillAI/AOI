# Nebius (Token Factory) - OneHill Inference-Provider Dossier

> **Score: computed by scripts/score.py** · HQ: Netherlands (Nasdaq-listed) · EU residency: two documented Token Factory data-plane regions (Finland, France); dedicated endpoints pinned, public endpoints not · Trains on inputs: by default, opt-out available
> Last verified: 2026-11-19
>
> _Re-verified 2026-11-19 against the live Services Agreement, Token Factory Supplemental Terms, DPA, sub-processor list, trust centre, SOC 3 report, ISO 27001 certificate, regions, SLA, status and the browser-rendered catalogue. The binding training clause survived a change of governing contract and still contradicts the Legal Quick Guide; compliance is now backed by two read third-party artefacts._

**Hard flags:** none

---

## 1. What it serves & how it's priced

Nebius Token Factory (formerly "Nebius AI Studio") lists 133 models (DeepSeek V4 generation, Kimi
K3 and K3.1 Pro, GLM-5.x, MiniMax M3, Qwen3.x, gpt-oss, Nemotron 3.x, Llama 3.x) over shared
per-token endpoints and dedicated single-tenant endpoints. Public prices are shown per model;
several models that were priced publicly in September (DeepSeek-V4-Pro, Llama-3.3-70B-Instruct)
are now dedicated-only after Serverless removal notices.

## 2. Data governance - where your prompts go

**The central finding of this entry, re-read verbatim:** the Legal Quick Guide says no training on
your content, but the binding Supplemental Terms Sec 5.1(b) (effective 2026-10-22) let Nebius use
Input and Output to "train smaller Models used for Speculative Decoding" by default, opt-out by
onboarding form or e-mail. Zero Data Retention is an account-level opt-in.

## 3. Compliance & certifications

A public Deloitte SOC 3 report (clean opinion, AI Studio inference in scope) and an ISO/IEC
27001:2022 certificate from SII-QCD were read in full, alongside a trust centre that lists SOC 2
Type II with HIPAA (NDA), ISO 27701 and 42001, CSA STAR Level 1 and a GDPR DPA. This lifts the
compliance score from 4 to 5; the SOC 2 report itself stays NDA-gated.

## 4. Residency & sovereignty

Token Factory documents two EU data-plane regions, Finland and France; the wider Nebius AI Cloud
now lists four public EU region IDs, but no Token Factory document names the extra two. DPA 6.1
pins dedicated endpoints to the region you select; public endpoints are "Global", not pinned, and
showed processing in Finland, the UK and the US on the day read. Your contracting entity is Nebius
B.V., Nebius Israel Ltd or Nebius Inc. by place of incorporation, and US sub-processors make CLOUD
Act exposure plausible.

## 5. Reliability & lock-in

There is no inference SLA: Supplemental Terms 7.4 expressly excludes service level commitments,
uptime guarantees and credits unless agreed in writing, and the SLA index lists no inference
service. Two Token Factory incidents fall in the status page's 14-day window. An OpenAI-compatible
API over a predominantly open-weight catalogue keeps workloads portable.

## 6. Sources & evidence

See [`entry.yaml`](entry.yaml) for the full evidence list,
[`docs/primary-sources/nebius/`](../../docs/primary-sources/nebius/) for the 2026-11-19 extracts
and [`docs/primary-sources/nebius/browser-verified/`](../../docs/primary-sources/nebius/browser-verified/)
for the independent September verification pass.

---

_Scored against [provider rubric v1.2](../../methodology/provider-scoring-rubric.md).
Data: [`entry.yaml`](entry.yaml)._
