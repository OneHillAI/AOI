doc_type: dpa (+ security, sla, status, pricing)
entity: baseten
source_url: baseten.co/dpa ; baseten.co/security-practices ; docs.baseten.co/observability/security ; baseten.co/service-level-agreement ; status.baseten.co ; baseten.co/pricing ; trust.baseten.co
document_effective_date: DPA 2026-09-15
retrieval_date: 2026-09-20
exists: yes
retrieved: true (all except Trust Center) / false (Trust Center)
tag: publisher

## DPA (VERBATIM)
[Sec 3.1 Roles] Baseten = "Processor"; Customer = "Controller, or as a Processor on behalf of its own controllers".
[Sec 12 + Schedule 1 Sec 3.3 SCCs] "the Parties shall comply with the SCCs incorporated by reference as set forth in Schedule 1"; Module Two (C2P) or Module Three (P2P) per role.
[Sec 7.1 Sub-processors] named list at trust.baseten.co with "at least fifteen (15) days prior to engaging a new Sub-Processor"; "Baseten will ensure each Sub-Processor is bound by a written agreement."
[Sec 7.2 Objection] Customer may object within 10 days via privacy@baseten.co.
[Sec 5.3 Confidentiality re personal data] personnel "subject to written confidentiality obligations."

## Security (VERBATIM)
[ZDR DEFAULT - security-practices] "Unless a customer, acting through an authorized representative, requests otherwise in writing, ZDR is the default configuration for the customer's use of the inference products." (This is where ZDR-default lives - NOT the Terms.)
[Model APIs ZDR] "Baseten will not store, retain, or otherwise make a persistent copy of model inputs or outputs during a customer's use of the Model APIs."
[No-train] "Baseten does not use Customer Content for model training, fine-tuning, or improvement of any algorithms."
[Encryption] in transit "TLS v.1.2 or higher"; at rest "AES-256 bit encryption."
[MFA] "Baseten enforces multi-factor authentication for all personnel."
[Pen-test] "Baseten engages qualified third-party security firms for periodic penetration testing." Bug bounty: not found.
[Isolation - CORRECTION] page describes LOGICAL separation ("access controls, unique customer identifiers, and namespace isolation") + "single-tenant dedicated clusters and self-hosted deployment options within the customer's own VPC." NOT an explicit "three-tier" model. Correct any "three-tier isolation" claim to: logical namespace isolation + single-tenant dedicated + self-hosted VPC. Docs add per-customer K8s namespaces, Calico/Cilium, "GPUs never shared across users," self-hosted control/workload plane split.
[Compliance claimed on retrievable pages] SOC 2 Type II, HIPAA, GDPR. ISO 27001 / PCI DSS / FedRAMP / CSA STAR: NOT FOUND on any retrievable Baseten page.

## Trust Center - retrieved:false
trust.baseten.co is a Vanta portal, JS-gated; every path (root + /subprocessors) returned only meta description + security@baseten.co. NO cert names/dates/scope; ISO 27001, PCI DSS, FedRAMP, CSA STAR CANNOT be confirmed. The named infra sub-processor list is behind this gate and unverifiable. Only marketing vendors are publicly named (Privacy Policy: Google Analytics, Segment, Sendgrid, Stripe) - these are NOT inference infra.

## SLA (VERBATIM) - committed number EXISTS
[Sec 2.0] "ninety-nine point nine percent (99.9%)" committed uptime - applies to BOTH Dedicated Inference and Model APIs on Baseten-managed infrastructure.
[Sec 1.5 def] "System Availability = (Total Monthly Time - Unscheduled Downtime) / (Total Monthly Time)", measured against status.baseten.co.
[Sec 4.2 credits cap] "The maximum amount of Service Credits ... in a single calendar month will not exceed forty percent (40%)."
[Sec 4.3] claim within 24 hours with evidence. [Sec 1.4] standard exclusions (customer non-compliance, third-party failures, force majeure, inadequate GPU reservation, network failures).
Enterprise plan offers "Custom SLAs."

## Status
status.baseten.co: "All Systems Operational"; 6 components (Dedicated Inference, Model APIs, Training, Model Management API, Web Application, Homepage and Docs). 90-day history, no numeric % on face. Incidents: 2026-09-20 Kimi K3 US endpoint outage (restored 01:13 PDT); 2026-09-14 India cluster elevated errors + Kimi K3 non-US partial (resolved same day); 2026-09-09 Nemotron Ultra partial (Dedicated Inference unaffected, resolved 10:49 PDT).

## Pricing / lock-in
Model APIs per-token (e.g. GLM-class ~$0.15 in / $0.50 out /1M). Dedicated Inference pay-per-minute (T4 ~$0.01052/min to B200 ~$0.16633/min) - SELF-SERVE today (Deploy buttons, Basic/Pro tiers). Self-hosted = Enterprise-gated (NOT self-serve), offers "Full control over data residency." Truss = open-source packaging standard (open-model portability). OpenAI-compatible API not mentioned on pricing page (not confirmed there). dedicated_availability = self_serve (dedicated compute); self-hosted/VPC = enterprise_only.
