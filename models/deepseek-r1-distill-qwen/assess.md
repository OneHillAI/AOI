# Assess - DeepSeek-R1-Distill (Qwen base)

_Should we adopt this? Openness, license, provenance, EU AI Act, safety, evaluation, and
the AOI score live here._

<!-- item: intended-use -->
## Intended & out-of-scope use

The DeepSeek-R1-Distill checkpoints built on Qwen2.5 bases (1.5B, 7B, 14B, 32B) are dense
reasoning models distilled from DeepSeek-R1 into far smaller, single-GPU-friendly weights.
They are intended for on-device / cost-sensitive reasoning and as cheap fine-tuning bases.
They are a **separate entry** from the flagship R1 and from the Llama-base distils because
they inherit a different licence - **Apache-2.0**, from their Qwen2.5 bases.

Out-of-scope: any unguarded customer-facing role (these are research distils with **no safety
tuning of their own**); any use requiring topic-neutral factuality (they inherit R1's
China-aligned filtering); and treating the 1.5B as a frontier model (it is modest).

<!-- item: limitations -->
## Known limitations, bias & failure modes

The defining caveat is that these are **research distils with no safety tuning of their own**
- deploy them behind your own safety system. They inherit R1's China-aligned topic
censorship, the distillation data is closed, and capability is strong-for-size rather than
frontier-absolute (the 1.5B especially). They emit explicit reasoning (think-tag) traces you
must parse.

<!-- item: openness -->
## Openness tier & components

`open_weights` tier (dimension ceiling 3). Apache-2.0 weights and open documentation, but the
distillation data is closed and training code partial. Meets the open-weights anchor.

<!-- item: license -->
## License terms & what you may do

These distils carry **Apache-2.0** - OSI-approved, permissive, with an explicit patent grant
and no field-of-use restriction - inherited from the Qwen2.5 bases they build on. That is a
cleaner licence than the Llama-base distils (`deepseek-r1-distill-llama`, Llama Community
Licence) and the equal of the MIT family models on permissiveness. It is what makes
use-and-modify strong and ownership substantial. Confirm the Apache-2.0 line per checkpoint
card.

<!-- item: provenance -->
## Supply-chain provenance

The canonical source is the verified `deepseek-ai` organisation on Hugging Face, safetensors
with checksums, no malicious-checkpoint incident (checklist ~5/8). These are the most widely
mirrored and quantized DeepSeek artifacts (they run on consumer hardware) - each mirror is a
separate artifact whose trust equals its uploader. Pin the revision, verify the checksum,
prefer the canonical org.

<!-- item: eu-ai-act -->
## EU AI Act posture

These are GPAI models but **not systemic-risk**: at 1.5B-32B they are orders of magnitude
below the 1e25-FLOP presumption. Apache-2.0 is a genuine FOSS licence, so the Article 53
open-source exemption applies to the transparency obligations - making these the **most
EU-comfortable DeepSeek artifacts**. The obligations that survive the exemption for all GPAI
(a copyright policy and a public training-content summary) are still not published by
DeepSeek, so the position is good but not complete. Legal scores 3.

<!-- item: evaluation -->
## Benchmarks & evaluation

The 14B/32B distils are notable strong-for-size public results; the 1.5B is modest. OneHill
has **not** re-run these benchmarks, so performance is a solid 3 (strong-for-size, not
frontier-absolute) and no specific figures are asserted as verified.

<!-- safety-eval is a `gap` item in entry.yaml - its gap_reason renders as a callout; no
     prose section is required. These are un-safety-tuned research distils; there is no
     independent red-team we can aggregate, and OneHill ran no safety eval this cycle. -->
