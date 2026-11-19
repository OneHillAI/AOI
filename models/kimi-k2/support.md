# Support - Kimi K2 (Moonshot AI)

_Troubleshooting, versions, security disclosure, channels and deprecation._

<!-- item: troubleshooting -->
## Common problems & fixes

Common pitfalls, not an exhaustive catalogue:

- Out-of-memory and sharding failures: the 1T model must be sharded across a multi-GPU or
  multi-node cluster. Size tensor and pipeline parallelism to the hardware, or use KTransformers
  CPU offload.
- Block-FP8 kernel or engine errors: match the vLLM, SGLang or TensorRT-LLM version to one that
  supports the block-FP8 weights and MLA attention. Version mismatch is a common cause.
- Garbled or over-verbose Instruct output: the chat template is most likely not applied. Use
  `apply_chat_template` and do not prompt the Base checkpoint as a chat model.
- Non-reproducible results or silent updates: a deployment floating on `main` changes under you.
  Pin an exact revision and verify checksums.

<!-- item: release-versioning -->
## Versions, changelog & cadence

Kimi K2 ships as Base and Instruct checkpoints on the verified `moonshotai` org, tracked as
immutable Hugging Face revisions. The revision hash is the changelog anchor: pin it and diff
against a newer revision when upgrading. The technical report "Kimi K2: Open Agentic
Intelligence" accompanies the release. The Instruct card marks `Kimi-K2-Instruct-0905` as the
newer version. Later generations (K2.5, K2.6, K2.7-Code and K3) exist and are not covered here.
On the hosted API, K2 series models closed to new users on 2026-10-31 and are planned for
retirement by the end of December 2026; the downloadable weights are not affected.

<!-- security-disclosure is a `gap` item - no formal published vulnerability-disclosure or
     security policy was found; contact is only the general moonshotai Hugging Face / GitHub org
     presence. See gap_reason. This absence is also why Governance scores 3 rather than higher. -->

<!-- item: channels -->
## Community & support channels

Usage questions go to the model discussion tabs on the `moonshotai` Hugging Face org
(`ev-kimi-hf`). Deployment, serving-engine and reproduction problems go to GitHub issues on
`moonshotai/Kimi-K2` (`ev-github`). There is no paid support tier for the open weights; support
is community and maintainer based.

<!-- deprecation is a `gap` item - no published deprecation/EoL policy. Older HF revisions remain
     downloadable, but no formal support window or sunset commitment is documented. See gap_reason. -->

<!-- item: known-issues -->
## Tracked known issues

These come from model-card and third-party caveats, not a formal issue tracker, so coverage is
partial. China-aligned topic censorship appears on politically sensitive prompts. Safety coverage
is lighter than at frontier labs, with no companion guard model. A 1T-parameter model carries an
operational burden: multi-node infrastructure is required, with no small fallback variant.
