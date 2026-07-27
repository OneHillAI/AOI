# runware - primary-source clauses

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
```
