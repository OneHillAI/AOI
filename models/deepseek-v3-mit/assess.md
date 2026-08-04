# Assess - DeepSeek-V3 (MIT)

_Should we adopt this? Openness, license, provenance, EU AI Act, safety, evaluation, and
the AOI score live here._

<!-- item: intended-use -->
## Intended & out-of-scope use

DeepSeek-V3 (MIT) is the general-purpose **instruct** line of DeepSeek-V3 as released under
a clean MIT licence - the V3-0324 refresh and the V3.1 hybrid generation, both 671B-total /
37B-active Mixture-of-Experts models with a 128K context. It is intended as a general
assistant, coding, and analysis engine. It is a separate entry from the original
December-2024 DeepSeek-V3 because the **licence changed**: original V3 weights shipped under
the custom DeepSeek License Agreement; V3-0324 and later moved to MIT.

Out-of-scope, in OneHill's read: any use requiring topic-neutral factuality (documented
censorship on certain political topics), and any unguarded customer-facing or high-stakes
deployment - the lighter safety tuning means the weights must be wrapped in your own safety
system. Separate the open weights from DeepSeek's hosted app/API, a different product with
its own privacy profile.

<!-- item: limitations -->
## Known limitations, bias & failure modes

The distinctive limitation is **topic censorship**: refusals and steered answers aligned
with Chinese content rules on certain political topics. Safety tuning is lighter than at
Western frontier labs, known jailbreaks are easier to elicit, and no first-party
guard/classifier model ships. V3.1's hybrid reasoning mode adds an output convention you
must handle. Recorded factually: this is a China-origin model; some organisations restrict
China-origin models by policy - a governance consideration, not a capability judgment.

<!-- item: openness -->
## Openness tier & components

DeepSeek-V3 (MIT) sits in the `open_weights` tier (dimension ceiling 3). The weights are
open and **MIT-licensed**, and the documentation - a detailed technical report - is a
strength. But training data is closed, training code partial, evaluation partial. That mix
meets the open-weights anchor rather than the fully-open top anchor.

<!-- item: license -->
## License terms & what you may do

The V3-0324 and V3.1 weights are released under the **OSI-approved MIT License** -
permissive, with commercial use and modification allowed and no field-of-use restriction.
This is a materially more open posture than the **original** December-2024 V3 weights, which
carry the custom "DeepSeek License Agreement v1.0" with RAIL-style use restrictions (that
generation is the `deepseek-v3-original` entry). Confirm you are on a V3-0324-or-later
checkpoint to get the MIT grant. The MIT move is what lifts use-and-modify to strong and
ownership to substantial.

<!-- item: provenance -->
## Supply-chain provenance

The canonical source is the verified `deepseek-ai` organisation on Hugging Face,
distributing safetensors with checksums and no malicious-checkpoint incident on the
canonical org (checklist ~5/8). Safetensors is data-only, so loading the canonical weights
cannot execute code. Short of a higher score only for the absence of cryptographic signing.
The caveat is the sprawling ecosystem of third-party quantizations - separate artifacts
whose trust equals their uploader. Pin the revision, verify the checksum, prefer the
canonical org.

**Open weights vs the hosted service.** This entry documents the *open weights*, run on your
own infrastructure with no data leaving your box - distinct from DeepSeek's *hosted app and
API*, which has faced data-privacy scrutiny and bans in several jurisdictions. Those issues
are not inherited by locally-run weights but are relevant if you call DeepSeek's own API.
Self-hosting the safetensors sidesteps the concern.

<!-- item: eu-ai-act -->
## EU AI Act posture

DeepSeek-V3 (MIT) is a GPAI model. The V3 technical report cites ~2.788M H800 GPU-hours over
14.8T tokens; at 671B the systemic-risk question is live, but DeepSeek publishes no FLOP
budget, so the 1e25 crossing is not a grounded figure. On the licence alone MIT is a real
free-and-open-source licence, a strong Article 53 exemption candidate. But the surviving
obligations are unmet: no Article 55 documentation, no copyright policy, no training-content
summary, and a China-based provider is unlikely to furnish an EU package. For a downstream
EU deployer this is a concrete compliance **gap** despite the permissive licence - legal
scores 2 and the grade holds at **C**.

<!-- item: evaluation -->
## Benchmarks & evaluation

On public-leaderboard evidence the MIT V3 generations are competitive among large
open-weight instruct models. OneHill has **not** re-run these benchmarks this cycle, so
performance is capped at 4 and no specific figures are asserted as verified. Evaluate
against your own task before adoption, particularly where topic-neutral factuality matters.

<!-- safety-eval is a `gap` item in entry.yaml - its gap_reason renders as a callout; no
     prose section is required. There is no independent, methodologically-documented
     red-team of the MIT V3 open weights we can aggregate, and OneHill ran no safety eval
     this cycle; the behavioural caveats are captured under limitations above. -->
