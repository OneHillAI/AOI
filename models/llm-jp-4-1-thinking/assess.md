# Assess - LLM-jp-4.1 thinking (8B, 32B-A3B, 33B)

_Openness, licence, provenance, EU AI Act position, safety, evaluation and the AOI score._

Scope. This entry scores the LLM-jp-4.1 post-trained "thinking" series from the National
Institute of Informatics (NII), Japan: `llm-jp-4.1-8b-thinking`, `llm-jp-4.1-32b-a3b-thinking`
and `llm-jp-4.1-33b-thinking`, plus their official GGUF builds. The three share one licence
(Apache-2.0), one card text, one corpus lineage and one safety statement, so they are one
release.

Not in this entry, and listed as follow-ups: the LLM-jp-4 (4.0) thinking models and the three
base models (their cards say the models "have not been tuned to ensure outputs align with human
intent and safety considerations", a different safety posture), the LLM-jp-4-VL vision-language
model, the `kaburi-tts` speech model, and third-party derivatives such as ELYZA-Thinking.

<!-- item: intended-use -->
## Intended & out-of-scope use

Use it for research and development on Japanese and English reasoning, chat, code and tool
calling. The cards are explicit that "the models released here are research and development
models and are not intended for direct use in production services" (`ev-card-41`). The NII
release page adds that users "are requested to use it appropriately and at their own
responsibility" under Japan's December 2025 guideline for AI research, development and
utilisation (`ev-release-page`).

That wording is use guidance from the publisher. It is not a clause of the Apache-2.0 licence,
so it does not forbid production use. It does mean the provider has not stated an intended
purpose that supports a production deployment, and that the evaluation burden sits with you.
Out of scope as presented: customer-facing or autonomous use without your own safety work,
and any use that relies on the models as a safety-tuned product.

<!-- item: limitations -->
## Known limitations, bias & failure modes

- Safety evidence is thin. The cards say the models "may still generate inaccurate,
  inappropriate, or otherwise undesirable outputs" (`ev-card-41`).
- Hard reasoning and tools trail peers. The publisher blog reports large gains from 4.0 to
  4.1 but a continuing gap to existing open-weight models on GPQA Diamond and AIME, and a large
  gap to Qwen3.5 on tool calling, especially long-context multi-turn (`ev-blog`).
- English trails Japanese. In the technical report the 32B-A3B model matches Qwen3-8B and
  gpt-oss-20b on Japanese llm-jp-eval (0.605 against 0.608 and 0.604) but scores 0.650 against
  0.714 and 0.704 on English (`ev-techreport`).
- SFT and DPO only: There is no reinforcement-learning stage; the blog says one is planned
  (`ev-blog`).
- Shorter answers in 4.1: The blog says 4.1 answers were made shorter and MT-Bench is flat or
  lower than 4.0 (`ev-blog`).
- Training-data provenance: Some training data was generated or filtered with other open
  models (gpt-oss-120b, Qwen3-32B); the Nemotron agentic subset came from several third-party
  models (`ev-sft-dpo`, `ev-techreport`).

<!-- item: openness -->
## Openness tier & components

The tier is `open_weights_recipe`.

| Component | Rating | Evidence |
|---|---|---|
| Weights | open | Apache-2.0, ungated, safetensors BF16 and official GGUF (`ev-hub-api`, `ev-gguf`) |
| Training data | partial | Pre-training and mid-training corpora are public on GitLab with per-source licences; some portions "are excluded from public release due to licensing constraints" (`ev-card-41`, `ev-corpus-v4`, `ev-corpus-v41`, `ev-corpus-mid2`) |
| Training code | partial | Pre-training and mid-training scripts and installers are public (`ev-code`); no document confirms the SFT and DPO code behind the 4.1 recipe |
| Evaluation | partial | llm-jp-judge and llm-jp-eval are Apache-2.0 and results are published (`ev-card-41`), but the judge for the headline evaluations is gpt-5.4, a closed model |
| Documentation | open | Model cards, a technical report, dataset cards and a cookbook (`ev-techreport`, `ev-cookbook`) |
| Licence | open | Apache-2.0 (`ev-license`) |

Downloadable: the GitLab projects for corpus v4.1, corpus v4 and mid-training corpus v2 are
public and list `.jsonl.gz` data files without login. The 4.1 SFT dataset and three DPO
datasets on Hugging Face are ungated.

What is not released: the NWJC (25.7B tokens, L2) and Ceek.jp News (12.5B tokens, L3) Japanese
subcorpora "cannot be redistributed" (`ev-corpus-v4`, `ev-techreport`); the ichikara
instruction data needs a paid licence; AnswerCarefully, the Japanese safety set used in SFT
and DPO, is gated; `llmc_math_dataset` and `synthetic_if_ja` are marked "To be released"
(`ev-sft-dpo`). The mid-training corpus includes `nemotron_pretraining_code_v2` (491B tokens)
under the "NVIDIA Data Access Agreement for Model Training", a custom agreement and not an open
licence (`ev-corpus-mid2`); check it before redistributing that corpus.

The technical report states that the models were designed to be "consistent with the Open
Source AI Definition" (`ev-techreport`). It does not claim full OSAID compliance, and with the
exclusions above OneHill does not rate it fully open.

Training code: the report links the 8B and 32B-A3B pre-training configurations on GitHub, and
the `llm-jp/scripts` tree contains 33B-dimension scripts (`v4-32b-phase1`, `v4-32b-mid`) with
installers and corpus-building scripts (`ev-code`). Pre-training and mid-training code is
public. Post-training code for 4.1 is not confirmed.

<!-- item: license -->
## License terms & permitted use

Apache License 2.0 on all three 4.1 thinking models and their GGUF builds. It grants a
perpetual, worldwide, royalty-free copyright licence to reproduce, modify, sublicense and
distribute, plus a patent licence, with no field-of-use clause, no user-count threshold and no
gate. Commercial use is allowed (`ev-license`).

Read plainly:

- Source of the grant: The model repositories contain no `LICENSE` file; a request for
  `raw/main/LICENSE` returned HTTP 404. The grant rests on the card front matter
  (`license: apache-2.0`), the card's License section and section 2.4 of the technical report.
  Press coverage also reports Apache-2.0 for all three models (`ev-pcwatch`). Copy the
  Apache-2.0 text and a notice into your own redistribution.
- Contradiction between the card and the licence: The card says the models are "not
  intended for direct use in production services". Apache-2.0 contains no such limit and Section
  7 only disclaims warranty ("You are solely responsible for determining the appropriateness of
  using or redistributing the Work"). Treat the card text as the publisher's statement of
  intended purpose and risk, not as a licence term. The technical report separates the two: it
  says the absence of use restrictions "does not imply that the societal impacts of model use
  are unimportant" and lists responsibilities of users (`ev-license`).
- Upstream data terms: The training data carries its own licences (ODC-BY, CC BY-SA, per
  repository code licences, a custom NVIDIA agreement for one mid-training corpus). The weights
  themselves are licensed by NII under Apache-2.0; the publisher's policy is to use only data
  whose use for public model training is permitted (release levels L1 to L3, `ev-techreport`).
  OneHill has not assessed whether any upstream term would reach model users.

<!-- item: provenance -->
## Supply-chain & provenance

- Source: `huggingface.co/llm-jp`, linked from NII's release page. The Hugging Face
  organisation is not verified (`isVerified: false`), so the badge control is missing
  (`ev-hub-api`, `ev-release-page`).
- Format: Safetensors BF16 shards with LFS sha256 for every shard; no pickle or `.bin`
  files; official GGUF in BF16 and Q4_K_M with an imatrix (`ev-hub-api`, `ev-gguf`).
- Scan: The hub scan finished with no flagged files (`ev-hub-api`).
- Signing: None; no provenance attestation.
- Executable repository code: Loading the Python paths needs `trust_remote_code=True`, which
  runs `llmjp4_tokenizer.py` and `llmjp4_harmony.py` from the model repository. Read both and pin
  the revision before first use (`ev-cookbook`, `ev-hub-api`).
- Mirrors: The official GGUF repositories are from the same organisation. Third-party
  derivatives exist (ELYZA); they are different artefacts with their own provenance.

Checklist: about 4 of 8 boxes (safetensors, checksums, scan, no incident found).

<!-- item: eu-ai-act -->
## EU AI Act posture

GPAI model provider obligations apply to the publisher if it places the model on the EU market.
Estimated training compute for the 33B dense model is about 2.3e24 FLOPs (6 x 33.2B x 11.7T
tokens, OneHill estimate), well below the 1e25 systemic-risk threshold, so there is no Article 55
duty (`ev-card-41`).

- Open-source exemption: Apache-2.0 with public parameters, architecture and usage
  information, and no monetisation evident, so the Article 53 exemption from Annex XI and XII
  documentation plausibly applies.
- Copyright policy: partly documented. It has a five-level dataset release policy built on
  Japanese copyright law, a statement that data construction processes must also comply with
  law, and a document-removal contact on the corpus pages (`ev-techreport`, `ev-corpus-v41`).
  There is no stated policy for EU text-and-data-mining opt-outs.
- Training-content summary: partly documented. Every pre-training subcorpus is listed with
  licence and token count (`ev-corpus-v4`, `ev-techreport`). It is not in the AI Office
  template and it covers the 4.0 data design, not a 4.1-specific summary.
- Downstream information: Model cards, cookbook and technical report; the report excludes
  the 33B results and the 4.1 post-training.
- Code of Practice: no signature is listed; status unknown.

Deployer effect of the "not for production" wording: a deployer who ships LLM-jp-4.1 inside a
product cannot point to a provider statement that supports that use, and must document their own
intended-purpose, risk and evaluation work.

<!-- item: evaluation -->
## Benchmarks & evaluation

All results are the publisher's own. No independent re-run exists. The only other comparison is
ELYZA's self-reported evaluation of its own derivative, which is not independent.

Technical report, LLM-jp-4-32b-a3b-thinking (`ev-techreport`):

| Benchmark | LLM-jp-4-32b-a3b | Qwen3-8B | gpt-oss-20b |
|---|---|---|---|
| llm-jp-eval Japanese average | 0.605 | 0.608 | 0.604 |
| llm-jp-eval English average | 0.650 | 0.714 | 0.704 |
| GPQA Diamond (EN) | 0.520 | 0.560 | 0.670 |

Model cards, llm-jp-judge with gpt-5.4 as judge, reasoning effort medium (`ev-card-41`):

| Model | MT-Bench JA | MT-Bench EN | AnswerCarefully | llm-jp-instructions |
|---|---|---|---|---|
| llm-jp-4.1-33b-thinking | 7.76 | 7.98 | 4.08 | 3.83 |
| llm-jp-4.1-32b-a3b-thinking | 7.69 | 7.85 | 3.91 | 3.79 |
| llm-jp-4.1-8b-thinking | 7.58 | 7.67 | 3.92 | 3.67 |
| gpt-oss-20b | 7.33 | 7.85 | 3.55 | 3.16 |
| gpt-5.4 | 8.87 | 8.89 | 4.43 | 4.82 |

The 4.1 cards also evaluate on the swallow-evaluation-instruct suite (math, science, knowledge,
code, instruction following, translation) and on BFCL and tau2-bench for tool calling, shown as
charts. The blog says LLM-jp-4.1 beats Qwen3 on tau2-bench overall but remains far behind Qwen3.5
(`ev-blog`). The chart values are not available as text and are not used for scoring.

<!-- item: safety-eval -->
## Independent safety evaluation

No independent safety evaluation exists. The only safety result is the publisher's AnswerCarefully score (336 Japanese
questions from the v2.0 test set, judged by gpt-5.4), 4.08 of 5 for the 33B model against 4.43
for gpt-5.4 and 4.00 for gpt-4o (`ev-card-41`). The dataset is gated and its licence terms are
unverified (`ev-ac-dataset`). No jailbreak test, no English or multi-domain safety evaluation, no
CBRN or cyber evaluation and no companion guard model exist.

## What the "not for production" wording does to the scores

- Legal (3): The licence still permits commercial and production use, so the wording does
  not drag the licence below 3. It keeps legal from 4 because there is no provider-stated
  intended purpose for production and the EU-format documentation package is incomplete.
- Safety (2): The publisher itself tells users not to put the models into production, and
  the evidence behind the safety post-training is one self-run Japanese benchmark. That is
  anchor 2, "thin or publisher-only safety evaluation". The cards say safety post-training was
  done, so it is not scored lower.
- Ownership reliability (weak): The ownership rule marks reliability weak when safety is 2
  or below, "unsafe to deploy as presented". Here the publisher says the same about its own
  release.
- What would change it: An independent safety and jailbreak evaluation, a published guard
  model, or a publisher statement of intended purpose that covers production would each lift
  safety or legal by one point.

## Scoring summary

Headline 54.4, grade D, one point below the C boundary (55). Dimensions: openness 4,
provenance 2, legal 3, safety 2, performance 2, operational 3, governance 3. Openness is the
strongest dimension; safety and performance are held down by missing
independent evidence, not by a measured failure.

## Follow-up entities

- `llm-jp-4-thinking` (4.0): same Apache-2.0, safety statement "not tuned", no tool calling;
  33B, 32B-A3B and 8B, created 2026-03-16 to 2026-08-14.
- `llm-jp-4-base`: base models (8B, 32B-A3B, 33B), Apache-2.0, untuned.
- `llm-jp-4-vl-9b`: vision-language model (Apache-2.0 tag; a SigLIP 2 encoder is reported but
  unverified; card not assessed).
- `kaburi-tts`: Japanese dialogue speech model (Apache-2.0 tag; card not assessed).
- Third-party derivatives: ELYZA-Thinking-1.0 on LLM-jp-4 (card not assessed).
