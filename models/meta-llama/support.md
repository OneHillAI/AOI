# Support - Meta Llama (Llama 3.x / Llama 4)

_How do we keep it running and get help? Troubleshooting, versions/changelog, security
disclosure, community channels, deprecation._

<!-- item: troubleshooting -->
## Common problems & fixes

The two most frequent problems are operational, not model quality:

- **Gated-access failures** (`401`/`403`, "you do not have access"). You must accept the
  license on the model page *and* authenticate with a Hugging Face token that has been
  granted access. Approval is not always instant. Use the same account for acceptance and
  token.
- **Tokenizer / chat-template mismatches.** Hand-built prompt strings or the wrong special
  tokens produce rambling, role-confused, or never-terminating output. Always render
  prompts with the tokenizer's `apply_chat_template` and make sure the end-of-turn token is
  configured as a stop token in your serving stack. Quantized community builds occasionally
  ship a stale tokenizer/template - cross-check against the canonical `meta-llama` repo.

<!-- item: release-versioning -->
## Versions & changelog

Meta ships on a predictable **generational cadence**: Llama 3.1 (8B/70B/405B) → Llama 3.3
(70B refresh narrowing the gap to 405B) → Llama 4 (Scout/Maverick/Behemoth, mixture-of-
experts, multimodal). Each generation is released with model cards documenting the changes.
There is no rolling per-commit changelog for the weights; the durable way to track and pin
a specific build is the **Hugging Face revision** (commit hash) on the canonical org.
Always pin a revision in production rather than tracking `main`.

<!-- item: security-disclosure -->
## Security disclosure process

Meta provides a **Responsible Use** reporting path for model issues, policy violations, and
feedback (via the Responsible Use Guide and associated reporting channels). What is **not**
present is a formal, CVE-style vulnerability-disclosure process or cryptographic signing
for the model weights themselves - this is the gap noted in the governance score. Coverage
is therefore partial: there is a documented way to report model behaviour, but no published
security-response SLA or signed-artifact verification path.

<!-- item: channels -->
## Community & support channels

Support is community- and platform-based rather than a formal support contract: the **Meta
Llama** community resources and documentation on llama.com, **Hugging Face model
discussions** on each repo, and Meta's **GitHub** repositories (llama-models, llama-recipes/
cookbook, torchtune) for issues and examples. The broad serving-ecosystem projects (vLLM,
llama.cpp, Ollama) also carry active Llama-specific issue trackers.

<!-- item: known-issues -->
## Tracked known issues

The model cards document the standing known issues honestly: **hallucination** in the
class-standard profile, residual **jailbreak and prompt-injection** susceptibility, and the
explicit warning that **base checkpoints are not safety-tuned** and must not be deployed as
chat models. Long-context recall softens mid-window, and multilingual quality outside the
eight officially supported languages is not validated. None are regressions unique to a
release; they are the persistent caveats the safe-deployment controls are designed to
contain.
