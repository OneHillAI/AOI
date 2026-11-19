# Support - GLM (Zhipu AI / Z.ai)

_Troubleshooting, versions, security disclosure, channels and deprecation._

<!-- item: troubleshooting -->
## Common problems & fixes

Common pitfalls, not an exhaustive catalogue.

Out-of-memory on the MoE: the 355B and 106B MoE hold their full parameter count in memory even
at 32B/12B active. Use a smaller variant, quantize, or move to a multi-GPU node, and reduce
max context to shrink the KV cache at the 200K window.

Garbled or over-verbose output usually means the chat template is not applied or the
thinking/agentic mode is mishandled. Use `apply_chat_template`.

Checksum drift across hubs: the dual Hugging Face (`zai-org`) / ModelScope distribution means
checksums must match, and a mismatch signals a stale mirror or the legacy `THUDM` org.

Wrong-LICENSE assumption: not every GLM checkpoint is MIT, and the original `glm-4-9b` is
custom-licensed. Read the LICENSE on the exact model.

Non-reproducible results come from floating on `main`. Pin an exact revision.

<!-- item: release-versioning -->
## Versions, changelog & cadence

Releases follow a rapid cadence, GLM-4-0414 → GLM-4.5 / GLM-4.5-Air → GLM-4.6, not a rolling
semantic-version stream. Versions are tracked as immutable Hugging Face / ModelScope revisions
on the verified `zai-org` org, so the revision hash is the changelog anchor. Pin it, and diff
against a newer revision when upgrading. GitHub repositories (`zai-org/GLM-4`,
`zai-org/GLM-4.5`) and technical reports accompany the releases.

Newer releases exist outside this entry's scope: GLM-4.7 (2025-12), GLM-5 (2026-02), GLM-5.1
(2026-04), GLM-5.2 (2026-06), GLM-5.3 and GLM-5.3-Flash (2026-08). They are not scored here,
and GLM-4.6 is the newest tracked checkpoint. GLM-5.3 carries a custom licence
(`ev-license-glm53`).

<!-- security-disclosure is a `gap` item - no formal published vulnerability-disclosure or
     security policy (SECURITY.md / advisory process) exists; contact is only the general
     zai-org Hugging Face / ModelScope / GitHub presence. See gap_reason. The absence is also
     why Governance scores 3, not higher. -->

<!-- item: channels -->
## Community & support channels

Usage questions go to the Hugging Face model discussion tabs on the `zai-org` org
(`ev-hf-zai`). The China-facing community is on ModelScope org discussions
(`ev-modelscope`). Inference-code and integration problems go to GitHub issues on the
`zai-org/GLM-4` and `zai-org/GLM-4.5` repositories (`ev-github`).

There is no paid support tier around the open weights, only community and maintainer support.
Zhipu offers a separate commercial hosted API under the Z.ai brand.

<!-- deprecation is a `gap` item - no published deprecation/EoL policy. Older HF/ModelScope
     revisions (including the legacy THUDM org) remain downloadable, but no formal support
     window or sunset commitment is documented. See gap_reason. -->

<!-- item: known-issues -->
## Tracked known issues

These come from model-card and third-party caveats, not a formal issue tracker, hence partial.
China-aligned alignment and hosted-API content moderation affect politically sensitive topics.
Safety tuning is lighter than at the large Western labs, with no companion guard model.
Capability leadership is concentrated in coding and agentic tasks. The 355B MoE has an
unresolved EU systemic-risk / Article 55 question, with no published documentation.
