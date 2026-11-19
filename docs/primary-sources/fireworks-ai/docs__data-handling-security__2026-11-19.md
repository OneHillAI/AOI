doc_type: docs
entity: fireworks-ai
source_urls: https://docs.fireworks.ai/guides/security_compliance/data_handling ; https://docs.fireworks.ai/guides/security_compliance/data_security ; https://docs.fireworks.ai/faq/enterprise/compliance/certifications
retrieval_date: 2026-11-19
exists: yes
retrieved: true (page text, read through a fetch-and-summarise tool; quotes marked "verbatim" were returned in quotation marks by that tool, the rest is paraphrase)
tag: publisher

## data_handling (Zero Data Retention page)
- ZDR for open models: no logging or storage of prompt or generation data without explicit user opt-in; data exists only in volatile memory during the request. Prompt caching can keep some prompt data and KV caches in volatile memory "for several minutes". Metadata such as token counts is still logged.
- Exclusions from ZDR: Batch API (needs dataset storage) and the Responses API with store=True (the default).
- Response API retention: stores user prompts, model responses and tools the model called; store=False prevents retention; retained up to 30 days; verbatim: "Stored responses are held in a cache and can be evicted earlier, often within about an hour."; the DELETE endpoint with a response_id removes a record immediately.
- Enterprise account admins can enable a ZDR policy that rejects requests and jobs that would persist or log customer content.
- DIFFERENCES from 2026-09-20: the Batch API exclusion, the prompt-cache window and metadata logging are now stated; an enterprise ZDR-enforcement policy is now described.

## data_security
- TLS 1.2+ in transit, AES-256 at rest; customer-managed keys (AWS KMS, Google Cloud KMS, Azure Key Vault) for datasets and checkpoints in LoRA SFT, DPO and RFT training.
- "Dedicated workloads run in logically isolated environments" (verbatim, unchanged); private network isolation, firewalls, DDoS protection.
- Least-privilege IAM; minimal staff production access, logged and reviewed.
- "Regular penetration testing validates controls." (verbatim, unchanged). No bug bounty mentioned. Regions: only a link to US-only Serverless.
- Certifications listed on the page: ISO 27001, ISO 27701, ISO 42001 ("achieved"), SOC 2 Type II, HIPAA compliant. Points to trust.fireworks.ai for reports.

## certifications FAQ
Same list; no dates, no auditor or certification body named. Directs readers to the Trust Center for certificates and audit reports.
