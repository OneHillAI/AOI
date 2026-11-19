# model_card / sarvam-105b-1711 (NVFP4/MXFP8) and sarvam-105b-1711-bf16

source_url: https://huggingface.co/sarvamai/sarvam-105b-1711 ; https://huggingface.co/sarvamai/sarvam-105b-1711-bf16 (raw README.md)
retrieval_date: 2026-11-19
exists: yes
retrieved: true

Verbatim extracts (publisher text, not edited). Notes by OneHill are marked NOTE.

## NVFP4 repo front matter
```
---
library_name: transformers
license: apache-2.0
pipeline_tag: text-generation
base_model:
- sarvamai/sarvam-105b-1711-bf16
tags:
- nvfp4
- mxfp8
---
```
## BF16 repo front matter
```
---
library_name: transformers
license: apache-2.0
pipeline_tag: text-generation
base_model:
- sarvamai/sarvam-105b
base_model_relation: finetune
---
```

## Introduction and benchmarks (NVFP4 card; the BF16 card has the same table)
```
# Sarvam-105B-1711 (NVFP4)

Sarvam-105B-1711 uses the same base model as [Sarvam-105B](https://huggingface.co/sarvamai/sarvam-105b), a 105B-parameter mixture-of-experts model with 10.3B active parameters, and is further post-trained to improve:

+ **Tool calling**
+ **Instruction following**
+ **Agentic tasks**
+ **Indian languages**

This repo has the NVFP4 build; the BF16 weights are at [`sarvamai/sarvam-105b-1711-bf16`](https://huggingface.co/sarvamai/sarvam-105b-1711-bf16).

## Benchmarks

| Benchmark | Sarvam-105B-1711<br>(BF16) | Sarvam-105B-1711<br>(NVFP4) | Gemma-4-31B | Nemotron-Super-120B | Mistral-Small-4 | GPT-5.6 Luna | Claude Haiku 4.5 | Gemini 3.5 Flash-Lite |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Instruction following** | | | | | | | | |
| IFEval | **96.5** | 96.4 | 94.7 | 90.8 | 82.3 | 93.1 | 86.1 | 95.6 |
| IFBench | **82.5** | 81.8 | 77.8 | 70.9 | 41.0 | 64.1 | 45.5 | 73.5 |
| MultiChallenge | 62.2 | 62.5 | 63.6 | 50.8 | 30.6 | 61.6 | 49.8 | **64.8** |
| **Chat** | | | | | | | | |
| Arena-Hard v2 | 76.6 | 75.3 | 75.0 | 73.5 | 54.6 | **79.8** | 60.9 | 77.2 |
| WritingBench | 86.5 | 86.6 | 79.2 | **87.3** | 85.5 | 84.4 | 83.2 | 80.7 |
| **Tool calling** | | | | | | | | |
| τ²-Bench | **85.5** | 84.1 | 81.1 | 77.5 | 55.3 | 79.5 | 62.1 | 83.1 |
| BFCL v4 | 62.4 | 62.7 | **68.8** | 55.4 | 55.0 | 67.7 | 68.6 | 67.8 |
| **Agentic** | | | | | | | | |
| GDPval-S | 66.9 | 65.2 | 61.1 | 56.8 | 49.2 | – | 66.2 | **73.0** |
| **Indic** | | | | | | | | |
| Indic Suite | 79.1 | 78.8 | 78.6 | 39.5 | 44.3 | **82.4** | 61.3 | 79.7 |
| **Knowledge** | | | | | | | | |
| MMLU-Pro | 85.2 | 85.0 | **88.1** | 85.1 | 80.6 | **88.1** | 83.0 | **88.1** |
| GPQA Diamond | 80.4 | 78.2 | 84.3 | 78.9 | 71.0 | **88.7** | 67.9 | 85.2 |
| Humanity's Last Exam | 12.3 | 11.4 | 22.1 | 17.3 | 9.6 | **35.8** | 10.1 | 17.9 |
| **Search** | | | | | | | | |
| BrowseComp | 41.4 | 35.0 | 33.2 | 27.9 | 14.5 | **76.3** | 18.4 | 42.9 |
| **Math** | | | | | | | | |
| AIME 2025 | 87.9 | 86.0 | 85.2 | 85.5 | 81.5 | **99.2** | 83.9 | 73.5 |
| AIME 2026 | 89.7 | 88.0 | 89.0 | 87.6 | 87.1 | **97.2** | 86.3 | 83.2 |
| HMMT Feb 2025 | 78.0 | 77.0 | 88.8 | 85.7 | 73.8 | **99.5** | 74.4 | 73.0 |
| HMMT Nov 2025 | 81.5 | 79.7 | 88.0 | 84.1 | 81.4 | **99.1** | 82.6 | 78.4 |
| HMMT Feb 2026 | 71.8 | 70.1 | 77.3 | 76.4 | 74.4 | **93.0** | 67.5 | 64.8 |
| **Coding** | | | | | | | | |
| LiveCodeBench v6 | 75.3 | 74.7 | 81.9 | 75.5 | 68.4 | **85.0** | 57.0 | 73.9 |

All scores are from our own runs; see [Benchmark details](#benchmark-details).


```

## Benchmark details
```
## Benchmark details

- **Setup**: all models were evaluated by us with the same harness and settings. Open-weight models were served with vLLM (context window 131,072 tokens for Sarvam-105B-1711, 262,144 for Gemma-4-31B, Nemotron-Super-120B and Mistral-Small-4); API models were called through OpenRouter at the provider's maximum context, with reasoning effort `max` for GPT-5.6 Luna and Claude Haiku 4.5 and `high` for Gemini 3.5 Flash-Lite. All scores are in thinking mode.
- **Defaults**: `temperature=1.0`, up to 65,536 output tokens, mean over 4 samples, official graders. Agentic benchmarks (τ²-Bench, BFCL v4, GDPval-S, BrowseComp) have no total output cap and 16,384 output tokens per step unless noted. Responses that run out of token budget, overflow the context or are malformed (for example unclosed thinking) score 0; infrastructure errors are retried.
- **IFEval**: prompt-level strict accuracy with the official checker (official setting: greedy decoding).
- **IFBench**: prompt-level strict accuracy with the official checker, mean over 8 samples (the official setting reports loose accuracy at temperature 0).
- **MultiChallenge**: pass rate, final turn judged by Gemini 2.5 Pro.
- **Arena-Hard v2**: win rate against o3-mini-2025-01-31, judged by GPT-4.1 with 5 verdicts and swapped positions, no style control, 100 bootstrap rounds.
- **WritingBench**: English prompts, mean criterion score (1–10, scaled ×10) from WritingBench-Critic-Qwen-7B; responses that overflow the critic's 32,768-token context score 0.
- **τ²-Bench**: mean reward over the airline, retail and telecom domains with GPT-5.2 (low) as the user simulator, up to 200 steps and 16,384 output tokens per step.
- **BFCL v4**: overall accuracy with the official grader, up to 20 steps per user turn and 65,536 output tokens per step; 3 `live_multiple` samples are excluded because the provider blocked their content.
- **GDPval-S**: Sarvam's version of GDPval: 209 tasks from [openai/gdpval](https://huggingface.co/datasets/openai/gdpval) run in our cowork harness with sandboxed tools and proxied internet access, up to 200 turns and 1 hour per task, context compaction at 55% of the window. The deliverable files are scored against each task's rubric by GPT-6 Luna; we report the mean rubric score (0–100).
- **Indic Suite**: Sarvam's internal suite of Indian-language tasks, mean rubric score judged by Gemini 3.1 Pro.
- **MMLU-Pro**: exact match on the choice letter.
- **GPQA Diamond**: exact match on the answer tag, mean over 8 samples.
- **Humanity's Last Exam**: accuracy without tools, judged by GPT-4.1 (official judge: o3-mini).
- **BrowseComp**: search agent with up to 101 steps, 8,192 output tokens per step and 122,880 input tokens, judged by GPT-4.1 on the extracted answer; runs that reach the step limit score 0.
- **AIME, HMMT**: without tools, symbolic match with math_verify (Gemini judge as fallback for HMMT), mean over 64 samples.
- **LiveCodeBench v6**: problems from August 2024 to May 2025, unit-test pass rate, mean over 8 samples.

```

NOTE: neither 1711 card has a language list in its front matter, a training-data section, a safety section or a limitations section. 'Indic Suite' is described as an internal suite, so it cannot be reproduced. The 1711 cards run vLLM 0.33.0 with --trust-remote-code and a glm45 tool and reasoning parser, with an optional DSpark speculative-decoding draft model in the dspark/ folder.
