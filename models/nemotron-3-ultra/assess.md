# Assess - NVIDIA Nemotron 3 Ultra (550B)

_Should we adopt this? Openness, license, provenance, EU AI Act, safety, evaluation, and
the AOI score live here._

<!-- item: intended-use -->
## Intended & out-of-scope use

Nemotron 3 Ultra is the frontier-scale head of the family: 550B total / 55B active, a Mamba2-Transformer
hybrid Latent Mixture-of-Experts with Multi-Token Prediction, a context window up to 1M tokens. Its
intended use is complex agentic workflows, long-context analysis and high-end reasoning where you want
an open, maximally-permissively-licensed model and can run a multi-node cluster.

Out of scope: EU high-stakes deployment until the systemic-risk position is resolved. Training compute
is undisclosed, so whether Ultra crosses the 1e25-FLOP threshold cannot be established. Because the
licence (OpenMDW-1.1) grants use "without restriction", the gating questions are hardware, safety
assurance and systemic-risk status, not permission.

<!-- item: limitations -->
## Known limitations, bias & failure modes

- **Representative recipe, not reproducible.** The released Ultra recipe is "a representative single
  pass"; its intermediate checkpoints "have not been open-sourced" and the 1M-context phase is
  excluded because its data "is not open-source".
- **No dedicated model-level safety evaluation.** The White Paper's "Evaluation, Safety and Release"
  section is a contributor list; safety appears only as post-training data curation.
- **Undisclosed training compute.** Only "approximately 20 trillion tokens" is stated, so the EU
  systemic-risk crossing is undeterminable.
- **Multi-node hardware.** At 550B / 55B active there is no small-variant portability; it is a
  multi-GPU / multi-node deployment.

The offsetting advantage is the most permissive licence in the family and genuine open-weights-recipe
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
It is **not OSI-approved** only because v1.1 is not yet on the OSI approved list. This "without
restriction" grant is what makes Ultra's use-and-modify and data-control factors strong.

<!-- item: provenance -->
## Supply-chain & provenance

Weights are distributed from the **verified `nvidia` org** on Hugging Face as **ungated safetensors**,
with official **BF16 / NVFP4** quantization variants and a clear canonical source. The checkpoint trust
checklist scores about **4/8**: published checksums, checkpoint scanning and a signing/attestation
policy were not verified this pass, which is why provenance is a 3. Pin the exact revision and verify
checksums.

<!-- item: eu-ai-act -->
## EU AI Act posture

Ultra is **GPAI**. Its OpenMDW licence is maximally permissive, but the EU information base is the same
as the rest of the family: **no formal GPAI documentation package, no copyright policy**, and NVIDIA is
**not a Code of Practice signatory**. The decisive issue is **systemic risk**: training compute is
undisclosed, so whether a 550B / 55B-active model trained on ~20T tokens crosses the **1e25-FLOP**
threshold is **undeterminable**. An EU deployer should treat systemic-risk status as unresolved before
high-stakes use.

<!-- item: evaluation -->
## Benchmarks & evaluation

Ultra is a frontier-scale open model (550B / 55B active, hybrid Mamba2-Transformer LatentMoE, up to 1M
context, ~20T tokens). OneHill did **not** run its own benchmarks this pass, and no independent
third-party re-runs were gathered, so the figures are publisher and architectural (white paper + card).
This is marked *partial* and holds the performance dimension at 3.

<!-- item: safety-eval -->
## Independent safety evaluation

There is **no dedicated model-level safety evaluation** for Ultra: the White Paper's "Evaluation, Safety
and Release" section is a contributor list, and safety otherwise appears only as post-training data
curation (Nemotron Content Safety v2, Gretel refusal data, keyword/regex filtering). The downloadable
**family guard stack** - the Nemotron-3-Content-Safety classifier, Apache-2.0 NeMo Guardrails, and
Apache-2.0 garak - is genuinely attributable and is what holds the safety dimension at 3 rather than 2;
the missing model-level evaluation holds it below 4. The guard-classifier scores are NVIDIA
self-reported.
