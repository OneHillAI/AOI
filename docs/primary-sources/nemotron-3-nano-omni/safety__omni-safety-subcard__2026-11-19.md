doc_type: safety
entity: nemotron-3-nano-omni
variant/applies-to: Nemotron 3 Nano Omni safety.md subcard and README data-pipeline text
source_url: https://huggingface.co/nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16/blob/main/safety.md
document_effective_date: repo last modified 2026-08-24
retrieval_date: 2026-11-19
exists: yes
retrieved: true
tag: publisher

## What the subcard says (VERBATIM table cells)
"Safety evaluations were conducted using AEGIS v2, Garak, RTVLM, and VLGuard, as well as NVIDIA Custom Datasets focused on
child safety and dehumanization risks. RL recipes for security improvements are applied during post-training. Ablation studies
for safety were conducted, and video safety and omni-specific benchmarks are investigated. An over-refusal evaluation is also
performed to balance safety with model utility."
"AEGIS 1.0 evaluation covers 13 content safety categories with a required >=95% overall score AND 0 items under the sexual
(minor) category. Qualitative review is conducted for every prompt/response under the suicide and self-harm category. Safety
evaluations are run with both Reasoning ON and OFF modes."
"Use of this model is governed by the NVIDIA Open Model Agreement" (link to the agreement above).

## Reading
This is the first model-specific description of a safety evaluation protocol for any of the three tracked entries: named suites,
a pass gate, and reasoning on and off runs. It publishes no scores, no per-category results, no jailbreak success rates and no
residual-risk disclosure, and the evaluation is run by NVIDIA, not independent. So it is a self-reported process statement, not a
published safety evaluation in the sense of scoring anchor 3 ("a published safety evaluation"). The score is left at 3 and the
statement is recorded as evidence. A fuller published result would justify revisiting it.

## README data-pipeline text (line 807 of the card, paraphrased)
All image and text datasets were CSAM-scanned; content-safety filtering used two independent safety judge models; synthetic
pipelines had quality and safety filtering stages.
