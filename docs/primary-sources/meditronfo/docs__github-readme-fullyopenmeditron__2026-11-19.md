# docs / github-readme-fullyopenmeditron

source_url: https://raw.githubusercontent.com/EPFLiGHT/FullyOpenMeditron/main/README.md
retrieval_date: 2026-11-19
retrieved_by: curl, text read in full or in the extracts marked below
note: Extracts: introduction, Layout, Data, Checked on 2026-09-26, Known gaps. The README is the repository owner's own statement of what is and is not released.

Verbatim extracts follow. Nothing below is paraphrased unless it is under a heading that says OneHill note.

```
# MeditronFO: code and results for *Fully Open Meditron*

This repository holds what is needed to reproduce the paper
[*Fully Open Meditron: An Auditable Pipeline for Clinical LLMs*](https://arxiv.org/abs/2605.16215): the data pipeline that builds
the training corpus, the training configs, the evaluations, and the scripts that turn the saved per-item
outputs of every reported run into the paper's figures and tables, together with those scripts' outputs
(every number in the paper can be checked against them).

Project page: [meditron.light-laboratory.org/meditronfo](https://meditron.light-laboratory.org/meditronfo/) (the models, the results and the paper). Chat with Apertus-70B-MeditronFO: [meditron.light-laboratory.org/#chat](https://meditron.light-laboratory.org/#chat).

The training corpus is on Hugging Face as
[`EPFLiGHT/fully-open-meditron`](https://huggingface.co/datasets/EPFLiGHT/fully-open-meditron), and the model
weights are in the [MeditronFO collection](https://huggingface.co/collections/EPFLiGHT/meditronfo). The
intermediate files and per-item evaluation outputs (tens of GB) are not released yet; [Data](#data) lists
what goes where.

Clone with the evaluation harness submodule: `git clone --recursive https://github.com/EPFLiGHT/FullyOpenMeditron.git`.


[...]
## Layout

| Path | What |
|---|---|
| `papers/sept_25th_iclr_paper/figures/` | the paper's figures, where the figure scripts write them |
| `data_gen/` | question generation (Synthetic Curated QA, Guidelines QA, synthetic vignettes) and the first distillation of Curated QA |
| `truncation/` | regeneration of answers that hit the token cap (`regenerate_truncated.py`) |
| `decontamination/` | MedExpQA drop, two-stage n-gram decontamination, `decontam_table.py` (appendix table) |
| `resampling/` | the eval-free MOOVE seed pool, pass@8 rejection-sampling distillation of every answer, corpus registry |
| `data/corpora.yaml` | registry of the corpora with row counts and sha256; the paper's corpus is `meditronfo_gptoss_v1`, the second teacher's `meditronfo_qwen38_v3` |
| `axolotl_config/teacher_ablation/` | the training config of every reported model, and `launch.sh`, which trains and evaluates them |
| `meditron_train.sh`, `meditron_eval.sh`, `new_launch.sh` | Slurm launchers: Axolotl training, the lm-eval medbench suite, any Python script in the vLLM container |
| `lm-evaluation-harness/` | submodule: [our fork of the harness](https://github.com/Xkrilandar/lm-evaluation-harness) at the commit the evaluations ran with (task group `medbench`: MedMCQA, MedQA, PubMedQA, MedXpertQA, MMLU-Pro, IFEval, ARC) |
| `healthbench/` | HealthBench answering and grading (`healthbench.py`), Figure 1 (`plot_healthbench_figures.py`) |
| `auto_moove/` | AutoMOOVE: pairwise judging (`auto_moove.py`), judge validation against clinicians (`auto_moove_check.py`), tables |
| `scripts/build_unanimous_eval_set.py` | builds the unanimous-576 AutoMOOVE test set from the clinicians' reviews |
| `corpus_audit/` | clinician audit data, LLM screen of the corpus, label-mismatch table |
| `tech_reports/figures/` | the scripts that compute every interval and draw the figures, and their JSON/TeX outputs |
| `container/` | the container specs (EDF) the jobs run in |

## Data

The corpus is released as [`EPFLiGHT/fully-open-meditron`](https://huggingface.co/datasets/EPFLiGHT/fully-open-meditron)
(Parquet, OpenAI `messages` format); the rest is not released yet. The MOOVE vignettes (`data/moove/`,
`moove/all_reviews.jsonl`, and the MOOVE sets that `decontamination/build_eval_benchmarks.py` writes) are
evaluation material and are not public. The scripts expect the data at these paths:

| Path | Content |
|---|---|
| `data/corpora/meditronfo_gptoss_v1/`, `data/corpora/meditronfo_qwen38_v3/` | the training corpora, one JSONL per training set (rows and sha256 in `data/corpora.yaml`; `python3 resampling/corpora.py check`) |
| `data/curated_qa/`, `data/guidelines/`, `data/moove/full_moove.jsonl` | pipeline inputs: the public QA sets, the public clinical guidelines corpus, the MOOVE vignette pool |
| `data/synthetic_qa/`, `data/guidelines_qa/`, `data/fixed/`, `data/decontaminated/`, `data/decontam_moove_v4/` | each pipeline stage's output for the paper corpus, with the decontamination reports |
| `data/resampling/` | rejected rows and reports of the pass@8 distillation (read by `label_mismatch.py`) |
| `data/moove/moove_eval_unanimous_576.jsonl`, `moove/all_reviews.jsonl` | the AutoMOOVE test set (576 pairs, 516 vignettes) and the clinicians' reviews it is built from |
| `data/healthbench/` | HealthBench full and hard, and OpenAI's hard and consensus subsets (`openai_subsets/`) |
| `eval_results/` | lm-eval per-sample outputs of the 25 medbench runs listed in `RUN` in `tech_reports/figures/iclr_clean_ci.py` |
| `healthbench/results/` | HealthBench answers and per-conversation grades (labels in `HBNAME` in the same file) |
| `auto_moove/results/unanimous576/` | AutoMOOVE per-question judgements |
| `auto_moove/judge_outputs/` | judge-validation runs on the 576 clinician pairs |
| `truncation/results/train/truncated.jsonl` | answers flagged as truncated (input of `regenerate_truncated.py`) |

Model weights: MeditronFO checkpoints are written to `$SCRATCH/meditronfo/models/<config>`; the released
weights are in the [MeditronFO collection](https://huggingface.co/collections/EPFLiGHT/meditronfo).


[...]
## Checked on 2026-09-26

Section 1 was rerun from this folder, with the data in place, on a fresh Python 3.12 environment
(`requirements-local.txt`):

- all 16 generated figures of the paper regenerate pixel-identical;
- `iclr_clean_ci.json`, `iclr_pref.json`, `healthbench_breakdown.json` and `gptoss_official_compare.json`
  match the paper's values (differences below 1e-3, i.e. floating-point noise);
- `decontam_table.py`, `audit_categories.py` and `label_mismatch.py` reproduce the
  saved tables exactly;
- `build_unanimous_eval_set.py` rebuilds the AutoMOOVE test set byte for byte from the clinicians' reviews.

## Known gaps

- **Figure 2** is a drawing, not generated.
- **Table cells are typed** into the paper from the JSON and text outputs above, not generated.
- **Intermediate data, per-item evaluation outputs and container images** are not part of this repository
  (see [Data](#data) and [Setup](#setup)), so section 1 cannot be rerun from a fresh clone yet.
- vLLM's continuous batching makes regenerated answers differ slightly from run to run even with a fixed
  seed, so a rerun from scratch reproduces the numbers within their intervals, not to the digit.

```
