doc_type: security (+ sla, status, pricing, catalogue)
entity: together-ai
source_url: together.ai/blog/soc-2-compliance ; trust.together.ai ; status.together.ai ; together.ai/pricing ; docs.together.ai/docs/serverless-models
document_effective_date: SOC2 blog 2025-07-08
retrieval_date: 2026-09-20
exists: yes
retrieved: true (blog/status/pricing/catalogue) / false (trust center, public SLA)
tag: publisher

## Security / compliance
[SOC 2 - blog VERBATIM] "Together AI has successfully completed a SOC 2 Type 2 examination."
[HIPAA - blog VERBATIM] "Together AI adheres to the stringent requirements of HIPAA, including data encryption in transit and at rest, audit logging, and strict business associate agreements."
[ISO 27001] blog references a related "ISO 27001:2022 certification" article.
SOC 2 report obtain method: "contact us" (effectively contact/NDA-gated - consistent with prior entry). Trust center trust.together.ai EXISTS but is a JS/SPA - body NOT extractable (only meta keywords). retrieved:false for cert content. together.ai/security = 404 (moved). Compliance is publisher/blog-grade; no independently dated public certificate readable.

## SLA / status
No public self-serve SLA document found; SLA/uptime commitments appear enterprise-contract only (reserved/provisioned-throughput). status.together.ai: "All services are online" (Sep 18 2026 16:50 UTC). Monitored components (Website, Playground, Inference-Vision/Chat/Images/Voice) with per-model uptimes (e.g. Llama-3.3-70B-Instruct-Turbo 100%, gpt-oss-120b 99.462%, DeepSeek-V4-Pro-0813 99.647%). NO SLA statement on the status page. reliability: public status good; no public committed SLA.

## Pricing / catalogue - the DECISIVE reversals (Q2, Q3) CONFIRMED
[Q2 - no serverless embeddings - CONFIRMED, real not artefact] docs.together.ai/docs/serverless-models Embedding section VERBATIM: "There are currently no embedding models offered via serverless." Confirmed twice. Rerank likewise VERBATIM: "There are currently no rerank models offered via serverless. Rerank models like `mixedbread-ai/mxbai-rerank-large-v2` are only available with dedicated model inference." Moderation likewise absent. Pricing page also lists no embedding models. The prior-entry reversal is REAL - embeddings/rerank are dedicated-only now.
[Q3 - Mistral/Mixtral absent from serverless - CONFIRMED] Full-text search of the serverless models page returns ZERO occurrences of "Mistral" or "Mixtral." Live serverless chat list contains only Thinking Machines, MiniMax, Qwen, Moonshot/Kimi, Z.ai/GLM, OpenAI gpt-oss, DeepSeek, Meta Llama, Prism-ML, Muse - NO Mistral family. Mixtral appears ONLY on the pricing page under FINE-TUNING ("Mixtral 8x7B Instruct v0.1", supervised FT ~$1.05). So Mistral/Mixtral = fine-tuning-only, correctly absent from the serverless catalogue.
[Serverless per-token rates - representative, cross-validated vs status component list] MiniMax M3 $0.30 in / $1.20 out; DeepSeek V4 Pro 0813 $1.32 / $3.96; Gemma 4 31B $0.39 / $0.97; GLM-5.3-Flash $0.15 / $0.50 (per 1M tokens).
[Dedicated / GPU] "Single-tenant GPU instances" (Dedicated Inference); GPU Clusters "On-demand Pay as you go GPU capacity on an hourly basis" (e.g. NVIDIA HGX H100 ~$3.99-5.49/hr); premium/large-scale = "Contact us" (NOT fully self-serve). Serverless token inference IS self-serve today. dedicated_availability = self_serve (serverless + on-demand GPU); largest-scale enterprise-negotiated.

## Lock-in / portability
OpenAI-compatible serverless API; open-weight models served (Llama, Qwen, DeepSeek, GLM, gpt-oss) - portable. Exit: standard API, no unusual lock-in noted.
