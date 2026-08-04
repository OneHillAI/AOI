# Assess - GLM-4-9B-Chat (original, glm-4 licence)

_Should we adopt this? Openness, license, provenance, EU AI Act, safety, evaluation, and
the AOI score live here._

<!-- item: intended-use -->
## Intended & out-of-scope use

The original GLM-4-9B-Chat (THUDM, mid-2024) is a 9B dense chat model - with a 128K variant
and a 1M-context GLM-4-9B-Chat-1M - that predates Zhipu's move to MIT. It is intended as a
small general assistant. It is a **separate entry** from the current MIT GLM line (the `glm`
entry) because its weights are governed by the custom, non-OSI **"glm-4" licence**.

Out-of-scope: any commercial use without completing the licence's registration; any use that
breaches the field-of-use terms (military, illegal, national-security-endangering); and, for
new work generally, any case where a current model would do - this is a dated 2024 checkpoint
superseded within its own family.

<!-- item: limitations -->
## Known limitations, bias & failure modes

Two limitations dominate. First, the **licence**: revocable, commercial-registration-gated,
with a mandatory "glm-4" name prefix and "Built with glm-4" attribution. Second, **dated
capability**: a 2024 9B superseded by GLM-4-9B-0414 and the 4.5/4.6 line. It also carries
China-aligned alignment, ships no first-party guard, and has closed training data and code.

<!-- item: openness -->
## Openness tier & components

`gated_open` tier (dimension score 2). The weights are downloadable and free for academic
research, but **commercial use is registration-gated** and the grant is **revocable**, with
training data and code closed. That sits a notch below the MIT GLM cluster's open-weights 3 -
the commercial path is gated and the grant can be withdrawn.

<!-- item: license -->
## License terms & what you may do

This is the reason for the split. The weights are governed by the custom non-OSI **"glm-4"
licence**: the copyright grant is "non-exclusive, worldwide, non-transferable,
non-sublicensable, **revocable**, royalty-free". Academic research is free, but **"commercial
users must complete registration"** before any business use. You must display **"Built with
glm-4"** and derivative model names must **begin with "glm-4"**. Use for military, illegal, or
national-security-endangering purposes is forbidden. It is governed by **PRC law**, with
disputes to Beijing's Haidian District People's Court (contact license@zhipuai.cn). A
revocable, registration-gated grant with a name-prefix rule is why use-and-modify is **weak**
and ownership is **limited** - the low end of the GLM family, and far below the MIT line.

<!-- item: provenance -->
## Supply-chain provenance

The canonical source is the verified `THUDM` organisation on Hugging Face, safetensors with
checksums, no malicious-checkpoint incident (checklist ~4/8). Widely mirrored and quantized as
a small 2024 model - each mirror is a separate artifact whose trust equals its uploader, and
redistribution must carry the glm-4 licence (including the "Built with glm-4" and name-prefix
rules). Pin the revision, verify the checksum, prefer the canonical org.

<!-- item: eu-ai-act -->
## EU AI Act posture

GPAI but **not systemic-risk** (a 9B model). Unlike the MIT GLM line, the glm-4 licence is
**not** FOSS (revocable, registration-gated, field-of-use and naming restrictions), so the
Article 53 open-source exemption does **not** apply on the licence axis. The systemic-risk
duties do not arise, but the transparency obligations are not exemption-covered, and no
copyright policy or training-content summary is published. The commercial-registration and
naming duties bind downstream, under PRC governing law. Legal scores 2.

<!-- item: evaluation -->
## Benchmarks & evaluation

Capable for a mid-2024 9B, but dated by 2026 and superseded within its family. OneHill has
**not** re-run any benchmarks, so performance is a 2 (below-average current capability) and no
specific figures are asserted as verified.

<!-- safety-eval is a `gap` item in entry.yaml - its gap_reason renders as a callout; no
     prose section is required. There is no independent red-team of GLM-4-9B-Chat we can
     aggregate, and OneHill ran no safety eval this cycle; the behavioural caveats are
     captured under limitations above. -->
