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
