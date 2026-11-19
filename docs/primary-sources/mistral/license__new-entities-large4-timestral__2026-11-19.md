# Licence texts for releases NOT tracked by the mistral or mistral-research-license entries (read 2026-11-19)

- **doc_type:** license
- **status:** recorded for the lead agent; these models are new entities and are not scored or described in the tracked entries
- **retrieval_date:** 2026-11-19
- **exists:** yes
- **retrieved:** true (raw LICENSE files, HTTP 200)

## A. Mistral Ecosystem Open-Weight License - Mistral-Large-4-1T-A52B and Mistral-Large-4-1T-A52B-NVFP4
source_url: https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B/raw/main/LICENSE (identical file in the NVFP4 repo; sha256 d242ebed...)

"Mistral Ecosystem Open-Weight License. This license is a modified version of the MIT license. Attribution notice: 2026 - Mistral"
Grant: "to deal in the Model without restriction, including without limitation the rights to (a) use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Model; (b) run, deploy, further train or otherwise modify the Model and create derivative works from it".
[1] Copyright and permission notice must be kept in all copies.
[2] "If the Licensee or any of its affiliates operates a Model as a Service business, the Licensee must enter into a separate commercial license with Mistral before using the Model or its derivative works for any commercial purpose."
"Model as a Service" means "giving a third party access to the Model or its derivative works for inference or post-training by any means (for instance via API or hosted endpoints), in a manner that allows such third party to exercise meaningful control over the inputs, parameters, or training data. This does not include (a) end-user products with model capabilities solely embedded within specific features or harnesses, or (b) mere relaying of requests to models hosted by others."
[3] Section 2 does not apply to "(a) internal use of the Model or its derivative works, defined as any use that does not make the Model or its derivative works available to third parties; or (b) any use of the Model accessed through Mistral's official products."

Card (README, front matter `license: other`): "a modified version of the MIT license, for both commercial and non-commercial use - operating a Model-as-a-Service business requires a separate commercial license with Mistral." Card facts: "1 trillion-parameter natively multimodal Mixture-of-Experts model with 49 billion active parameters per token (52 billion including embeddings and output layers)", 1M context, text and image input, repo `gated: false`, created 2026-09-30, technical report PDF in the repo, NVFP4 build created 2026-10-15.

## B. Modified MIT License with a monthly-revenue cap - Timestral-5M, 28M, 123M, 209M and Mistral-Medium-3.5-128B
source_url: https://huggingface.co/mistralai/Timestral-5M/raw/main/LICENSE (identical file, sha256 64819472..., in all four Timestral repos and in Mistral-Medium-3.5-128B)

"Modified MIT License. Attribution notice: 2026 - Mistral AI". MIT-style grant over "the weights of this model and associated documentation files".
[2] "You are not authorized to exercise any rights under this license if the global consolidated monthly revenue of your company (or that of your employer) exceeds $20 million (or its equivalent in another currency) for the preceding month. This restriction in (b) applies to the Model and any derivatives, modifications, or combined works based on it, whether provided by Mistral AI or by a third party. You may contact Mistral AI (sales@mistral.ai) to request a commercial license, which Mistral AI may grant you at its sole discretion, or choose to use the Model on Mistral AI's hosted services available at https://mistral.ai/."

Drafting defect: the clause refers to "This restriction in (b)" but the licence has no sub-clause (b). The cap is on the licensee's (or employer's) own company revenue, not on a deployment, and it reaches derivatives made by third parties. It is not the Apache-style "no field-of-use" grant, and a revenue cap is a field-of-use style restriction that the Open Source Definition does not allow, so this is not an OSI-approved licence.

Timestral card: `library_name: timestral`, `license: other`, "Models have been released under a Modified MIT license"; sizes 5,208,960 / 27,821,184 / 122,606,720 / 209,312,256 parameters; time-series foundation models for zero-shot forecasting; repos `gated: false`, created 2026-10-14. Card sentence: "You must not use this model in a manner that infringes, misappropriates, or otherwise violates any third party's rights".

## C. Same Modified MIT text, 2025 attribution - Devstral-2-123B-Instruct-2512
source_url: https://huggingface.co/mistralai/Devstral-2-123B-Instruct-2512/raw/main/LICENSE (sha256 867daee3...). Same $20 million monthly-revenue clause; attribution notice reads "2025 - Mistral AI". Devstral-Small-2-24B-Instruct-2512 is Apache-2.0.

## D. Other recent tags
Voxtral-4B-TTS-2603: `cc-by-nc-4.0` (HF tag; card not read). LIDstral-Arabic: `apache-2.0`. Voxtral-Mini-4B-Realtime-Arabic: card licence section says Apache 2.0 (no HF tag).
