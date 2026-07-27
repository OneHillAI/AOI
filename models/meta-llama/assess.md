# Assess - Meta Llama (Llama 3.x / Llama 4)

_Should we adopt this? Openness, license, provenance, EU AI Act, safety, evaluation, and
the AOI score live here._

<!-- item: intended-use -->
## Intended & out-of-scope use

Llama is intended as a broad, general-purpose assistant lineage: text generation,
summarisation, retrieval-augmented question answering, coding help, and multilingual
chat, with the Llama 4 generation adding image understanding. Meta positions the
**Instruct** checkpoints for assistant use and the **base** checkpoints as starting
points for further fine-tuning. In practice Llama is the default self-hosted base for
internal assistants, RAG systems, and agentic prototypes.

Out of scope: any use forbidden by the Acceptable Use Policy (illegal activity, weapons,
CSAM, targeted harassment, high-stakes unsupervised decision-making, and similar), and the
base checkpoints deployed directly as chat models. The base models are
un-tuned and should never face users; deploy the safety-tuned Instruct variant paired
with Llama Guard instead.

<!-- item: limitations -->
## Known limitations, bias & failure modes

Llama carries the class-standard limitation profile, documented candidly in Meta's model
cards. It hallucinates plausibly and confidently, can reflect training-data bias, and -
like every current LLM - retains residual susceptibility to prompt injection and
determined jailbreaks. Retrieved documents and tool outputs must be treated as untrusted
input, never as instructions. Long-context recall degrades toward the far end of the
window, and the smaller checkpoints trade capability for footprint. None of these are
defects unique to Llama; they are the reason the safe-deployment controls below are
non-optional.

<!-- item: openness -->
## Openness tier & license classification

Llama sits in the `gated_open` tier, which caps the openness dimension at 3. Weights are
genuinely downloadable and the documentation (model cards, intended-use and limitations
sections) is strong, but access is gated behind a click-through acceptance on Hugging
Face, and both the training data and the training code are closed; evaluation is only
partially released. The result is transparency about the *artifact* without the *recipe*.
The license classification is `open_weight` rather than open source - see the next section.

<!-- item: license -->
## License terms & what you may do

The license is the crux of the assessment. The **Llama Community License is not
OSI-approved** and should not be described as open source. It permits commercial use only
*with conditions*: any deployer crossing **700 million monthly active users** must obtain
a separate license from Meta; an **Acceptable Use Policy** governs permitted applications;
and **"Built with Llama"** attribution plus naming requirements attach to derivatives.
Most consequentially for European adopters, Meta does **not** license the **multimodal**
Llama models to **EU-domiciled entities** - a field-of-use restriction with no analogue
in a true open-source license. Branding Llama as "open source" is, on these terms,
inaccurate; it is open-weight with real strings attached.

<!-- item: provenance -->
## Supply-chain & provenance

Provenance is a relative strength. The canonical source is the **verified `meta-llama`
organisation on Hugging Face**; distribution is **safetensors-only** (no unsafe pickle
load path from the canonical source), **checksums** are published, and there is no
malicious-checkpoint incident on Meta's own org - a checkpoint-checklist score of roughly
6/8. The gap to full marks is the absence of cryptographic model signing (no
Sigstore/OpenSSF model-signing) and no SLSA-style provenance attestation.

Adopters should note the vast secondary ecosystem: community GGUF quantizations
(bartowski, unsloth) and hosted endpoints on Bedrock, Azure, Vertex, Together, and Groq.
Each is a separate artifact whose trust equals its uploader or host - pin the exact
revision from the canonical org and verify the checksum before deploying.

<!-- item: eu-ai-act -->
## EU AI Act posture

Llama is a **GPAI model**, and the largest checkpoints (Llama 3.1 405B and the large
Llama 4 models) exceed the **1e25-FLOP** training-compute threshold, triggering the
**systemic-risk** presumption. Two independent facts collapse the open-source exemption.
First, the community license - with its acceptable-use policy, MAU threshold, and EU
multimodal ban - likely fails the Act's "free and open-source" test in the first place.
Second, and decisively, systemic-risk models receive **no** open-source exemption
regardless of license: the full Article 53 + 55 obligation set applies. Meta's provider
package is only **partial** against that bar - detailed model cards and safety evaluations
(good downstream/Annex-XII information) but not a complete Article 55 systemic-risk
package, and only partial copyright-policy and training-content-summary coverage.
Compounding the governance signal, Meta publicly **declined to sign the EU GPAI Code of
Practice** in 2025. A downstream EU deployer inherits an incomplete compliance file, must
not touch the multimodal variants, and - if fine-tuning and placing a derivative on the
EU market under its own name - likely becomes a provider itself with its own Annex XI/XII
duties.

<!-- item: evaluation -->
## Benchmarks & evaluation

On public leaderboards Llama is consistently strong across reasoning, coding, and
instruction-following, and is fairly judged a **leader among open-weight generalist
families**. This is an **aggregated, third-party** read: performance is third-party framed,
so no specific numbers are asserted as verified and the performance dimension is capped
accordingly. Treat leaderboard standing as directional evidence of class-leading quality
rather than a reproduced measurement.

<!-- item: safety-eval -->
## Independent safety / red-team results

Meta publishes its **own** safety evaluations in the model cards and ships two first-party
safety classifiers - **Llama Guard** (content classification) and **Prompt Guard**
(injection detection) - as companion models. What is *not* available is a comprehensive,
**independent third-party** red-team spanning all harm domains. Coverage is therefore
marked partial: the publisher's safety evidence is
real and useful, but it is not a substitute for independent adversarial evaluation, which
remains the missing piece for a top safety score.
