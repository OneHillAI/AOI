# Assess - Meta Llama 4 (multimodal)

_Should we adopt this? Openness, license, provenance, EU AI Act, safety, evaluation, and
the AOI score live here._

<!-- item: intended-use -->
## Intended & out-of-scope use

Meta Llama 4 is the natively multimodal, mixture-of-experts generation: Scout and Maverick
(released) and the larger Behemoth. For **non-EU** users it is a strong, well-supported
multimodal family for general, coding, multimodal, and long-context work. It is a **separate
entry** from the Llama 3.x text line (the `meta-llama` entry) because of a licence divergence
that actually bites.

Out-of-scope, **decisively for EU-domiciled entities**: the Llama 4 multimodal licence is **not
granted** to individuals domiciled in, or companies with a principal place of business in, the
EU - so an EU-domiciled organisation cannot licence these models at all (only downstream end
users of someone else's product are exempted).

<!-- item: limitations -->
## Known limitations, bias & failure modes

The dominant limitation is legal, not behavioural: the **EU-domiciled multimodal licence gap**,
the **systemic-risk** status of the large models, the 700M-MAU commercial trigger, the "Built
with Llama" naming duty, and the download access gate. Training data and code are closed, and
Maverick/Behemoth need very large infrastructure.

<!-- item: openness -->
## Openness tier & components

`gated_open` tier (dimension score 3 on access). Weights are downloadable after click-through
acceptance and documentation is strong, but training data and code are closed and the licence
is conditional. The licence conditions are scored under legal, not openness.

<!-- item: license -->
## License terms & what you may do

The **Llama 4 Community Licence** (non-OSI). The load-bearing clause is in the incorporated AUP,
verbatim: "with respect to any multimodal models included in Llama 4, the rights granted under
Section 1(a) ... are not being granted to you if you are an individual domiciled in, or a
company with a principal place of business in, the European Union" (downstream end users
exempted). Because Llama 4 **is** multimodal, EU-domiciled entities get no licence. The licence
also keeps the **700M-MAU** commercial trigger, "Built with Llama" naming/attribution, an AUP
with six prohibited-use categories, and California governing law. The Llama 3.1 text models do
**not** carry the EU carve-out. This is why legal scores 2 and EU-domiciled ownership is
effectively none.

<!-- item: provenance -->
## Supply-chain provenance

The canonical source is the verified, **access-gated** `meta-llama` organisation on Hugging
Face, distributing safetensors with checksums and per-version licence tags, with no
malicious-checkpoint incident. Major clouds (Bedrock, Vertex, Together, Groq) host Llama 4 - a
hosted end-user product is the AUP-exempted path for EU **end users**, but not for EU-domiciled
entities building on the weights. Pin the revision and verify checksums.

<!-- item: eu-ai-act -->
## EU AI Act posture

GPAI, and **systemic-risk** for the large models (>1e25 FLOP). The Article 53 open-source
exemption does not apply for two independent reasons: the Community Licence is not FOSS, and the
large models are systemic-risk. Meta also declined the EU GPAI Code of Practice and publishes no
copyright policy or training-content summary. And the **EU-multimodal carve-out** denies
EU-domiciled entities a licence outright. For EU-domiciled use, prefer the Llama 3.1 text models
(the `meta-llama` entry) or a non-Llama family. Legal scores 2, with a hard flag.

<!-- item: evaluation -->
## Benchmarks & evaluation

Llama 4 Maverick is competitive among open multimodal models, and the family adds native
multimodality and very long context. OneHill has **not** re-run these benchmarks, so performance
is capped at 4 and no specific figures are asserted as verified.

<!-- item: safety-eval -->
## Independent safety evaluation

A genuine strength: Meta ships **Llama Guard** (input/output moderation) and **Prompt Guard**
(prompt-injection/jailbreak detection) with the family, alongside documented safety tuning. No
broad independent multimodal red-team is aggregated here, so safety is a strong 4 rather than 5.
