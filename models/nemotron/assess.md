# Assess - NVIDIA Nemotron 3

_Should we adopt this? Openness, license, provenance, EU AI Act, safety, evaluation, and
the AOI score live here._

<!-- item: intended-use -->
## Intended & out-of-scope use

Nemotron 3 is NVIDIA's open, agent-focused family across a real size ladder: Nano (30B / 3.5B
active), Super (120B / 12B), Ultra (550B / 55B) and the multimodal Nano Omni (31B / ~3B), most
with up to a 1M-token context. Its intended use is general-purpose reasoning, chat and agentic
workloads where you want open weights, runnable recipes and downloadable safety tooling, and where
a portable small variant matters.

Out of scope: EU high-stakes or regulated decision-making, especially on Ultra, without
self-assembled compliance and a resolved systemic-risk assessment (training compute is undisclosed).
Because the governing licence is source-available, revocable and split three ways across the
family, confirm the exact variant's licence before shipping.

<!-- item: limitations -->
## Known limitations, bias & failure modes

- **Partial corpus, not reproducible.** The official recipes "train exclusively on the open-sourced
  subset of training data", and NVIDIA's commitment is hedged to "all data for which we hold
  redistribution rights", so you can adapt but not reproduce the model.
- **Licence split and revocability.** Three source-available (non-OSI) licences across the family;
  the base NVIDIA grant is revocable, carries a Trustworthy-AI use restriction, and auto-terminates
  on guardrail circumvention or IP litigation.
- **Self-reported safety.** The guard-classifier and model-level safety scores are NVIDIA
  self-reported, with no independent third-party red-team, and the base card lacks a filled safety
  section.
- **Undisclosed training compute.** No FLOP figure is published, so Ultra's EU systemic-risk status
  cannot be resolved.

The offsetting advantage is genuine openness plus a real safety stack, rare together in one family.

<!-- item: openness -->
## Openness tier & components

Nemotron 3 is `open_weights_recipe` (tier 4), materially more open than the open-weights norm.
**Weights** are ungated safetensors, **training code** is released as runnable recipes, the
**documentation** includes a white paper, and **post-training data** is genuinely CC-BY-4.0. It
stops short of `fully_open` because the **training data** is only partially released: the recipes
train on the open subset only, and the pretraining web corpus (Nemotron-CC-v2.1) sits under a
custom NVIDIA data licence, so the full model is not reproducible.

<!-- item: license -->
## License terms & permitted use

The licence is **not shared across the family** - three source-available, non-OSI licences: the
**NVIDIA Nemotron Open Model License** (Super, Nano), **OpenMDW 1.1** (Ultra), and the **NVIDIA
Open Model Agreement** (Nano Omni). The base NVIDIA Open Model License is highly permissive
commercially - "perpetual, worldwide, non-exclusive, no-charge, royalty-free, revocable" rights to
use, modify, sell and distribute, and NVIDIA "claims no ownership rights in outputs". The catch is
in the conditions: the grant is **revocable**, use "must be consistent with NVIDIA's Trustworthy AI
terms", and it **auto-terminates** if you circumvent safety guardrails or initiate IP litigation
over the Model. Confirm the exact variant's licence before deployment. These caveats are the
load-bearing input to the legal (3) score.

<!-- item: provenance -->
## Supply-chain & provenance

Weights are distributed from the **verified `nvidia` org** on Hugging Face as **ungated
safetensors**, with official **BF16 / FP8 / NVFP4** quantization variants and a clear canonical
source. The checkpoint trust checklist scores about **4/8**: published checksums, checkpoint
scanning and a signing/attestation policy were not verified this pass, which is why provenance is a
3, not higher. Gating applies to some training datasets, not the weights. Pin the exact revision and
verify checksums.

<!-- item: eu-ai-act -->
## EU AI Act posture

Nemotron 3 is **GPAI**. NVIDIA (US-based) publishes more than most - a white paper, runnable
recipes, and partially released, partly CC-BY-4.0 data - but there is **no formal EU GPAI
documentation package, no copyright policy**, and NVIDIA is **not a Code of Practice signatory**.
The revocable, use-restricted, non-OSI licence most likely **does not** reach the open-source
exemption, and Ultra sits under a different licence again (OpenMDW 1.1). **Training compute is
undisclosed** (only tokens), so whether Ultra 550B crosses the 1e25-FLOP systemic-risk threshold is
**undeterminable**. An EU deployer must map obligations per variant and self-assemble compliance.

<!-- item: evaluation -->
## Benchmarks & evaluation

Nemotron 3 is a competitive frontier-scale family (hybrid Mamba-Transformer LatentMoE, up to 1M
context, ~25T training tokens) presented across a Nano-to-Ultra ladder. OneHill did **not** run its
own benchmarks this pass, and no independent third-party re-runs were gathered, so the figures are
publisher and architectural (white paper + cards). This is marked *partial* and holds the
performance dimension at 3: capable and well-documented, but class-leading claims are not
independently verified.

<!-- item: safety-eval -->
## Independent safety evaluation

Unusually for an open family, NVIDIA ships a real, downloadable safety stack: guard/moderation
classifiers (**Nemotron-3-Content-Safety** on Gemma-3-4B, 23 categories / 12 languages; **Aegis**),
the Apache-2.0 **NeMo Guardrails** programmable-rails toolkit, and the Apache-2.0 **garak** red-team
scanner. The strongest independently verifiable evidence is the artefacts themselves (open cards +
Apache-licensed repos). The caveat: the reported classifier scores are NVIDIA self-reported with no
third-party head-to-head, and the base model card lacks a filled safety/alignment section. This is
a genuine strength (safety 4), short of 5 for want of an independent red-team.
