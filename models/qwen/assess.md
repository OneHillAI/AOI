# Assess - Qwen (Qwen3 family)

_Openness, licence, provenance, EU AI Act position, safety, evaluation and the AOI score._

<!-- item: intended-use -->
## Intended & out-of-scope use

Qwen3 is Alibaba's general-purpose open-weight family, strongest in coding and agentic work. Qwen3-Coder-480B-A35B is among the strongest open coding models. Intended use spans assistant, coding and tool-using applications across sizes from 0.6B laptop models to a 480B coder.

Parts of the family are out of scope. Built-in alignment is lighter than at Western frontier labs, so deploy behind your own guardrails. The systemic-risk large variants (235B, 480B-Coder) carry an unclosed EU AI Act Article 55 gap, so they are out of scope for EU high-stakes use unless the deployer closes that gap.

<!-- item: limitations -->
## Known limitations, bias & failure modes

Qwen3 shows China-aligned topic censorship: the models decline or steer on subjects sensitive under Chinese content rules, which matters for any knowledge or retrieval use.

Instruct alignment withstands casual jailbreaks but is lighter than at Western frontier labs, and no companion guard or classifier model exists. Capability leadership is concentrated in coding and agentic tasks and is not uniform across domains.

<!-- item: openness -->
## Openness tier & components

Qwen is open_weights: Apache-2.0 weights and a good model card, with closed training data and training code and only partially reproducible evaluation. The model can be run and adapted, but its training cannot be reproduced.

<!-- item: license -->
## License terms & permitted use

The mainstream Qwen3 sizes are OSI-approved Apache-2.0 with unconditional commercial use, which is more permissive than the restrictive community licences some peers use. Licensing is not uniform across the family: some large or legacy variants use the Tongyi Qianwen community licence. Verify the LICENSE file per checkpoint.

<!-- item: provenance -->
## Supply-chain & provenance

Qwen is distributed from the verified Qwen org on Hugging Face and officially dual-published on Alibaba's ModelScope hub. Checkpoints are safetensors with checksums, and no canonical-org malicious incident is on record.

Dual-hub distribution is a supply-chain surface in itself, so verify that checksums match across Hugging Face and ModelScope. There is no cryptographic signing or provenance attestation.

<!-- item: eu-ai-act -->
## EU AI Act posture

Qwen is a GPAI model. The mainstream Apache-2.0 sizes plausibly qualify for the open-source exemption. The 235B MoE and Qwen3-Coder-480B likely exceed the 1e25 FLOPs systemic-risk threshold, and for systemic-risk models the exemption is void and the full Article 55 package is owed.

That documentation is not published, and a China-based provider is unlikely to furnish an EU AI Office package. An EU deployer of the large variants therefore has a compliance gap that upstream artifacts cannot close.

<!-- item: evaluation -->
## Benchmarks & evaluation

Third-party evaluation shows strong general capability and class-leading open coding (Qwen3-Coder). The results are third-party and the evaluation harness is only partially open, so treat the numbers as indicative and not as verified results.
