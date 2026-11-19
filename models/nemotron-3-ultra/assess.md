# Assess - NVIDIA Nemotron 3 Ultra (550B)

_Openness, licence, provenance, EU AI Act position, safety, evaluation and the AOI score._

<!-- item: intended-use -->
## Intended & out-of-scope use

Nemotron 3 Ultra is the frontier-scale head of the family: 550B total / 55B active, a Mamba2-Transformer
hybrid Latent Mixture-of-Experts with Multi-Token Prediction, a context window up to 1M tokens. Its
intended use is complex agentic workflows, long-context analysis and high-end reasoning where you want
an open, maximally-permissively-licensed model and can run a multi-node cluster.

Out of scope: EU high-stakes deployment until the systemic-risk position is resolved. Training compute
is undisclosed, so whether Ultra crosses the 1e25-FLOP threshold cannot be established. The licence
(OpenMDW-1.1) grants use "without restriction", so the gating questions are hardware, safety
assurance and systemic-risk status.

<!-- item: limitations -->
## Known limitations, bias & failure modes

The released Ultra recipe is "a representative single pass". Its intermediate checkpoints "have not
been open-sourced" and the 1M-context phase is excluded because its data "is not open-source", so the
model is not reproducible. There is no dedicated model-level safety evaluation: the White Paper's
"Evaluation, Safety and Release" section is a contributor list, and safety appears only as
post-training data curation. Only "approximately 20 trillion tokens" is stated for training compute,
so the EU systemic-risk crossing is undeterminable. At 550B / 55B active there is no small-variant
portability, and Ultra is a multi-GPU / multi-node deployment.

The offsetting advantages are the most permissive licence in the family and open-weights-recipe
transparency.

<!-- item: openness -->
## Openness tier & components

Ultra is `open_weights_recipe` (tier 4). **Weights** are ungated safetensors, **training code** is a
representative recipe (Pretrain -> SFT -> MOPD -> Quant), the **documentation** includes a white paper,
and **post-training data** is CC-BY-4.0. It stops short of `fully_open` because the recipe is explicitly
representative: the **intermediate checkpoints** it depends on are not open-sourced, and the 1M-context
data is not open, so the model is not fully reproducible.

<!-- item: license -->
## License terms & permitted use

Ultra is governed by the **OpenMDW License Agreement v1.1 (OpenMDW-1.1)**, authored by the OpenMDW
project under the Linux Foundation and adopted by NVIDIA. It is the **most permissive** of the three
Nemotron 3 licences: the grant is "permission is hereby granted, free of charge, to deal in the Model
Materials without restriction", covering weights, data, documentation and software together. Commercial
use is allowed with no field-of-use limit. The only condition is a **defensive** termination that fires
if the licensee brings, maintains or voluntarily joins a patent or copyright infringement lawsuit over
the Model Materials, with an explicit carve-out where that suit answered one brought first against them.
It is **not OSI-approved** because v1.1 is not on the OSI approved list. This "without
restriction" grant is what makes Ultra's use-and-modify and data-control factors strong.

The raw licence file has no acceptable-use, guardrail or revocation clause. OpenMDW-1.1 was submitted
for OSI review in August 2026 and no approval is listed, so it is recorded as not OSI-approved.

<!-- item: provenance -->
## Supply-chain & provenance

Weights are distributed from the **verified `nvidia` org** on Hugging Face as **ungated safetensors**,
with official **BF16 / NVFP4** quantization variants and a clear canonical source. The checkpoint trust
checklist scores about **4/8**: published checksums, checkpoint scanning and a signing/attestation
policy are not verified, which is why provenance is a 3. Pin the exact revision and verify
checksums.

<!-- item: eu-ai-act -->
## EU AI Act posture

Ultra is **GPAI**. Its OpenMDW licence is maximally permissive, but the EU information base is the same
as the rest of the family: **no formal GPAI documentation package, no copyright policy**, and NVIDIA is
**not a Code of Practice signatory**. The open issue is **systemic risk**: training compute is
undisclosed, so whether a 550B / 55B-active model trained on ~20T tokens crosses the **1e25-FLOP**
threshold is **undeterminable**. An EU deployer should treat systemic-risk status as unresolved before
high-stakes use.

<!-- item: evaluation -->
## Benchmarks & evaluation

Ultra is a frontier-scale open model (550B / 55B active, hybrid Mamba2-Transformer LatentMoE, up to 1M
context, ~20T tokens). OneHill has **not** run its own benchmarks, and no independent third-party
re-runs exist, so the figures are publisher and architectural (white paper + card). This is marked
*partial* and holds the performance dimension at 3.

<!-- item: safety-eval -->
## Independent safety evaluation

There is **no dedicated model-level safety evaluation** for Ultra: the White Paper's "Evaluation, Safety
and Release" section is a contributor list, and safety otherwise appears only as post-training data
curation (Nemotron Content Safety v2, Gretel refusal data, keyword/regex filtering). The downloadable
**family guard stack** - the Nemotron-3-Content-Safety classifier, Apache-2.0 NeMo Guardrails, and
Apache-2.0 garak - is attributable to Ultra and holds the safety dimension at 3, not 2. The missing
model-level evaluation holds it below 4. The guard-classifier scores are NVIDIA self-reported.

Ultra has a dedicated technical report (arXiv 2606.15007, June 2026). Its safety content is
training-side: a safety SFT blend translated into six languages and an "agentic safety teacher"
trained against indirect prompt injection with an automated red-teaming loop. It publishes no
benchmark results, jailbreak results or residual-risk disclosure, and the `safety.md` subcard gives
no scores either. There is no published model-level safety evaluation.
