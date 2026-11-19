# Support - Ai2 OLMo (OLMo 2 / OLMo 3)

_Troubleshooting, versions, security disclosure, channels and deprecation._

<!-- item: troubleshooting -->
## Common problems & fixes

Common pitfalls, not an exhaustive catalogue:

- Out-of-memory on the 32B: use a smaller variant, quantise (GGUF/AWQ/4-bit) or move to multi-GPU, and reduce max context to shrink the KV cache.
- Garbled or over-verbose Instruct output: the chat template is usually not applied. Use `apply_chat_template`, and do not prompt a base checkpoint as a chat model.
- Non-reproducible results or silent updates: floating on `main` causes them. Pin an exact HF revision and verify checksums.
- Slow first token: cold model load and KV-cache allocation. Keep the process warm and size VRAM for the target context length.

<!-- item: release-versioning -->
## Versions, changelog & cadence

Releases follow a generational cadence (OLMo 2 to OLMo 3), not a rolling semantic-version stream. Each generation has base and Instruct checkpoints plus intermediate training checkpoints.

Individual versions are tracked as immutable Hugging Face revisions on the `allenai` org, so the revision hash is the changelog anchor: pin it, and diff against a newer revision when upgrading. Ai2's technical reports accompany each generation and document what changed.

<!-- security-disclosure is a `gap` item - no formal published vulnerability-disclosure or
     security policy was found; contact is only the general Ai2 / Hugging Face org presence.
     See gap_reason. This absence is also why Governance scores 4 rather than 5. -->

<!-- item: channels -->
## Community & support channels

Support channels:

- The Ai2 community and OLMo project page (`ev-olmo-page`) for announcements and docs.
- The Hugging Face model and dataset discussion tabs on the `allenai` org (`ev-hf-allenai`) for usage questions.
- GitHub issues on `allenai/OLMo` and `allenai/OLMo-core` (`ev-github`) for training-code and reproduction problems.

There is no paid support tier. Support is community and maintainer support around an open project.

<!-- deprecation is a `gap` item - no published deprecation/EoL policy. Older HF revisions
     remain downloadable, but no formal support window or sunset commitment is documented.
     See gap_reason. -->

<!-- item: known-issues -->
## Tracked known issues

Known issues come from model-card caveats and not a formal issue tracker, so the item is marked partial.

- Safety tuning is lighter than at the large commercial labs, with no companion guard model.
- Capability is in-class and not leading, so frontier behaviour on hard tasks should not be expected.
- Behaviour is English-centric and other-language quality is unverified.
- Base checkpoints are untuned research artifacts and must not be deployed as assistants.
