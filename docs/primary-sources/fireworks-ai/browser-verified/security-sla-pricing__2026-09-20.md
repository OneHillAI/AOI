doc_type: security (+ sla, docs, pricing)
entity: fireworks-ai
source_url: docs.fireworks.ai (data_security, data_handling, certifications, openai-compatibility, ondemand-deployments) ; fireworks.ai/blog ; status.fireworks.ai ; fireworks.ai/pricing
document_effective_date: various 2023-2026
retrieval_date: 2026-09-20
exists: yes
retrieved: true (docs/status/pricing) / false (Trust Center)
tag: publisher

## Security (docs, VERBATIM)
[Encryption] "Data is encrypted in transit (TLS 1.2+) and at rest (AES-256)."
[Tenant isolation] "Dedicated workloads run in logically isolated environments, preventing cross-customer access or data leakage."
[Access control] "Fine-grained access controls are enforced across all Fireworks environments, following the principle of least privilege." ; "All customer data access is logged, monitored, and protected against tampering."
[Pen testing] "Regular penetration testing validates controls." Bug bounty: NOT mentioned (not found).
[HIPAA] "Fireworks is HIPAA compliant and supports healthcare and life sciences organizations..."
[CMEK] Customer-Managed Encryption Keys docs page exists (capability present).

## Response API retention EXCEPTION (docs, VERBATIM) - decisive Q2 CONFIRMED
Source: docs.fireworks.ai/guides/security_compliance/data_handling
[Default store] "The Response API operates under a different retention model when `store=True` (the default setting)."
[Auto-delete] "Stored conversation data automatically deletes after 30 days."
[Opt-out] "Users can prevent storage by setting `store=False` in API requests."
[Immediate delete] "The DELETE API endpoint enables immediate removal of specific records by providing the `response_id`."
[Scope] "The Response API retention policy only applies to conversation data when using the Response API endpoints. All other Fireworks services follow the zero data retention policy described above."
So the Response API default-retention exception is REAL and documented (in docs, not a readable ToS section). ZDR is the posture for all other services per the same docs page.

## Compliance claims (publisher-grade; NO auditor/dates)
- Docs certifications FAQ: "SOC 2 Type II" + "HIPAA Certified" (no ISO, no dates, no auditor).
- Blog 2023-10-27: "the Fireworks.ai inference platform is both SOC 2 Type II and HIPAA compliant"; "validated by a third-party" (auditor NOT named, period NOT stated).
- Blog 2025-11-19: ISO 27001, ISO 27701, ISO 42001 (certification body NOT named, dates NOT stated).
- Trust Center trust.fireworks.ai: FULLY JS-gated - no dated SOC2 report or ISO certs render (retrieved:false). Compliance therefore stays publisher/blog-grade, NOT independently-dated-certificate grade. No compliance-dimension upgrade justified from this pass.

## SLA / status
status.fireworks.ai (rendered): "We're fully operational," 28 serverless components, mostly "100% uptime"; lowest shown "Kimi K3 at 99.67% uptime." No incidents listed. NO committed uptime %, NO service-credit terms on the page; no formal SLA doc located. (reliability: no committed SLA number found.)

## Docs / pricing / lock-in
[Base URL] "https://api.fireworks.ai/inference/v1"; OpenAI-compatible Chat Completions + Completions (embeddings not confirmed on that page; NO Responses API/MCP documented there).
[Deployment] On-demand/dedicated deployments SELF-SERVE today (CLI + API, GPU-second billing); enterprise sales for higher quota/regions; no on-prem in the on-demand doc (separate airgapped/EKS doc exists). dedicated_availability = self_serve (dedicated); on-prem/airgapped = enterprise/separate.
[Pricing] serverless per-token (embeddings $0.008-$0.1 /1M input; $1 free credit); training $0.50-$40.00 /1M tokens; on-demand per-GPU-second (H100 80GB $0.134/min ~$8/hr; GB300 288GB $0.334/min ~$20/hr); enterprise "Contact us."
