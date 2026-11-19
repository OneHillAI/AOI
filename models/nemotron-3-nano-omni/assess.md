# Assess - NVIDIA Nemotron 3 Nano Omni (multimodal)

_Openness, licence, provenance, EU AI Act position, safety, evaluation and the AOI score._

<!-- item: intended-use -->
## Intended & out-of-scope use

Nemotron 3 Nano Omni is the multimodal member of the family: 31B total / roughly 3B active, a
Mamba2-Transformer hybrid Mixture-of-Experts that takes video, audio, image and text in and
returns text, with a 256k-token context. It is intended for small, portable, multimodal
reasoning and agentic work where an open, permissively licensed model is wanted.

Autonomous deployment without a self-run red-team of the multimodal input path is out of scope,
because there is no model-level safety evaluation and the video/audio/image surface widens the
misuse path. Ordinary commercial use and modification are unencumbered: the licence is
irrevocable and carries no field-of-use restriction.

<!-- item: limitations -->
## Known limitations, bias & failure modes

The openness posture is weaker than the rest of the family. Unlike the Super/Nano/Ultra cards,
the Nano Omni card does not carry the "open weights, training data, and recipes"
self-description. It links only an image-training dataset and a deploy cookbook, and the model
is classified `open_weights`, not `open_weights_recipe`.

There is no model-level safety evaluation. Safety is post-training data curation only, over a
wider multimodal misuse surface.

A recipe exists in the NeMo repo, but it surfaces only the public subset of the alignment
corpus, so full reproduction is not possible.

The NVIDIA Open Model Agreement's version line is "v. March 9, 2026" in both the HTML and the
PDF, but the web page header shows a release date of April 2, 2026. The operative text is the
same either way.

The offsetting advantage is a small, portable, natively multimodal model under a clean
irrevocable licence.

<!-- item: openness -->
## Openness tier & components

Nano Omni is `open_weights` (tier 3). The weights are ungated safetensors, with a model card and
a clear licence. The card does not carry the family's open-data/recipe self-description and links
only an image-training dataset and a TensorRT-LLM deploy cookbook.

A training recipe exists in the NeMo repo (`docs/nemotron/omni3`, SFT then RL), but it surfaces
only the public subset of the alignment corpus, and the card signals do not carry the recipe
claim. On card signals this is open_weights, not open_weights_recipe: the repo recipe alone does
not raise the tier.

<!-- item: license -->
## License terms & permitted use

Nano Omni is governed by the NVIDIA Open Model Agreement (v. March 9, 2026), a third distinct
family licence whose text is near-identical to the NVIDIA Nemotron Open Model License. It is
Apache-2.0-derived and permissive: a "perpetual, worldwide, non-exclusive, no-charge,
royalty-free, irrevocable license to reproduce, prepare Derivative Works of ... sublicense, and
distribute the Work ... in source or object form". Commercial use is allowed, and the
Trustworthy-AI, acceptable-use and guardrail clauses are absent.

The licence terminates only if the licensee brings patent or copyright litigation over the Work
or an output from it. It is source-available and not OSI. The text is identical in the HTML and
the PDF and matches the Nemotron Open Model License apart from the attribution notice. Both
formats end "(v. March 9, 2026)"; the April 2, 2026 date appears only in the HTML header and the
PDF file name.

Section 7 ends with a general indemnity ("You will indemnify and hold harmless NVIDIA from and
against any claim by any third party arising out of or related to your use or distribution of the
Works"). It is a liability term and not a use restriction. These terms underlie the legal score
of 3.

<!-- item: provenance -->
## Supply-chain & provenance

Weights are distributed from the verified `nvidia` org on Hugging Face as ungated safetensors
with an official BF16 variant. The repo id (`nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16`)
has no "NVIDIA-" prefix, unlike its siblings, so pin the exact path. The checkpoint trust
checklist scores about 4/8. Published checksums, checkpoint scanning and a signing/attestation
policy are not verified, which is why provenance is a 3. Pin the exact revision and verify
checksums.

<!-- item: eu-ai-act -->
## EU AI Act posture

Nano Omni is GPAI. The licence is irrevocable with no acceptable-use restriction, but there is no
formal EU GPAI documentation package and no copyright policy, and NVIDIA is not a Code of
Practice signatory. The open-data posture is weaker than the rest of the family. A non-OSI
licence with a weaker open-data posture most likely does not reach the open-source exemption
cleanly.

Training compute is undisclosed, but at 31B / ~3B active on ~717B tokens a systemic-risk
designation is not indicated. An EU deployer must also weigh the multimodal input surface.

<!-- item: evaluation -->
## Benchmarks & evaluation

Nano Omni is a small multimodal reasoning model, competitive for its class and modality. OneHill
has not run its own benchmarks, and no independent third-party re-runs of the multimodal
benchmarks are aggregated, so the figures are publisher and architectural (the model card). The
item is marked partial and holds the performance dimension at 3.

<!-- item: safety-eval -->
## Independent safety evaluation

There is no dedicated model-level safety evaluation for Nano Omni, and its multimodal input
surface (video/audio/image) widens the misuse path without a published characterisation. Safety
is post-training data curation only. The Nemotron-3-Content-Safety classifier is multimodal (text
and images) and so is partly attributable, and NeMo Guardrails and garak are Apache-2.0. That
downloadable stack holds the safety dimension at 3 and not 2, while the missing model-level
evaluation over the wider surface holds it below 4. The guard-classifier scores are NVIDIA
self-reported.

The model's `safety.md` subcard says safety evaluations were run with AEGIS v2, Garak, RTVLM and
VLGuard plus custom child-safety and dehumanization datasets. It describes an AEGIS 1.0 gate of
at least 95 percent with zero sexual-minor items, runs with reasoning on and off, and an
over-refusal evaluation. It publishes no scores, per-category results or residual-risk
disclosure, and NVIDIA ran it. This is a self-reported process statement, not a published
evaluation, and a published result table would justify a higher safety score.
