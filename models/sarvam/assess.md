# Assess - Sarvam-30B, Sarvam-105B and Sarvam-105B-1711

_Openness, licence, provenance, EU AI Act position, safety, evaluation and the AOI score._

Scope. This entry scores `sarvamai/sarvam-30b`, `sarvamai/sarvam-105b` and `sarvamai/sarvam-105b-1711` (BF16 and NVFP4), with their official FP8 and GGUF builds. The three share one Apache-2.0 declaration, one weights-only openness tier and one base. The 1711 build is a further post-trained finetune of Sarvam-105B (`ev-card-1711`).

Separate releases, listed as follow-ups: `sarvam-translate` (tagged GPL-3.0), `prism` (a LoRA fine-tune of the 105B with its own LICENSE file), `sarvam-m` (Apache-2.0 tag, described by Artificial Analysis as built on Mistral Small), `sarvam-1`, `shuka-1`, `OpenHathi-7B`, and the hosted-only `sarvam-105b-conversations` (`ev-hub`, `ev-aa`, `ev-api-docs`).

<!-- item: intended-use -->
## Intended & out-of-scope use

The cards describe reasoning, coding, agentic and Indian-language use for the 105B, and low-latency conversation and voice-agent tool calls for the 30B (`ev-card-105b`, `ev-card-30b`). They state no out-of-scope uses and no intended-purpose statement.

The hosted Terms prohibit several uses, including professional advice without review. Those Terms govern Sarvam's service, and the weights carry no acceptable-use policy (`ev-api-docs`, `ev-tos`).

<!-- item: limitations -->
## Known limitations, bias & failure modes

No card lists a limitation, bias or risk (`ev-card-105b`, `ev-card-30b`, `ev-card-1711`).

Artificial Analysis reports high hallucination rates for both March builds, with AA-Omniscience indexes of -60 (105B) and -72 (30B). It also reports TerminalBench Hard scores of 1.5% and 2.3% (`ev-aa`).

The API documentation lists one limitation. Reasoning is on by default and its tokens count against `max_tokens` (`ev-api-docs`). Open Hugging Face threads report an import error with newer Transformers and thinking that cannot be turned off (`ev-discussions`).

<!-- item: openness -->
## Openness tier & components

The tier is `open_weights`.

| Component | Rating | Evidence |
|---|---|---|
| Weights | open | Ungated safetensors for all builds, plus official FP8 and GGUF (`ev-hub`, `ev-quant-code`) |
| Training data | closed | The blog describes categories only. No dataset is released (`ev-blog`) |
| Training code | closed | The GitHub organisation holds forks and SDKs, no training code (`ev-quant-code`) |
| Evaluation | partial | The indivibe prompt set is public under CC-BY-4.0. Results are charts, with no judge outputs or code (`ev-indivibe`) |
| Documentation | partial | Cards and a blog exist. There is no technical report (`ev-no-report`) |
| Licence | open | Apache-2.0 declared, with no LICENSE file (`ev-license`) |

Only post-trained reasoning models are released. No base checkpoint repo exists in the organisation (`ev-hub`). A community comment claiming base and instruct variants is wrong against the repo list (`ev-discussions`).

<!-- item: license -->
## License terms & permitted use

Apache-2.0 is declared in the front matter of every card and in the sentence "open-sourced under the Apache License" (`ev-license`). No weights repo holds a LICENSE file. The cards give no version number and no link. The standard text grants copyright and patent licences and allows commercial use.

Sarvam's own legal documents add a layer the weights repos never mention. Terms of Service v2.0 clause 10.5 bars using the Offerings or their output to train AI systems and bars discovering model weights. The EULA defines Software to include "proprietary language models", bars derivative works and bars training competing models (`ev-tos`, `ev-eula`).

Neither document mentions the Apache-2.0 weights or carves them out. The text does not say whether they reach a copy downloaded under Apache-2.0. Get legal review before building a derivative.

<!-- item: provenance -->
## Supply-chain & provenance

The canonical source is the `sarvamai` Hugging Face organisation. It is not verified. Weights are safetensors with LFS sha256 values, no pickle files, and a completed hub scan with no flagged files on the main repos. The GGUF repos show no completed scan (`ev-hub`).

Nothing is signed. Loading needs `trust_remote_code=True`, and the 30B and 105B repos ship `hotpatch_vllm.py`, which installs vLLM 0.15.0 and edits its registry (`ev-card-105b`, `ev-hub`).

Sarvam says the models were trained from scratch on in-house data (`ev-blog`). That is a publisher claim. Artificial Analysis repeats it without checking (`ev-aa`). No base model is named for the 30B or the 105B. The 1711 build declares `sarvamai/sarvam-105b` as its base (`ev-card-1711`).

<!-- item: eu-ai-act -->
## EU AI Act posture

These are general-purpose AI models. At about 7.4e23 FLOPs for the 105B and 2.3e23 for the 30B (OneHill estimates from publisher token counts and active parameters), they are far below the 1e25 systemic-risk line.

Sarvam publishes no technical documentation package, no training-data summary in the AI Office template and no copyright policy (`ev-no-report`, `ev-blog`). Its Code of Practice status is unknown.

The open-source exemption is uncertain. Apache-2.0 is declared, and Sarvam also charges for API access to the same models (`ev-token-factory`). A deployer assembles Annex XI and XII style information alone.

<!-- item: evaluation -->
## Benchmarks & evaluation

All card and blog numbers are the publisher's own. The 105B card reports 98.6 on Math500, 78.7 on GPQA Diamond and 68.3 on tau2-Bench. The 30B card reports 97.0, 66.5 and 45.7. The 1711 card reports 80.4 on GPQA Diamond, 85.5 on tau2-Bench and 79.1 on an internal Indic Suite (`ev-card-105b`, `ev-card-30b`, `ev-card-1711`).

The blog and the 30B card disagree on AIME 25: 80.0 against 88.3 (`ev-blog`, `ev-card-30b`).

Artificial Analysis scored the 105B at 18 and the 30B at 12 on its Intelligence Index in April 2026. Both trail every peer it lists. The score covers the March builds only (`ev-aa`).

The Indian-language claim rests on a pairwise LLM-judge comparison over the public indivibe prompts. The blog reports average win rates of 90% (105B) and 89% (30B) against models it does not list in text. Per-language results are charts (`ev-blog`, `ev-indivibe`).

<!-- item: safety-eval -->
## Independent safety evaluation

No safety, red-team or jailbreak evaluation of any build was found, from Sarvam or from a third party. The blog describes safety fine-tuning data with India-specific risks and red-team prompts and gives no results (`ev-blog`).
