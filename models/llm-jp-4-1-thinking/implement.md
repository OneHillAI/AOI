# Implement - LLM-jp-4.1 thinking (8B, 32B-A3B, 33B)

_How do we deploy and run it? Install, hardware, serving, quantization, fine-tuning, and the
safe-deployment controls & Deployment Ceiling (**T1, conditional**)._

<!-- item: install -->
## Install & run

Start from the publisher cookbook (`github.com/llm-jp/llm-jp-4-cookbook`, Apache-2.0), which
defaults to `llm-jp/llm-jp-4.1-8b-thinking` and uses `uv` with a lockfile per runtime
(`ev-cookbook`). The Python examples use `trust_remote_code=True` to load the custom tokenizer
and bundled helper files, so the model repository's Python code runs on your machine.

```bash
# Transformers (5.0.0 or later), from llmjp4_transformers/
uv sync --locked
uv run --locked example_basic.py
```

Pin the Hugging Face revision (`revision="<commit-sha>"`) and read `llmjp4_tokenizer.py` and
`llmjp4_harmony.py` before first use. The weights are ungated and need no login (`ev-hub-api`).

<!-- item: hardware -->
## Hardware & VRAM requirements

The publisher gives no minimum. The cookbook records one test machine (Intel Core i9-14900K,
32 GiB RAM, one NVIDIA RTX 6000 Ada, CUDA 12.8 or 13.0) and says it is "not a statement of minimum
requirements" (`ev-cookbook`). File sizes give a floor (`ev-hub-api`, `ev-gguf`):

| Build | Weights on disk | Note |
|---|---|---|
| 33B BF16 (safetensors) | about 66 GB | 14 shards; plan for about 70 GB plus KV cache |
| 33B GGUF Q4_K_M | 20.4 GB | the build the publisher validated on llama.cpp v0.6.0 with a 4,096-token context |
| 32B-A3B BF16 | about 64 GB | 13 shards; holds all experts in memory, computes with 3.8B active |
| 8B BF16 | about 17 GB | 4 shards |

These are OneHill sums of published file sizes, not publisher requirements. KV-cache memory at
the full 64K context is not documented; measure it for your batch size.

<!-- item: serving -->
## Serving stacks

| Stack | Minimum per the cookbook | Condition |
|---|---|---|
| Transformers | 5.0.0 | `parse_response` support for the bundled schemas; `trust_remote_code=True` |
| vLLM | 0.30.0 | plus `llm-jp-vllm` 0.1.1 or later for the Harmony reasoning and tool parsers |
| llama.cpp | upstream v0.6.0 | native LLM-jp-4.1 Harmony parsing, GGUF only |

Contradiction: the GGUF model card says llama.cpp "currently requires a fork" because upstream
lacked the tokenizer fixes, while the cookbook says upstream v0.6.0 or later includes the parser
(`ev-gguf`, `ev-cookbook`). The cookbook is the newer repository push but the card was modified
later (2026-10-20). Test your llama.cpp build with a chat and a tool-call request before relying
on it. Ollama and TGI support are not documented by the publisher.

<!-- item: safe-deployment -->
## Safe-deployment controls & Deployment Ceiling

**Ceiling: T1 (internal assistant, human reads every output), conditional.** The publisher says
the models are not intended for direct production use, evidence for safety is one self-run
benchmark, and no guard model exists, so OneHill does not place customer-facing use (T2) within
reach without your own evidence.

To reach T2 you would need, at minimum:

- your own jailbreak and misuse evaluation in the languages you serve, run on the exact revision;
- an input and output guardrail layer and a guard classifier of your own;
- review of `llmjp4_tokenizer.py` and `llmjp4_harmony.py`, and a pinned revision with verified
  sha256 values;
- sandboxed execution for any tool the model calls, since tool calling is new in 4.1 and only
  evaluated on BFCL and tau2-bench by the publisher;
- a written statement of intended purpose that records you are deploying a model its publisher
  describes as research and development only.

<!-- item: quantization -->
## Available quantizations

Official GGUF repositories for all three sizes, created 2026-09-24: BF16 and Q4_K_M files with an
imatrix (`ev-gguf`). No official AWQ, GPTQ, FP8 or MLX build was found. Community derivatives
were not assessed.

<!-- item: fine-tuning -->
## Fine-tuning & adaptation

What is available: Apache-2.0 base models (8B, 32B-A3B, 33B from the 4.0 series), the 4.1 SFT
dataset (subsets under CC BY, ODC-BY, CC BY-SA, Apache-2.0 and MIT) and the three DPO datasets,
all ungated (`ev-sft-dpo`). The release page lists trl-based SFT and DPO scripts and a Nemo-Aligner
route (`ev-release-page`).

What is not confirmed: that those scripts are the ones used for the 4.1 recipe (they sit in
repositories last pushed in 2024), and the withheld subsets (AnswerCarefully, ichikara,
`llmc_math_dataset`, `synthetic_if_ja`). If you fine-tune, keep the modified Harmony chat template
(`ev-cookbook`) and mix in your own safety data, because SFT on new data can undo the safety
post-training.

<!-- item: integration -->
## API / OpenAI-compatible integration

vLLM serve exposes `/v1/chat/completions` with the publisher's parsers, which separate reasoning
from the final answer and support tool calls (`ev-cookbook`):

```bash
vllm serve llm-jp/llm-jp-4.1-8b-thinking \
    --reasoning-parser llmjp4 --reasoning-parser-plugin llm_jp_vllm.llmjp4 \
    --enable-auto-tool-choice --tool-call-parser llmjp4 --tool-parser-plugin llm_jp_vllm.llmjp4 \
    --trust-remote-code
```

`llama serve -hf llm-jp/llm-jp-4.1-8b-thinking-gguf:Q4_K_M` gives an OpenAI-compatible endpoint
that accepts `tools` and `tool_choice`. NII also announced a trial hosted API and chat service
through the University of Tokyo mdx-MaaS, mainly for researchers (`ev-pcwatch`); it is not a
production service and its terms were not read.
