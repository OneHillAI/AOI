# Assess - DeepSeek-R1-Distill (Llama base)

_Should we adopt this? Openness, license, provenance, EU AI Act, safety, evaluation, and
the AOI score live here._

<!-- item: intended-use -->
## Intended & out-of-scope use

The DeepSeek-R1-Distill checkpoints built on Meta Llama bases - Llama-8B (Llama 3.1) and
Llama-70B (Llama 3.3) - are dense reasoning models distilled from DeepSeek-R1. They are
intended for cost-sensitive reasoning and as fine-tuning bases within the Llama ecosystem.
They are a **separate entry** from the Qwen-base distils because they inherit a different,
more restrictive licence - the **Llama Community Licence**.

Out-of-scope: any unguarded customer-facing role (research distils with **no safety tuning of
their own**); any use requiring topic-neutral factuality (inherited China-aligned filtering);
and any use that breaches Meta's Acceptable Use Policy or the 700M-MAU clause.

<!-- item: limitations -->
## Known limitations, bias & failure modes

The defining caveats are the **use-restricted licence** (relative to the Apache-2.0 Qwen
distils) and the absence of **own safety tuning**. They inherit R1's China-aligned topic
censorship, the distillation data is closed, and capability is strong-for-size rather than
frontier-absolute (the 8B is modest). They emit explicit reasoning (think-tag) traces.

<!-- item: openness -->
## Openness tier & components

`open_weights` tier (dimension ceiling 3), with a **conditional** (Llama community) licence.
Weights and documentation are open, but the distillation data is closed and training code
partial. Meets the open-weights anchor; the restrictions bite on legal and ownership.

<!-- item: license -->
## License terms & what you may do

These distils carry the **Llama Community Licence** (8B on Llama 3.1, 70B on Llama 3.3) -
**non-OSI**, and materially more restrictive than the Apache-2.0 Qwen distils. Commercial use
is allowed, but subject to Meta's **Acceptable Use Policy**, the **"700 million monthly active
users"** clause (above which you must obtain a separate licence from Meta), and
**naming/attribution** requirements ("Built with Llama"; derivative model names must include
"Llama"). These flow down to derivatives. The field-of-use restrictions are why
use-and-modify is **moderate** and ownership is **partial** - one step below the Qwen distils.

<!-- item: provenance -->
## Supply-chain provenance

The canonical source is the verified `deepseek-ai` organisation on Hugging Face, safetensors
with checksums, no malicious-checkpoint incident (checklist ~5/8). Widely mirrored and
quantized via the Llama ecosystem (the broadest toolchain support of any distil base) - each
mirror is a separate artifact whose trust equals its uploader, and redistribution must carry
the Llama licence and AUP. Pin the revision, verify the checksum, prefer the canonical org.

<!-- item: eu-ai-act -->
## EU AI Act posture

These are GPAI models but **not systemic-risk** (8B-70B). Unlike the Apache-2.0 Qwen distils,
the Llama Community Licence is **not** FOSS (it carries acceptable-use and 700M-MAU
restrictions), so the Article 53 open-source exemption does **not** apply on the licence axis.
The systemic-risk duties do not arise, but the transparency obligations are not
exemption-covered here, and DeepSeek publishes no copyright policy or training-content
summary. You must also honour Meta's AUP and the 700M-MAU clause. Legal scores 2.

<!-- item: evaluation -->
## Benchmarks & evaluation

The 70B distil is a notable strong-for-size public result; the 8B is modest. OneHill has
**not** re-run these benchmarks, so performance is a solid 3 (strong-for-size, not
frontier-absolute) and no specific figures are asserted as verified.

<!-- safety-eval is a `gap` item in entry.yaml - its gap_reason renders as a callout; no
     prose section is required. These are un-safety-tuned research distils; there is no
     independent red-team we can aggregate, and OneHill ran no safety eval this cycle. -->
