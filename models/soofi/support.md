# Support - Soofi (Soofi-S)

_Troubleshooting, versions, security disclosure, channels and deprecation._

<!-- item: troubleshooting -->
## Common problems & fixes

Preview pitfalls, not an exhaustive catalogue:

- `AutoModel` fails to load or reports an unknown architecture: Soofi-S is a custom hybrid
  Mamba-2/MoE. Pass `trust_remote_code=True` and use a recent transformers build.
- Tool calling is silently ignored: the runtime is not applying the native tool template. Run
  `llama-server --jinja` (llama.cpp) instead of a runtime whose template strips tools (e.g.
  Ollama).
- The serving stack rejects the model: custom-architecture support is still maturing. Confirm
  your vLLM or llama.cpp version supports the hybrid architecture, or fall back to a first-party
  GGUF build.
- Out-of-memory when loading weights: decode uses ~3B active params, but all ~30B must be
  resident. Use a first-party GGUF or 3-bit quant or multi-GPU; the near-constant cache means long
  context is not the cause.
- Non-reproducible results or silent updates: a deployment floating on `main` changes under you.
  Pin an exact Hugging Face revision and verify checksums.

<!-- item: release-versioning -->
## Versions, changelog & cadence

Soofi-S is on an early preview/beta cadence, not a settled semantic-version stream. Alongside
Soofi-S-Base there are Instruct-Preview, Isar-Preview (reasoning) and Rhine-Preview variants,
first-party GGUF and 3-bit quant repos, and named iteration checkpoints (e.g. `iter_1056000`, the
final constant-annealing checkpoint used for evaluation). Versions are tracked as Hugging Face
revisions on the `Soofi-Project` org, so the revision hash is the changelog anchor: pin it and
diff against a newer revision when upgrading. The pretraining technical report documents
architecture, data and evaluation for the release.

<!-- security-disclosure is a `gap` item - no formal published vulnerability-disclosure or security
     policy exists; contact is only the Soofi-Project Hugging Face / GitHub org presence. See
     gap_reason. This absence is part of why Governance scores 4 rather than 5. -->

<!-- item: channels -->
## Community & support channels

Usage questions go to the model and dataset discussion tabs on the `Soofi-Project` Hugging Face
org (`ev-hf-org`). Training-code and reproduction problems go to GitHub issues on
`soofi-project/Soofi-Pretraining`, `soofi-trainer` and `soofi-model-hosting` (`ev-github`).
Announcements come from the `soofi.info` project site and the CAIRNE launch page (`ev-cairne`),
plus the KI-Bundesverband-coordinated consortium behind the project. There is no paid support
tier; support is community and consortium based.

<!-- deprecation is a `gap` item - no published deprecation/EoL policy. As an early preview, prior
     revisions remain downloadable, but no formal support window or sunset commitment is documented.
     See gap_reason. -->

<!-- item: known-issues -->
## Tracked known issues

These come from model-card caveats, not a formal issue tracker, so coverage is partial.

- Preview status: capability, safety and tooling are still stabilising.
- Safety and privacy features are documented as incomplete, with no companion guard model.
- Tool-call templates are inconsistent across runtimes (native under `--jinja`; omitted by some).
- Runtime support is immature: not every serving stack and version handles the hybrid Mamba-2/MoE
  yet.
