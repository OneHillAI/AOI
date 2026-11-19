# groq - primary-source clauses

Re-read 2026-11-19 by a code session; server-rendered Groq pages (console.groq.com docs and legal pages,
groq.com, groqstatus.com) were fetched directly. The trust centre is a JavaScript-only page and could
not be read. Clause extracts are in the `*__2026-11-19.md` files in this folder. Earlier rows from the
2026-07-25 search-extraction pass are superseded where a 2026-11-19 row exists.

## _sources.md
```
doc_type       | source_url                                                              | retrieval_date | exists | retrieved | notes
terms          | https://console.groq.com/docs/legal/services-agreement                  | 2026-11-19     | yes    | yes       | Last Modified 2026-06-22, unchanged. Sec 4.2 no-training, Sec 10 mutual confidentiality, "Eligible Customers" ZDR gap, $5,000 free/beta cap, Groq UK Limited for EEA. See terms__services-agreement__2026-11-19.md
dpa            | https://console.groq.com/docs/legal/customer-data-processing-addendum   | 2026-11-19     | yes    | yes       | Effective 2025-10-15, unchanged. Sub-processor list lives at trust.groq.com/subprocessors; US processing permitted; SCCs deemed signed
dpa            | https://console.groq.com/docs/legal/customer-business-associate-addendum | 2026-11-19    | yes    | yes       | Effective 2025-10-15. Covered Cloud Services exclude beta/preview/non-GA
terms          | https://console.groq.com/docs/legal/ai-policy                           | 2026-11-19     | yes    | yes       | Acceptable Use & Responsible AI Policy, Effective 2025-10-15 (first read in this folder)
docs           | https://console.groq.com/docs/your-data                                 | 2026-11-19     | yes    | yes       | No default inference retention; up to 30 days troubleshooting/abuse logs unless ZDR; batch 30 days; fine-tune until deleted; US GCP. See docs__your-data__2026-11-19.md
docs           | https://console.groq.com/docs/models ; /deprecations ; /openai ; /rate-limits | 2026-11-19 | yes    | yes       | Catalogue, prices, deprecations. See docs__models-and-deprecations__2026-11-19.md
marketing      | https://groq.com/pricing                                                | 2026-11-19     | no     | no        | Redirects to the Groq home page; no prices. Prices taken from the docs models page
sla            | https://groqstatus.com/                                                 | 2026-11-19     | yes    | yes       | incident.io status page; Aug-Nov 2026 uptime API 100%, production 100%, preview 99.98%; no SLA statement. See docs__status-security-and-platform__2026-11-19.md
security       | https://groq.com/security ; https://groq.com/platform                   | 2026-11-19     | yes    | yes       | Private HackerOne programme; 13 data centers incl. EU-1 Vantaa, EU-2 London. See docs__status-security-and-platform__2026-11-19.md
security       | https://trust.groq.com/                                                 | 2026-11-19     | yes    | no        | JavaScript-only single-page app, ~7 KB shell with no content. SOC 2 claim not re-confirmed
subprocessors  | https://trust.groq.com/subprocessors                                    | 2026-11-19     | yes    | no        | JavaScript-only; the ~21 named entries and regions could not be read. Still OUTSTANDING for a browser session
security       | (SOC 2 Type II report itself)                                           | -              | yes    | no        | Gated behind trust-centre request; not obtained
```
