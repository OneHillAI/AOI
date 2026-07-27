# Together AI - OneHill Inference-Provider Dossier

> **Score: 75.2/100 · Grade B** · HQ: United States · EU residency: yes (gated) · Trains on inputs: opt-in only, off by default
> Last verified: 2026-07-25
>
> _Right for teams wanting a broad open-model catalogue with strong default privacy; the biggest caveat is that EU residency and region pinning are reserved for Scale/Enterprise tiers._

**Hard flags:** none

---

## At a glance

| Dimension | Score | One-line reason |
|---|---|---|
| Data Governance & Privacy | 4/5 | No retention by default, training opt-in and off - but self-documented |
| Compliance & Certifications | 4/5 | SOC 2 Type II confirmed; ISO 27001 unconfirmed, HIPAA indicated |
| Data Residency & Sovereignty | 4/5 | EU data centres (incl. Sweden), but gated to higher tiers |
| Security Posture | 4/5 | Encryption + audit logging consistent with SOC 2 Type II |
| Reliability & SLA | 3/5 | No incidents surfaced, but no public SLA verified |
| Transparency & Lock-in | 5/5 | OpenAI-compatible API + fully portable open models |
| Cost & Value | 4/5 | Competitive serverless rates plus dedicated GPU endpoints |

## 1. What it serves & how it's priced

Together AI is a US-headquartered inference provider running on NVIDIA GPUs. It serves one of the broadest open catalogues in the market: Llama 3.x and 4, DeepSeek V3/R1, Qwen3 up to 235B, Mistral/Mixtral, gpt-oss 20B/120B, plus embedding and image models. Pricing is mixed - per-token serverless for on-demand use, and dedicated GPU endpoints on the Scale and Enterprise tiers. Example serverless rates (third-party, approximate and fast-moving) include gpt-oss-120B at roughly $0.15/$0.60 per million in/out tokens, Qwen3-235B near $0.20/$0.60, and DeepSeek-V3 around $1.25/M.

## 2. Data governance - where your prompts go

Together documents that it does not store inputs or outputs by default, with only temporary caching for performance. Zero-data-retention is described as the default posture, and training on customer data is opt-in and off by default. Because the catalogue is entirely open-weight, there is no closed third-party model routing, so no other vendor's data terms attach to inference. The main caveats: this posture is self-documented on Together's own pages rather than independently attested, and a formal sub-processor list was not confirmed.

## 3. Compliance & certifications

SOC 2 Type II is confirmed via Together's compliance announcement. GDPR/DPA coverage is available through EU residency. HIPAA/BAA support is indicated - encryption, audit logging, and BAA references appear - but this reads as indicated rather than a formal attestation we could verify, so treat it as unconfirmed until a BAA is in hand. ISO 27001 is unconfirmed. Trust materials sit at the privacy page.

## 4. Residency & sovereignty

EU data centres are available for both inference and storage, including Sweden GPU capacity, with enterprise region pinning. The material limitation is tiering: EU and dedicated endpoints are restricted to Scale/Enterprise customers, so serverless free/standard users do not get EU residency by default.

**CLOUD Act disclosure:** As a US-headquartered provider, Together is subject to US jurisdiction, including the CLOUD Act, even for data hosted in EU regions. This is disclosed as standing context. It is not scored as a defect on its own.

## 5. Reliability & lock-in

No incidents surfaced in research, but no public uptime SLA was independently verified, holding reliability at 3. Lock-in is minimal: an OpenAI-compatible API serving portable open-weight checkpoints means the same models run on other providers or self-hosted stacks, giving a clean exit path.

## 6. Choosing this provider - the practical guideline

Together suits teams that want breadth of open models with privacy-forward defaults. For regulated or EU-resident data, budget for Scale/Enterprise to obtain EU region pinning, and secure a signed BAA before sending PHI rather than relying on the indicated HIPAA posture. Confirm ZDR toggles and enterprise terms in your contract before production data.

## 7. Sources & evidence

See [`data.yaml`](data.yaml) for the full evidence list: privacy/security documentation (publisher), the SOC 2 Type II announcement and EU data-centre support article (third_party), and pricing (third_party, approximate).

---

_Scored against [provider rubric v1.0](../../methodology/provider-scoring-rubric.md).
Data: [`data.yaml`](data.yaml)._
