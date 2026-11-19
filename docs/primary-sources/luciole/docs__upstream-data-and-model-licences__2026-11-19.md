doc_type: docs
entity: luciole
variant/applies-to: upstream datasets and models named by the Luciole dataset cards (not Luciole documents)
source_url: https://huggingface.co/datasets/nvidia/Nemotron-Instruction-Following-Chat-v1 ; https://huggingface.co/datasets/nvidia/Nemotron-Math-v2 ; https://huggingface.co/datasets/allenai/Dolci-Instruct-SFT ; https://huggingface.co/api/models/Qwen/Qwen3-32B (and -14B, -8B, -0.6B) ; https://huggingface.co/api/models/openai/gpt-oss-120b ; https://huggingface.co/api/models?author=mistralai&search=Ministral-3-14B
retrieval_date: 2026-11-19
exists: yes
retrieved: true (cards and tags); not read: Nemotron-Post-Training-Dataset-v2 card (HTTP 401), the Ministral-3 licence file

## Findings

nvidia/Nemotron-Instruction-Following-Chat-v1 (card): licence cc-by-4.0, "This dataset is ready for commercial use." It "combines refreshed chat data from Nemotron-Post-Training-Dataset-v2 ... with synthetic dialogues produced by strong frontier models such as GPT-OSS-120B and Qwen3-235B variants", with responses from "GPT-OSS-120B, Qwen3-235B-A22B-Thinking-2507, and Qwen3-235B-A22B-Instruct-2507".
nvidia/Nemotron-Math-v2 (card): problems "solved multiple times by the gpt-oss-120b model"; AOPS subset CC BY 4.0, StackOverflow and MathGenSelect subsets CC BY-SA 4.0.
allenai/Dolci-Instruct-SFT (card): licence odc-by; its source list includes "WildChat with upgraded responses from GPT-4.1 (ODC-BY-1.0), 302,406 prompts". Whether the Luciole selection includes that WildChat part is not stated in the Luciole card (the Luciole table names only the Precise IF, python algorithms, SciRIFF, FLAN and logic puzzles parts).
Hugging Face tags and LICENSE files: Qwen3-32B, -14B, -8B and -0.6B carry license:apache-2.0, are not gated and ship a LICENSE file (Qwen3-32B LICENSE opens "Apache License Version 2.0"); openai/gpt-oss-120b carries license:apache-2.0 with LICENSE and USAGE_POLICY files; mistralai/Ministral-3-14B-Instruct-2512 and -Reasoning-2512 carry license:apache-2.0 (tag only; the LICENSE file was not read).

## What it establishes

The generator models named for the Luciole post-training and synthetic pretraining data (Qwen3 family, gpt-oss-120b, Ministral-3-14B) are published under Apache-2.0 per their Hugging Face tags (Qwen3 and gpt-oss licence files not opened in full here; the AOI gpt-oss entry holds the read gpt-oss text). Apache-2.0 places no output-use restriction in the text. GPT-4.1 output sits in an upstream AllenAI dataset and would carry OpenAI terms; not read.
