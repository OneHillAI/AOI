doc_type: docs
entity: luciole
variant/applies-to: github.com/OpenLLM-France/Luciole-Training (training, data, conversion and evaluation code)
source_url: https://github.com/OpenLLM-France/Luciole-Training (README.md, SECURITY.md, evaluation/README.md, data/synthetic_generation/README.md, tree/main, tree/main/finetune, tree/main/finetune/model_cards)
retrieval_date: 2026-11-19
exists: yes
retrieved: true

## Repository facts (GitHub page, 2026-11-19)

532 commits, 17 stars, 4 watchers, 1 fork; licence GPL-3.0; top-level directories include data, pretrain, finetune, evaluation, tokenizer_train. finetune/ holds model_cards, nemo, nemo-rl and an image; finetune/model_cards has one folder each for 1B-Instruct-1.1, 1B-Thinking-1.1, 23B-Instruct-1.1, 23B-Thinking-1.1, 8B-Instruct-1.1, 8B-Thinking-1.1 and 8B-KD-Math-Thinking-1.1. (The raw finetune/README.md returned HTTP 404, so the fine-tuning recipe files were not opened line by line; only their existence was confirmed.) The GitHub REST API was rate limited, so the page HTML was used.

## README (verbatim extracts)

"Training pipeline for the Luciole series of multilingual (French-English) large language models, part of the OpenLLM-France initiative. This repository covers the full LLM lifecycle: data preparation, tokenizer training, pretraining, fine-tuning, and evaluation. It is designed to run on the Jean-Zay HPC cluster (NVIDIA H100 GPUs) via SLURM."
Directory table: "data/processing/ 50+ dataset-specific preprocessing scripts (FineWeb, DCLM, Gallica, StarCoder, ...)"; "data/synthetic_generation/ Generate synthetic training data using LLMs"; "tokenizer_train/ Train and evaluate custom BPE tokenizers"; "pretrain/train/ Distributed pretraining via NeMo + SLURM"; "pretrain/conversion/ Convert NeMo checkpoints to HuggingFace format"; "finetune/ SFT and RL fine-tuning with NeMo"; "evaluation/ Benchmark evaluation with lighteval".
Pretrain launch example: "python slurm_launcher.py --output_dir ... --arch nemotron1b --mode phase1 --datamix datamixes/luciole_phase1.json". Supported recipes include "Nemotron 1B, 4B, 8B, 22B, 23B + variants" and "NemotronH 8B, 47B".
Environment notes: pretraining needs "NeMo module on Jean-Zay"; fine-tuning "NeMo-RL with uv"; evaluation uses OpenLLM-France forks of lighteval and datatrove.

## SECURITY.md (verbatim extract)

"If you believe you have found a security vulnerability in this repository (the Luciole data processing, tokenizer, training, conversion or evaluation code), please report it privately rather than opening a public issue. Contact: contact@openllm-france.fr ... We will acknowledge your report as soon as we can ... Please allow a reasonable time for the issue to be addressed before any public disclosure. This policy covers the source code in this repository. The released Luciole models and datasets are distributed on the Hugging Face Hub under the OpenLLM-France organization; issues specific to a published model or dataset can also be raised there." (No response-time commitment; the address was not used.)

## evaluation/README.md

Evaluation scripts and task lists (en, fr, multilingual, mmlu, gsm8k, ruler) run with the OpenLLM-France lighteval fork; no safety or red-team task list is listed.

## data/synthetic_generation/README.md

A distilabel-based pipeline that annotates FineWeb pages (educational score, toxicity, ads, topic) with an LLM (user-chosen, "--disable_thinking ... for qwen model") and trains fastText classifiers. It does not name the teacher model used for the released data.

## What it establishes

Data-processing, tokenizer, pretraining, fine-tuning and evaluation code are public in one repository under GPL-3.0, with a security-reporting address for the code. Reproduction needs the Jean Zay cluster, NeMo and NeMo-RL environments, and the datamix files; none of that was run here.
