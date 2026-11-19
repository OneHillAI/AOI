# Support - DeepSeek-R1-Distill (Llama base)

_Troubleshooting, versions, security disclosure, channels and deprecation._

<!-- item: troubleshooting -->
## Common problems & fixes

Recurring issues are reasoning / think-tag parsing at the client, quant-quality trade-offs at
8B, and confusing a distil with the full R1. The list is not exhaustive. The large
Llama-ecosystem community is the practical first stop.

<!-- item: release-versioning -->
## Versions, changelog & cadence

R1-Distill-Llama-8B and -70B are published on the verified `deepseek-ai` organisation. There
is no formal changelog document. The Hugging Face revision hash is the changelog anchor.

<!-- item: security-disclosure -->
## Security / vulnerability disclosure

No formal vulnerability-disclosure or security policy is published. The only contact is the
general `deepseek-ai` org presence. This is a gap, so deployers need their own
incident-response plan.

<!-- item: channels -->
## Community & support channels

The `deepseek-ai` Hugging Face organisation and GitHub, plus the large Llama-ecosystem
community around these consumer-runnable distils.

<!-- item: deprecation -->
## Deprecation / end-of-life policy

No deprecation or end-of-life policy is published for the distil checkpoints. Older revisions
remain downloadable, but no sunset commitment is documented.

<!-- item: known-issues -->
## Tracked known issues

The standing issues are the use-restricted Llama licence (compared with the Qwen distils), the
absence of own safety tuning, China-aligned censorship carried over from R1, and quant-quality
trade-offs at 8B. Assess has the detail.
