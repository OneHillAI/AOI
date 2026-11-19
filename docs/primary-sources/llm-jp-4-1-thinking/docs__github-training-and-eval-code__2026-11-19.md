# docs / github-training-and-eval-code

source_url: https://github.com/llm-jp/scripts ; https://github.com/llm-jp ; https://api.github.com/orgs/llm-jp/repos
retrieval_date: 2026-11-19
exists: yes
retrieved: true

Verbatim extracts (publisher text, not edited). Notes by OneHill are marked NOTE.

NOTE (OneHill): read through the GitHub REST API (unauthenticated) and raw.githubusercontent.com on 2026-11-19. Nothing was cloned or run.

## github.com/llm-jp repositories relevant to the release (GitHub API, org listing of 84 repos, name | SPDX licence field | last push | description)
```
llm-jp-eval-inference | Apache-2.0 | pushed 2026-11-18 | 
llm-jp-eval | Apache-2.0 | pushed 2026-11-18 | 
llm-jp-judge | Apache-2.0 | pushed 2026-11-18 | Python tool for automated evaluation of generation
llm-jp-4-vl | Apache-2.0 | pushed 2026-11-12 | LLM-jp-4-VL is a series of vision-language models developed by LLM-jp.
llm-jp-vllm | None | pushed 2026-11-05 | vLLM extensions for LLM-jp models
scripts | Apache-2.0 | pushed 2026-10-28 | 
llm-jp-tokenizer | Apache-2.0 | pushed 2026-10-27 | 
sglang | Apache-2.0 | pushed 2026-10-16 | SGLang is a high-performance serving framework for large language mode
llm-jp-4-cookbook | Apache-2.0 | pushed 2026-10-07 | Example scripts for LLM-jp-4 models
ollama | MIT | pushed 2026-10-07 | Get up and running with Kimi, GLM, MiniMax, DeepSeek, gpt-oss, Qwen, G
llama.cpp | MIT | pushed 2026-10-01 | LLM inference in C/C++
kaburi-tts | Apache-2.0 | pushed 2026-09-09 | A spoken dialogue synthesis system that generates two-speaker Japanese
Megatron-LM | NOASSERTION | pushed 2026-08-02 | 
swallow-evaluation-instruct | NOASSERTION | pushed 2026-05-08 | Swallowプロジェクト 事後学習済み大規模言語モデル 評価フレームワーク
vllm | Apache-2.0 | pushed 2026-03-23 | A high-throughput and memory-efficient inference and serving engine fo
nemo-rl | Apache-2.0 | pushed 2025-11-03 | Scalable toolkit for efficient model reinforcement
llm-jp-sft | Apache-2.0 | pushed 2024-06-13 | 
llm-jp-dpo | Apache-2.0 | pushed 2024-02-06 | 
```

## llm-jp/scripts (Apache-2.0): LLM-jp-4 pre-training and mid-training configuration present in the tree (git tree API, 738 paths, truncated=false)
Pre-training script directories:
```
pretrain/scripts/v4-291b-a27b-phase1
pretrain/scripts/v4-2b-phase1
pretrain/scripts/v4-2b-phase2
pretrain/scripts/v4-32b-a3.8b-mid
pretrain/scripts/v4-32b-a3.8b-phase1
pretrain/scripts/v4-32b-a3.8b-phase2
pretrain/scripts/v4-32b-mid
pretrain/scripts/v4-32b-phase1
pretrain/scripts/v4-32b-phase2
pretrain/scripts/v4-332b-a31b-phase1
pretrain/scripts/v4-8b-mid
pretrain/scripts/v4-8b-phase1
pretrain/scripts/v4-8b-phase2
pretrain/scripts/v4-corpus-ratio-abci
pretrain/scripts/v4-high-quality-abci
pretrain/scripts/v4-midtraining
pretrain/scripts/v4-moe-ablation
pretrain/scripts/v4-preprocess
pretrain/scripts/v4-training
pretrain/scripts/v4-upstream-megatron-config-validation
pretrain/scripts/v4-upstream-training-template
```
Installer directories:
```
pretrain/installers/v4-megatron-abci
pretrain/installers/v4-megatron-sakura
pretrain/installers/v4-moe-upstream-megatron-abci
pretrain/installers/v4-upstream-megatron-abci
pretrain/installers/v4-upstream-megatron-b200
```
Corpus-building scripts: `corpus/llm-jp-corpus-v4` (dedup, en, ja, stats). Checkpoint conversion: `ckpt_converter/`. No directory under llm-jp/scripts is named for SFT, DPO or post-training (search of all 738 paths for "sft", "dpo", "post", "align" found only a dedup postprocess script).

## Example: pretrain/scripts/v4-32b-phase1/base/params.sh (the 33B dense model: hidden 5120, FFN 27648, 40 heads, matching the model card) key lines
```
    --hidden-size 5120
    --ffn-hidden-size 27648
    --num-attention-heads 40
    --seq-length 4096
    --train-iters 12000000
    --micro-batch-size 2
    --global-batch-size 512
```
The technical report states: "The complete training configurations are publicly available for the dense model [v4-8b-phase1] and the MoE model [v4-32b-a3.8b-phase1]".

## Post-training code
The publisher release page (https://llm-jp.nii.ac.jp/en/release-en/) lists under Tools: "[Fine-tuning Script] trl-based SFT", "[Fine-tuning Script] trl-based DPO" and "[Fine-tuning Script] Nemo-Aligner based *Supports both SFT and DPO", linking github.com/llm-jp/llm-jp-sft and github.com/llm-jp/llm-jp-dpo (last pushed 2024-06 and 2024-02 per the org listing) and an NVIDIA NeMo-RL fork. The tree of llm-jp-sft holds `train.py`, `configs`, `converter`, `data`; llm-jp-dpo holds `train.py`, `accelerate_configs`. NOTE: OneHill found no document stating that these scripts are the exact SFT/DPO recipe used for llm-jp-4.1-*-thinking (a Harmony-format reasoning model with tool calling). Treat post-training code as UNVERIFIED for 4.1.
