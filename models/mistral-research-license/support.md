# Support - Mistral (research / non-production licence)

_Troubleshooting, versions, security disclosure, channels and deprecation._

<!-- item: troubleshooting -->
## Common problems & fixes

Recurring issues are tokenizer / chat-template mismatches on the newer models, multi-GPU
sharding for the 123B/124B, and image-preprocessing for Pixtral Large. The list is not
exhaustive; Mistral's docs and the community are the practical first stop.

<!-- item: release-versioning -->
## Versions, changelog & cadence

Models are released on the verified `mistralai` organisation with dated version tags (e.g.
`-2411`). The Hugging Face revision hash is the changelog anchor, and the licence tier is
per-model, so verify each against Mistral's weights doc.

<!-- item: security-disclosure -->
## Security / vulnerability disclosure

No formal published model vulnerability-disclosure / security policy exists; Mistral's general
terms and contact are the only channel. Recorded as a gap.

<!-- item: channels -->
## Community & support channels

The `mistralai` Hugging Face organisation, Mistral's docs/platform, and a large community.
Commercial licensing is via Mistral directly, which is the route to production use of these
models.

<!-- item: deprecation -->
## Deprecation / end-of-life policy

No published deprecation or end-of-life policy exists for the open-weight checkpoints. Dated
versions remain downloadable, but no sunset commitment is documented. Recorded as a gap.

<!-- item: known-issues -->
## Tracked known issues

The standing issues are the non-commercial licence bar, historically lighter safety tuning, no
first-party guard model, and the large infrastructure the flagship sizes demand. See Assess for
the detail.
