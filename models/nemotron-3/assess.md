# Assess - NVIDIA Nemotron 3 (Super + Nano)

_Openness, licence, provenance, EU AI Act position, safety, evaluation and the AOI score._

<!-- item: intended-use -->
## Intended & out-of-scope use

Nemotron 3 Super (120B / 12B active) and Nano (30B / 3.5B active) are the text flagships of NVIDIA's open, agent-focused hybrid Mamba-Transformer family, both with a context window up to 1M tokens. Their intended use is general-purpose reasoning, chat, coding and agentic workloads where you want open weights, runnable recipes and a downloadable guard model, and where a portable small variant matters.

Autonomous or high-stakes deployment is out of scope without a self-run red-team, because no model-level safety evaluation is published. Ordinary commercial use and modification are unencumbered: the governing licence is irrevocable and carries no field-of-use restriction. The open question is safety assurance.

<!-- item: limitations -->
## Known limitations, bias & failure modes

The corpus is partial, so the model is not reproducible. The official recipes "train exclusively on the open-sourced subset of training data", so the model can be adapted and not reproduced.

No model-level safety evaluation is published. Safety appears only as post-training data curation (a Nemotron-SFT-Safety dataset plus keyword/regex filtering). The base cards carry no safety benchmarks, and the white paper's safety section is a contributor list.

Performance is publisher-reported. Frontier-scale claims come from the cards and white paper. OneHill has not reproduced them, and no independent re-runs exist.

The licence is not OSI-approved. The grant is irrevocable, but the licence is Apache-2.0-derived and redistribution must carry the NVIDIA attribution notice.

The offset is a downloadable safety stack that a deployer can assemble.

<!-- item: openness -->
## Openness tier & components

Super and Nano are `open_weights_recipe` (tier 4), materially more open than the open-weights norm. Weights are ungated safetensors, training code is released as runnable recipes, documentation includes a white paper, and post-training data is CC-BY-4.0. They fall short of `fully_open` because the training data is only partially released. The recipes train on the open subset only, and the pretraining web corpus (Nemotron-CC-v2.1) sits under a custom NVIDIA data licence, so the full model is not reproducible.

<!-- item: license -->
## License terms & permitted use

Both models are governed by the NVIDIA Nemotron Open Model License (v. 2025-12-15). It is Apache-2.0-derived and permissive: a "perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable license to reproduce, prepare Derivative Works of, publicly display, publicly perform, sublicense, and distribute the Work ... in source or object form". Commercial use is allowed. There is no Trustworthy-AI clause, no acceptable-use or field-of-use restriction and no guardrail clause.

The licence terminates only if the licensee institutes patent or copyright litigation alleging that the Work or an output from it infringes. Redistribution must carry the notice "Licensed by NVIDIA Corporation under the NVIDIA Nemotron Model License". The licence is source-available and not OSI, because a termination reaching an output from the Work is broader than Apache-2.0. These terms drive the legal score of 3.

The licence text was last modified December 15, 2025. Section 7 ends with a general indemnity: "You will indemnify and hold harmless NVIDIA from and against any claim by any third party arising out of or related to your use or distribution of the Works". That is a liability term and not a use restriction.

The Nano repo's `safety.md` subcard links the generic NVIDIA Open Model License (revocable, with a guardrail termination) under "Use Case Restrictions". The Nano README, the Hugging Face licence tag and the licence link all name the Nemotron Open Model License. The README and tag govern, and the subcard link is probably an error on NVIDIA's side. Pin the licence text downloaded with the weights.

<!-- item: provenance -->
## Supply-chain & provenance

Weights are distributed from the verified `nvidia` org on Hugging Face as ungated safetensors, with official BF16 / FP8 / NVFP4 quantization variants and a clear canonical source. The checkpoint trust checklist scores about 4/8. Published checksums, checkpoint scanning and a signing/attestation policy are unconfirmed, which is why provenance is a 3 and not higher. Gating applies to some training datasets and not to the weights. Pin the exact revision and verify checksums.

<!-- item: eu-ai-act -->
## EU AI Act posture

Super and Nano are GPAI. NVIDIA (US-based) publishes more than most: a white paper, runnable recipes, and partially released, partly CC-BY-4.0 data. The governing licence is irrevocable with no acceptable-use restriction. But there is no formal EU GPAI documentation package and no copyright policy, and NVIDIA is not a Code of Practice signatory. A non-OSI licence without the GPAI documentation package most likely does not cleanly reach the open-source exemption.

Training compute is undisclosed (only tokens). At ~25T tokens on a 120B / 30B scale, a systemic-risk designation is not indicated for these two models.

<!-- item: evaluation -->
## Benchmarks & evaluation

Super and Nano are a competitive frontier-scale pair (hybrid Mamba-Transformer LatentMoE, up to 1M context, ~25T training tokens). OneHill has not run its own benchmarks, and no independent third-party re-runs exist, so the figures are publisher and architectural (white paper and cards). The evaluation is marked partial and holds the performance dimension at 3.

<!-- item: safety-eval -->
## Independent safety evaluation

There is no published model-level safety evaluation or independent red-team for Super or Nano. Safety is post-training data curation only. At the family level NVIDIA ships a downloadable safety stack: the Nemotron-3-Content-Safety guard classifier (Gemma-3-4B base, 23 categories / 12 languages), the Apache-2.0 NeMo Guardrails toolkit, and the Apache-2.0 garak red-team scanner. That stack holds the safety dimension at 3 and not 2. The missing model-level evaluation holds it below 4. The guard-classifier scores are NVIDIA self-reported.

The Super and Nano `safety.md` subcards publish no scores. They say a guard model filtered the training data and that content-safety evaluation uses Nemotron Content Safety Dataset V2 plus an internal dataset. A newer 4B guard, Nemotron-3.5-Content-Safety (OpenMDW licence, created 2026-05-22), is also downloadable. It is a companion classifier and not an evaluation of these two models.
