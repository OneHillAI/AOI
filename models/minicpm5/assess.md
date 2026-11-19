# Assess - MiniCPM5-1B

_Should we adopt this? Openness, licence, provenance, EU AI Act, safety, evaluation, and the AOI score live here._

Decision: adopt MiniCPM5-1B for local assistants, tool-calling agents and fine-tuning on small devices, behind your own safety layer. Do not adopt it for user-facing use on the strength of the publisher benchmark table or the safety text, because neither is backed by anything independent. Scope: this entry is the MiniCPM5-1B release (final, SFT-only and Base checkpoints, plus the official GGUF and MLX conversions). The MiniCPM5-2B release is listed as a follow-up.

<!-- item: intended-use -->
## Intended & out-of-scope use

The publisher positions the model for "local assistants, coding agents, tool-use workflows, and reasoning scenarios where a compact model is preferred" and for "on-device, local deployment, and resource-constrained scenarios" (`ev-card`). The GitHub repository ships a desktop-pet demo that runs it locally (`ev-github`). It is text-only. The card says generated content "should be reviewed and verified before use in high-stakes settings", so high-stakes decisions are out of scope without your own controls. Only English and Chinese are documented.

<!-- item: limitations -->
## Known limitations, bias & failure modes

- **No safety evaluation.** The card's only safety text says the model "may produce inaccurate, biased, or unsafe outputs" and leaves safeguards to the user (`ev-card`).
- **Mixed benchmark rows.** On the publisher's own table the model is behind LFM2.5-1.2B on GPQA-Diamond (26.26 vs 34.85), IFEval (80.41 vs 84.84), Multi-IF (43.54 vs 55.61) and MultiChallenge (19.48 vs 23.28), and behind both Qwen baselines on BFCLv4 (25.15 vs 25.43 and 25.53) (`ev-bench`).
- **Small-model capacity.** A 1.08B model scores 48.85 on MMLU-Pro in that table; expect weak factual recall and long-tail knowledge.
- **Two languages.** The card lists English and Chinese; nothing else is documented or evaluated.
- **Synthetic-data lineage.** The decay-phase pretraining tier was synthesised with MiniCPM4 and Qwen3 (`ev-datasets`), so the model inherits those generators' errors and biases.

<!-- item: openness -->
## Openness tier & components

`open_weights_recipe`, as a judgement call between the 3 and 4 anchors. What is open: Apache-2.0 weights at four stages (Base, SFT-only, final, plus official GGUF and MLX), a recipe description on the card, and three pretraining datasets that the card names as the training corpus and that are public and Apache-2.0 tagged on the Hub: Ultra-FineWeb, Ultra-FineWeb-L3 and UltraData-Math (`ev-card`, `ev-datasets`). That is more training data than most open-weight models release. What is not: the SFT dataset UltraData-SFT-2605 sits behind an automatic Hub access gate and its card could not be read (`ev-sft-dataset`); the synthesised RLVR data and the pairwise RLHF data are not linked; the repository holds user-side fine-tuning and quantisation scripts but no pretraining, RL or OPD pipeline and no evaluation harness (`ev-github`); and there is no MiniCPM5 technical report, because the card's "Tech Report" link is the MiniCPM4 paper (`ev-papers`). Components: weights open, licence open, training data partial, training code partial, evaluation partial, documentation partial.

<!-- item: license -->
## License terms & permitted use

Apache License 2.0 for all MiniCPM5 checkpoints. The GitHub LICENSE file was line-compared with the canonical apache.org text; only the copyright line differs ("Copyright [OpenBMB]"), so there is no field-of-use, scale, branding or registration clause (`ev-license`). The Hub metadata of the 1B and 2B families all read apache-2.0 and ungated (`ev-license-meta`). Commercial use, modification, redistribution and sublicensing are permitted under the standard Apache terms (attribution, notice, patent grant and termination).

Two things to know. First, the LICENSE file is in the GitHub code repository; the Hub model repository has no LICENSE file and relies on the card sentence and metadata. Keep a copy of the GitHub file with any redistribution. Second, earlier MiniCPM generations (the 2B and V-2 era) had their weights under a custom General Model License that required commercial authorisation by registration (`ev-legacy-gml`). The MiniCPM5 README replaced that with Apache-2.0. If you hold an older checkpoint, its terms differ; check before assuming this entry applies. The datasets are also Apache-2.0 tagged, but the Ultra-FineWeb card warns that its source datasets have their own licences (`ev-datasets`).

<!-- item: provenance -->
## Supply-chain & provenance

Canonical source: huggingface.co/openbmb/MiniCPM5-1B, linked from the OpenBMB/MiniCPM GitHub README. The openbmb Hub org is not verified (`isVerified: false`), so identity rests on the GitHub cross-links and on Artificial Analysis attributing the model to OpenBMB (`ev-repo-files`, `ev-aa`). Weights are a single safetensors shard with an LFS sha256; there is no pickle file. The Hub's own scan reports no flagged files. There is no signature or attestation. Official GGUF (F16, Q8_0, Q4_K_M) and MLX 4-bit conversions come from the same org; many community conversions exist, including repos named "Uncensored", which were not inspected. Data lineage: Ultra-FineWeb-L3 was generated with MiniCPM4 and Qwen3, and the math selection used unnamed proprietary models (`ev-datasets`). Checkpoint checklist: 5 of 8.

<!-- item: eu-ai-act -->
## EU AI Act posture

A general-purpose AI model. At 1.08B parameters it would need roughly 1.5 quadrillion training tokens to reach 1e25 FLOPs (6 x parameters x tokens), so it is not a systemic-risk model and no Article 55 package applies. Under Apache-2.0 with public weights it plausibly qualifies for the Article 53 open-source exemption from the Annex XI and XII documentation duties. The surviving duties are a copyright policy and a public training-content summary. OpenBMB states no copyright policy and no EU-specific statement. The dataset cards are public and describe the pretraining sources, which partly serves as a training-content summary, but the SFT card is gated, no pretraining token count is given, and the source-dataset licence caveat applies. Whether OpenBMB or Modelbest has signed the GPAI Code of Practice was not checked. A deployer who fine-tunes and places the result on the EU market may become the provider for that derivative and should document the gaps above.

<!-- item: evaluation -->
## Benchmarks & evaluation

All numbers come from one publisher image on the model card (`ev-bench`): Thinking mode only, against three small thinking-mode models (Qwen3-0.6B, Qwen3.5-0.8B, LFM2.5-1.2B), with no harness or prompt detail and no non-thinking results. Average score 42.57 against 35.61 for LFM2.5-1.2B; MATH-500 91.60; AIME-2025 and AIME-2026 both 40.42; LCB-v6 33.52; MMLU-Pro 48.85; tau2-Bench Telecom 79.53; BFCLv4 25.15. The card says the advantage is most visible in tool use, but on BFCLv4 the model is level with or below the Qwen baselines, so the tool-use lead rests on one benchmark. The comparison set has no Gemma, Llama, SmolLM, Granite or Qwen3-1.7B baseline. Artificial Analysis lists the model but publishes no score (`ev-aa`), and no other independent evaluation was found. Treat the table as an unverified publisher claim and run your own evaluation on your task.

<!-- safety-eval is a `gap` item in entry.yaml - see its gap_reason. No safety, red-team or misuse evaluation was found. -->
