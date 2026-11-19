# baseten - primary-source clauses

**CORRECTED 2026-09-21** after an independent Cowork browser verification pass - see
[`browser-verified/`](browser-verified/) for the full capture and
[`RESEARCH-RETURN__baseten__2026-09-20.md`](browser-verified/RESEARCH-RETURN__baseten__2026-09-20.md)
for the field-by-field findings. Net result: mostly CONFIRMATORY and even strengthened (mutual
confidentiality independently confirmed on two fetches; a real SLA was found where none had been
located before), with one retraction (a prior ISO 27001 claim had no basis anywhere) and one
location correction (ZDR default lives on the Security Practices page, not the Terms directly).

## _sources.md
```
doc_type       | url                                                                | exists | retrieved | notes
terms          | https://www.baseten.co/terms-and-conditions/                      | yes    | yes       | Independently browser-confirmed on TWO separate fetches. Sec 11 mutual confidentiality (Customer Content + Customer Models named symmetrically), Sec 6.3 never-train, Sec 6.1 customer IP, Sec 2.5 ZDR (conditional on Security Practices designation), Sec 7.4 30-day export, Sec 12.8 California law, Sec 9.1 liability cap.
security       | https://www.baseten.co/security-practices/                        | yes    | yes       | Independently browser-confirmed verbatim. ZDR DEFAULT stated HERE (not the Terms); logical namespace isolation + single-tenant dedicated + self-hosted VPC (NOT an explicit "three-tier" model); TLS1.2+/AES-256; MFA; pen-testing; SOC2/HIPAA/GDPR claimed (NOT ISO 27001).
dpa            | https://www.baseten.co/dpa                                        | yes    | yes       | Dated 2026-09-15. Processor/Controller roles, SCCs Module 2/3, 15-day sub-processor notice (Sec 7.1), objection right (Sec 7.2), personal-data confidentiality (Sec 5.3).
marketing      | https://www.baseten.co/blog/soc-2-type-2/                        | yes    | yes       | SOC 2 Type II, named audit firm (Sensiba San Filippo LLP).
docs           | https://docs.baseten.co/deployment/regional-environments          | yes    | yes       | No published region-name list; requires contacting support.
docs           | https://www.baseten.co/deployments/baseten-self-hosted/           | yes    | yes       | Full workload plane in customer VPC, Enterprise-tier marketing.
sla            | https://status.baseten.co/                                        | yes    | YES (upgraded) | Independently browser-read: "All Systems Operational", 6 components, 3 incidents in current window (Sep 9/14/20 2026), all resolved same/next-day. A prior draft cited a single, differently-dated incident from a search snippet only.
sla            | https://www.baseten.co/service-level-agreement/                   | yes    | YES (new)      | NEW FINDING: a real, committed SLA. Sec 2.0 - 99.9% uptime (Dedicated Inference + Model APIs); Sec 4.2 - credits capped at 40%/month; Sec 4.3 - 24h claim window. A prior draft said none had been located.
marketing      | https://www.baseten.co/pricing/                                   | yes    | yes       | Per-token Model API rates + per-GPU-minute dedicated rates (T4 through B200).
docs           | https://www.baseten.co/library/                                   | yes    | yes       | Curated Model Library catalogue.
docs           | https://docs.baseten.co/overview                                  | yes    | yes       | Three product pathways (Model APIs, custom dedicated deploys, Training Jobs/Loops); OpenAI + beta Anthropic API compatibility.
security       | https://trust.baseten.co/ (+ /subprocessors)                      | yes    | no        | Vanta portal, JS-gated - every path tried returns only a meta description + security@baseten.co. RETRACTION: a prior claim of ISO 27001 certification has NO basis here or anywhere else checked - do not assert it. PCI DSS/FedRAMP/CSA STAR and the named sub-processor list also remain unconfirmed.
```

## Freshness re-verification 2026-11-19 (code session, curl and the statuspage JSON API)

```
doc_type       | source_url                                                          | retrieval_date | exists | retrieved | notes
terms          | https://www.baseten.co/terms-and-conditions/                        | 2026-11-19     | yes    | yes       | Unchanged word for word (Sec 2.5, 6.1, 6.3, 7.4, 11.1-11.4). Sec 2.6 Infrastructure Providers and Sec 6.4 telemetry now recorded. See terms__unchanged-recheck__2026-11-19.md
dpa            | https://www.baseten.co/dpa                                          | 2026-11-19     | yes    | yes       | Last Updated September 15, 2026, unchanged. 15-day sub-processor notice (Sec 7.1), SCCs Ireland.
security       | https://www.baseten.co/security-practices/                          | 2026-11-19     | yes    | yes       | CHANGED: page now stamped Last Updated November 12, 2026. The explicit "ZDR is the default configuration" sentence is gone; ZDR is now stated as a posture across Model APIs and Dedicated Inference, with a ZDR Configuration Changes paragraph and a new Customer-Controlled Factors carve-out. See security__security-practices__2026-11-19.md
docs           | https://docs.baseten.co/deployment/regional-deployments             | 2026-11-19     | yes    | yes       | CHANGED: region table lists us (United States) and eu (European Union), selectable per deployment by CLI or API. See docs__regional-deployments__2026-11-19.md
docs           | https://docs.baseten.co/deployment/regional-environments            | 2026-11-19     | yes    | yes       | Unchanged: initial configuration by Baseten, contact support.
docs           | https://docs.baseten.co/inference/model-apis/overview.md            | 2026-11-19     | yes    | yes       | Model APIs residency needs a support-enabled compliance policy; supported-models table.
docs           | https://docs.baseten.co/inference/model-apis/pricing-and-limits.md  | 2026-11-19     | yes    | yes       | Rate-limit table now published (closes the baseline gap). See docs__model-apis-limits-and-deprecation__2026-11-19.md
docs           | https://docs.baseten.co/inference/model-apis/deprecation.md         | 2026-11-19     | yes    | yes       | 30-day deprecation notice policy now published (closes the baseline gap).
docs           | https://docs.baseten.co/security.md                                 | 2026-11-19     | yes    | yes       | Data handling per product; "Synchronous requests run under ZDR by default" (Dedicated Inference).
docs           | https://docs.baseten.co/observability/security.md                   | 2026-11-19     | yes    | yes       | Compliance policy region control; Calico/Cilium isolation; annual penetration tests by independent firms.
docs           | https://docs.baseten.co/hosting-options/overview.md                 | 2026-11-19     | yes    | yes       | Baseten Cloud, single-tenant (Enterprise), self-hosted (Enterprise), hybrid; control plane operated by Baseten for every option.
sla            | https://www.baseten.co/service-level-agreement/                     | 2026-11-19     | yes    | yes       | Last Updated September 15, 2026, unchanged. Service Standard is a "commercially reasonable measures" undertaking to reach 99.9%. See sla__status-and-pricing__2026-11-19.md
sla            | https://status.baseten.co/ (+ /api/v2/*.json)                       | 2026-11-19     | yes    | yes       | All Systems Operational; 7 major or critical incidents since 2026-09-20, longest 11 h 45 min (2026-09-29).
marketing      | https://www.baseten.co/pricing/                                     | 2026-11-19     | yes    | yes       | New Model APIs list (Kimi K3.1 Pro, GLM-5.3-Flash, GPT OSS 120B, Nemotron, Muse Spark Open...). DeepSeek V4.1 Flash cached input 0.007 (was recorded 0.03).
docs           | https://www.baseten.co/library/                                     | 2026-11-19     | yes    | yes       | Landing page shows a subset; Llama 3.3 70B and Qwen3.5 35B-A3B not seen on it or on the Model APIs list.
privacy        | https://www.baseten.co/privacy-policy/                              | 2026-11-19     | yes    | yes       | Website policy; Baseten is a processor of Customer Content under the customer agreement.
security       | https://trust.baseten.co/ (+ /resources, /subprocessors, /updates)  | 2026-11-19     | yes    | yes (browser) | Rendered in the in-app browser (curl still returns only a title). Compliance block: SOC 2, ISO 27001:2022, HIPAA, CCPA, GDPR, PCI DSS SAQ D. This CONTRADICTS the 2026-09-21 retraction: an update dated 2026-08-24 announces the ISO 27001 certification. Certificates, SOC 2/3 reports, pen test (October 2026), PCI AOC and FedRAMP 20x documents are access-gated and were NOT read; the claims are publisher-only. 13-row sub-processor list read; 8 later additions in the updates feed. See security__trust-centre__2026-11-19.md
docs           | https://docs.baseten.co/inference/model-apis/overview.md (context table) | 2026-11-19 | yes | yes | Per-model context and max-output table published (closes the use-domain context-limits gap). See docs__model-apis-limits-and-deprecation__2026-11-19.md
```
