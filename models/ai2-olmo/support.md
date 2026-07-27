# Support - Ai2 OLMo (OLMo 2 / OLMo 3)

_How do we keep it running and get help? Troubleshooting, versions/changelog, channels;
security-disclosure and deprecation policy are current gaps._

<!-- item: troubleshooting -->
## Common problems & fixes

Aggregated common pitfalls (not an exhaustive catalogue):

- **Out-of-memory on the 32B.** Use a smaller variant, quantize (GGUF/AWQ/4-bit), or move to
  multi-GPU; reduce max context to shrink the KV cache.
- **Garbled or over-verbose Instruct output.** You are almost certainly not applying the chat
  template - use `apply_chat_template`, and don't prompt a *base* checkpoint as a chat model.
- **Non-reproducible results / silent updates.** You floated on `main`; pin an exact HF
  revision and verify checksums.
- **Slow first token.** Cold model load and KV-cache allocation; keep the process warm and
  size VRAM for your target context length.

<!-- item: release-versioning -->
## Versions, changelog & cadence

Releases follow a **generational cadence - OLMo 2 → OLMo 3** - rather than a rolling
semantic-version stream, with base and Instruct checkpoints per generation plus intermediate
training checkpoints. Individual versions are tracked as **immutable Hugging Face revisions**
on the `allenai` org, so the revision hash is your changelog anchor: pin it, and diff against
a newer revision when you choose to upgrade. Ai2's technical reports accompany each
generation and document what changed.

<!-- security-disclosure is a `gap` item - no formal published vulnerability-disclosure or
     security policy was found; contact is only the general Ai2 / Hugging Face org presence.
     See gap_reason. This absence is also why Governance scores 4 rather than 5. -->

<!-- item: channels -->
## Community & support channels

- **Ai2 community** and the OLMo project page (`ev-olmo-page`) for announcements and docs.
- **Hugging Face** model and dataset discussion tabs on the `allenai` org (`ev-hf-allenai`)
  for usage questions.
- **GitHub issues** on `allenai/OLMo` and `allenai/OLMo-core` (`ev-github`) for training-code
  and reproduction problems.

There is no paid support tier - this is community and maintainer support around an open
project.

<!-- deprecation is a `gap` item - no published deprecation/EoL policy. Older HF revisions
     remain downloadable, but no formal support window or sunset commitment is documented.
     See gap_reason. -->

<!-- item: known-issues -->
## Tracked known issues

Drawn from model-card caveats rather than a formal issue tracker (hence *partial*):

- Safety tuning is **lighter** than the large commercial labs, with no companion guard model.
- Capability is **in-class rather than leading** - don't expect frontier behaviour on hard tasks.
- Behaviour is **English-centric**; other-language quality is unverified.
- Base checkpoints are **untuned research artifacts** and must not be deployed as assistants.
