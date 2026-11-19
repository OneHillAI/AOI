doc_type: terms
entity: nebius
source_url: https://docs.nebius.com/legal/token-factory
document_effective_date: Publication date October 22, 2026; Effective date October 22, 2026 (previous version archived at docs.nebius.com/legal/archive/token-factory-20260915)
retrieval_date: 2026-11-19
exists: yes
retrieved: true
tag: publisher (binding contract text)

## What changed (the governing document moved)
The 2026-09-20 pass read the standalone "Token Factory Terms of Service" at docs.tokenfactory.nebius.com/legal/terms-of-service (Sec 7). That document now opens with:
"IMPORTANT NOTICE. These Terms of Service apply exclusively to Nebius Token Factory customers who have an active reserve as of September 15, 2026, and shall remain in effect for those customers until the expiration of their respective reserve period. If you are not a customer with an active reserve, please note that as of September 28, 2026, your use of the Service is governed by the updated Terms of Service available at https://docs.nebius.com/legal/agreement." (legacy page: Publication date August 20, 2026.)
New customers are therefore governed by the Nebius Services Agreement (docs.nebius.com/legal/agreement) plus these Token Factory Supplemental Terms. The Supplemental Terms are "incorporated into and form part of" the Agreement.

## Verbatim clauses
[1 Definitions] "“Customer AI Content” means Customer’s Inputs, Outputs, Adapters, Fine-Tuned Models, Distilled Models, Datasets, Models and smaller Models for Speculative Decoding. ... Customer AI Content is considered Customer Data for purposes of the Agreement ..."
[1] "“Speculative Decoding” means an inference-time method that speeds up Output generation by using a smaller, specific-purpose (“draft”) Model to propose multiple tokens, which are then verified or rejected by a larger (“target”) Model."

[3.1 Customer Content] "As between the parties and to the extent permitted by law, Customer retains ownership of Customer Content, including its Input and Output. Customer acknowledges that Outputs may not be unique, and other users of the Token Factory Service may receive the same or similar Outputs."
[3.2] "Nebius retains ownership of any smaller Models for Speculative Decoding created by or for Nebius."

[5.1 Processing of Input and Output - TRAINING CLAUSE] "Nebius processes Input to generate Output and to operate, maintain, and provide the Token Factory Service. Subject to the terms of the DPA, Nebius may access, use, host, cache, store, copy, modify, and otherwise process Input and Output to (a) provide, maintain, monitor, protect, and support the Services, Token Factory Service or (b) train smaller Models used for Speculative Decoding. These rights and licenses are royalty free, transferable, sub-licensable, and worldwide."
[5.3 Deletion] "Subject to the terms of the DPA, Nebius reserves the right, and has absolute discretion, to remove, screen, or delete any Inputs or Outputs at any time, for any reason, and without notice."
[5.4 Opt Out] "If Customer prefers that Nebius (i) does not store Customer’s Inputs and Outputs for the purposes of providing the Services, or (ii) does not collect and process them for Speculative Decoding, Customer may opt out at any time. Customer can indicate such preference through the opt-out mechanism available in the onboarding form or by submitting a request to Nebius’ support team via email at tokenfactory-support@nebius.com. Please be aware that opting out may, in some cases, limit the Services’ ability to address Customer’s specific use case effectively. ..."

[7.4 No Service Level Agreement - NEW EXPRESS CLAUSE] "The Service Level Agreement (“SLA”) available at https://docs.nebius.com/legal/sla does not apply to the Token Factory Service. Nebius does not provide any service level commitments, uptime guarantees, or associated compensation for the Token Factory Service. For the avoidance of doubt, no compensation or credits shall be available to Customer in connection with any unavailability or underperformance of the Token Factory Service, unless agreed otherwise in writing."

[2.4] Customer is the "provider" of any AI system it builds with the API under the EU AI Act. [2.10] Nebius may delete Fine-Tuned or Distilled Models on three days' written notice.

## Comparison with the legacy Terms Sec 7 (read 2026-09-20, same clause moved)
Legacy: "As part of providing the Service, the Company collects and processes both Input and Output data for the purpose of training smaller Models used exclusively for Speculative Decoding." Supplemental 5.1(b): "train smaller Models used for Speculative Decoding" - the word "exclusively" is no longer in the training sentence (Nebius retains ownership of those models, 3.2). The default-on training, the opt-out by onboarding form or email, and the absolute-discretion deletion right are all unchanged. The clause is now "Subject to the terms of the DPA", and the Agreement's Customer Data purpose limitation (10.1.3) points back to these Supplemental Terms.
