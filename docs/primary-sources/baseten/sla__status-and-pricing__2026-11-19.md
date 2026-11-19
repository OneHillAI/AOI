doc_type: sla (+ status, pricing)
entity: baseten
source_urls: https://www.baseten.co/service-level-agreement/ ; https://status.baseten.co/ (and /api/v2/summary.json, /api/v2/incidents.json) ; https://www.baseten.co/pricing/
retrieval_date: 2026-11-19
exists: yes
retrieved: true
tag: publisher

## SLA (page stamped "Last Updated: September 15, 2026", so unchanged since the 2026-09-20 browser read)
Sec 2 (VERBATIM): "Baseten will undertake commercially reasonable measures to ensure that System Availability of the SLA Service equals or exceeds ninety-nine point nine percent (99.9%) during each calendar month (the "Service Standard")." NOTE the wording: a "commercially reasonable measures" undertaking to meet 99.9%, not an unqualified guarantee. Credit table (Sec 4.1): below 99.9% but at least 99.5% = 10%; below 99.5% but at least 99.0% = 15%; below 99.0% = 30%. Sec 4.2: maximum credits "will not exceed forty percent (40%)". Sec 4.3: claim by e-mail "within twenty four hours following such Unscheduled Downtime". Scope: "This SLA does not apply to Services deployed on infrastructure that Customer controls, including self-hosted deployments."

## Status page (statuspage JSON, read 2026-11-19 12:30 UTC)
Overall: "All Systems Operational". Components: Dedicated Inference, Model APIs, Training, Model Management API, Web Application, Homepage and Docs, Sandboxes (plus Sandboxes sub-regions Oregon us-pdx-1, Virginia us-was-1, Frankfurt eu-fra-1; these are Sandboxes regions, not inference regions).
Incidents since the 2026-09-20 read (impact; duration to resolution):
- 2026-09-21 major, inference 500s, subset of models on GCP central1 (7 min)
- 2026-09-24 major, inference 500s, subset of models in 1 US-East cluster (43 min)
- 2026-09-29 major, "Elevated 500s in Single us-central Region" (11 h 45 min)
- 2026-10-05 major, DeepSeek v4.1 outage on Model APIs (13 min)
- 2026-10-20 major, DeepSeek V4.1 Flash Fast outage on Model APIs (6 min)
- 2026-11-11 critical, "Model APIs are down for all models" (21 min; "We've resolved the issue and we see recovery for all models")
- 2026-11-18 major, "Outage on app.baseten.co. Inference is not affected" (11 min)
plus 13 minor incidents in the window. All listed incidents show resolved. Status page is the SLA's measurement source (SLA Sec 2 refers to status.baseten.co).

## Pricing page (Model APIs, USD per 1M tokens: input / cached input / output)
GLM-5.3 1.40 / 0.14 / 4.40; GLM-5.3 Fast 2.10 / 0.21 / 6.60; GLM-5.3-Flash 0.15 / 0.03 / 0.50; DeepSeek V4.1 Flash 0.30 / 0.007 / 1.20 (cached input was recorded as 0.03 on 2026-09-20); DeepSeek V4.1 Flash Fast 0.60 / 0.014 / 2.40; DeepSeek V4 Pro 0813 1.32 / 0.132 / 3.96; DeepSeek-V4-Flash-0731 0.13 / 0.028 / 0.26; Kimi K3 3.00 / 0.30 / 15.00; Kimi K3.1 Pro 2.00 / 0.20 / 10.00; Nemotron 3 Ultra 0.60 / 0.12 / 2.40; GPT OSS 120B 0.10 / - / 0.50; Muse Spark Open 1.25 / 0.15 / 4.25.
Dedicated per-minute: T4 16GiB $0.01052; L4 $0.01414; A10G $0.02012; A100 80GiB $0.06667 (~$4.00/hr); H100 MIG 40GiB $0.0625; H100 80GiB $0.10833 (~$6.50/hr); B200 180GiB $0.16633 (~$9.98/hr). (Unchanged for the GPUs recorded before.) Tiers on the page: pay as you go; "Production scale" with volume discounts, reserved and priority compute, custom regions.
