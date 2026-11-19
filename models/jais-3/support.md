# Support - Jais 3 (0.9B, 3.7B, 7B, 32B, MoVA-36B-A4B, 375B-A23B)

_Troubleshooting, versions, security disclosure, channels and deprecation._

<!-- item: troubleshooting -->
## Common problems & fixes

From the cards (`ev-card-32b`); this is not an exhaustive list.

- Reasoning text mixed into answers, or tool calls not parsed: start the server with `--reasoning-parser k2_horizon` and `--tool-call-parser k2_horizon`.
- Odd output in plain completion: leave both parsers off.
- Truncated reasoning: allow at least 32,768 output tokens.
- Weaker answers at low effort: set `reasoning_effort="high"`.
- 375B on SGLang: the validated recipe disables multithreaded weight loading.
- Transformers errors on `generate`: drop `token_type_ids` from the tokenizer output.
- Wrong checkpoint: pass an exact branch name to `--revision` (`CPT`, `Cooldown`, `FTPO`, `SFT`).

<!-- item: release-versioning -->
## Versions, changelog & cadence

Dates come from the hub listing (`ev-hub`), the JaisVoice README (`ev-announce`) and the report (`ev-report-release`).

| Date | Release |
|---|---|
| 2026-09-29 | Jais-3 weights repositories created (0.9B, 3.7B, 7B, 32B, MoVA-36B-A4B, 375B-A23B) and Uno adapters |
| 2026-09-29 to 2026-10-02 | FP8 and MLX builds |
| 2026-10-06 | Jais-3-Data sample created |
| 2026-10-12 to 2026-10-13 | GGUF builds |
| 2026-10-15 | Release announced |
| 2026-11-06 and 2026-11-12 | Technical report v1 and v2 |
| 2026-11-12 | Weights repositories last modified |

Revisions are Hugging Face commits and stage branches. The repository changelog is the commit history. The cards link no release notes, so the content of the 2026-11-12 update is not documented.

<!-- item: channels -->
## Community & support channels

Hugging Face repository discussion tabs (not opened), GitHub Issues on the ifm-ai repositories (`ev-code`), and the jaischat.ai web service named in the report. Correspondence addresses in the report are at mbzuai.ac.ae. The cards give no support contact.

<!-- item: known-issues -->
## Known issues

- The cards say the code repository is coming soon, while the report names three public repositories (`ev-card-32b`, `ev-code`).
- The card names (32B, 375B) differ from the safetensors counts (34.8B, 379.2B). The counts include embeddings.
- The cards mark some benchmarks as to be released later.
- The xLLM and RL360 READMEs cover K2 Horizon, so Jais-3 reproduction steps are not documented (`ev-code`).
- The K2 Horizon datasets named on the base card return HTTP 401 on the hub API (`ev-k2-card`).
