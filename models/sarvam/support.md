# Support - Sarvam-30B, Sarvam-105B and Sarvam-105B-1711

_Troubleshooting, versions, security disclosure, channels and deprecation._

<!-- item: troubleshooting -->
## Common problems & fixes

Reported in Hugging Face discussions and on the cards (`ev-discussions`, `ev-card-105b`, `ev-card-1711`):

- vLLM does not load the March builds natively. Use the fork or `hotpatch_vllm.py`.
- An `is_torch_fx_available` import error appears with newer Transformers. A staff fix for Transformers 5 loading and RoPE was merged on 12 November 2026.
- Thinking cannot be turned off on some builds. Pass `enable_thinking=False`, or `chat_template_kwargs` on vLLM for 1711.
- Short `max_tokens` values are consumed by reasoning. Raise the limit.

<!-- item: release-versioning -->
## Versions, changelog & cadence

The 30B and 105B were created on 3 March 2026, with FP8 and GGUF builds in March. A fix for 105B MoE routing was merged on 21 September. A fix for 30B Transformers 5 loading was merged on 12 November. Sarvam-105B-1711 was released on 17 November, with a DSpark vLLM fix on 18 November. Revisions are Hugging Face commits (`ev-hub`, `ev-card-1711`).

The meaning of "1711" is not stated on the cards. The 105B discussion #14 asked for newer checkpoints on 29 October 2026 (`ev-discussions`).

<!-- item: security-disclosure -->
## Security / vulnerability disclosure

No security policy covers the weights or the custom code. The Trust Center lists a security email for the hosted platform, and its audit reports are shared under NDA (`ev-trust`).

<!-- item: channels -->
## Community & support channels

Hugging Face discussions on each repo, the `sarvamai` GitHub organisation, and enterprise support plans on the hosted platform (`ev-discussions`, `ev-quant-code`, `ev-trust`).

Sarvam also hosts the 105B on its own API and documents zero retention for Model APIs. Its binding Privacy Policy sets a 30-day default retention, and its documentation says retention is indefinite until set. The Privacy Policy states an opt-in default for training and then describes opt-out. The EULA promises opt-in only, and the Terms of Service control on conflict. Do not rely on the hosted API for confidential data before Sarvam resolves these (`ev-privacy`, `ev-retention-docs`, `ev-eula`, `ev-tos`).

<!-- item: deprecation -->
## Deprecation / end-of-life policy

No deprecation policy covers the weights. The hosted API has deprecated Sarvam-M and Sarvam-30B and tells users to migrate to Sarvam-105B (`ev-api-docs`).

<!-- item: known-issues -->
## Tracked known issues

Open Hugging Face threads cover loading errors, the thinking toggle, MLX support, newer checkpoints and training-data requests (`ev-discussions`). The blog and the 30B card disagree on the AIME 25 score. Artificial Analysis reports high hallucination for the March builds (`ev-aa`).
