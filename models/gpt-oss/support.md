# Support - OpenAI gpt-oss (gpt-oss-120b / gpt-oss-20b)

_How do we keep it running and get help? Troubleshooting, versions/changelog, channels, and
known issues; security-disclosure and deprecation policy are current gaps._

<!-- item: troubleshooting -->
## Common problems & fixes

Aggregated common pitfalls (not an exhaustive catalogue):

- **Malformed or empty output / leaked reasoning.** You are almost certainly not applying the
  **harmony** format - build prompts with the `openai/harmony` renderer, and never display the
  raw reasoning channel to users.
- **Model won't load / dtype errors.** MXFP4 needs a recent runtime; upgrade
  transformers/vLLM/llama.cpp and load with `torch_dtype="auto"` so the library picks MXFP4.
- **GGUF loads in one runtime but not another.** Quant type codes have differed between
  llama.cpp and Ollama for gpt-oss; use a GGUF built for your specific runtime and re-verify.
- **Out-of-memory.** Serve the 20b, keep native MXFP4, or reduce max context to shrink the KV
  cache; the 120b needs an 80GB GPU.
- **Non-reproducible results / silent updates.** You floated on `main`; pin an exact Hugging
  Face revision and verify checksums.

<!-- item: release-versioning -->
## Versions, changelog & cadence

gpt-oss launched in **August 2025** as a **single release of two sizes** (gpt-oss-120b and
gpt-oss-20b) rather than a rolling semantic-version stream. Individual versions are tracked as
**immutable Hugging Face revisions** on the `openai` org, so the revision hash is your
changelog anchor: pin it, and diff against a newer revision if OpenAI republishes. The model
card / arXiv report documents what shipped. (OpenAI's separate `gpt-oss-safeguard` classifier
family is a *different* release rather than a new gpt-oss version.)

<!-- security-disclosure is a `gap` item - no formal, weight-specific vulnerability-disclosure
     or cryptographic signing process was found. OpenAI ran a launch red-teaming challenge and
     accepts GitHub issues, but there is no documented ongoing CVE-style process for the
     weights. See gap_reason. This absence is also part of why Governance scores 4 rather than 5. -->

<!-- item: channels -->
## Community & support channels

- **GitHub** - `openai/gpt-oss` (reference implementations, serving/fine-tuning guidance) and
  `openai/harmony` (the response-format renderer) for code-level issues (`ev-github`).
- **OpenAI Cookbook** guides for gpt-oss deployment and harmony usage.
- **Hugging Face** model discussion tabs on the `openai` org (`ev-hf-openai`) for usage
  questions.

There is no paid support tier for the open weights - this is community and maintainer support
around an open release.

<!-- deprecation is a `gap` item - no published deprecation/EoL policy for gpt-oss checkpoints.
     The released Hugging Face revisions remain downloadable, but no formal support window or
     sunset commitment is documented. See gap_reason. -->

<!-- item: known-issues -->
## Tracked known issues

Drawn from model-card caveats rather than a formal issue tracker (hence *partial*):

- **Raw chain-of-thought is unsafe to display** - it is deliberately unaligned and can contain
  incorrect or harmful content.
- **Safety tuning is removable** on open weights - the exact concern behind OpenAI's
  malicious-fine-tuning study; re-evaluate any derivative.
- **Standard hallucination profile** for its class - strong reasoning does not eliminate
  confabulation.
- **English-centric** - other-language quality is unverified.
