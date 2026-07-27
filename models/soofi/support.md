# Support - Soofi (Soofi-S)

_How do we keep it running and get help? Troubleshooting, versions/changelog, channels, and known
issues; security-disclosure and a deprecation policy are current gaps._

<!-- item: troubleshooting -->
## Common problems & fixes

Aggregated preview pitfalls (not an exhaustive catalogue):

- **`AutoModel` fails to load / unknown architecture.** Soofi-S is a custom hybrid Mamba-2/MoE - pass
  `trust_remote_code=True` and use a recent transformers build.
- **Tool calling silently ignored.** Your runtime is not applying the native tool template - run
  `llama-server --jinja` (llama.cpp) rather than a runtime whose template strips tools (e.g. Ollama).
- **Serving stack rejects the model.** Custom-architecture support is still maturing; confirm your
  vLLM/llama.cpp version supports the hybrid arch, or fall back to a first-party GGUF build.
- **Out-of-memory loading weights.** Decode uses ~3B active params, but all ~30B must be resident -
  use a first-party GGUF/3-bit quant or multi-GPU; the near-constant cache means long context is not
  the culprit.
- **Non-reproducible results / silent updates.** You floated on `main`; pin an exact Hugging Face
  revision and verify checksums.

<!-- item: release-versioning -->
## Versions, changelog & cadence

Soofi-S is in an early **preview/beta** cadence rather than a settled semantic-version stream:
alongside **Soofi-S-Base** there are **Instruct-Preview**, **Isar-Preview** (reasoning) and
**Rhine-Preview** variants, plus first-party GGUF/3-bit quant repos and named **iteration
checkpoints** (e.g. `iter_1056000`, the final constant-annealing checkpoint used for evaluation).
Individual versions are tracked as **Hugging Face revisions** on the `Soofi-Project` org, so the
revision hash is your changelog anchor - pin it and diff against a newer revision when you upgrade.
The pretraining technical report documents architecture, data and evaluation for the release.

<!-- security-disclosure is a `gap` item - no formal published vulnerability-disclosure or security
     policy exists; contact is only the Soofi-Project Hugging Face / GitHub org presence. See
     gap_reason. This absence is part of why Governance scores 4 rather than 5. -->

<!-- item: channels -->
## Community & support channels

- **Hugging Face** model/dataset discussion tabs on the `Soofi-Project` org (`ev-hf-org`) for usage
  questions.
- **GitHub issues** on `soofi-project/Soofi-Pretraining`, `soofi-trainer` and `soofi-model-hosting`
  (`ev-github`) for training-code and reproduction problems.
- **The `soofi.info` project site** and the **CAIRNE** launch page (`ev-cairne`) for announcements,
  plus the **KI-Bundesverband-coordinated consortium** behind the project.

There is no paid support tier - this is community and consortium support around an open project.

<!-- deprecation is a `gap` item - no published deprecation/EoL policy. As an early preview, prior
     revisions remain downloadable, but no formal support window or sunset commitment is documented.
     See gap_reason. -->

<!-- item: known-issues -->
## Tracked known issues

Drawn from model-card caveats rather than a formal issue tracker (hence *partial*):

- **Preview status** - capability, safety and tooling are still stabilising.
- **Safety/privacy features documented as incomplete**, with no companion guard model.
- **Tool-call template inconsistencies** across runtimes (native under `--jinja`; omitted by some).
- **Custom-architecture runtime-support maturity** - not every serving stack/version handles the
  hybrid Mamba-2/MoE yet.
