# Assess - Meta Llama 3.x (Llama 3.1 / 3.3 text line)

_Openness, licence, provenance, EU AI Act position, safety, evaluation and the AOI score._

<!-- item: intended-use -->
## Intended & out-of-scope use

Llama is a general-purpose assistant lineage for text generation, summarisation,
retrieval-augmented question answering, coding help and multilingual chat. Meta positions the
Instruct checkpoints for assistant use and the base checkpoints as starting points for further
fine-tuning. Llama is the default self-hosted base for internal assistants, RAG systems and
agentic prototypes.

Out of scope: any use forbidden by the Acceptable Use Policy (illegal activity, weapons, CSAM,
targeted harassment, high-stakes unsupervised decision-making, and similar), and base
checkpoints deployed directly as chat models. Base models are un-tuned and should never face
users. Deploy the safety-tuned Instruct variant with Llama Guard instead.

<!-- item: limitations -->
## Known limitations, bias & failure modes

Meta's model cards document the class-standard limitation profile. Llama hallucinates plausibly
and confidently, can reflect training-data bias, and retains residual susceptibility to prompt
injection and determined jailbreaks. Treat retrieved documents and tool outputs as untrusted
input, never as instructions. Long-context recall degrades toward the far end of the window, and
the smaller checkpoints trade capability for footprint. These limits are shared by current LLMs,
which is why the safe-deployment controls are mandatory.

<!-- item: openness -->
## Openness tier & license classification

Llama sits in the `gated_open` tier, which caps the openness dimension at 3. Weights are
downloadable and the documentation (model cards, intended-use and limitations sections) is
strong. Access is gated behind a click-through acceptance on Hugging Face, both the training data
and the training code are closed, and evaluation is only partially released. The artifact is
documented but the recipe is not. The license classification is `open_weight`, not open source.

<!-- item: license -->
## License terms & what you may do

The Llama Community License is not OSI-approved and should not be described as open source. It
permits commercial use with conditions. Any deployer above 700 million monthly active users must
obtain a separate license from Meta. An Acceptable Use Policy governs permitted applications, and
"Built with Llama" attribution plus naming requirements attach to derivatives.

The text-only models in this entry carry no EU-domicile restriction (the multimodal carve-out is
tracked in the separate llama-4 entry). Calling Llama "open source" is inaccurate on these terms;
it is open-weight with conditions attached.

<!-- item: provenance -->
## Supply-chain & provenance

The canonical source is the verified `meta-llama` organisation on Hugging Face. Distribution is
safetensors-only (no unsafe pickle load path from the canonical source), checksums are published,
and there is no malicious-checkpoint incident on Meta's own org, a checkpoint-checklist score of
roughly 6/8. Missing for full marks are cryptographic model signing (no Sigstore/OpenSSF
model-signing) and a SLSA-style provenance attestation.

The secondary ecosystem includes community GGUF quantizations (bartowski, unsloth) and hosted
endpoints on Bedrock, Azure, Vertex, Together, and Groq. Each is a separate artifact whose trust
equals its uploader or host. Pin the exact revision from the canonical org and verify the checksum
before deploying.

<!-- item: eu-ai-act -->
## EU AI Act posture

Llama is a GPAI model. The largest checkpoints (Llama 3.1 405B; the large Llama 4 models are in
the llama-4 entry) exceed the 1e25-FLOP training-compute threshold, which triggers the
systemic-risk presumption. Systemic-risk models receive no open-source exemption regardless of
license, so the full Article 53 + 55 obligation set applies. The community license, with its
acceptable-use policy, MAU threshold and access gate, likely fails the Act's "free and
open-source" test in any case.

Meta's provider package is only partial against that bar. It has detailed model cards and safety
evaluations (good downstream/Annex-XII information) but not a complete Article 55 systemic-risk
package, and only partial copyright-policy and training-content-summary coverage. Meta publicly
declined to sign the EU GPAI Code of Practice in 2025.

A downstream EU deployer receives an incomplete compliance file and must treat any multimodal
Llama model separately. A deployer that fine-tunes and places a derivative on the EU market under
its own name likely becomes a provider itself, with its own Annex XI/XII duties.

<!-- item: evaluation -->
## Benchmarks & evaluation

On public leaderboards Llama is consistently strong across reasoning, coding and
instruction-following, and is a leader among open-weight generalist families. This is an
aggregated, third-party read: performance is third-party framed, no specific numbers are asserted
as verified, and the performance dimension is capped accordingly. Leaderboard standing is
directional evidence of class-leading quality, not a reproduced measurement.

<!-- item: safety-eval -->
## Independent safety / red-team results

Meta publishes its own safety evaluations in the model cards and ships two first-party safety
classifiers as companion models: Llama Guard (content classification) and Prompt Guard
(injection detection). No independent third-party red-team spans all harm domains, so coverage is
marked partial. The publisher's safety evidence is useful but does not replace independent
adversarial evaluation, the missing piece for a top safety score.
