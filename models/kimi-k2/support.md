# Support - Kimi K2 (Moonshot AI)

_How do we keep it running and get help? Troubleshooting, versions/changelog, channels;
security-disclosure and deprecation policy are current gaps._

<!-- item: troubleshooting -->
## Common problems & fixes

Aggregated common pitfalls (not an exhaustive catalogue):

- **Out-of-memory / sharding failures.** The 1T model must be sharded across a multi-GPU/multi-node
  cluster; size tensor/pipeline parallelism to your hardware, or use KTransformers CPU-offload.
- **Block-FP8 kernel or engine errors.** Match your vLLM/SGLang/TensorRT-LLM version to one that
  supports the block-FP8 weights and MLA attention; version mismatches are a common cause.
- **Garbled or over-verbose Instruct output.** You are almost certainly not applying the chat
  template - use `apply_chat_template`, and don't prompt the *Base* checkpoint as a chat model.
- **Non-reproducible results / silent updates.** You floated on `main`; pin an exact revision and
  verify checksums.

<!-- item: release-versioning -->
## Versions, changelog & cadence

Kimi K2 ships as **Base** and **Instruct** checkpoints on the verified `moonshotai` org, tracked
as **immutable Hugging Face revisions** - the revision hash is your changelog anchor: pin it, and
diff against a newer revision when you choose to upgrade. Moonshot's "Kimi K2: Open Agentic
Intelligence" technical report accompanies the release and documents what the model is. (Any newer
Kimi variants beyond K2 are out of scope for this entry until independently verified.)

<!-- security-disclosure is a `gap` item - no formal published vulnerability-disclosure or
     security policy was found; contact is only the general moonshotai Hugging Face / GitHub org
     presence. See gap_reason. This absence is also why Governance scores 3 rather than higher. -->

<!-- item: channels -->
## Community & support channels

- **Hugging Face** model discussion tabs on the `moonshotai` org (`ev-kimi-hf`) for usage
  questions.
- **GitHub issues** on `moonshotai/Kimi-K2` (`ev-github`) for deployment, serving-engine, and
  reproduction problems.

There is no paid support tier for the open weights - this is community and maintainer support
around an open-weight release.

<!-- deprecation is a `gap` item - no published deprecation/EoL policy. Older HF revisions remain
     downloadable, but no formal support window or sunset commitment is documented. See gap_reason. -->

<!-- item: known-issues -->
## Tracked known issues

Drawn from model-card and third-party caveats rather than a formal issue tracker (hence *partial*):

- **China-aligned topic censorship** on politically sensitive prompts.
- **Lighter safety coverage** than frontier labs, with **no companion guard model**.
- **Operational burden** of a 1T-parameter model - multi-node infrastructure is required with no
  small fallback variant.
