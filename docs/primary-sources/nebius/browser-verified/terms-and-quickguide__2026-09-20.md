doc_type: terms (+ legal_quick_guide)
entity: nebius
source_url: https://docs.tokenfactory.nebius.com/legal/terms-of-service ; https://docs.tokenfactory.nebius.com/legal/legal-quick-guide
document_effective_date: not shown
retrieval_date: 2026-09-20
exists: yes
retrieved: true
tag: publisher

## THE LOAD-BEARING FINDING - Token Factory ToS Section 7 (DATA USAGE AND STORAGE) - CONFIRMED VERBATIM
[License grant] "By using the Service, You grant Us a license to access, use, host, cache, store, copy, and modify Inputs and Outputs for the purposes of providing the Service."
[Default collection + TRAINING - VERBATIM] "As part of providing the Service, the Company collects and processes both Input and Output data for the purpose of training smaller Models used exclusively for Speculative Decoding."
[Opt-out required - VERBATIM] "If you prefer that we (i) do not store Your Inputs and Outputs for the purposes of providing the Service and (ii) do not collect and process them for Speculative Decoding, You may opt out at any time." (mechanism: onboarding form or email tokenfactory-support@nebius.com.)
Sec 7 contains NO explicit retention duration.
=> The binding ToS states Nebius COLLECTS AND PROCESSES Input+Output BY DEFAULT to TRAIN its own "smaller Models used exclusively for Speculative Decoding," and the customer must OPT OUT. training-on-inputs = by_default (opt-out). This is the most consequential fact in the entry and it holds up verbatim.

## Other ToS clauses (VERBATIM)
[Sec 10 IP / ownership] "You hold exclusive ownership of all rights, titles, and interests (including intellectual property rights) to Customer's Content." AND "We do not claim any rights to Customer's Content, except as described in Sections 7, 12, 13 and 13A." (The Sec 7 data-use carve-out is an explicit EXCEPTION to customer ownership.)
[Sec 18 Confidentiality] "Each Party agrees to maintain the confidentiality of all Confidential Information disclosed by the other Party." (General confidential-info duty in the ToS; the DPA's duty is narrower - personal data only, see dpa file.)
[Governing law] Netherlands law (ToS body returned "the laws of the Netherlands"; DPA cross-references "Section 17 of the Terms of Service" - section number 17 vs 19 uncertain, treat Netherlands as the law).
[Sec 16 Liability - VERBATIM] "OUR TOTAL LIABILITY UNDER THESE TERMS WILL BE LIMITED TO THE GREATER OF EITHER THE AMOUNT YOU PAID FOR THE SERVICE THAT CAUSED THE CLAIM WITHIN THE 12 MONTHS PRECEDING THE INCIDENT OR FIVE HUNDRED DOLLARS ($500)."

## Legal Quick Guide - the CONTRADICTION (Q2) - documented tension, not a clean disclosure
[Sec 4.2 Default Behavior - VERBATIM] "Your content is not used to train any models in either mode."
[FAQ - VERBATIM] "No. We do not use your content to train, fine-tune or improve any AI models - ours or third parties'."
[Sec 4.1 ZDR - VERBATIM] "with ZDR enabled, your data is not used for Speculative Decoding and is not used to train, fine-tune or improve any model - whether ours or a third party's."
[Retention purpose - VERBATIM] "unless you enable Zero Data Retention, we keep your inputs and outputs to speed up inference using the Speculative Decoding technique."
[Sec 3.2 role] "for the content you submit to our model inference and fine-tuning endpoints ... and the output you receive, we act as the Data Processor under our DPA."

RECONCILIATION: The Quick Guide treats "Speculative Decoding" as data RETENTION FOR INFERENCE SPEED-UP and asserts it does NOT constitute "training," while the binding ToS Sec 7 literally calls the same activity "training smaller Models." The marketing-facing blanket ("we do not use your content to train any AI models") is in GENUINE TENSION with the binding ToS Sec 7. The only reconciling move is Nebius carving Speculative-Decoding models out of the category "AI models." Net: the Quick Guide is more customer-favourable than, and semantically inconsistent with, the binding ToS Sec 7. For the entry, the BINDING document (ToS Sec 7) governs: train-by-default with opt-out. Flag the Quick Guide as a documented inconsistency.
