doc_type: terms
entity: morena
variant/applies-to: Gemma Terms of Use (Gemma 1 to 3 and others in its Appendix), read to test whether MORENA's use of Gemma-family models for synthetic training data raises an upstream-terms question. This is NOT a MORENA document; it is an upstream third-party licence.
source_url: https://ai.google.dev/gemma/terms
document_effective_date: last modified April 1, 2026 (as printed on the page)
retrieval_date: 2026-11-19
exists: yes
retrieved: true

## Governing clauses (verbatim)

[1.1(e) Model Derivatives] ""Model Derivatives" means all (i) modifications to Gemma, (ii) works based on Gemma, or (iii) any other machine learning model which is created by transfer of patterns of the weights, parameters, operations, or Output of Gemma, to that model in order to cause that model to perform similarly to Gemma, including distillation methods that use intermediate data representations or methods based on the generation of synthetic data Outputs by Gemma for training that model. For clarity, Outputs are not deemed Model Derivatives."

[3.1 Distribution] "You may reproduce or Distribute copies of Gemma or Model Derivatives if you meet all of the following conditions: You must include the use restrictions referenced in Section 3.2 as an enforceable provision in any agreement (e.g., license agreement, terms of use, etc.) governing the use and/or distribution of Gemma or Model Derivatives ... You must provide all third party recipients of Gemma or Model Derivatives a copy of this Agreement."

[3.3 Generated Output] "Google claims no rights in Outputs you generate using Gemma. You and your users are solely responsible for Outputs and their subsequent uses."

[Appendix] lists Gemma 1, 1.1, 2, 3, 3n among covered models.

## Why it is logged

The MORENA paper (p6-7) says the post-training corpus is "mostly synthetic" and was "generated per language by Gemma-family and GPT-OSS-120b models", with gemma-3-12b-it named for the benign set, the safety prompts and the judge. Under 1.1(e)(iii) a model trained on synthetic Outputs of Gemma "in order to cause that model to perform similarly to Gemma" can be a Model Derivative, and 3.1 then requires the Gemma use restrictions to travel with it. Whether the MORENA SFT data meets that test (which Gemma versions, and whether the purpose was to make MORENA perform like Gemma) is not stated by Vambo and was not resolved here. This is an open licence-consistency question, not a finding that Apache-2.0 is invalid. The gpt-oss-120b terms were not read.
