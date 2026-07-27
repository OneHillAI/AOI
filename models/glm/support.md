# Support - GLM (Zhipu AI / Z.ai)

_How do we keep it running and get help? Troubleshooting, versions/changelog, channels, and
known issues. Security-disclosure and deprecation policy are current gaps._

<!-- item: troubleshooting -->
## Common problems & fixes

Aggregated common pitfalls (not an exhaustive catalogue):

- **Out-of-memory on the MoE.** The 355B/106B MoE hold their full parameter count in memory
  even at 32B/12B active - use a smaller variant, quantize, or move to a multi-GPU node;
  reduce max context to shrink the KV cache at the 200K window.
- **Garbled or over-verbose output.** You are almost certainly not applying the chat template
  or are mishandling the thinking/agentic mode - use `apply_chat_template`.
- **Checksum drift across hubs.** The dual Hugging Face (`zai-org`) / ModelScope distribution
  means checksums must match; a mismatch signals a stale mirror or the legacy `THUDM` org.
- **Wrong-LICENSE assumption.** Not every GLM checkpoint is MIT - the original `glm-4-9b` is
  custom-licensed; read the LICENSE on the exact model.
- **Non-reproducible results.** You floated on `main`; pin an exact revision.

<!-- item: release-versioning -->
## Versions, changelog & cadence

Releases follow a **rapid cadence - GLM-4-0414 → GLM-4.5 / GLM-4.5-Air → GLM-4.6** - rather
than a rolling semantic-version stream. Individual versions are tracked as **immutable Hugging
Face / ModelScope revisions** on the verified `zai-org` org, so the revision hash is your
changelog anchor: pin it, and diff against a newer revision when you choose to upgrade. GitHub
repositories (`zai-org/GLM-4`, `zai-org/GLM-4.5`) and technical reports accompany the releases.

Newer variants occasionally referenced elsewhere (GLM-5, GLM-4.7, GLM-4.6V) are **not verified**
in this entry and are deliberately omitted; anchor to GLM-4.6 as the current confirmed flagship.

<!-- security-disclosure is a `gap` item - no formal published vulnerability-disclosure or
     security policy (SECURITY.md / advisory process) exists; contact is only the general
     zai-org Hugging Face / ModelScope / GitHub presence. See gap_reason. This absence is also
     why Governance scores 3 rather than higher. -->

<!-- item: channels -->
## Community & support channels

- **Hugging Face** model discussion tabs on the `zai-org` org (`ev-hf-zai`) for usage
  questions.
- **ModelScope** org discussions (`ev-modelscope`) for the China-facing community.
- **GitHub issues** on the `zai-org/GLM-4` and `zai-org/GLM-4.5` repositories (`ev-github`)
  for inference-code and integration problems.

There is no paid support tier around the open weights - this is community and maintainer
support (Zhipu also offers a separate commercial hosted API under the Z.ai brand).

<!-- deprecation is a `gap` item - no published deprecation/EoL policy. Older HF/ModelScope
     revisions (including the legacy THUDM org) remain downloadable, but no formal support
     window or sunset commitment is documented. See gap_reason. -->

<!-- item: known-issues -->
## Tracked known issues

Drawn from model-card and third-party caveats rather than a formal issue tracker (hence
*partial*):

- **China-aligned alignment** and hosted-API content moderation on politically sensitive
  topics.
- Safety tuning is **lighter** than the large Western labs, with no companion guard model.
- Capability leadership is **concentrated in coding/agentic** rather than uniform.
- An **unresolved EU systemic-risk / Article 55 question** on the 355B MoE, with no published
  documentation.
