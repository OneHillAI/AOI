doc_type: safety
entity: nemotron-3
variant/applies-to: Nemotron 3 Super + Nano - safety posture and family safety tooling
source_url: https://huggingface.co/nvidia/Nemotron-3-Content-Safety ; https://github.com/NVIDIA-NeMo/Guardrails ; https://github.com/NVIDIA/garak
document_effective_date: various (current-gen artefacts 2025-2026)
retrieval_date: 2026-08-03
exists: yes
retrieved: true
tag: publisher

## Model-level safety on the base cards (the honest gap)
The Super and Nano base cards carry NO published model-level safety evaluation or red-team result -
only a data-filtering note, VERBATIM: "we apply targeted keyword- and regex-based filters and remove
all trajectories matching such behavior". The Nano card adds VERBATIM: "iterative testing and
validation at both unit and system levels are essential to mitigate risks ... before deployment".
The White Paper Section 3 "Evaluation, Safety and Release" is a contributor list, with no
methodology, red-team or safety benchmarks in the text read. So there is NO dedicated model-level
safety evaluation; safety appears only as post-training data curation (Nemotron-SFT-Safety-v1 +
keyword/regex filtering).

## Companion guard classifier (family-level, downloadable, genuinely attributable)
[Nemotron-3-Content-Safety - VERBATIM] "A Large Language Model (LLM) classifier that uses Google's
Gemma-3-4B-it as the base and is fine-tuned by NVIDIA on multimodal and multilingual content-safety
related datasets" ; 23 categories, 12 languages ; benchmark evals published (NVIDIA self-reported,
no third-party head-to-head) ; "ready for commercial use."

## Guardrails + red-team tooling
[NeMo Guardrails - VERBATIM] "an open-source toolkit for easily adding programmable guardrails to
LLM-based conversational systems". Licence Apache 2.0.
[garak - VERBATIM] "Generative AI Red-teaming & Assessment Kit". Licence Apache 2.0.

## Assessment
Safety-tuned release with a genuinely downloadable, multi-domain companion guard classifier and
Apache-2.0 guardrails + red-team tooling, but NO published model-level safety evaluation or
independent red-team. This lands the safety dimension at 3 (held below 4 by the missing model-level
evaluation; held above 2 by the real, downloadable companion guard stack). The guard-classifier
scores are NVIDIA self-reported.
