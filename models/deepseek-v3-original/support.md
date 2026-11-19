# Support - DeepSeek-V3 (original, DeepSeek License)

_Troubleshooting, versions, security disclosure, channels and deprecation._

<!-- item: troubleshooting -->
## Common problems & fixes

Recurring issues are multi-node OOM and sharding for the 671B model, Base-vs-Chat variant
confusion (deploying the un-tuned Base by mistake), and quant-engine version mismatches on
lower-bit builds. The list is not exhaustive. The large community ecosystem is the practical
first stop for deployment questions.

<!-- item: release-versioning -->
## Versions, changelog & cadence

The original December-2024 V3 (Base + Chat) is published on the verified `deepseek-ai`
organisation. The MIT V3-0324/V3.1 generations (`deepseek-v3-mit`) replace it for new work and
carry a cleaner licence. The Hugging Face revision hash is the changelog anchor.

<!-- item: security-disclosure -->
## Security / vulnerability disclosure

No formal vulnerability-disclosure or security policy is published for DeepSeek-V3. The only
contact is the general `deepseek-ai` org presence. Account for this gap in the incident-response
plan.

<!-- item: channels -->
## Community & support channels

The `deepseek-ai` Hugging Face organisation and GitHub are the primary channels for usage and
deployment questions, backed by a large third-party community.

<!-- item: deprecation -->
## Deprecation / end-of-life policy

No deprecation or end-of-life policy is published. The original V3 remains downloadable and the
MIT generations replace it for new work, with no documented sunset commitment.

<!-- item: known-issues -->
## Tracked known issues

The standing issues are the use-restricted licence (relative to the MIT generations),
China-aligned censorship on sensitive topics, lighter safety coverage with no first-party guard
model, and the operational burden of a 671B model. See Assess for the detail.
