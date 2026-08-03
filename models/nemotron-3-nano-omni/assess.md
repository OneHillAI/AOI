# Assess - NVIDIA Nemotron 3 Nano Omni (multimodal)

_Should we adopt this? Openness, license, provenance, EU AI Act, safety, evaluation, and
the AOI score live here._

<!-- item: intended-use -->
## Intended & out-of-scope use

Nemotron 3 Nano Omni is the multimodal member of the family: 31B total / roughly 3B active, a
Mamba2-Transformer hybrid Mixture-of-Experts that takes video, audio, image and text in and returns
text, with a 256k-token context. Its intended use is small, portable, multimodal reasoning and agentic
work where you want an open, permissively-licensed model.

Out of scope: autonomous deployment without a self-run red-team of the multimodal input path, because
there is no model-level safety evaluation and the video/audio/image surface widens the misuse path.
Ordinary commercial use and modification are unencumbered - the licence is irrevocable and carries no
field-of-use restriction.

<!-- item: limitations -->
## Known limitations, bias & failure modes

- **Weaker openness posture.** Unlike the Super/Nano/Ultra cards, the Nano Omni card does not carry
  the "open weights, training data, and recipes" self-description; it links only an image-training
  dataset and a deploy cookbook. It is classified `open_weights`, not `open_weights_recipe`.
- **No model-level safety evaluation.** Safety is post-training data curation only, over a wider
  multimodal misuse surface.
- **Recipe surfaces only the public subset.** A recipe exists in the NeMo repo, but it surfaces only
  the public subset of the alignment corpus, so full reproduction is not possible.
- **Licence date inconsistency.** The NVIDIA Open Model Agreement's on-document date (v. 2026-03-09)
  is inconsistent with a later HTML date and is unverified against the PDF.

The offsetting advantage is a small, portable, natively multimodal model under a clean irrevocable
licence.

<!-- item: openness -->
## Openness tier & components

Nano Omni is `open_weights` (tier 3). **Weights** are ungated safetensors, with a **model card** and a
clear **licence**, but the card does not carry the family's open-data/recipe self-description and links
only an image-training dataset and a TensorRT-LLM deploy cookbook. A genuine training recipe does exist
in the NeMo repo (`docs/nemotron/omni3`, SFT then RL), but it surfaces only the public subset of the
alignment corpus, and the card signals do not carry the recipe claim. On card signals this is
open_weights, not open_weights_recipe: the openness tier is not forced up on the repo recipe alone.

<!-- item: license -->
## License terms & permitted use

Nano Omni is governed by the **NVIDIA Open Model Agreement (v. 2026-03-09)**, a third distinct family
licence whose text is near-identical to the NVIDIA Nemotron Open Model License. On the corrected reading
it is Apache-2.0-derived and permissive: a "perpetual, worldwide, non-exclusive, no-charge,
royalty-free, irrevocable license to reproduce, prepare Derivative Works of ... sublicense, and
distribute the Work ... in source or object form", with commercial use allowed and the **Trustworthy-AI,
acceptable-use and guardrail clauses confirmed absent**. It terminates **only** on the licensee bringing
patent or copyright litigation over the Work or an output from it. It is source-available and **not
OSI**. The on-document date is inconsistent with the HTML date and unverified against the PDF, so confirm
the version before relying on it. These are the load-bearing inputs to the legal (3) score.

<!-- item: provenance -->
## Supply-chain & provenance

Weights are distributed from the **verified `nvidia` org** on Hugging Face as **ungated safetensors**
with an official **BF16** variant. Note the repo id (`nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16`)
has **no "NVIDIA-" prefix**, unlike its siblings, so pin the exact path. The checkpoint trust checklist
scores about **4/8**: published checksums, checkpoint scanning and a signing/attestation policy were not
verified this pass, which is why provenance is a 3. Pin the exact revision and verify checksums.

<!-- item: eu-ai-act -->
## EU AI Act posture

Nano Omni is **GPAI**. The licence is irrevocable with no acceptable-use restriction, but there is **no
formal EU GPAI documentation package, no copyright policy**, and NVIDIA is **not a Code of Practice
signatory**; the open-data posture is weaker than the rest of the family. A non-OSI licence with a
weaker open-data posture most likely **does not** cleanly reach the open-source exemption. Training
compute is undisclosed, but at **31B / ~3B active** on ~717B tokens a systemic-risk designation is **not
indicated**. An EU deployer must additionally weigh the multimodal input surface.

<!-- item: evaluation -->
## Benchmarks & evaluation

Nano Omni is a small multimodal reasoning model competitive for its class and modality. OneHill did
**not** run its own benchmarks this pass, and no independent third-party re-runs of the multimodal
benchmarks were gathered, so the figures are publisher and architectural (the model card). This is
marked *partial* and holds the performance dimension at 3.

<!-- item: safety-eval -->
## Independent safety evaluation

There is **no dedicated model-level safety evaluation** for Nano Omni, and its **multimodal input
surface** (video/audio/image) widens the misuse path without a published characterisation of it. Safety
is post-training data curation only. The **Nemotron-3-Content-Safety** classifier is multimodal (text
and images) and so is partly attributable, and NeMo Guardrails and garak are Apache-2.0 - that
downloadable stack is what holds the safety dimension at 3 rather than 2, while the missing model-level
evaluation over the wider surface holds it below 4. The guard-classifier scores are NVIDIA
self-reported.
