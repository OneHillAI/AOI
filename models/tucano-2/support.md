# Support - Tucano 2 (Qwen-derived 0.5B, 1.5B and 3.7B; Base, Instruct and Think)

_Troubleshooting, versions, security disclosure, channels and deprecation._

<!-- item: troubleshooting -->
## Common problems & fixes

- Repetition or run-on output: keep `repetition_penalty` near 1.2 and set a hard `max_new_tokens` (`ev-card-instruct`).
- Wrong format or poor answers: build the prompt with the repo's chat template, not hand-written strings (`ev-configs`).
- Failures beyond 4,096 tokens: split the input and retrieve.
- Invented facts: the cards and a third-party run both report hallucination, so verify outputs (`ev-community`).
- Weak instruction following or code: pair the model with tooling, or fine-tune. The paper says the SFT data lacks IFEval-style prompts and has few coding samples (`ev-paper`).

<!-- item: release-versioning -->
## Versions, changelog & cadence

The models were uploaded in February 2026, and the paper is dated 3 March 2026 (`ev-paper`). The post-trained repos were last edited on 2026-08-13, and the GigaVerbo-v2 dataset card on 2026-09-30 (`ev-hf-platform`, `ev-gv2`). There is no changelog file or release notes. The commit hash is the anchor, so pin it. The publisher has since released similar suites for Hindi and Bengali, and no roadmap for Tucano 2 is stated.

<!-- item: security-disclosure -->
## Security / vulnerability disclosure

The llm-foundry code repository has a SECURITY.md that asks reporters to email a maintainer privately and calls the project research software without a security team (`ev-code`). The model repos publish no security policy or contact.

<!-- item: channels -->
## Community & support channels

Hugging Face discussions are open and empty on the repos inspected (`ev-hf-platform`). The llm-foundry repository takes GitHub issues. The dataset cards list a Polygl0t project address and maintainer emails (`ev-gv2-post`).

<!-- deprecation is a `gap` item in entry.yaml - see its gap_reason. -->

<!-- item: known-issues -->
## Tracked known issues

The publisher lists hallucination, bias, repetition and language limits on every card, and the paper lists weak instruction following, coding and long-context retrieval (`ev-card-instruct`, `ev-paper`). The corpus licence is mixed with two non-commercial sources, and Tucano2-qwen-1.5B-Base has no LICENSE file (`ev-gv2`, `ev-licence-files`). The models have no public issue tracker.
