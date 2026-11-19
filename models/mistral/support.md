# Support - Mistral AI (open-weight family)

_Troubleshooting, versions, security disclosure, channels and deprecation._

<!-- item: troubleshooting -->
## Common problems & fixes

Common pitfalls, not an exhaustive catalogue.

Garbled or over-verbose instruct output usually means the chat template is not applied. Use
`apply_chat_template` or `mistral-common`, do not prompt a base checkpoint as a chat model,
and mind the Tekken tokenizer on newer models.

Out-of-memory errors on Mixtral and Mistral Large occur because all Mixtral experts must be
resident. Use a smaller variant, quantize (GGUF, AWQ, FP8, 4-bit), move to multi-GPU, or
reduce max context to shrink the KV cache.

An unexpected licence blocker arises when an MRL model (Ministral 8B, Mistral Large 2, Pixtral
Large) is picked on the assumption of Apache. Check the model card before committing to
commercial use.

Non-reproducible results and silent updates come from floating on `main`. Pin an exact Hugging
Face revision and verify checksums.

<!-- item: release-versioning -->
## Versions, changelog & cadence

Mistral uses dated snapshot versioning: model ids carry a date suffix (for example `-2407`,
`-2410`, `-2506`), tracked as immutable Hugging Face revisions on the `mistralai` org. The
revision hash is the changelog anchor. Pin it, and diff against a newer dated snapshot when
upgrading. Release news posts (for example Mistral Small 3) accompany major models and
document what changed and the licence in force.

<!-- security-disclosure is a `gap` item - no formal published vulnerability-disclosure or security
     policy (SECURITY.md / advisory process) exists for the open-weight checkpoints; the contact
     is only the general Mistral / Hugging Face org presence. See gap_reason. The absence is also
     part of why Governance scores 4, not 5. -->

<!-- item: channels -->
## Community & support channels

Usage questions go to the Hugging Face model discussion tabs on the `mistralai` org (`ev-hf`).
Inference and templating problems go to GitHub issues on `mistralai/mistral-inference` and the
`mistralai/cookbook` (`ev-inference`). The Mistral Discord and the platform documentation
carry announcements and how-tos. Mistral Studio (formerly La Plateforme) offers a paid
commercial support path and is where MRL commercial licences are arranged.

<!-- item: deprecation -->
## Deprecation / end-of-life policy

Mistral uses dated model versioning and deprecates legacy models on its API platform, which
gives more structure than a download-and-forget release. The open-weight Hugging Face
checkpoints have no formal sunset commitment: older revisions remain downloadable indefinitely
and no support window is stated. Coverage is partial, because the platform-side policy does
not translate to a documented lifecycle guarantee for the weights.

<!-- item: known-issues -->
## Tracked known issues

These come from model-card and release caveats, not a formal issue tracker, hence partial.
Safety tuning is lighter than at the largest US labs, and the companion classifier is a hosted
API, not a broadly shipped open guard-weight. Prompt-injection susceptibility remains, as with
all current LLMs. Tool-use reliability has varied across releases (improved in Mistral Small
3.2). The licence split catches teams expecting every model to be Apache-2.0.
