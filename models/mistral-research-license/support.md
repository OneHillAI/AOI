# Support - Mistral (research / non-production licence)

_Will it be maintained? Troubleshooting, versioning, security disclosure, channels, and
deprecation live here._

<!-- item: troubleshooting -->
## Common problems & fixes

The recurring issues are tokenizer / chat-template mismatches on the newer models, multi-GPU
sharding for the 123B/124B, and image-preprocessing for Pixtral Large. Not exhaustive - Mistral's
docs and the community are the practical first stop.

<!-- item: release-versioning -->
## Versions, changelog & cadence

Released on the verified `mistralai` organisation with dated version tags (e.g. `-2411`). The
**Hugging Face revision hash is the changelog anchor**, and the **licence tier is per-model** -
verify each against Mistral's weights doc.

<!-- item: security-disclosure -->
## Security / vulnerability disclosure

No formal published model vulnerability-disclosure / security policy was found; Mistral's general
terms and contact are the only channel. Recorded as a gap.

<!-- item: channels -->
## Community & support channels

The `mistralai` Hugging Face organisation, Mistral's docs/platform, and a large community.
**Commercial licensing is via Mistral directly** - the route to production use of these models.

<!-- item: deprecation -->
## Deprecation / end-of-life policy

No published deprecation or end-of-life policy for the open-weight checkpoints. Dated versions
remain downloadable, but there is no documented sunset commitment - recorded as a gap.

<!-- item: known-issues -->
## Tracked known issues

The standing issues are the non-commercial licence bar, historically lighter safety tuning, no
first-party guard model, and the large infrastructure the flagship sizes demand. See Assess for
the detail.
