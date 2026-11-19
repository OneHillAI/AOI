# Assess - Meta Llama 4 (multimodal)

_Openness, licence, provenance, EU AI Act position, safety, evaluation and the AOI score._

<!-- item: intended-use -->
## Intended & out-of-scope use

Llama 4 is Meta's natively multimodal mixture-of-experts generation: Scout and Maverick are
released and Behemoth is the larger sibling. For non-EU users it is a capable, well-supported
family for general, coding, multimodal and long-context work. It has its own entry, separate from
the Llama 3.x text line (the `meta-llama` entry), because the licence differs.

It is out of scope for EU-domiciled entities. The multimodal licence is not granted to
individuals domiciled in, or companies with a principal place of business in, the EU, so an
EU-domiciled organisation cannot license these models. Only downstream end users of someone
else's product are exempt.

<!-- item: limitations -->
## Known limitations, bias & failure modes

The main limitation is legal. EU-domiciled entities have no licence to the multimodal models, the
large models are systemic-risk, and the licence adds a 700M-MAU commercial trigger, "Built with
Llama" naming and a download access gate. Training data and code are closed, and Maverick and
Behemoth need very large infrastructure.

<!-- item: openness -->
## Openness tier & components

The tier is `gated_open` (dimension score 3 on access). Weights are downloadable after
click-through acceptance and documentation is strong, but training data and code are closed and
the licence is conditional. Licence conditions are scored under legal.

<!-- item: license -->
## License terms & what you may do

The Llama 4 Community Licence is not OSI-approved. The incorporated AUP states: "with respect to
any multimodal models included in Llama 4, the rights granted under Section 1(a) ... are not
being granted to you if you are an individual domiciled in, or a company with a principal place
of business in, the European Union". Downstream end users are exempt. Llama 4 is multimodal, so
EU-domiciled entities get no licence.

The licence also keeps the 700M-MAU commercial trigger, "Built with Llama" naming and
attribution, an AUP with five prohibited-use categories, and California governing law. The
Llama 3.1 text models carry no EU carve-out. Legal therefore scores 2, and EU-domiciled ownership
is effectively none.

<!-- item: provenance -->
## Supply-chain provenance

The canonical source is the verified, access-gated `meta-llama` organisation on Hugging Face.
It distributes safetensors with checksums and per-version licence tags and has no
malicious-checkpoint incident. Bedrock, Vertex, Together and Groq host Llama 4. A hosted end-user
product is the AUP-exempt path for EU end users, but not for EU-domiciled entities building on
the weights. Pin the revision and verify checksums.

<!-- item: eu-ai-act -->
## EU AI Act posture

Llama 4 is GPAI, and the large models are systemic-risk (>1e25 FLOP). The Article 53
open-source exemption does not apply, for two reasons: the Community Licence is not FOSS, and
systemic-risk models are excluded from the exemption. Meta declined the EU GPAI Code of Practice
and publishes no copyright policy or training-content summary.

The EU-multimodal carve-out denies EU-domiciled entities a licence outright. For EU-domiciled
use, prefer the Llama 3.1 text models (the `meta-llama` entry) or a non-Llama family. Legal
scores 2, with a hard flag.

<!-- item: evaluation -->
## Benchmarks & evaluation

Llama 4 Maverick is competitive among open multimodal models, and the family adds native
multimodality and very long context. OneHill has not reproduced the benchmarks, so performance
is capped at 4 and no specific figures are asserted as verified.

<!-- item: safety-eval -->
## Independent safety evaluation

Meta ships Llama Guard (input/output moderation) and Prompt Guard (prompt-injection and
jailbreak detection) with the family, alongside documented safety tuning. No broad independent
multimodal red-team is available to aggregate, so safety scores 4, not 5.
