# Assess - Qwen (Qwen3 family)

_Should we adopt this? Openness, license, provenance, EU AI Act, and evaluation - plus the
AOI score (67.6/100 · Grade C) - live here._

<!-- item: intended-use -->
## Intended & out-of-scope use

Qwen3 is Alibaba's general-purpose open-weight family with a standout strength in
**coding and agentic** workloads (Qwen3-Coder-480B-A35B is among the strongest open coding
models). Its intended use spans assistant, coding and tool-using applications across an
unusually wide size ladder - from 0.5B laptop models to a 480B coder.

Two things push parts of the family out of scope. First, deploy behind **your own
guardrails**: built-in alignment is lighter than Western frontier labs. Second, the
**systemic-risk large variants** (235B, 480B-Coder) carry an unclosed EU AI Act Article 55
gap, so treat them as out of scope for EU high-stakes use unless you close that gap
yourself.

<!-- item: limitations -->
## Known limitations, bias & failure modes

- **China-aligned topic censorship.** The models decline or steer on subjects sensitive
  under Chinese content rules - a behavioural quirk to account for in any
  knowledge/retrieval use.
- **Lighter safety tuning.** Instruct alignment withstands casual jailbreaks but is lighter
  than Western frontier labs, and there is no companion guard/classifier model.
- **Concentrated capability leadership.** The family leads on coding/agentic tasks rather
  than uniformly across all domains.

<!-- item: openness -->
## Openness tier & components

Qwen is **open_weights**: Apache-2.0 weights and a good model card, but **training data and
training code are closed** and evaluation is only partially reproducible. That is
open-weight distribution over a closed training recipe: you can run and adapt the model but
cannot reproduce its training.

<!-- item: license -->
## License terms & permitted use

The **mainstream Qwen3 sizes are OSI-approved Apache-2.0** with unconditional commercial use
- a genuine advantage over the restrictive community licenses some peers use. The important
caveat: **verify the LICENSE file per checkpoint.** Some large or historical variants used
the **Tongyi Qianwen community license** rather than Apache-2.0, so licensing is not uniform
across the whole family.

<!-- item: provenance -->
## Supply-chain & provenance

Qwen is distributed from the **verified Qwen org on Hugging Face** and, officially,
**dual-published on Alibaba's ModelScope** hub. Checkpoints are safetensors with checksums,
and there is no canonical-org malicious incident. The dual-hub distribution is a
supply-chain surface in itself: **verify checksums match across Hugging Face and
ModelScope**, and note there is no cryptographic signing or provenance attestation.

<!-- item: eu-ai-act -->
## EU AI Act posture

Qwen is a **GPAI** model. The mainstream Apache-2.0 sizes plausibly qualify for the
open-source exemption, but the **235B MoE and Qwen3-Coder-480B likely exceed the 1e25 FLOPs
systemic-risk threshold** - and for systemic-risk models the exemption is void and the full
**Article 55 package is owed**. That documentation is **not published**, and a China-based
provider is unlikely to furnish an EU AI Office package, so an EU deployer of the large
variants inherits a real compliance gap it cannot close from upstream artifacts.

<!-- item: evaluation -->
## Benchmarks & evaluation

Aggregated from third-party evaluation, Qwen3 shows **strong general capability and
class-leading open coding** (Qwen3-Coder). These results are **third-party framed**, and
because the evaluation harness is only partially open, treat the numbers as indicative
rather than independently verified.
