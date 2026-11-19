# Assess - DeepSeek-R1-Distill (Qwen base)

_Openness, licence, provenance, EU AI Act position, safety, evaluation and the AOI score._

<!-- item: intended-use -->
## Intended & out-of-scope use

The DeepSeek-R1-Distill checkpoints built on Qwen2.5 bases (1.5B, 7B, 14B, 32B) are dense
reasoning models distilled from DeepSeek-R1 into small, single-GPU weights. They are intended
for on-device and cost-sensitive reasoning and as cheap fine-tuning bases. They form a separate
entry from the flagship R1 and from the Llama-base distils because they are small dense models
on Qwen2.5 bases. DeepSeek releases them under the MIT licence.

Out of scope are any unguarded customer-facing role (these are research distils with no safety
tuning of their own) and any use that needs topic-neutral factuality (they carry R1's
China-aligned filtering). The 1.5B is modest and is not a frontier model.

<!-- item: limitations -->
## Known limitations, bias & failure modes

These are research distils with no safety tuning of their own, so deploy them behind your own
safety system. They carry R1's China-aligned topic censorship and the distillation data is
closed. Capability is strong for the size but not frontier-absolute, and the 1.5B is weakest.
They emit explicit reasoning (think-tag) traces that the client must parse.

<!-- item: openness -->
## Openness tier & components

Open-weights tier (dimension ceiling 3). The weights are MIT-licensed and the documentation is
open, but the distillation data is closed and the training code is partial. This meets the
open-weights anchor.

<!-- item: license -->
## License terms & what you may do

The distil repositories carry DeepSeek's MIT licence, and the card metadata declares `mit`. It is
OSI-approved and permissive, with no field-of-use restriction. That is more permissive than the
Llama Community Licence of the Llama-base distils (`deepseek-r1-distill-llama`) and the same as
the flagship R1. It makes use-and-modify strong and ownership substantial. The Qwen2.5 base
weights are Apache-2.0 per their cards, and the DeepSeek card describes the distils as derived
from them. Confirm the licence on each checkpoint card.

<!-- item: provenance -->
## Supply-chain provenance

The canonical source is the verified `deepseek-ai` organisation on Hugging Face, with
safetensors and checksums and no malicious-checkpoint incident (checklist ~5/8). These are the
most widely mirrored and quantized DeepSeek artifacts because they run on consumer hardware.
Each mirror is a separate artifact whose trust equals its uploader. Pin the revision, verify
the checksum and prefer the canonical org.

<!-- item: eu-ai-act -->
## EU AI Act posture

These are GPAI models but not systemic-risk: at 1.5B-32B they are orders of magnitude below
the 1e25-FLOP presumption. The MIT licence is free and open-source, so the Article 53
open-source exemption applies to the transparency obligations. That makes these the most
EU-comfortable DeepSeek artifacts. DeepSeek still publishes no copyright policy and no public
training-content summary, the obligations that survive the exemption for all GPAI. Legal scores 3.

<!-- item: evaluation -->
## Benchmarks & evaluation

The 14B and 32B distils are strong for their size on public benchmarks; the 1.5B is modest.
OneHill has not re-run the benchmarks, so performance scores 3 (strong for size, not
frontier-absolute) and no specific figure is asserted as verified.

<!-- safety-eval is a `gap` item in entry.yaml - its gap_reason renders as a callout; no
     prose section is required. These are un-safety-tuned research distils; there is no
     independent red-team we can aggregate, and OneHill ran no safety eval. -->
