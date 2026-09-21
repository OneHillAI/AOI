doc_type: security (+ sla, status, pricing)
entity: nebius
source_url: nebius.com/blog SOC2 post + nebius.com/trust-center ; docs.nebius.com/legal/sla + /sla-levels ; status.nebius.com ; tokenfactory.nebius.com prices
document_effective_date: SOC2 post announced 2025-10-14
retrieval_date: 2026-09-20
exists: yes
retrieved: true (security/sla/status) / false (authoritative price list)
tag: publisher

## Security / compliance (VERBATIM)
[SOC 2 Type II auditor] "Deloitte, an accredited third-party firm that evaluates the design and operational effectiveness of our measures to protect customer data."
[HIPAA] "SOC 2 Type II also includes a section that confirms compliance with the Health Insurance Portability and Accountability Act (HIPAA)."
[ISO 27001 scope - VERBATIM] "Spanning Nebius AI Cloud, AI Studio and TractoAI..." - confirms AI Studio (= Token Factory) is in the ISO 27001 scope.
NOTE: the SOC 2 Type II report itself requires an NDA to access; no public audit dates/validity window disclosed. Compliance is publisher-grade + named auditor (Deloitte), NOT an independently-dated public certificate.

## SLA (Q5) - CONFIRMED: NO committed inference SLA number
[Master SLA - VERBATIM] "The list of Services which provides Service Levels and links for Service Levels for specific Service are available at: https://docs.nebius.com/legal/sla-levels" and "Service Level and amount of Compensation is determined for each Service separately." No number in the master doc; no mention of inference/Token Factory/AI Studio.
[sla-levels index] lists EXACTLY 7 services: Compute Cloud, Managed Service for Kubernetes, Managed Service for MLflow, Managed Service for PostgreSQL, Object Storage, Standalone Applications, Virtual Private Cloud. NO inference / Token Factory / AI Studio sub-page exists.
=> Any 99.9% figure is MARKETING-COPY ONLY and is NOT backed by a binding SLA sub-page. Do NOT attribute a committed uptime to Token Factory inference. reliability: no committed inference SLA.

## Status
status.nebius.com: has a dedicated "Token Factory" component (current status "Operational") - no separate "Inference"/"AI Studio" component. Regions covered: EU-NORTH1, EU-NORTH2, EU-WEST1, EU-WEST2, UK-SOUTH1, US-CENTRAL1, ME-WEST1. "Uptime over the past 90 days" shown, no numeric % on the main view. Incidents Sep 9-17 2026 (compute partial, eu-west1 metrics, us-central1 Object Storage 5xx, eu-north1 SkyPilot 503, VM creation) - all resolved.

## Pricing / catalogue (Q6) - MIXED; "dedicated-only" claim NOT supported
Authoritative price list tokenfactory.nebius.com/organization/prices is AUTH-GATED (retrieved:false). Evidence from readable sources: open models ARE publicly served per-token (data point: Llama-3.3-70B-Instruct $0.13/1M in, $0.40/1M out, standard public rate, no "dedicated" qualifier). The live catalogue has ROTATED to newer versions (e.g. Kimi-K2.7-Code $0.95/$4.00; GLM-5.x). The specifically named Kimi-K2-Instruct, Llama-3.3-70B-Instruct, GLM-4.5 do NOT appear in the current live list - they read as SUPERSEDED/rotated out, not "hidden as dedicated-only." So the draft's "dedicated-endpoint-only, no public price" framing is NOT supported; evidence favours public per-token serving, but the exact three named versions are largely off the current self-serve catalogue. Verify against the authenticated prices page before asserting a specific number.
