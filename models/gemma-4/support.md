# Support - Gemma 4 (E2B, E4B, 12B, 26B A4B, 31B)

_Troubleshooting, versions, security disclosure, channels and deprecation._

<!-- item: troubleshooting -->
## Common problems & fixes

These come from the model card best practices and open repository discussions, and are not an exhaustive catalogue:

- Odd or looping tool calls, unbalanced turn tags and lost reasoning are chat-template defects fixed in commits to the repositories (for example 'chat template - null handling, reasoning preservation, turn-tag balance, input validation' and a later response-template addition). Update to the current revision, then pin it (`ev-hf-scan`).
- Thinking text in the answer or in history: parse the response with the processor's `parse_response`, and do not feed earlier thinking back except on tool-call turns (`ev-card-31b`).
- An empty thought block with thinking off is expected for every size except E2B and E4B.
- Weak image or audio results: put images before text and audio after text, and raise the image token budget for OCR (`ev-card-31b`).
- A fine-tuned model that never stops needs the right end token: base models end with `<eos>`, instruction-tuned models with `<turn|>` (`ev-tech-report`).
- Out of memory on the 26B A4B: all 25.2B parameters must be resident even though 3.8B are active (`ev-docs-overview`).

<!-- item: release-versioning -->
## Versions, changelog & cadence

Gemma 4 launched on 2 April 2026 with four sizes (E2B, E4B, 26B A4B, 31B). The 12B Unified model followed (Hugging Face repository created 23 May 2026) and the model card lists five sizes (`ev-blog`, `ev-hf-inventory`). Official QAT and drafter checkpoints appeared from April to June 2026.

The technical report is v2 (v1 2 July, v2 24 July 2026) (`ev-tech-report`). The Hugging Face repositories were last modified between July and November 2026. The 31B-it commit history shows chat-template fixes on 10 April, 28 April, 18 May and 15 July and a response-template addition on 20 July (`ev-hf-scan`). The EU training-content summary is v1 dated 31 July 2026 (`ev-eu-summary`).

Hugging Face revisions are immutable, so the commit hash is the changelog anchor: pin it, and diff against a newer revision when upgrading.

<!-- security-disclosure is a `gap` item - no Gemma-specific security policy, contact or
     advisory process is published. Google's organisation-wide GitHub policy names g.co/vulnz
     (`ev-security-policy`) but no document says it covers model weights. This absence also
     holds Governance to 3. -->

<!-- item: channels -->
## Community & support channels

- Hugging Face repository discussions on each `google/gemma-4-*` repository, which are active (`ev-hf-scan`).
- GitHub issues for the `google-deepmind/gemma` library, and the `google-gemma` organisation that the model card links (`ev-gemma-lib`, `ev-card-31b`).
- The documentation at gemma.ai (`ev-docs-overview`). Kaggle is named as a distribution channel but is unchecked.

There is no paid support tier from Google for the open weights. Hosted use goes through Google Cloud services named in the launch blog (`ev-blog`), under their own terms, which are not assessed here.

<!-- deprecation is a `gap` item - no published deprecation or end-of-life policy for Gemma 4
     checkpoints. Older revisions remain on Hugging Face but no support window is stated.
     See gap_reason. -->

<!-- item: known-issues -->
## Tracked known issues

Known issues come from the repository discussions, commits and independent pages, and are partial because there is no single issue tracker for the weights:

- Chat-template defects, including an open report dated 18 November 2026 that an image-only tool result renders its placeholder after the tool block closes (`ev-hf-scan`).
- Thinking-block behaviour differs between the small and larger models (`ev-card-31b`).
- A lower rank on the Artificial Analysis Intelligence Index v5.0.1 than the launch coverage suggested (`ev-aa`).
- Gemma 3 derivatives and other Gemma releases keep the older Gemma Terms; check each checkpoint's licence tag before reusing a Gemma 4 conclusion (see Assess, license item).
