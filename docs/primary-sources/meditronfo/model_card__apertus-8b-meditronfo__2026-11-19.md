# model_card / apertus-8b-meditronfo

source_url: https://huggingface.co/EPFLiGHT/Apertus-8B-MeditronFO/raw/main/README.md
retrieval_date: 2026-11-19
retrieved_by: curl, text read in full or in the extracts marked below
note: Extracts: front matter, headline bullets, benchmark table, training and limitations sections. Revision c0f8a017b6abaed4335e68a5f6c5e0096c17115f.

Verbatim extracts follow. Nothing below is paraphrased unless it is under a heading that says OneHill note.

```
---
license: apache-2.0
language:
- en
library_name: transformers
pipeline_tag: text-generation
tags:
- medical
- clinical
- healthcare
- meditron
- fully-open
- medical-llm
base_model: swiss-ai/Apertus-8B-Instruct-2509
base_model_relation: finetune
datasets:
- EPFLiGHT/fully-open-meditron
---


[...]
- **Part of the Fully Open Meditron family:** End to end fully open clinical LLMs
- **Best medical accuracy among small fully open medical LLMs:** 48.26% on the five-benchmark average, against 42.39% for Apertus-8B-Instruct
- **Preferred over Apertus-8B-Instruct in 74.2% of comparisons** on AutoMOOVE, the clinician-validated LLM-judge evaluation (three-judge majority, 516 clinician-written vignettes)
- **Largest HealthBench gain in the MeditronFO family:** +16.1 points over its base (26.0 → 42.1)


[...]
## Benchmark

Accuracy (%) on four multiple-choice medical benchmarks (greedy decoding) and score (%) on HealthBench (all 5,000 conversations, Gemma-4-31B grader). See the paper for the full evaluation details, confidence intervals and the AutoMOOVE results.

| Benchmark | Apertus-8B-Instruct | **Apertus-8B-MeditronFO** | Δ |
|---|---:|---:|---:|
| MedMCQA | 47.8 | **52.0** | +4.2 |
| MedQA | 52.1 | **60.7** | +8.6 |
| PubMedQA | 74.3 | **71.4** | −2.9 |
| MedXpertQA | 11.8 | **15.1** | +3.3 |
| HealthBench | 26.0 | **42.1** | +16.1 |
| **Average (5)** | 42.39 | **48.26** | +5.87 |


[...]
## Training

- **Base model:** [Apertus-8B-Instruct](https://huggingface.co/swiss-ai/Apertus-8B-Instruct-2509)
- **Corpus:** [Fully Open Meditron](https://huggingface.co/datasets/EPFLiGHT/fully-open-meditron), 533,888 examples: Curated QA (195.5k, seven public medical QA datasets), Synthetic Curated QA (184.5k), Guidelines QA (129.8k, generated from 14,192 clinical practice guidelines) and Synthetic vignettes (24.0k, modelled on clinician-written MOOVE vignettes). Every answer is written by gpt-oss-120b with rejection sampling (pass@8; multiple-choice answers must match the gold label), with generation prompts co-authored by four clinicians
- **Decontamination:** two-stage n-gram decontamination against all evaluation benchmarks and the AutoMOOVE test set (4,197 rows removed)
- **Recipe:** 1 epoch, learning rate 1e-5 with cosine decay and 10% warmup, effective batch 64 sequences of 8,192 packed tokens, AdamW, seed 42
- **Framework:** Axolotl with DeepSpeed ZeRO-3, bf16

Full hyperparameters are in the training appendix of the paper.

## Compute & footprint
The training was done on 2 nodes of 4 NVIDIA GH200 GPUs for 51 min (7 GPU-hours) on the Alps supercomputer of the CSCS Swiss National Supercomputing Centre. 
Our trainings have a carbon neutral footprint as the CSCS data center is carbon neutral ([CSCS energy efficiency](https://ethz.ch/en/news-and-events/eth-news/news/2022/11/at-cscs-energy-efficiency-is-a-key-priority-even-at-high-performance.html)).

## Limitations & intended use

MeditronFO can produce text on a variety of topics, but the generated content may not always be factually accurate, logically consistent, or free from biases present in the training data. MeditronFO has been trained to be specialised for Medicine and is intended to be used for Medicine related tasks evaluation. These models should be used as assistive tools rather than definitive sources of information. Users should always verify important information and critically evaluate any generated content.


```
