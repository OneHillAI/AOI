# Implement - Jais 3 (0.9B, 3.7B, 7B, 32B, MoVA-36B-A4B, 375B-A23B)

_Installation, hardware, serving, safe-deployment controls, quantisation, fine-tuning and integration._

<!-- item: install -->
## Install & run

The weights are ungated and need no login (`ev-hub`). Load them with Transformers 5.15.0 (the version the cards validate) and `trust_remote_code=True`, or serve them with vLLM or SGLang.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
model_id = "inception42/Jais-3-7B"
tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_id, device_map="auto", dtype="bfloat16", trust_remote_code=True
)
```

The card example drops `token_type_ids` from the tokenizer output before `generate` (`ev-card-32b`). Pass `revision="<commit-sha>"` or a stage branch name to pin a version. Read `configuration_k2_horizon.py` and `modeling_k2_horizon.py` before first use, because they run on your machine under `trust_remote_code=True`.

<!-- item: hardware -->
## Hardware & VRAM requirements

The cards give tested SGLang layouts on H100 GPUs, with BF16 and FlashAttention-3 (`ev-card-32b`).

| Model | Tested layout | BF16 weights (from safetensors parameter counts) |
|---|---|---|
| 0.9B, 3.7B, 7B | 1 GPU (TP=1) | about 2 GB, 10 GB, 18 GB |
| 32B | 2 GPUs (TP=2) | about 70 GB |
| MoVA-36B-A4B | 2 GPUs (TP=2, EP=2) | about 75 GB |
| 375B-A23B | 16 H100 across two nodes (TP=16, EP=16), or one 8xH200 node (TP=8, EP=8) | about 758 GB |

The weight sizes are OneHill arithmetic from the hub parameter counts (`ev-hub`). No figure is published for the KV cache at 512K context, which adds a large amount of memory. FP8, GGUF and MLX builds reduce weight memory (`ev-quants`).

<!-- item: serving -->
## Serving stacks

The cards document three paths (`ev-card-32b`).

vLLM 0.30.0 or later:

```shell
vllm serve inception42/Jais-3-32B --trust-remote-code --model-impl vllm --dtype bfloat16 \
  --tensor-parallel-size 2 --reasoning-parser k2_horizon \
  --enable-auto-tool-choice --tool-call-parser k2_horizon
```

SGLang 0.5.20 or later with `--reasoning-parser k2_horizon` and `--tool-call-parser k2_horizon`. Transformers 5.15.0 with PyTorch 2.13.0 and Safetensors 0.8.0.

GGUF builds target llama.cpp and Ollama according to the cards. MLX builds target Apple silicon. OneHill has not run any of these stacks.

<!-- item: safe-deployment -->
## Safe-deployment controls & Deployment Ceiling

Ceiling: T1 (internal assistant, human reads every output), conditional. Every safety result is the publisher's own, no text guard model is released, and no result covers tool, terminal or file actions. Customer-facing use (T2) needs your own evidence first.

To reach T2, complete these steps.

- Run your own jailbreak and misuse evaluation in the dialects you serve, on the exact revision you deploy.
- Add input and output guardrails and a guard classifier of your own.
- Pin the revision, verify the LFS sha256 values and read the two custom Python files.
- Sandbox every tool the model can call. Agent behaviour is the model's main design goal, and its safety has no published test.
- Record that you deploy an Apache-2.0 model whose card tells users to add safeguards before deployment (`ev-cards-all`).

<!-- item: quantization -->
## Available quantizations

The IFM organisation publishes official builds (`ev-quants`).

| Format | Sizes | Notes |
|---|---|---|
| FP8 | 3.7B, 7B, 32B, MoVA-36B-A4B, 375B-A23B | no 0.9B build |
| MLX 4-bit, 8-bit, bf16 | 0.9B, 3.7B, 7B, 32B, MoVA-36B-A4B | Apple silicon |
| GGUF | 0.9B, 3.7B, 7B, 32B, MoVA-36B-A4B | the 32B repository holds BF16, Q4_K_M, Q5_0, Q5_K_M, Q6_K and Q8_0; none for the 375B |

GGUF files appeared on 2026-10-12 and 2026-10-13, two weeks after the weights. The Uno LoRA adapters speed up decoding, but they carry no licence tag (`ev-uno`). Community quantisations were not assessed.

<!-- item: fine-tuning -->
## Fine-tuning & adaptation

Every size has branches for the CPT, Cooldown, FTPO and SFT checkpoints, so you can continue from any stage (`ev-branches`). The xLLM repository covers pretraining and SFT, RL360 covers RLVR, and the data sample covers four Arabic subsets (`ev-code`, `ev-data-sample`).

No Jais-3 run configuration was found in xLLM or RL360, whose READMEs describe K2 Horizon. The report lists configurations and W&B logs as released, but they were not opened. Check them before planning to reproduce a stage.

Keep the model's chat template, include reasoning-format samples, and mix in your own safety data. Further training on new data can erode safety behaviour, as the report itself notes for continued training of post-trained models.

<!-- item: integration -->
## API / OpenAI-compatible integration

vLLM and SGLang expose OpenAI-compatible `/v1/chat/completions` endpoints (`ev-card-32b`). Set reasoning depth per request:

```python
extra_body={"top_k": 20, "chat_template_kwargs": {"reasoning_effort": "high"}}
```

Reasoning is returned in `reasoning_content` and the answer in `content`. For tools, start the server with `--enable-auto-tool-choice --tool-call-parser k2_horizon` and pass `tool_call_format` (`xml`, `json` or `xml_typed`) in `chat_template_kwargs`. The card advises `reasoning_effort="high"`, at least 32,768 output tokens, temperature 0.7 for Arabic thinking and 1.0 for English thinking.
