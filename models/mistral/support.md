# Support - Mistral AI (open-weight family)

_How do we keep it running and get help? Troubleshooting, versions/changelog, channels,
deprecation and known issues; security-disclosure is a current gap._

<!-- item: troubleshooting -->
## Common problems & fixes

Aggregated common pitfalls (not an exhaustive catalogue):

- **Garbled or over-verbose instruct output.** You are almost certainly not applying the chat
  template - use `apply_chat_template` / `mistral-common`, and don't prompt a *base* checkpoint as
  a chat model. Mind the **Tekken** tokenizer on newer models.
- **Out-of-memory on Mixtral / Mistral Large.** All Mixtral experts must be resident; use a smaller
  variant, quantize (GGUF/AWQ/FP8/4-bit), or move to multi-GPU; reduce max context to shrink the KV
  cache.
- **Unexpected licence blocker.** You assumed Apache but picked an **MRL** model (Ministral 8B,
  Mistral Large, Pixtral Large) - check the model card before committing to commercial use.
- **Non-reproducible results / silent updates.** You floated on `main`; pin an exact HF revision and
  verify checksums.

<!-- item: release-versioning -->
## Versions, changelog & cadence

Mistral uses **dated snapshot versioning** - model ids carry a date suffix (e.g. `-2407`, `-2410`,
`-2506`) - tracked as **immutable Hugging Face revisions** on the `mistralai` org. The revision hash
is your changelog anchor: pin it, and diff against a newer dated snapshot when you choose to upgrade.
Release news posts (e.g. Mistral Small 3) accompany major models and document what changed and the
licence in force.

<!-- security-disclosure is a `gap` item - no formal published vulnerability-disclosure or security
     policy (SECURITY.md / advisory process) was found for the open-weight checkpoints; contact is
     only the general Mistral / Hugging Face org presence. See gap_reason. This absence is also part
     of why Governance scores 4 rather than 5. -->

<!-- item: channels -->
## Community & support channels

- **Hugging Face** model discussion tabs on the `mistralai` org (`ev-hf`) for usage questions.
- **GitHub issues** on `mistralai/mistral-inference` and the `mistralai/cookbook` (`ev-inference`)
  for inference and templating problems.
- **Mistral Discord** and the platform documentation for announcements and how-tos.
- **La Plateforme** offers a paid/commercial support path (and is where MRL commercial licences are
  arranged).

<!-- item: deprecation -->
## Deprecation / end-of-life policy

Mistral operates **dated model versioning** and deprecates legacy models on its **API platform**,
which gives more structure than a pure "download and forget" release. For the **open-weight HF
checkpoints**, however, there is **no formal sunset commitment** - older revisions remain
downloadable indefinitely and there is no stated support window. Marked *partial* to reflect that
the platform-side policy does not fully translate to a documented lifecycle guarantee for the weights.

<!-- item: known-issues -->
## Tracked known issues

Drawn from model-card and release caveats rather than a formal issue tracker (hence *partial*):

- Safety tuning is **lighter** than the largest US labs, with the companion classifier offered as a
  hosted API rather than a broadly-shipped open guard-weight.
- Residual **prompt-injection** susceptibility, as with all current LLMs.
- **Tool-use reliability** has had noted variability across releases (improved in Mistral Small 3.2).
- The **licence split** catches teams expecting every model to be Apache-2.0.
