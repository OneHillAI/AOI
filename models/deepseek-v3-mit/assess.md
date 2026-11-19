# Assess - DeepSeek-V3 (MIT)

_Openness, licence, provenance, EU AI Act position, safety, evaluation and the AOI score._

<!-- item: intended-use -->
## Intended & out-of-scope use

DeepSeek-V3 (MIT) is the general-purpose instruct line of DeepSeek-V3 under the MIT licence: the V3-0324 refresh and the V3.1 hybrid generation. Both are 671B-total / 37B-active Mixture-of-Experts models with a 128K context. They are intended as a general assistant, coding and analysis engine.

The original December-2024 DeepSeek-V3 is a separate entry because its weights use the custom DeepSeek License Agreement. V3-0324 and later use MIT.

Out of scope are uses that need topic-neutral factuality, because the model censors certain political topics, and unguarded customer-facing or high-stakes deployment. Safety tuning is light, so the weights need the deployer's own safety system. DeepSeek's hosted app and API are a different product with their own privacy profile.

<!-- item: limitations -->
## Known limitations, bias & failure modes

The model refuses or steers answers on certain political topics in line with Chinese content rules. Safety tuning is lighter than at Western frontier labs, known jailbreaks are easier to elicit, and no first-party guard or classifier model ships. V3.1's hybrid reasoning mode adds an output convention that the client must handle. The model is of China origin, and some organisations restrict China-origin models by policy. That is a governance consideration and not a capability judgment.

<!-- item: openness -->
## Openness tier & components

DeepSeek-V3 (MIT) sits in the `open_weights` tier (dimension ceiling 3). The weights are MIT-licensed and a detailed technical report documents the model. Training data is closed, training code partial and evaluation partial, which meets the open-weights anchor and not the fully-open top anchor.

<!-- item: license -->
## License terms & what you may do

The V3-0324 and V3.1 weights use the OSI-approved MIT License. Commercial use and modification are allowed and there is no field-of-use restriction. The original December-2024 V3 weights carry the custom "DeepSeek License Agreement v1.0" with RAIL-style use restrictions (the `deepseek-v3-original` entry). A V3-0324-or-later checkpoint is needed for the MIT grant. The MIT grant lifts use-and-modify to strong and ownership to substantial.

<!-- item: provenance -->
## Supply-chain provenance

The canonical source is the verified `deepseek-ai` organisation on Hugging Face. It distributes safetensors with checksums and has no malicious-checkpoint incident (checklist ~5/8). Safetensors is data-only, so loading the canonical weights cannot execute code. The score stops short of higher only because the weights are not cryptographically signed.

Third-party quantizations are separate artifacts whose trust equals their uploader. Pin the revision, verify the checksum and prefer the canonical organisation.

This entry covers the open weights, run on the deployer's own infrastructure with no data leaving it. DeepSeek's hosted app and API have faced data-privacy scrutiny and bans in several jurisdictions. Those issues do not apply to locally run weights but do apply to calls to DeepSeek's own API.

<!-- item: eu-ai-act -->
## EU AI Act posture

DeepSeek-V3 (MIT) is a GPAI model. The V3 technical report cites ~2.788M H800 GPU-hours over 14.8T tokens. At 671B the systemic-risk question is open, but DeepSeek publishes no FLOP budget, so the 1e25 crossing is not a grounded figure.

On the licence alone, MIT is a free and open-source licence and a strong candidate for the Article 53 exemption. The surviving obligations are unmet: no Article 55 documentation, no copyright policy and no training-content summary exist, and a China-based provider is unlikely to furnish an EU package. A downstream EU deployer faces a concrete compliance gap despite the permissive licence. Legal scores 2 and the grade is C.

<!-- item: evaluation -->
## Benchmarks & evaluation

The MIT V3 generations are competitive among large open-weight instruct models on public leaderboards. OneHill has not re-run the benchmarks, so performance is capped at 4 and no specific figure is asserted as verified. Test against the deployer's own task before adoption, especially where topic-neutral factuality matters.

<!-- safety-eval is a `gap` item in entry.yaml - its gap_reason renders as a callout; no
     prose section is required. No methodologically documented independent red-team of the
     MIT V3 open weights exists to aggregate; the behavioural caveats are under limitations. -->
