# glm - primary-source clauses (2026-07-25)

## _sources.md (index)
```
doc_type | source_url | retrieval_date | exists | retrieved | notes
license | https://huggingface.co/zai-org/GLM-5.2/resolve/main/LICENSE | 2026-07-25 | yes | true | ACTUAL MIT LICENSE file (Copyright 2026 Zhipu AI); confirms family MIT is real
license | https://huggingface.co/zai-org/GLM-4.6 (+4.5, +GLM-4-32B-0414) | 2026-07-25 | unknown(no LICENSE file) | true(metadata) | MIT via metadata/README; no in-repo LICENSE file (raw/blob 404)
license | https://huggingface.co/THUDM/glm-4-9b/raw/main/LICENSE | 2026-07-25 | yes | true | custom "glm-4" license; PRC law/Haidian court; commercial registration + "Built with glm-4"
terms | https://chat.z.ai/legal-agreement/terms-of-service | 2026-07-25 | yes | true | Singapore law/SIAC; individual vs API content-use split
privacy_policy | https://chat.z.ai/legal-agreement/privacy-policy | 2026-07-25 | yes | true | Singapore processing; API content not stored
model_card | https://huggingface.co/zai-org | 2026-07-25 | yes | true(low-confidence) | org listing conflicts with verified per-model pages
```

## license MIT - GLM-5.2 (real LICENSE file)
source_url: huggingface.co/zai-org/GLM-5.2/resolve/main/LICENSE | exists: yes | retrieved: true
Standard MIT, no custom clauses. "Copyright (c) 2026 Zhipu AI." Resolves the earlier 4.5/4.6/0414 metadata-only gap: a sibling ships a real MIT file, confirming the family's MIT is genuine.

## license MIT - GLM-4.5/4.6/0414 (metadata only)
source_url: huggingface.co/zai-org/GLM-4.6 (+4.5, +GLM-4-32B-0414) | exists: unknown (no in-repo LICENSE file) | retrieved: true(metadata)
[File-tree] GLM-4.6 raw/blob LICENSE 404; no LICENSE file in tree. [Metadata/README] "License: mit" on all three; GLM-4.5 README: "They are released under the MIT open-source license and can be used commercially and for secondary development."

## license custom "glm-4" - glm-4-9b (NOT plain MIT)
source_url: huggingface.co/THUDM/glm-4-9b/raw/main/LICENSE | exists: yes | retrieved: true
[Sec 2] "a non-exclusive, worldwide, non-transferable, non-sublicensable, revocable, royalty-free copyright license." Free for academic research; "Commercial users must complete registration at a specified form to use the model for business purposes." Must display "Built with glm-4" prominently; "AI models created using glm-4 materials should include 'glm-4' at the beginning of the model name." [Sec 3] no use "for any military or illegal purposes"; no endangering national security/unity. [Sec 6] "governed and construed in accordance with the laws of People's Republic of China," disputes to "Beijing's Haidian District People's Court." Contact license@zhipuai.cn. These commercial-registration, "Built with glm-4", name-prefix, and PRC-law/Haidian-court clauses are what make it NOT plain MIT.

## terms - Z.ai
source_url: chat.z.ai/legal-agreement/terms-of-service | exists: yes | retrieved: true
[Individual] broad perpetual license to use User Content to improve services. [API/enterprise] "We will not use End User Content for developing or improving Services, unless you explicitly agree." [Jurisdiction] Singapore law; SIAC arbitration (seat Singapore). NOTE: Singapore, NOT PRC - differs from glm-4-9b weights license.

## privacy_policy - Z.ai
source_url: chat.z.ai/legal-agreement/privacy-policy | exists: yes | retrieved: true
[Training consumer] "when we train and improve our models." [API carve-out] content "not saved on our servers." [Location] Singapore processing.

## model_card - zai-org org page (low confidence)
source_url: huggingface.co/zai-org | exists: yes | retrieved: true(low-confidence)
Org listing render conflicted with verified per-model pages; treat per-model findings (4.5/4.6/0414 = MIT; glm-4-9b = custom) as the reliable data.
