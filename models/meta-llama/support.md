# Support - Meta Llama 3.x (Llama 3.1 / 3.3 text line)

_Troubleshooting, versions, security disclosure, channels and deprecation._

<!-- item: troubleshooting -->
## Common problems & fixes

The two most frequent problems are operational, not model quality.

Gated-access failures (`401`/`403`, "you do not have access") occur when the license has not been
accepted on the model page or the Hugging Face token has not been granted access. Approval is not
always instant. Use the same account for acceptance and token.

Tokenizer and chat-template mismatches produce rambling, role-confused, or never-terminating
output. This happens with hand-built prompt strings or the wrong special tokens. Render prompts
with the tokenizer's `apply_chat_template` and configure the end-of-turn token as a stop token in
your serving stack. Quantized community builds occasionally ship a stale tokenizer/template, so
cross-check against the canonical `meta-llama` repo.

<!-- item: release-versioning -->
## Versions & changelog

Meta ships on a predictable generational cadence: Llama 3.1 (8B/70B/405B), Llama 3.3 (a 70B
refresh narrowing the gap to 405B), then Llama 4 (Scout/Maverick/Behemoth, mixture-of-experts,
multimodal). Each generation is released with model cards documenting the changes. There is no
rolling per-commit changelog for the weights. The durable way to track and pin a build is the
Hugging Face revision (commit hash) on the canonical org. Pin a revision in production instead of
tracking `main`.

<!-- item: security-disclosure -->
## Security disclosure process

Meta provides a Responsible Use reporting path for model issues, policy violations, and feedback
(via the Responsible Use Guide and associated reporting channels). There is no formal CVE-style
vulnerability-disclosure process and no cryptographic signing for the model weights, which is the
gap noted in the governance score. Coverage is partial: model behaviour can be reported, but no
security-response SLA or signed-artifact verification path is published.

<!-- item: channels -->
## Community & support channels

Support is community- and platform-based, with no formal support contract. Channels are the Meta
Llama community resources and documentation on llama.com, Hugging Face model discussions on each
repo, and Meta's GitHub repositories (llama-models, llama-recipes/cookbook, torchtune) for issues
and examples. The serving-ecosystem projects (vLLM, llama.cpp, Ollama) also carry active
Llama-specific issue trackers.

<!-- item: known-issues -->
## Tracked known issues

The model cards document the standing known issues: hallucination in the class-standard profile,
residual jailbreak and prompt-injection susceptibility, and the explicit warning that base
checkpoints are not safety-tuned and must not be deployed as chat models. Long-context recall
softens mid-window, and multilingual quality outside the eight officially supported languages is
not validated. These caveats persist across releases, and the safe-deployment controls are
designed to contain them.
