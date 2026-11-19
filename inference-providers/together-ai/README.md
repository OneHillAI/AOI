# Together AI - OneHill Inference-Provider Dossier

> **Score: 69.6/100 · Grade C** · HQ: United States · EU residency: sales-led dedicated and VPC only · Trains on inputs: opt-in only, off by default
> Last verified: 2026-11-19 · Ownership: partial
>
> _Right for teams that want a broad, fast-moving open-model catalogue on an OpenAI-compatible API. The caveats are default prompt storage, an opt-in ZDR, default-on passthrough models, a disclaimed confidentiality duty and no EU serverless option._

**Hard flags:** none (the confidentiality disclaimer caps Data Governance at 3 under rubric 1.2)

---

## At a glance

| Dimension | Score | One-line reason |
|---|---|---|
| Data Governance & Privacy | 3/5 | Prompts stored by default, ZDR is opt-in, passthrough on; confidentiality disclaimed |
| Compliance & Certifications | 4/5 | SOC 2 Type II and ISO 27001:2022 announced (reports on request only); DPA with SCCs |
| Data Residency & Sovereignty | 3/5 | US-only processing endpoint on serverless; EU only via sales-led dedicated or VPC |
| Security Posture | 4/5 | DPA commits to annual pen tests and daily scans; private HackerOne programme |
| Reliability & SLA | 3/5 | Public status page with per-model uptime; no self-serve SLA |
| Transparency & Lock-in | 4/5 | OpenAI-compatible API over portable open models; passthrough routing unlabelled |
| Cost & Value | 4/5 | Live per-token rates, cached-input prices and GPU-hour dedicated rates |

## 1. What it serves & how it's priced

Together AI is a US-headquartered inference provider on NVIDIA GPUs. The serverless chat catalogue has 24 models, led by DeepSeek V4, GLM-5.3, Kimi K3 and K3.1 Pro, the Qwen 3.5 to 4 family, gpt-oss-120B and MiniMax M3.1 Flash, plus vision, image, video and audio models. Llama 3.3 70B, Gemma 4 31B and Qwen3-235B are not served on serverless, and there are no serverless embedding, rerank or moderation models. Pricing is per token (gpt-oss-120B $0.15/$0.60 per million, DeepSeek V4.1 Flash $0.30/$1.20), with a 25% premium for US-only processing, on-demand dedicated GPUs from $5.49 per GPU hour, and provisioned throughput through sales.

## 2. Data governance - where your prompts go

By default Together stores prompts and responses and, per its docs, "may use them for product improvements". Zero data retention is an organisation-admin opt-in that also switches off passthrough models. Passthrough models forward your prompts to an upstream provider and are on by default. Training on your data is a separate opt-in, off by default, and you own Your Content and Output. Terms Sec 9 expressly disclaims confidentiality, so on standard terms Together owes no duty of confidence over your prompts. None of this is independently audited.

## 3. Compliance & certifications

SOC 2 Type II (blog, 2025-07-08) and ISO 27001:2022 from A-LIGN (blog, 2026-06-10) are vendor announcements. The report and certificate are available only on request, and the trust centre is a JavaScript-only page. A GDPR DPA with EU SCCs and the UK Addendum is published as a PDF. HIPAA and BAAs are stated in the SOC 2 blog, but Terms Sec 4 bars sending medical or financial data on standard terms, so get a signed BAA before sending PHI.

## 4. Residency & sovereignty

Serverless offers one region guarantee: US-only inference processing at `us-api.together.ai`, which does not cover storage, logs or network routing. Requests to `api.together.ai` carry no region guarantee, and there is no EU serverless endpoint. EU residency needs a dedicated endpoint or VPC deployment through sales. The support article that says so is a year old and names tiers the docs call legacy.

**CLOUD Act disclosure:** As a US-headquartered provider, Together is subject to US jurisdiction, including the CLOUD Act, even for data hosted in EU regions. This is disclosed as standing context and is not scored as a defect on its own.

## 5. Reliability & lock-in

status.together.ai is public and shows per-model 90-day uptime from 99.28% to 100%, with no incident posts since January 2025. There is no self-serve SLA: the Terms disclaim uptime and the docs call serverless best-effort. Lock-in is minimal. An OpenAI-compatible API serving portable open-weight checkpoints means the same models run on other providers or self-hosted stacks.

## 6. Choosing this provider - the practical guideline

Together suits teams that want breadth and fast access to new open models. Turn prompt storage off to enable ZDR, which also disables passthrough models. For regulated or EU-resident data, budget for a sales-led dedicated or VPC deployment. Negotiate confidentiality, a BAA and an SLA in an enterprise contract and do not rely on the default terms.

## 7. Sources & evidence

See [`entry.yaml`](entry.yaml) for the evidence list and [`docs/primary-sources/together-ai/`](../../docs/primary-sources/together-ai/) for the clause extracts: Terms of Service, Privacy Policy, DPA PDF, product docs on retention, ZDR and geo-specific inference, pricing and catalogue, status page and the SOC 2 and ISO announcements. The trust centre has no readable content.

---

_Scored against [provider rubric v1.2](../../methodology/provider-scoring-rubric.md).
Data: [`entry.yaml`](entry.yaml)._
