# Support - DeepSeek-R1-Distill (Qwen base)

_Troubleshooting, versions, security disclosure, channels and deprecation._

<!-- item: troubleshooting -->
## Common problems & fixes

The recurring issues are reasoning (think-tag) parsing in the client, quant-quality trade-offs
at the smallest sizes, and confusing a distil with the full R1. The list is not exhaustive.
The large community around these consumer-runnable models is the practical first stop.

<!-- item: release-versioning -->
## Versions, changelog & cadence

The R1-Distill-Qwen sizes are published on the verified `deepseek-ai` organisation. There is
no formal changelog document; the Hugging Face revision hash is the changelog anchor.

<!-- item: security-disclosure -->
## Security / vulnerability disclosure

No formal vulnerability-disclosure or security policy is published. The only contact is the
general `deepseek-ai` org presence. This is a gap, so build it into your own
incident-response plan.

<!-- item: channels -->
## Community & support channels

The `deepseek-ai` Hugging Face organisation and GitHub, plus a very large community ecosystem
around these consumer-runnable distils.

<!-- item: deprecation -->
## Deprecation / end-of-life policy

No deprecation or end-of-life policy is published for the distil checkpoints. Older revisions
remain downloadable, but no sunset commitment is documented. This is a gap.

<!-- item: known-issues -->
## Tracked known issues

The standing issues are the absence of safety tuning, China-aligned censorship carried over from
R1, and quant-quality trade-offs at the smallest sizes. See Assess for the detail.
