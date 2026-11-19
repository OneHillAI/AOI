# deepinfra - primary-source clauses

DeepInfra's own pages are now readable by curl (HTTP 200); earlier sessions saw HTTP 403 and an
unreachable trust centre. Verbatim governing text is stored in the `__2026-11-19.md` files in
this folder. The earlier scaffold is superseded by the table below.

## _sources.md (2026-11-19 re-verification, rubric 1.2)
```
doc_type       | source_url                                         | retrieval_date | exists | retrieved | notes
terms          | https://deepinfra.com/terms                        | 2026-11-19     | yes    | yes       | Last modified 2026-10-15. Sec 7(b) ZDR + no-train with exceptions (i) to (iv), Sec 5(a) DPA incorporated by reference, Sec 6(a) subcontractors without consent, Sec 17 mutual confidentiality (Customer Data not named), Sec 18 third-party models. See terms__tos-2026-10-15__2026-11-19.md
dpa            | https://trust.deepinfra.com/resources (DPA file "2026-10-05 - Deep Infra - DPA.docx.pdf") | 2026-11-19 | yes | no | EXISTS: incorporated by Terms Sec 5(a); listed on the trust centre, dated 2026-10-05. Text NOT read: signed app.sprinto.com file URL returned HTTP 403 (CloudFront) and was not worked around. SCC (Modules 1 to 3), UK IDTA, Swiss terms and 7-day sub-processor notice are FAQ statements only. See security__trust-centre__2026-11-19.md
security       | https://trust.deepinfra.com/ and /compliance       | 2026-11-19     | yes    | yes       | Page text readable: SOC 2 Compliant, ISO 27001 Compliant, GDPR In progress, HIPAA Compliant; SOC 2 Type 1 report and bridge letter, ISO 27001 certificate, ISMS manual, pen-test report and BAA listed; sub-processors AWS, GCP, Stripe (all US); FAQ on retention, US-only processing, DPA and BAA.
security       | (SOC 2 Type 1 report, ISO 27001 certificate, pen-test report, BAA) | 2026-11-19 | yes | no | Listed on the trust centre; attachments gated or WAF-blocked, not opened. Certificate date, scope and certifying body unknown. Not scored beyond what the page text states.
subprocessors  | https://docs.deepinfra.com/account/subprocessors   | 2026-11-19     | yes    | yes       | Stripe, AWS, GCP; stamped last updated 2024-09-06.
privacy_policy | https://deepinfra.com/privacy                      | 2026-11-19     | yes    | yes       | Last modified 2026-08-15; US processing; DPO named; no SCC or DPA text. See docs__data-privacy-and-privacy-policy__2026-11-19.md
docs           | https://docs.deepinfra.com/account/data-privacy (and /docs/data) | 2026-11-19 | yes | yes   | Memory-only inference, bulk batch encrypted on disk then deleted, Google and Anthropic exceptions. No US-only statement on this page now.
docs           | https://docs.deepinfra.com/account/rate-limits     | 2026-11-19     | yes    | yes       | 200 concurrent requests per public model by default; dedicated endpoints unlimited by account.
sla            | https://status.deepinfra.com/                      | 2026-11-19     | yes    | yes       | Readable. Measured 90-day uptime per core service and per model, maintenance page, scheduled deprecations. No incident history page. See sla__status-page__2026-11-19.md
sla            | (uptime SLA document)                              | 2026-11-19     | no     | no        | None found: /sla returns 404; Terms Sec 4(b) gives a 24-hour hardware replacement undertaking only. Recorded exists: no.
marketing      | https://deepinfra.com/pricing                      | 2026-11-19     | yes    | yes       | Per-token list prices, service tiers, dedicated GPU-hour prices (A100 $1.49 to B300 $5.89), spending limit. See marketing__pricing-and-catalogue__2026-11-19.md
docs           | https://api.deepinfra.com/models/list              | 2026-11-19     | yes    | yes       | 411 entries; 232 public and not deprecated, 93 of them text-generation; 94 flagged partner.
```
