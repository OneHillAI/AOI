# Assess - DeepSeek-R1-Distill (Llama base)

_Openness, licence, provenance, EU AI Act position, safety, evaluation and the AOI score._

<!-- item: intended-use -->
## Intended & out-of-scope use

Two DeepSeek-R1-Distill checkpoints are built on Meta Llama bases: Llama-8B (Llama 3.1) and
Llama-70B (Llama 3.3). Both are dense reasoning models distilled from DeepSeek-R1. They suit
cost-sensitive reasoning and serve as fine-tuning bases within the Llama ecosystem.

Out of scope: any unguarded customer-facing role (the models have no safety tuning of their
own), any use that needs topic-neutral factuality (China-aligned filtering carried over from
R1), and any use that breaches Meta's Acceptable Use Policy or the 700M-MAU clause.

<!-- item: limitations -->
## Known limitations, bias & failure modes

The Llama Community Licence is more restrictive than the Apache-2.0 licence of the Qwen-base
distils, and the models have no safety tuning of their own. They carry R1's China-aligned
topic censorship, the distillation data is closed, and capability is strong for the size but
below frontier (the 8B is modest). They emit explicit reasoning (think-tag) traces.

<!-- item: openness -->
## Openness tier & components

The tier is `open_weights` (dimension ceiling 3) with a conditional (Llama community)
licence. Weights and documentation are open, the distillation data is closed and training
code is partial. The restrictions are scored under legal and ownership.

<!-- item: license -->
## License terms & what you may do

The distils carry the Llama Community Licence (8B on Llama 3.1, 70B on Llama 3.3). It is
non-OSI and more restrictive than the Apache-2.0 licence of the Qwen distils. Commercial use
is allowed, subject to Meta's Acceptable Use Policy, the "700 million monthly active
users" clause (above it a separate Meta licence is required) and the naming and attribution
requirements ("Built with Llama"; derivative model names must include "Llama").

These terms pass to derivatives. They hold use-and-modify at moderate and ownership at
partial, one step below the Qwen distils.

<!-- item: provenance -->
## Supply-chain provenance

The canonical source is the verified `deepseek-ai` organisation on Hugging Face. Weights ship
as safetensors with checksums, and there is no malicious-checkpoint incident (checklist ~5/8).
The models are widely mirrored and quantized, and each mirror is a separate artifact whose
trust equals its uploader. Redistribution must carry the Llama licence and AUP. Pin the
revision, verify the checksum and prefer the canonical org.

<!-- item: eu-ai-act -->
## EU AI Act posture

The models are GPAI but not systemic-risk (8B-70B). The Llama Community Licence is not FOSS
(it carries acceptable-use and 700M-MAU restrictions), so the Article 53 open-source
exemption does not apply on the licence axis, unlike the Apache-2.0 Qwen distils. The
systemic-risk duties do not arise. The transparency obligations are not exemption-covered, and
DeepSeek publishes no copyright policy or training-content summary. Deployers must also
honour Meta's AUP and the 700M-MAU clause. Legal scores 2.

<!-- item: evaluation -->
## Benchmarks & evaluation

The 70B distil is a strong public result for its size and the 8B is modest. OneHill has not
reproduced the benchmarks, so no specific figures are asserted as verified. Performance
scores 3: strong for the size, below frontier.

<!-- safety-eval is a `gap` item in entry.yaml - its gap_reason renders as a callout; no
     prose section is required. These are un-safety-tuned research distils; no independent
     red-team exists to aggregate, and OneHill has run no safety eval. -->
