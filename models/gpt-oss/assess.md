# Assess - OpenAI gpt-oss (gpt-oss-120b / gpt-oss-20b)

_Openness, licence, provenance, EU AI Act position, safety, evaluation and the AOI score._

<!-- item: intended-use -->
## Intended & out-of-scope use

gpt-oss is OpenAI's first open-weight release since GPT-2 (August 2025). It comprises two
mixture-of-experts reasoning models, gpt-oss-120b (~117B total / 5.1B active) and gpt-oss-20b
(~21B total / 3.6B active), built for coding, math, agentic tool use and general reasoning with
configurable low/medium/high effort. The intended use is general-purpose assistant and agentic
workloads that need a strong reasoning model, run and customised on the deployer's own
hardware under a permissive licence.

Only safety-tuned reasoning checkpoints ship (there is no raw base release), and the models
are text-only. High-stakes, autonomous or regulated decision-making is out of scope without
the external control stack described in the Implement domain. Because the weights are open,
downstream parties can fine-tune the safety tuning away.

<!-- item: limitations -->
## Known limitations, bias & failure modes

Strong reasoning does not remove confabulation, so factual output should be treated as
unverified.

Raw chain-of-thought is unfiltered. OpenAI deliberately did not align the visible reasoning
trace, so it can contain unsafe or incorrect content and must not be shown to end users or
used as a safety signal.

The model card presents training as primarily English, so other-language behaviour is
incidental and not a supported target.

Safety tuning is removable. Because the weights are open, the safety behaviour can be
fine-tuned out, which is the risk OpenAI probed with its malicious-fine-tuning study.

The models are trained solely for the harmony response format, so plain prompt strings
underperform or misbehave.

<!-- item: openness -->
## Openness tier & components

gpt-oss is `open_weights`, not `fully_open`. Open: ungated, downloadable Apache-2.0 weights and
strong public documentation (a detailed model card and arXiv report). Closed: the training
data and training code. Evaluation is only partially open.

The release is more open than a gated community licence, but it does not publish the data and
code needed to reproduce the model from scratch. The open-weights tier caps Dimension 1 at 3,
and gpt-oss sits at the top of that band.

<!-- item: license -->
## License terms & permitted use

The licence is Apache-2.0, OSI-approved, applied to both models with no click-through gate.
There is no acceptable-use policy, no monthly-active-user threshold, no attribution or naming
requirement and no field-of-use restriction. Commercial use is unconditional, subject only to
the standard Apache attribution and notice terms.

This is among the least restrictive licences in the registry and feeds both the openness (3)
and legal (4) scores. The legal score is held at 4 by the EU AI Act training-content-summary
gap (see below), not by anything in the licence.

<!-- item: provenance -->
## Supply-chain & provenance

Weights are distributed from the verified `openai` org on Hugging Face as safetensors (no
pickle requirement) with per-file checksums, shipped natively in MXFP4. There is a clear
canonical source and no malicious-checkpoint incident on record for the canonical org. The
checkpoint trust checklist scores 6/8. The two missing controls are cryptographic weight
signing (Sigstore/model-signing) and SLSA build attestation, which is why provenance scores 4,
not 5.

Community MXFP4/GGUF redistributions (Ollama, LM Studio, llama.cpp) are separate artifacts.
Pin the exact `openai` revision and verify checksums.

<!-- item: eu-ai-act -->
## EU AI Act posture

gpt-oss is a GPAI model under the 10²⁵-FLOPs systemic-risk threshold (gpt-oss-120b was trained
on roughly 2.1M H100-hours, an estimated <1e25 FLOPs), so no Article 55 regime applies.
Released under an OSI-approved licence, ungated and not monetised, it plausibly qualifies for
the Article 53 open-source exemption from the Annex XI/XII technical-documentation duties.

The surviving obligation is a public training-content summary. gpt-oss does not publish its
training data, so that summary depends on OpenAI authoring it and cannot be reconstructed from
a released corpus. This is why the legal score is capped at 4.

OpenAI has committed to the EU GPAI Code of Practice. A fine-tuner placing a derivative on the
EU market under its own name may become a provider for that derivative and must maintain its
own documentation.

<!-- item: evaluation -->
## Benchmarks & evaluation

Aggregated from OpenAI's model card and independent leaderboards (`ev-perf`,
`ev-model-card`): gpt-oss-120b is reported near OpenAI o4-mini and gpt-oss-20b near o3-mini on
core reasoning benchmarks, and both rank strongly among open-weight models on public
leaderboards. The scores are publisher and third-party framing, so the performance dimension
is capped at 4.

<!-- item: safety-eval -->
## Independent safety evaluation

The safety evaluation is a strength relative to most open-weight families, but it is partial.
OpenAI published a substantial safety evaluation under its Preparedness Framework, including a
worst-case malicious-fine-tuning study that fine-tuned gpt-oss on biology and cyber data to
probe uplift. It concluded that the models did not reach "High" capability thresholds.

The methodology was independently reviewed by external experts (METR, SecureBio and Daniel
Kang; `ev-metr`), which is why `misuse_exposure` is assessed partial and the safety dimension
can cite a third-party source. It stops short of a full independent red-team across all harm
domains, so coverage is marked partial.
