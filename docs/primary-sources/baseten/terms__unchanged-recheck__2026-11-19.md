doc_type: terms
entity: baseten
source_url: https://www.baseten.co/terms-and-conditions/ ; https://www.baseten.co/dpa
retrieval_date: 2026-11-19
exists: yes
retrieved: true
tag: publisher
read_by: code session (curl, raw HTML to text)

## Result: the clauses quoted in browser-verified/terms__2026-09-20.md are unchanged word for word
Terms (no effective date on the page; footer 2026): Sec 2.5 (ZDR by reference to the Security Practices, "Where the Services or a product are designated as operating under a 'Zero Data Retention' posture in the Security Practices..."), Sec 6.1 customer IP, Sec 6.3 no training, Sec 7.4 30-day export, Sec 9.1 12-month liability cap, Sec 11.1 to 11.4 mutual confidentiality, Sec 12.8 California law, all re-read and identical to the stored extract.
DPA: "Last Updated: September 15, 2026" (unchanged). Sec 3.1 roles, Sec 7.1 sub-processors "including those listed at https://trust.baseten.co/" with "at least fifteen (15) days prior" notice, Sec 7.2 10-day objection, Sec 4.5 ZDR retention, Schedule 1 SCCs Module Two / Three with Clause 17 and 18 Ireland.

## Clauses present on the live page that the baseline extract did not record
Terms Sec 2.6 (VERBATIM): "Customer acknowledges that Baseten may deploy and operate compute, networking, storage, and hardware resources from third-party cloud service providers, GPU and hardware suppliers, data center and colocation operators, and chip developers (collectively, "Infrastructure Providers") to deliver the Services." "Infrastructure Providers are not subprocessors under the DPA unless they have logical access to Customer Content containing personal data. Upon reasonable request, Baseten will make available a list of material Infrastructure Providers."
Terms Sec 6.4 (telemetry): Baseten may use "Usage Information" to operate and improve the Services and, beyond direct operation, "only in aggregated or de-identified form". Sec 6.2: licence to Customer Content limited to providing the Services, preventing or addressing technical problems, support at the Customer's request, or compelled disclosure.
Terms Sec 6.5: a perpetual, irrevocable licence to Feedback.

## Trust centre
https://trust.baseten.co/ and /subprocessors: a JavaScript-only Vanta portal, so curl returns only a title and a meta description pointing to security@baseten.co. CORRECTION (later on 2026-11-19): the portal renders in a real browser and was read there; see security__trust-centre__2026-11-19.md. It lists ISO 27001:2022 and PCI DSS SAQ D next to SOC 2 and HIPAA, and a 13-row sub-processor list. The certificates and reports themselves are access-gated and were not read.

## Additional clauses re-read in the DPA
DPA Sec 4.4 (VERBATIM): "Consistent with the Agreement, Baseten will not use Customer Personal Data to train, fine-tune, or otherwise develop machine learning or artificial intelligence models." DPA Sec 4.5: "Where the Services are provided under a Zero Data Retention posture (as described in the Security Practices ...), Baseten shall not log, record, or save Customer Personal Data contained in model inputs or outputs to persistent storage after real-time processing, subject to the product-specific practices and limited exceptions described" there. Both Terms Sec 2.5 and DPA Sec 4.5 make the ZDR commitment depend on the Security Practices designating the product as ZDR, which the 2026-11-12 Security Practices do for Model APIs and Dedicated Inference.
