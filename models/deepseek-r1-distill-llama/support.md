# Support - DeepSeek-R1-Distill (Llama base)

_Will it be maintained? Troubleshooting, versioning, security disclosure, channels, and
deprecation live here._

<!-- item: troubleshooting -->
## Common problems & fixes

The recurring issues are reasoning / think-tag parsing at the client, quant-quality
trade-offs at 8B, and confusing a distil with the full R1. Not exhaustive - the very large
Llama-ecosystem community is the practical first stop.

<!-- item: release-versioning -->
## Versions, changelog & cadence

The R1-Distill-Llama-8B/70B are published on the verified `deepseek-ai` organisation. There is
no formal changelog document; the **Hugging Face revision hash is the changelog anchor**.

<!-- item: security-disclosure -->
## Security / vulnerability disclosure

No formal published vulnerability-disclosure or security policy was found; the only contact is
the general `deepseek-ai` org presence. Recorded as a gap - factor it into your own
incident-response plan.

<!-- item: channels -->
## Community & support channels

The `deepseek-ai` Hugging Face organisation and GitHub, plus the very large Llama-ecosystem
community around these consumer-runnable distils.

<!-- item: deprecation -->
## Deprecation / end-of-life policy

No published deprecation or end-of-life policy for the distil checkpoints. Older revisions
remain downloadable, but there is no documented sunset commitment - recorded as a gap.

<!-- item: known-issues -->
## Tracked known issues

The standing issues are the use-restricted Llama licence (relative to the Qwen distils), the
absence of own safety tuning, inherited China-aligned censorship, and quant-quality
trade-offs at 8B. See Assess for the detail.
