# Support - Gemma 4 (E2B, E4B, 12B, 26B A4B, 31B)

_How do we keep it running and get help? Troubleshooting, versions/changelog, channels;
security-disclosure and deprecation policy are current gaps._

<!-- item: troubleshooting -->
## Common problems & fixes

Aggregated from the model card best practices and open repository discussions (not an
exhaustive catalogue):

- **Odd or looping tool calls, unbalanced turn tags, lost reasoning.** These are chat-template
  defects fixed in commits to the repositories (for example 'chat template - null handling,
  reasoning preservation, turn-tag balance, input validation' and a later response-template
  addition). Update to the current revision, then pin it (`ev-hf-scan`).
- **Thinking text appears in the answer or in history.** Parse the response with the
  processor's `parse_response`, and do not feed earlier thinking back except on tool-call turns
  (`ev-card-31b`).
- **Empty thought block with thinking off.** Expected for every size except E2B and E4B.
- **Weak image or audio results.** Put images before text and audio after text, and raise the
  image token budget for OCR (`ev-card-31b`).
- **Fine-tuned model never stops.** Base models end with `<eos>`, instruction-tuned models
  with `<turn|>`; add the right end token (`ev-tech-report`).
- **Out of memory on the 26B A4B.** All 25.2B parameters must be resident even though 3.8B are
  active (`ev-docs-overview`).

<!-- item: release-versioning -->
## Versions, changelog & cadence

Gemma 4 launched on 2 April 2026 with four sizes (E2B, E4B, 26B A4B, 31B); the 12B Unified
model followed (Hugging Face repository created 23 May 2026) and the model card now lists five
sizes (`ev-blog`, `ev-hf-inventory`). Official QAT and drafter checkpoints appeared from April
to June 2026. The technical report is v2 (v1 2 July, v2 24 July 2026) (`ev-tech-report`), and
the Hugging Face repositories were last modified between July and November 2026, with the
31B-it commit history showing chat-template fixes on 10 April, 28 April, 18 May and 15 July and a response-template addition on 20 July (`ev-hf-scan`). The EU
training-content summary is v1 dated 31 July 2026 (`ev-eu-summary`). Hugging Face revisions are
immutable, so the commit hash is your changelog anchor: pin it, and diff against a newer
revision when you choose to upgrade.

<!-- security-disclosure is a `gap` item - no Gemma-specific security policy, contact or
     advisory process was found. Google's organisation-wide GitHub policy names g.co/vulnz
     (`ev-security-policy`) but no document read says it covers model weights. This absence also
     holds Governance to 3. -->

<!-- item: channels -->
## Community & support channels

- **Hugging Face repository discussions** on each `google/gemma-4-*` repository, which are active
  (`ev-hf-scan`).
- **GitHub:** issues for the `google-deepmind/gemma` library, and the `google-gemma` organisation
  that the model card links (`ev-gemma-lib`, `ev-card-31b`).
- **Documentation:** gemma.ai (`ev-docs-overview`); Kaggle is named as a distribution channel but
  was not checked.

There is no paid support tier from Google for the open weights. Hosted use goes through Google
Cloud services named in the launch blog (`ev-blog`), under their own terms, which this entry
does not assess.

<!-- deprecation is a `gap` item - no published deprecation or end-of-life policy for Gemma 4
     checkpoints. Older revisions remain on Hugging Face but no support window is stated.
     See gap_reason. -->

<!-- item: known-issues -->
## Tracked known issues

From the repository discussions, commits and independent pages (partial, because there is no
single issue tracker for the weights):

- Chat-template defects, including an open report dated 18 November 2026 that an image-only
  tool result renders its placeholder after the tool block closes (`ev-hf-scan`).
- Thinking-block behaviour differs between the small and larger models (`ev-card-31b`).
- A lower rank on the Artificial Analysis Intelligence Index v5.0.1 than the launch coverage
  suggested (`ev-aa`).
- Gemma 3 derivatives and other Gemma releases keep the older Gemma Terms; check each
  checkpoint's licence tag before reusing a Gemma 4 conclusion (see Assess, license item).
