# Research return: fireworks-ai (FULL grounding pass) - 2026-09-20

## Headline: the two most load-bearing contractual documents could NOT be browser-read
The Fireworks Terms of Service and DPA are page-level NOINDEXED (ROBOTS_DISALLOWED) and the Trust Center is fully JS-gated. A real browser pass therefore CANNOT ground the ToS ZDR/no-train clause, the confidentiality-clause direction, or the DPA sub-processor list (incl. the Anthropic claim). These must be treated as retrieved:false / code-session-PDF-only, not browser-verified. This is a correction to the draft, which implied these were read.

## Decisive questions - CONFIRM / CORRECT
1. ToS ZDR + no-train clause? -> CANNOT CONFIRM from ToS (retrieved:false, noindexed). SUBSTANCE confirmed via Privacy Policy verbatim ("We do not use your prompts, training data, or API inputs to train or improve our AI models without your explicit opt-in") but NOT as a numbered ToS clause.
2. Response API retention exception? -> CONFIRMED (docs, verbatim): store=True default, 30-day auto-delete, store=False opt-out, DELETE endpoint by response_id; all other services ZDR.
3. Confidentiality clause direction? -> CANNOT DETERMINE (ToS unreadable). Do NOT classify functional_only/explicit/mutual on browser evidence.
4. DPA names Anthropic as AI-services sub-processor? -> CANNOT CONFIRM (DPA + Trust Center unreadable). Naming unverified.
5. Trust Center dated SOC2 Type II + ISO certs? -> NO - fully JS-gated. Compliance stays publisher/blog-grade (SOC2 Type II + HIPAA blog 2023-10-27; ISO 27001/27701/42001 blog 2025-11-19; no auditor/dates). No compliance upgrade.

## Field-by-field (browser-grounded only)
| Field | Value | Grounded? |
|-------|-------|-----------|
| retention (default) | ZDR posture for all non-Response-API services (docs); Response API stores by default 30 days unless store=false | docs (publisher) |
| training-on-inputs | never without explicit opt-in (Privacy Policy verbatim) | privacy (publisher); NOT ToS |
| confidentiality | UNDETERMINED - ToS unreadable | NOT grounded |
| sub-processors (Anthropic) | UNDETERMINED - DPA unreadable | NOT grounded |
| compliance | SOC2 Type II + HIPAA + ISO 27001/27701/42001 - blog/publisher only, no auditor/dates, Trust Center JS-gated | publisher only |
| encryption | TLS1.2+/AES-256 | docs |
| isolation | logical isolation of dedicated workloads; CMEK available | docs |
| pen-test | yes (periodic); bug bounty not found | docs |
| SLA | no committed % / credits found; status page live uptimes only | status only |
| OpenAI-compat | api.fireworks.ai/inference/v1; chat+completions | docs |
| dedicated_availability | self_serve (dedicated GPU-second); airgapped/EKS separate/enterprise | docs |
| pricing | published per-token + per-GPU-second | pricing |

## _sources.md row changes to apply
- terms -> retrieved:false (noindex; browser cannot read) - flag confidentiality + ZDR-clause as code-session-PDF-only
- dpa -> retrieved:false (noindex/JS) - Anthropic sub-processor NOT browser-confirmed
- privacy -> retrieved:true (no-train opt-in substitute)
- security docs (data_security, data_handling, certifications) -> retrieved:true
- Response API exception -> retrieved:true (docs)
- trust.fireworks.ai -> retrieved:false (JS-gated)
- status/pricing/openai-compat/ondemand -> retrieved:true

## RE-DO
Obtain a rendered ToS + DPA PDF or authenticated Trust Center access to close Q1/Q3/Q4 and to move compliance beyond publisher-grade.
