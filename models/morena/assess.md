# Assess - MORENA 1.5B (base and instruct)

_Should we adopt this? Openness, licence, provenance, EU AI Act, safety, evaluation, and the
AOI score live here. Evidence ids refer to entry.yaml; every source is stored under
docs/primary-sources/morena/._

<!-- item: intended-use -->
## Intended & out-of-scope use

Adopt MORENA as a fine-tuning starting point for twelve African languages, not as a finished
assistant. The publisher says the same: the base card calls it "the recommended starting point
for fine-tuning, continued pretraining and domain adaptation", and the paper states that the
instruct model "is not an assistant" (`ev-card-base`, `ev-paper`). The instruct model is suited
to experiments with translation into African languages, short chat in the reserved-token format,
and tool-call formatting. It is out of scope for retrieval-augmented question answering, grounded
summarisation, or any use where a refusal on an ordinary request is costly, and for anything
safety-critical. The base checkpoint is not a chat model and has no safety evaluation.

<!-- item: limitations -->
## Known limitations, bias & failure modes

All of these come from the publisher's own card and paper (`ev-card-instruct`, `ev-paper`).

- **Over-refusal.** 41% of ordinary benign requests are not answered well, mostly by refusing.
  Benign answering is 58.9%, up from 47.9% in the previous version. An earlier version refused to
  recommend a dry cleaner.
- **Near-chance comprehension.** Retrieval QA accuracy is 0.325 against a 0.25 floor; Belebele is
  0.309 over ten African languages; African multiple choice is at chance, as it is for every
  model under 12B the paper measured. MMLU is 0.284.
- **Unfaithful grounding.** Fully faithful grounded paragraphs fell from 31% to 23% (22 of 96).
- **Degenerate output.** 1.3% degenerate in the safety set, and about one generation in six
  does not emit an end-of-sequence token within 200 tokens.
- **Uneven languages.** isiNdebele is evaluated on speech transcripts only. Safety is weakest in
  Igbo (75%), Yoruba (82%), Setswana (83%) and isiXhosa (87%). Table 2 of the paper shows no
  machine-translated pool for Yoruba, isiNdebele or Nigerian Pidgin; Yoruba is also the weakest
  language for translation into it (chrF++ 26.9).
- **Translation direction.** Into English it trails MADLAD-400-3B (48.7 against 53.6), and in 59
  of 1,000 into-English prompts the model echoed the instruction instead of translating.
- **Judge bias.** One model, gemma-3-12b-it, wrote the safety prompts, wrote much of the training
  data and judged the answers. No native speaker has rated an answer.

<!-- item: openness -->
## Openness tier & components

MORENA earns `open_weights` (ceiling 3 on the openness dimension). Weights, tokenizer and
documentation are open; the other components are partial.

| Component | Grade | Evidence |
|---|---|---|
| Weights | open | base and instruct safetensors, ungated (`ev-hf-platform`) |
| Training data | partial | sources and per-source shares named in the paper and card metadata; the corpus is "not released"; the paper promises corpus and datasheet "once the legal review is complete"; only the Fikira SFT component (50,000 rows, MIT) is public; `vamboai/morena-sft-corpus` is listed but returns HTTP 401 (`ev-paper`, `ev-fikira`) |
| Training code | partial | `modeling_morena.py` is a full production trainer (FSDP2, Muon, mixture sampler, checkpointing), but the configs, TRAIN_README.md and data pipeline are missing and the card does not mention the trainer (`ev-trainer`) |
| Evaluation | partial | results, methods and a defect log in the paper, no harness code (`ev-paper`) |
| Documentation | open | detailed cards and a 23-page paper with limitations (`ev-card-instruct`, `ev-paper`) |
| Licence | open | Apache-2.0 declared (`ev-licence`) |

An earlier research lead said no training code was found. That is wrong in part: the trainer
file ships in the repo, so the tier turns on the missing configs and data, not on missing code.
It stays below `open_weights_recipe` because the framework asks for runnable training code and
released evaluation code, and neither is present.

<!-- item: license -->
## Licence terms & permitted use

The declared licence is Apache-2.0 for base, instruct, GGUF, mini, mini-instruct and nano
(`ev-licence`, `ev-siblings`). The card adds: "Commercial use is permitted, including
fine-tuning and redistributing derivatives, under the terms of the licence." The repos are not
gated. Three caveats apply.

1. **No licence file.** No LICENSE, NOTICE or copyright-holder file exists in any repo read
   (raw LICENSE returns 404). The licence rests on Hugging Face metadata and one card paragraph.
   Apache-2.0 section 4 expects recipients to receive a copy of the licence, so a redistributor
   must add the text themselves (`ev-apache-text`).
2. **Late declaration.** A commit on 2026-09-17 removed the licence wording and one on
   2026-09-18 restored it as "Licence: Apache 2.0, commercial use permitted". The final state is
   consistent across all repos read.
3. **Upstream terms, unresolved.** The paper says the SFT corpus is "mostly synthetic" and was
   generated by "Gemma-family and GPT-OSS-120b models". The Gemma Terms of Use define a Model
   Derivative to include a model trained on synthetic Outputs of Gemma to perform similarly to
   Gemma, and require the Gemma use restrictions to pass on to recipients (`ev-gemma-terms`).
   Vambo does not say which Gemma versions it used or address the clause. This is an open
   question, not a finding that the Apache-2.0 declaration is invalid. The base model's
   pretraining mixture also includes machine-translated text from an unnamed system and 1.1B
   tokens of synthetic passages from an unnamed generator; the terms of those tools are
   unknown. The gpt-oss-120b terms were not read.

<!-- item: provenance -->
## Supply-chain & provenance

The canonical source is `huggingface.co/vamboai`, which Hugging Face reports as not verified,
with one member (`ev-hf-platform`). Weights are safetensors only, there is no pickle file, a
publisher-written `SHA256SUMS` exists and its `model.safetensors` value equals the host's LFS
hash, and Hugging Face's scan flagged no files (`ev-checksums`). That is about 4 of 8 checklist
boxes; the gaps are an unverified organisation, no signature, no build attestation and a custom
loader. The score is 2 because the verified-organisation test for anchor 3 is not met.

**"Trained from scratch" is a publisher claim.** It appears in the instruct card ("a 1.5B-parameter
decoder trained from scratch"), the base card, the paper's title block and abstract ("trained from
scratch, with its own tokenizer and data mixture") and the Vambo research page (`ev-card-instruct`,
`ev-paper`). No document names a base model or initialisation checkpoint, `config.json` and the
trainer carry a plain random-initialisation setting (`init_std 0.02`), and the paper reports 60,000
pretraining steps on 251.7B tokens. OneHill has not verified it, and the claim covers the 1.5B
weights only: the 0.5B and 0.2B models are pruned and distilled from the 1.5B base, and the
post-training data is synthetic output of other models. "From scratch" here means weight
initialisation, not independence from other models' outputs.

Loading the weights means running `modeling_morena.py` from the repo. It is a 52 KB trainer file;
an outline read found no subprocess, socket or HTTP use, but it was not audited line by line.
`load_example.py` still describes the weights as "preview weights" although the card's pre-release
wording was removed on 2026-09-18.

<!-- item: eu-ai-act -->
## EU AI Act posture

MORENA is a general-purpose AI model, and by the paper's own figure (6 x parameters x tokens)
training took about 2.8e21 FLOPs, far under the 1e25 systemic-risk threshold, so no Article 55
duties apply (`ev-paper`). Whether the Article 53 open-source exemption applies is uncertain:
Apache-2.0 would normally qualify and the parameters and architecture are public, but no licence
text ships, the monetisation context is not documented, and the Gemma Terms question could attach
use restrictions to the instruct model. The exemption never covers the two duties that remain:
a copyright policy (none found) and a public training-content summary. The paper's Table 2 gives
sources and shares, but it is not in the AI Office template, and it omits the machine-translation
system and the synthetic-data generators. No code-of-practice signatory status appears in any
document read. A fine-tuner who places a derivative on the EU market may become a provider for it.
This is guidance, not legal advice.

<!-- item: evaluation -->
## Benchmarks & evaluation

Every figure below is the publisher's own, from a harness it has not released and that its paper
says had five defects (`ev-card-instruct`, `ev-card-base`, `ev-paper`). No independent re-run was
found, and the press repeats the publisher numbers and says they are unverified (`ev-press`).

| Measure | Result | Reference points in the paper |
|---|---|---|
| African bits per byte, mean of 12 (base) | 1.408, lowest of 26 models | Lugha-Llama-8B 1.423, gemma-3-12b-it 2.159 |
| Same, instruct | 1.441 | second to Lugha-Llama-8B on the 12-language mean |
| FLORES+ chrF++, English into 5 languages, 3-shot (instruct) | 45.8 (45.1 to 46.5) | MADLAD-400-3B 37.8, Lugha-Llama-8B 36.8 |
| Same, 5 languages into English | 48.7 (47.5 to 49.7) | MADLAD-400-3B 53.6, Lugha-Llama-8B 52.4 |
| ARC-easy / ARC-challenge (base, English) | 0.676 / 0.412 | Qwen2.5-1.5B 0.668 / 0.440 |
| MMLU (base) | 0.284 | Qwen2.5-1.5B 0.324 |
| Belebele, ten African languages (instruct) | 0.309 | chance 0.25 |
| Tool calling, marker prefilled | 98.1% correct, 100% valid JSON | marker is prefilled; unprompted it almost never calls a tool |

The paper compares outside models under a plain few-shot prompt without a chat template, which
it says may understate instruction-tuned baselines. The coverage note: translation was scored on
five of the twelve languages only (Swahili, Hausa, Yoruba, isiXhosa, isiZulu), 200 sentences per
direction. The press claim that MORENA beats "a Google model eight times its size" names no model; it most
likely refers to gemma-3-12b-it (12.19B against 1.485B parameters) on bits per byte, which is a
language-modelling measure and not a task benchmark. That match is OneHill's inference, not a
statement by the publisher or the press.

<!-- safety-eval is a `gap` item in entry.yaml - see its gap_reason. The publisher's own
     safety numbers are in the limitations and evaluation sections above. -->

## Score summary

Rubric 1.1, computed by scripts/score.py from the dimension scores in entry.yaml: openness 3,
provenance 2, legal 3, safety 2, performance 2, operational 2, governance 2. The reasons are in
each dimension rationale in entry.yaml.

## Ownership verdict

Level: partial. Use and modify is strong and data control is strong, transparency is moderate,
and reliability is weak because operational readiness and safety are both rated 2. See the
`ownership` block in entry.yaml for the verdict text and the conditions that would raise it.

## Contradictions and surprises

- **Marketing against binding text.** Press coverage calls the model "open-source" (Daba Finance)
  and says licence, data and compute were not public (Tech In Africa). The cards and paper show
  an Apache-2.0 declaration and named data and compute, so the second claim is wrong; the corpus
  and most training code are not released, so "open-weight" is the accurate term.
- **Trainer in the repo.** The card describes `modeling_morena.py` as a "reference implementation"
  while the file calls itself the "production trainer".
- **Paper inconsistency.** Page 15 says the machine-translated pool does not exist for isiNdebele
  and Nigerian Pidgin, but Table 2 shows nine machine-translated pools and none for Yoruba.
- **Unverified organisation.** The Hugging Face org is not verified and the company site states
  no country, so South Africa rests on three press reports.
