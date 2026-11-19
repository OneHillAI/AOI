# runware - primary-source clauses

**UPDATE 2026-11-19:** all rows below were re-checked by a code session. The Terms (last updated
2026-09-29) no longer carry the adverse licence or non-confidentiality clauses read on 2026-07-26 and
2026-08-06, and now add a Serverless section with express confidentiality. Hosting is named as the
United States, Germany and Romania, which contradicts the help-centre claim of EU-only storage.
The 2026-11-19 extracts supersede the 2026-07-26 clause files for the points they cover; the older
files are kept as the historical record. The 2026-09-21 browser read was logged in the entry but never
stored as a file here, so no earlier copy of the 2026-09-21 text exists in this folder.

Runware's binding documents were read by a browser (Cowork) session on 2026-07-26. The read text
contradicts Runware's marketing on data handling: nominal output ownership sits with the customer,
but the Terms grant Runware a worldwide, perpetual, transferable licence over inputs and outputs
and reference storing training data; the Privacy Policy has generic retention with no auto-purge
and does not address training. The binding entity is Runware Ltd (UK), UK governing law. See the
clause files in this folder.

## _sources.md
```
doc_type       | source_url                                                        | retrieval_date | exists      | retrieved     | notes
terms          | https://runware.ai/terms                                          | 2026-07-26     | yes         | yes           | Runware Ltd (UK); customer owns Generations BUT grants Runware a worldwide perpetual transferable licence over inputs/outputs; references "storing training data and models per our pricing schedule"; UK law, London arbitration; termination at sole discretion; deletion on request
privacy_policy | https://runware.ai/privacy                                        | 2026-07-26     | yes         | yes           | Runware Ltd (UK); generic retention ("as long as necessary"/account life); sub-processors named = Stripe + Google Analytics only; GDPR/UK GDPR referenced but NO SCC/DPF; training use NOT addressed; no auto-purge/opt-in-storage clause
docs           | https://runware.ai/trust                                          | 2026-07-26     | yes         | partial       | Trust page badge "Data residency EU & US"; no contractual region-pinning doc; CLOUD Act not addressed; binding entity UK
security       | https://runware.ai/trust ; https://runware.ai/security-disclosure | 2026-07-26     | yes (claim) | no            | ISO 27001 + SOC 2 shown as badges only; NO readable certificate/report (no number/issuer/scope/type/period); security-disclosure page is vuln-reporting only
dpa            | https://runware.ai/dpa ; https://runware.ai/data-processing-agreement | 2026-07-26  | unknown     | no            | No public/self-serve DPA located (both 404); likely enterprise/on-request. Not-readable, not confirmed absent
marketing      | https://runware.ai/pricing                                        | 2026-07-26     | yes         | yes           | pay-as-you-go; representative rates captured
third_party    | https://siliconangle.com/2025/12/11/ai-inference-startup-runware-raises-50m-make-ai-run-faster/ | 2026-07-26 | yes | yes | USD 50M Series A; markets US HQ (San Francisco) though binding entity is Runware Ltd (UK); US + central-Europe pods; ~400K HF open models
terms          | https://runware.ai/terms                                          | 2026-11-19     | yes         | yes           | Last updated 2026-09-29; no licence over Outputs; no training on Training Data/Trained Models/Customer Material; express confidentiality for private models (Sec 2) and Serverless (Sec 4); hosted US, Germany, Romania (Sec 16); HIPAA excluded (Sec 1); English law, London arbitration. See terms__2026-11-19.md
privacy_policy | https://runware.ai/privacy                                        | 2026-11-19     | yes         | yes           | Sec 6 retention unchanged (account lifetime, no numeric window); third parties named are analytics/payment only; no SCC/DPF, no sub-processor list. See privacy_policy__2026-11-19.md
docs           | https://runware.ai/docs/models-api/zero-data-retention            | 2026-11-19     | yes         | yes           | ZDR enterprise-only, sales-enabled, listed models only; outputs 7 days without ZDR; provider terms apply to partner models. See docs__zdr__2026-11-19.md
docs           | https://help.runware.ai/articles/4921342244-does-runware-offer-a-data-processing-agreement-dpa | 2026-11-19 | yes | yes | DPA only via enterprise agreement process; DPA text not read. See docs__help-centre-and-status__2026-11-19.md
docs           | https://help.runware.ai/articles/4781590666-where-is-runware-data-stored | 2026-11-19 | yes | yes | Claims EU-only storage; contradicted by Terms Sec 16 (US, Germany, Romania). See docs__help-centre-and-status__2026-11-19.md
sla            | https://status.runware.ai/                                        | 2026-11-19     | yes         | yes           | Public incident.io status page, Aug-Nov 2026 uptime Models 99.93%, Serverless 99.90%; no SLA stated. /history 404
security       | https://trust.runware.ai/                                         | 2026-11-19     | yes         | no            | JavaScript-only single-page app, empty shell without rendering; no certificate, report or sub-processor list read
security       | https://runware.ai/trust ; https://runware.ai/security-disclosure | 2026-11-19     | yes         | yes           | /trust is now a Trust & Safety abuse-report form; footer badges ISO 27001 / SOC 2 / GDPR (marketing, no report); disclosure page = responsible disclosure, no bug bounty. See docs__help-centre-and-status__2026-11-19.md
marketing      | https://runware.ai/pricing                                        | 2026-11-19     | yes         | yes           | 420 priced models incl. closed partner models; serverless per-second GPU rates; $2 free credit. See marketing__pricing__2026-11-19.md
dpa            | https://runware.ai/dpa ; https://runware.ai/data-processing-agreement | 2026-11-19 | no (404)    | no            | Still no public DPA; help centre says enterprise-only
```
