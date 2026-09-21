# Research return: baseten (FULL grounding pass) - 2026-09-20

## Decisive questions - CONFIRM / CORRECT
1. ZDR default + never-train? -> CONFIRMED, with a location nuance: ZDR is the DEFAULT per the Security Practices page ("ZDR is the default configuration for the customer's use of the inference products"), NOT the Terms - Terms Sec 2.5 only honours whatever the Security Practices designate. CORRECT any "ZDR default per the Terms" wording. Never-train CONFIRMED (Terms Sec 6.3 verbatim).
2. Mutual confidentiality + survival? -> CONFIRMED and strong. Section 11 is genuinely mutual (symmetric Disclosing/Receiving Party; Customer Content + Models named as Customer's confidential info; single shared standard of care Sec 11.2), survives 3 years, trade secrets indefinitely (Sec 11.4). This is a legitimate differentiating finding - state it clearly. confidentiality = mutual.
3. Trust Center ISO 27001 / PCI DSS / FedRAMP / CSA STAR? -> retrieved:false. Vanta portal JS-gated; NONE confirmable. Only SOC 2 Type II, HIPAA, GDPR are publicly claimed (Security Practices/docs). Do NOT assert ISO 27001/PCI/FedRAMP/CSA STAR - no independent read. No compliance upgrade from those.
4. Named sub-processor list? -> PARTIAL. Baseten COMMITS to a named list (DPA 7.1 + Security Practices) with 15-day notice, but the list sits behind the Vanta gate (unverifiable). Only marketing vendors are publicly named (Privacy Policy). Treat the named infra list as NOT independently confirmed.

## Field-by-field
| Field | Value | Grounded |
|-------|-------|----------|
| retention | ZDR DEFAULT (Security Practices); Terms Sec 2.5 conditional | security/terms |
| training-on-inputs | never (Terms 6.3; Security Practices) | terms/security |
| confidentiality | MUTUAL (Sec 11.1-11.2), 3-yr survival + trade secrets indefinite (11.4) | terms (verbatim x2) |
| customer IP | customer reserves all rights (Sec 6.1) | terms |
| export | 30-day post-term export (Sec 7.4) | terms |
| compliance | SOC2 Type II + HIPAA + GDPR (publisher); ISO27001/PCI/FedRAMP/CSA STAR NOT confirmed (Vanta JS-gated) | security; trust:false |
| encryption | TLS1.2+/AES-256 | security |
| isolation | logical namespace + single-tenant dedicated + self-hosted VPC (NOT "three-tier") | security/docs |
| pen-test | yes; bug bounty not found | security |
| SLA | 99.9% committed (Model APIs + Dedicated); 40% max monthly credits; 24h claim | sla (verbatim) |
| status | all operational; incidents Sep 9/14/20 | status |
| dedicated_availability | self_serve (dedicated per-minute); self-hosted = enterprise_only | pricing |
| governing law / liability | California; 12-mo cap (Sec 9.1) | terms |
| sub-processors | 15-day notice + list at trust.baseten.co (JS-gated, unread) | dpa/security; trust:false |

## Corrections to the draft entry
1. "ZDR default per the Terms" -> per the Security Practices page (incorporated by reference); Terms Sec 2.5 only honours the designated posture.
2. "Three-tier isolation model" -> not stated; describe as logical namespace + single-tenant dedicated + self-hosted VPC.
3. "Named sub-processor list published" -> committed but Vanta-gated/unverifiable; only marketing vendors publicly named.
4. ISO 27001 / PCI DSS / FedRAMP / CSA STAR -> NOT found; only SOC2 Type II / HIPAA / GDPR publicly claimed.
CONFIRMED STRONG: mutual confidentiality with 3-year (indefinite trade-secret) survival.

## RE-DO
Authenticated/JS render of trust.baseten.co to read the Vanta certificate list (ISO/PCI/FedRAMP/CSA STAR status + dates) and the named infra sub-processor inventory.
