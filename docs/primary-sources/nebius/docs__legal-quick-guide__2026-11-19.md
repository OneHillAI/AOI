doc_type: docs
entity: nebius
source_url: https://docs.tokenfactory.nebius.com/legal/legal-quick-guide
document_effective_date: not dated on the page (a plain-language summary that states it "does not amend or replace our Terms of Service, Data Processing Agreement (DPA) or Privacy Policy; in case of any inconsistency, those documents prevail")
retrieval_date: 2026-11-19
exists: yes
retrieved: true
tag: publisher (non-binding summary)

## Verbatim
[FAQ, still present] "Is my data used to train your AI models? No. We do not use your content to train, fine-tune or improve any AI models – ours or third parties’. Unless you enable Zero Data Retention, your inputs and outputs may be stored and used solely for Speculative Decoding (see Section 3), which does not involve training any model."
[4.2] "Unless you enable Zero Data Retention, we keep your inputs and outputs to speed up inference using the Speculative Decoding technique described in Section 3. Your content is not used to train any models in either mode."
[3.3] "It is enabled by default for best performance; you can opt out at any time by enabling Zero Data Retention."
[4.1 ZDR] "with ZDR enabled, your inputs (prompts) and outputs (responses) are not stored on our systems after each request is processed – no retained copy exists beyond ephemeral in-flight processing." ZDR is org-level, enabled in account settings.
[5.1] Public endpoints: "the Region field shows Global. The processing location is decided dynamically ... can change at any time without prior notice ... not intended for production use cases that require a stable, predictable region." Retained Speculative Decoding data "stored in Finland (EU), regardless of where real-time processing takes place."
[5.2] Dedicated endpoints: region is a contractual commitment (DPA 6.1), "We do not use multi-region routing, load balancing, or automatic overflow/failover to other regions for dedicated endpoints".
[5.3] All fine-tuning datasets, artifacts and outputs are stored "exclusively in EU data centers".

## Marketing versus binding text (still unresolved)
Binding Supplemental Terms 5.1(b) (effective 2026-10-22): Nebius may "train smaller Models used for Speculative Decoding" on Input and Output, default on, opt-out by onboarding form or email. The Quick Guide FAQ answers "No" to "Is my data used to train your AI models?" and says Speculative Decoding "does not involve training any model". The two cannot both be right as plain English; the contract is the binding one. The Quick Guide has also become more specific than in September: it now ties the opt-out to enabling ZDR (the Terms name the onboarding form or an email to support).
