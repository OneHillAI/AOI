doc_type: docs (data privacy) and privacy_policy
entity: deepinfra
source_urls: https://docs.deepinfra.com/account/data-privacy (also https://deepinfra.com/docs/data) ; https://deepinfra.com/privacy
retrieval_date: 2026-11-19
exists: yes
retrieved: true
tag: publisher

## Data privacy docs page (VERBATIM)
"When using DeepInfra inference APIs, we do not store the data you submit to our APIs on disk. We only hold it in memory during the inference process. Once inference is complete, the data is deleted from memory."
"When using our bulk inference APIs (submitting multiple requests in a single call), we may need to store data for a longer period, potentially on disk in encrypted form. Once inference is complete and results are returned to you, the data is deleted from disk and memory after a short retention period."
"We do not use data you submit to our APIs for training models, except when using Google or Anthropic models, where the receiving company's training policy applies."
"We do not share data you submit to our APIs with any third party, except when using Google or Anthropic models, where we are required to transfer data to those endpoints to fulfill the request."
"We do not log the content of your requests. We log only metadata useful for debugging: request ID, cost, sampling parameters."
"If you opt to use a Google model, Google will store the output as outlined in their Privacy Notice. If you opt to use an Anthropic model, Anthropic will store the output as outlined in their Trust Center." "When using the Google model, Google logs prompts and responses for a limited period solely to detect violations of their Prohibited Use Policy."
The page has no residency statement; the "US-based data centres" wording recorded on 2026-07-25 (ev5) is not on the page now. The US-only statement is in the trust-centre FAQ (security__trust-centre__2026-11-19.md) and the Privacy Policy.
The page now carries a Subprocessors link, a Prompt Cache Retention page, and in llms.txt a Rate Limits page.

## Privacy Policy (stamp "Last modified: August 15th 2026")
"We will not store, sell, or train using this data unless we have your explicit consent." (about inference inputs and outputs, pointing to the docs page). "Your data may be transferred, stored, and processed outside of your jurisdiction, specifically in the United States." Technical and organisational measures "for GDPR and HIPAA" are mentioned. DPO named: Nikola Borisov, dpo@deepinfra.com. The policy contains no SCC, DPA or Data Privacy Framework text; the DPA is a separate document (Terms Sec 5(a)).
Rate limits page (docs.deepinfra.com/account/rate-limits): "every account has a default limit of 200 concurrent requests per model" on public models; "Private dedicated endpoints have no rate limits".
