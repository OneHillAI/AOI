# Support - DeepSeek-R1

_Troubleshooting, versions, security disclosure, channels and deprecation._

<!-- item: troubleshooting -->
## Common problems & fixes

Recurring issues are multi-node OOM and sharding for the 671B model, reasoning (think-tag) parsing at the client, and quant-engine version mismatches on lower-bit builds. The list is not exhaustive. The large community ecosystem is the practical first stop for deployment questions.

<!-- item: release-versioning -->
## Versions, changelog & cadence

R1 and the R1-0528 refresh are published on the verified `deepseek-ai` organisation. No formal changelog document exists, so the Hugging Face revision hash is the changelog anchor. Pin it and diff revisions when a refresh lands.

<!-- item: security-disclosure -->
## Security / vulnerability disclosure

No formal vulnerability-disclosure or security policy is published for DeepSeek-R1. The only contact is the general `deepseek-ai` org presence. This is a gap, so build it into the deployer's own incident-response plan.

<!-- item: channels -->
## Community & support channels

The `deepseek-ai` Hugging Face organisation and GitHub are the primary channels for usage and deployment questions. A large third-party community surrounds the R1 weights and their distils.

<!-- item: deprecation -->
## Deprecation / end-of-life policy

No deprecation or end-of-life policy is published for DeepSeek-R1 checkpoints. Older revisions remain downloadable, but no sunset commitment is documented. This is a gap.

<!-- item: known-issues -->
## Tracked known issues

The standing issues are China-aligned censorship on sensitive topics, lighter safety coverage with no first-party guard model, and the operational burden of a 671B model. See Assess for the behavioural detail.
