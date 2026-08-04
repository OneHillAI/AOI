# Assess - NVIDIA Nemotron 3 (Super + Nano)

_Should we adopt this? Openness, license, provenance, EU AI Act, safety, evaluation, and
the AOI score live here._

<!-- item: intended-use -->
## Intended & out-of-scope use

Nemotron 3 Super (120B / 12B active) and Nano (30B / 3.5B active) are the text flagships of NVIDIA's
open, agent-focused hybrid Mamba-Transformer family, both with a context window up to 1M tokens.
Their intended use is general-purpose reasoning, chat, coding and agentic workloads where you want
open weights, runnable recipes and a downloadable guard model, and where a portable small variant
matters.

Out of scope: autonomous or high-stakes deployment without a self-run red-team, because there is no
published model-level safety evaluation to lean on. Ordinary commercial use and modification are
unencumbered - the governing licence is irrevocable and carries no field-of-use restriction - so the
gating question is safety assurance, not permission.

<!-- item: limitations -->
## Known limitations, bias & failure modes

- **Partial corpus, not reproducible.** The official recipes "train exclusively on the open-sourced
  subset of training data", so you can adapt but not reproduce the model.
- **No published model-level safety evaluation.** Safety appears only as post-training data curation
  (a Nemotron-SFT-Safety dataset plus keyword/regex filtering); the base cards carry no safety
  benchmarks and the white paper's safety section is a contributor list.
- **Publisher-reported performance.** Frontier-scale claims come from the cards and white paper;
  OneHill has not reproduced them and no independent re-runs were gathered this pass.
- **Non-OSI licence.** The grant is clean and irrevocable, but it is Apache-2.0-derived rather than
  OSI-approved, and redistribution must carry the NVIDIA attribution notice.

The offsetting advantage is genuine openness plus a real, downloadable safety stack you can assemble
yourself.

<!-- item: openness -->
## Openness tier & components

Super and Nano are `open_weights_recipe` (tier 4), materially more open than the open-weights norm.
**Weights** are ungated safetensors, **training code** is released as runnable recipes, the
**documentation** includes a white paper, and **post-training data** is genuinely CC-BY-4.0. They
stop short of `fully_open` because the **training data** is only partially released: the recipes
train on the open subset only, and the pretraining web corpus (Nemotron-CC-v2.1) sits under a custom
NVIDIA data licence, so the full model is not reproducible.

<!-- item: license -->
## License terms & permitted use

Both models are governed by the **NVIDIA Nemotron Open Model License (v. 2025-12-15)**. On the
corrected reading it is Apache-2.0-derived and genuinely permissive: a "perpetual, worldwide,
non-exclusive, no-charge, royalty-free, irrevocable license to reproduce, prepare Derivative Works
of, publicly display, publicly perform, sublicense, and distribute the Work ... in source or object
form", with commercial use allowed and **no** Trustworthy-AI clause, **no** acceptable-use or
field-of-use restriction and **no** guardrail clause. It terminates **only** if the licensee
institutes patent or copyright litigation alleging that the Work or an output from it infringes.
Redistribution must carry the notice "Licensed by NVIDIA Corporation under the NVIDIA Nemotron Model
License". It is source-available and **not OSI** (the termination reaching an output from the Work is
broader than Apache-2.0). These are the load-bearing inputs to the legal (3) score.

<!-- item: provenance -->
## Supply-chain & provenance

Weights are distributed from the **verified `nvidia` org** on Hugging Face as **ungated
safetensors**, with official **BF16 / FP8 / NVFP4** quantization variants and a clear canonical
source. The checkpoint trust checklist scores about **4/8**: published checksums, checkpoint scanning
and a signing/attestation policy were not verified this pass, which is why provenance is a 3, not
higher. Gating applies to some training datasets, not the weights. Pin the exact revision and verify
checksums.

<!-- item: eu-ai-act -->
## EU AI Act posture

Super and Nano are **GPAI**. NVIDIA (US-based) publishes more than most - a white paper, runnable
recipes, and partially released, partly CC-BY-4.0 data - and the governing licence is irrevocable
with no acceptable-use restriction. But there is **no formal EU GPAI documentation package, no
copyright policy**, and NVIDIA is **not a Code of Practice signatory**. A non-OSI licence without the
GPAI documentation package most likely **does not** cleanly reach the open-source exemption.
**Training compute is undisclosed** (only tokens), but at ~25T tokens on a 120B / 30B scale a
systemic-risk designation is not indicated for these two models.

<!-- item: evaluation -->
## Benchmarks & evaluation

Super and Nano are a competitive frontier-scale pair (hybrid Mamba-Transformer LatentMoE, up to 1M
context, ~25T training tokens). OneHill did **not** run its own benchmarks this pass, and no
independent third-party re-runs were gathered, so the figures are publisher and architectural (white
paper + cards). This is marked *partial* and holds the performance dimension at 3.

<!-- item: safety-eval -->
## Independent safety evaluation

There is **no published model-level safety evaluation or independent red-team** for Super or Nano:
safety is post-training data curation only. What NVIDIA does ship, at the family level, is a genuinely
downloadable safety stack - the **Nemotron-3-Content-Safety** guard classifier (Gemma-3-4B base, 23
categories / 12 languages), the Apache-2.0 **NeMo Guardrails** toolkit, and the Apache-2.0 **garak**
red-team scanner. That downloadable stack is what holds the safety dimension at 3 rather than 2; the
missing model-level evaluation is what holds it below 4. The guard-classifier scores are NVIDIA
self-reported.
