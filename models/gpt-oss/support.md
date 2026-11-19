# Support - OpenAI gpt-oss (gpt-oss-120b / gpt-oss-20b)

_Troubleshooting, versions, security disclosure, channels and deprecation._

<!-- item: troubleshooting -->
## Common problems & fixes

Common pitfalls, not an exhaustive catalogue.

Malformed or empty output, or leaked reasoning, usually means the harmony format is not
applied. Build prompts with the `openai/harmony` renderer and never display the raw reasoning
channel to users.

Model load or dtype errors: MXFP4 needs a recent runtime. Upgrade transformers, vLLM or
llama.cpp and load with `torch_dtype="auto"` so the library picks MXFP4.

A GGUF that loads in one runtime but not another: quant type codes have differed between
llama.cpp and Ollama for gpt-oss. Use a GGUF built for the specific runtime and verify it.

Out-of-memory: serve the 20b, keep native MXFP4, or reduce max context to shrink the KV cache.
The 120b needs an 80GB GPU.

Non-reproducible results and silent updates come from floating on `main`. Pin an exact
Hugging Face revision and verify checksums.

<!-- item: release-versioning -->
## Versions, changelog & cadence

gpt-oss launched in August 2025 as a single release of two sizes (gpt-oss-120b and
gpt-oss-20b), not a rolling semantic-version stream. Versions are tracked as immutable
Hugging Face revisions on the `openai` org, so the revision hash is the changelog anchor. Pin
it, and diff against a newer revision if OpenAI republishes. The model card and arXiv report
document what shipped. OpenAI's separate `gpt-oss-safeguard` classifier family is a different
release, not a new gpt-oss version.

<!-- security-disclosure is a `gap` item - no formal, weight-specific vulnerability-disclosure
     or cryptographic signing process exists. OpenAI ran a launch red-teaming challenge and
     accepts GitHub issues, but there is no documented ongoing CVE-style process for the
     weights. See gap_reason. The absence is also part of why Governance scores 4, not 5. -->

<!-- item: channels -->
## Community & support channels

Code-level issues go to GitHub: `openai/gpt-oss` (reference implementations, serving and
fine-tuning guidance) and `openai/harmony` (the response-format renderer) (`ev-github`). The
OpenAI Cookbook has guides for gpt-oss deployment and harmony usage. Usage questions go to the
Hugging Face model discussion tabs on the `openai` org (`ev-hf-openai`).

There is no paid support tier for the open weights, only community and maintainer support
around an open release.

<!-- deprecation is a `gap` item - no published deprecation/EoL policy for gpt-oss checkpoints.
     The released Hugging Face revisions remain downloadable, but no formal support window or
     sunset commitment is documented. See gap_reason. -->

<!-- item: known-issues -->
## Tracked known issues

These come from model-card caveats, not a formal issue tracker, hence partial. Raw
chain-of-thought is unsafe to display, because it is deliberately unaligned and can contain
incorrect or harmful content. Safety tuning is removable on open weights, the concern behind
OpenAI's malicious-fine-tuning study, so any derivative needs re-evaluation. The hallucination
profile is standard for the class, since strong reasoning does not eliminate confabulation.
Behaviour is English-centric, and other-language quality is unverified.
