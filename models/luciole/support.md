# Support - Luciole 1.1 Instruct (23B, 8B, 1B)

_Troubleshooting, versions, security disclosure, channels and deprecation._

<!-- item: troubleshooting -->
## Common problems & fixes

- Ollama output is poor: use the official GGUF files and the published Modelfile (`ev-card-instruct`).
- Tool calls are not returned in vLLM: start the server with `--enable-auto-tool-choice --tool-call-parser hermes`.
- The Thinking models need `--reasoning-parser qwen3` and a recent vLLM (`ev-card-thinking`).
- A user has opened a discussion on the Instruct repo about an extra vLLM parser configuration (`ev-hf-platform`).
- The Modelfile comment names "Luciole-1B-Instruct-1.2". The file loads the 1.1 GGUF it points to, so ignore the comment.
- The 8B fails to load without repository code: the hybrid architecture ships `modeling_nemotron_h.py` in the repo.

<!-- item: release-versioning -->
## Versions, changelog & cadence

The base models appeared on 2026-02-17 and Instruct 1.1 on 2026-07-07, with GGUF and FP8 builds on 2026-07-08. Thinking-1.1 followed on 2026-09-09, Audio-1.0 on 2026-09-18, KD-Math on 2026-09-28 and 2026-10-13, and FP8 builds of the Thinking models on 2026-11-05 (`ev-hf-platform`).

The Instruct repo has nine commits since the initial release, the latest on 2026-11-12 for transformers 5 compatibility. There is no changelog file. The card calls Instruct-1.1 the first iteration and says later iterations with more French data are planned. The cards give no schedule.

<!-- item: security-disclosure -->
## Security / vulnerability disclosure

The SECURITY.md of the Luciole-Training repository asks for private reports to contact@openllm-france.fr. It covers the code, and says issues in a published model or dataset can be raised on Hugging Face. It sets no response time and offers no signed disclosure process (`ev-code-repo`).

<!-- item: channels -->
## Community & support channels

The Hugging Face repo has one open discussion. The consortium site lists contact@openllm-france.fr for contributions and a data-deletion form for the datasets (`ev-hf-platform`, `ev-website`). No commercial support channel is listed.

<!-- deprecation is a `gap` item - no deprecation or support-window statement exists. -->

<!-- item: known-issues -->
## Tracked known issues

The publisher lists these (`ev-card-instruct`, `ev-card-thinking`):

- hallucination, and limited memorisation at 23B;
- post-training almost entirely in English;
- 16,384-token post-training sequences;
- tool use in progress;
- for the Thinking model, no identity training and over-refusal of tool calls.

No public issue tracker for the models was found. The training-code repository is GPL-3.0 and has a public issue tab that was not reviewed.
