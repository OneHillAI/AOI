doc_type: license
entity: glm-5 (NEW - licence-divergent from the tracked `glm` MIT cluster)
source_url: https://huggingface.co/zai-org (GLM-5 / 5.1 / 5.2 / 5.3 / 5.3-Flash) ; GLM-5.3 License
document_effective_date: GLM-5 generation, 2026
retrieval_date: 2026-09-21
exists: yes
retrieved: true
tag: publisher

## What moved
Z.ai/Zhipu has shipped a **GLM-5 generation** - **GLM-5, GLM-5.1, GLM-5.2, GLM-5.3, GLM-5.3-Flash** - governed by a **custom "GLM-5.3 License"** that is materially different from the MIT-cluster licence the tracked `glm` entry records.

## Load-bearing term
The GLM-5.3 License adds a **Model-as-a-Service security-review gate**: above a large MaaS scale threshold (reported at the **$10B** level) the licensee is required to undergo a **security review**. This is a governance restriction on commercial deployment at scale - analogous in shape to the Kimi K3 / GLM-5.3 MaaS gates - and it does not exist in the MIT-cluster GLM entry.

## Recommendation (for the code session - do not fold)
Create a **new `glm-5` entity/family split** rather than updating the MIT `glm` entry. The licence divergence (custom GLM-5.3 License + MaaS security-review gate vs MIT) is exactly the kind of split AOI already uses elsewhere (mistral apache/mrl/mnpl; deepseek mit/original). `use_modify` for `glm-5` is gated by the security-review clause and should be scored separately from the MIT cluster.

retrieved: true - GLM-5 cards + GLM-5.3 License re-read this pass. (The $10B threshold figure should be re-confirmed verbatim from the licence text before it is quoted publicly.)
