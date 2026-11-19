# Support - MORENA 1.5B (base and instruct)

_Troubleshooting, versions, security disclosure, channels and deprecation._

<!-- item: troubleshooting -->
## Common problems & fixes

Aggregated from the cards, the paper and the repo files (`ev-card-instruct`, `ev-trainer`, `ev-paper`). The list is not exhaustive.

Garbage or looping output usually means `<|user|>` strings or the wrong markers. Use `<reserved_0>` and `<reserved_1>` as in the chat template.

Refusals on harmless requests are a known issue: 41% of ordinary benign requests are not answered well. Rephrase, or fine-tune for your domain.

About one generation in six does not emit an end-of-sequence token within 200 tokens. Set a hard token limit and stop on `<eos>`.

In 59 of 1,000 into-English prompts the model repeated the instruction instead of translating, and Yoruba was worst. Check the prompt and the language.

Loading with transformers fails by design. Use the publisher PyTorch file or the GGUF.

`load_example.py` still says "preview weights", but the card and paper describe the same files as the release.

<!-- item: release-versioning -->
## Versions, changelog & cadence

All eight repos were created on 2026-09-15 and made public on 2026-09-18, the release date in the paper. The only later change to the instruct repo is `tokenizer_config.json` with a chat template on 2026-10-14. There is no changelog file or release notes, so pin the commit hash.

The card compares against a "previous version" (benign answering 47.9%, grounded faithfulness 31%) that is not published in the org. No release cadence or roadmap is stated beyond the paper's promise of a corpus and datasheet "once the legal review is complete" (`ev-hf-platform`, `ev-paper`).

<!-- security-disclosure is a `gap` item - no SECURITY.md, security contact or disclosure
     process was found in either repo or on vambo.ai. See gap_reason. This holds Governance
     at 2. -->

<!-- item: channels -->
## Community & support channels

The Hugging Face discussions tab on `vamboai/morena-1.5b-instruct` is open but empty (2026-11-19). The Vambo AI site (vambo.ai) offers contact and enterprise forms. Its blog has no posts, and the MORENA paper is listed only on the research page (`ev-vambo-site`).

The Fikira dataset card lists a general questions address. It is not a support or security channel for the model.

<!-- deprecation is a `gap` item - no deprecation or support-window statement exists. -->

<!-- item: known-issues -->
## Tracked known issues

There is no public issue tracker. The publisher lists its own known issues in the card and paper (`ev-card-instruct`, `ev-paper`).

Over-refusal of benign requests (41%) is only partly fixed. Grounded generation faithfulness fell from 31% to 23% against the previous version. The chosen checkpoint misses the publisher's own selection rule on privacy (by 0.1 points), drugs (1.0), violence (2.6) and degeneracy (1.3% against a 1% limit). Retrieval QA and African multiple choice are near chance.

isiNdebele is evaluated on transcripts only. The 0.5B model loses about a third of the teacher's English reasoning, and neither smaller model has been safety-tested.
