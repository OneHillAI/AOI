# model_card / IFM/K2-Horizon-32B (the base model Jais-3-32B is adapted from)

source_url: https://huggingface.co/IFM/K2-Horizon-32B (raw README); https://huggingface.co/api/models/IFM/K2-Horizon-32B; https://huggingface.co/api/models?author=IFM
retrieval_date: 2026-11-19
doc_type: model_card
exists: yes
retrieved: true
tag: publisher

NOTE (OneHill): K2 Horizon is a separate entity and is not scored here. API facts: gated false; created 2026-09-01; last modified 2026-11-04; card front matter license apache-2.0 and datasets IFM/K2-Horizon-Pretrain-Data and IFM/K2-Horizon-Midtrain-Data; raw LICENSE returned HTTP 404 (no LICENSE file in the 32B repo). The two datasets named in the front matter returned HTTP 401 from the Hugging Face API on 2026-11-19 (https://huggingface.co/api/datasets/IFM/K2-Horizon-Pretrain-Data and .../K2-Horizon-Midtrain-Data), so their access status is unverified; IFM/TxT360-v2 (linked as the data repository) returned HTTP 200, ungated, licence cc-by-4.0. The card text below says the technical report was "In Progress" at its last update (2026-09-28); the K2-Horizon report is on arXiv as 2611.21003 (see technical_report__k2-horizon-arxiv-abstract). The IFM organisation is not verified on Hugging Face (isVerified false).

## Raw README (verbatim; benchmark table and CSS omitted)
```
---
license: apache-2.0
model_name: K2-Horizon-32B
pipeline_tag: text-generation
library_name: transformers
language:
  - en
datasets:
  - IFM/K2-Horizon-Pretrain-Data
  - IFM/K2-Horizon-Midtrain-Data
tags:
  - k2-horizon
  - 32b
  - dense
  - open-weights
  - ifm
---

# K2-Horizon-32B

[Training Code](https://github.com/ifm-ai/xllm) - [Evaluation Code](https://github.com/ifm-ai/Eval360) - [All Training Data](https://github.com/ifm-ai/DATA_NAVIGATOR)


K2-Horizon-32B is the large dense member of the K2-Horizon family: a 32B decoder-only model with a 512K context window.

<p align="center">
  <img src="assets/k2-horizon-32b-benchmarks.png" alt="K2-Horizon-32B benchmark results against open dense models and GPT-5.6 Luna (medium)" width="100%">
</p>

## K2-Horizon-32B Highlights

- **Strong dense baseline.** A 32B dense model evaluated on the same agentic, coding, and reasoning benchmarks as the rest of the family (see [Benchmark Results](#benchmark-results)).
- **512K context.** Native 524,288-token context from the midtraining stages onward.
- **Intermediate checkpoints.** Intermediate checkpoints are released so capability changes can be studied across training rather than at a single checkpoint.
- **Fully open.** Training data/recipe and the training code are public.

## Benchmark Results

<!-- TABLE:START -->
[BENCHMARK TABLE HTML OMITTED]
<!-- TABLE:END -->

<p style="font-size:1.25em;line-height:1.6">Scores in %. Bold marks the best score in each row. Sections follow the <a href="https://artificialanalysis.ai/methodology/intelligence-benchmarking">Artificial Analysis Intelligence Index</a> categories. Baseline scores are from Artificial Analysis; Muse Glimmer-30B at high reasoning effort, other open models in their reasoning mode.</p>

## Quickstart

### Serving

vLLM, recipe at [recipes.vllm.ai/IFM](https://recipes.vllm.ai/IFM):

```shell
vllm serve IFM/K2-Horizon-32B \
  --revision main \
  --model-impl vllm \
  --tensor-parallel-size 2 \
  --trust-remote-code \
  --dtype bfloat16 \
  --reasoning-parser k2_horizon \
  --enable-auto-tool-choice \
  --tool-call-parser k2_horizon
```

Use an exact branch name from the inventory with vLLM's `--revision` option. For example, `--revision pretrain_1100000` selects the final checkpoint of Pretraining, at step 1,100,000.

SGLang recipe validated on 2× H200 in the [SGLang K2 Horizon cookbook](https://docs.sglang.io/cookbook/autoregressive/IFM/K2-Horizon):

```shell
python3 -m sglang.launch_server \
  --model-path IFM/K2-Horizon-32B \
  --revision main \
  --tp 2 \
  --dtype bfloat16 \
  --attention-backend fa3 \
  --reasoning-parser k2_horizon \
  --tool-call-parser k2_horizon \
  --host 0.0.0.0 --port 30000
```

### API Usage

> [!Tip]
> Recommended settings: `reasoning_effort="high"`, `temperature=1.0`, `top_p=0.95`.
> Reasoning depth is selected per request through `chat_template_kwargs`. Thinking is returned in `reasoning_content` and the answer in `content`.

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:30000/v1", api_key="EMPTY")
response = client.chat.completions.create(
    model="IFM/K2-Horizon-32B",
    messages=[{"role": "user", "content": "Explain the result step by step."}],
    temperature=1.0,
    top_p=0.95,
    max_tokens=32768,
    extra_body={"chat_template_kwargs": {"reasoning_effort": "high", "tool_call_format": "xml"}},
)
message = response.choices[0].message
print("Reasoning:", getattr(message, "reasoning_content", None))
print("Answer:", message.content)
```

Our model supports multiple tool-call formats, which can be changed with `chat_template_kwargs`. The supported values are `json`, `xml`, and `xml_typed`. The default is `xml`. Keep `--tool-call-parser k2_horizon` enabled to parse the selected format.

### Transformers

Validated with Transformers 5.15.0, PyTorch 2.13.0, Safetensors 0.8.0.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "IFM/K2-Horizon-32B"
tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_id, device_map="auto", dtype="bfloat16", low_cpu_mem_usage=True, trust_remote_code=True
)

inputs = tokenizer("Explain why long-context evaluation is difficult.", return_tensors="pt").to(model.device)
inputs.pop("token_type_ids", None)
outputs = model.generate(**inputs, max_new_tokens=32768, temperature=1.0, top_p=0.95, do_sample=True)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

## Training Overview

The table below lists the training stages in order and the purpose of each stage.

Training steps are counted within each stage or phase. Token budgets cover only the additional training in that stage or phase. For example, the 50B tokens listed for SFT Phase 2 are additional to the 219B tokens in Phase 1, bringing the cumulative budget to 269B tokens by the end of Phase 2. Here, B and T denote billion and trillion tokens, respectively.

Each stage or phase continues from the final checkpoint of the preceding stage or phase.

Some stages, such as SFT, have multiple phases with slight changes to the data mix while retaining the same overall purpose.

| Training stage | Training steps | Training tokens | Sequence length | Purpose |
| --- | --- | --- | --- | --- |
| Pretraining | 1100000 | 22.9T | 8K | Pretraining. |
| Midtraining — Stage 1 | 55000 | 1.1T | 32K | Context extension. |
| Midtraining — Stage 2 | 25000 | 498B | 128K | Context extension. |
| Midtraining — Stage 3 | 5500 | 110B | 512K | Context extension. |
| Midtraining — Stage 4 | 10000 | 199B | 512K | Continued context extension from Stage 3, with the data mix shifted toward agentic and reasoning SFT data. |
| SFT — Phase 1 | 11000 | 219B | 512K | SFT for better domain coverage, starting from the final checkpoint of midtraining stage 4. |
| SFT — Phase 2 | 2500 | 50B | 512K | SFT on a high-quality subset of the data used in Phase 1, with learning rate decay. |

## Release Artifacts

The tables below list the release artifacts for **K2-Horizon-32B**, their availability, and the expected release dates for remaining items.

**Last updated:** 2026-09-28

**Status:**

- **Available** — fully released for the scope listed;
- **Partial** — some items are available, with remaining items listed in the notes;
- **In Progress** — being prepared for release but not yet available.

### Artifact Index

| Artifact | Link | Status | Remaining items / expected availability |
| --- | --- | --- | --- |
| Model card | [Hugging Face](https://huggingface.co/IFM/K2-Horizon-32B) | Available | N/A |
| Training logs | [W&B](https://wandb.ai/llm360/K2-Horizon-32B) | Available | N/A |
| Blog post | [Blog post](https://ifm.ai/blog/k2/) | Available | N/A |
| Checkpoints | [Checkpoint inventory](#checkpoint-inventory) | Available | N/A |
| Technical report | Not yet available | In Progress | End of September 2026 |
| Code repository | [GitHub](https://github.com/ifm-ai/xllm) | Available | N/A |
| Data | [Hugging Face](https://huggingface.co/datasets/IFM/TxT360-v2) | Available | N/A |

### Checkpoint Inventory

**Model repository:** [IFM/K2-Horizon-32B](https://huggingface.co/IFM/K2-Horizon-32B)

Branch names below refer to this repository. Patterns containing `*` group branches by training stage or phase. The `*` is a placeholder for a training-step number, not a literal branch name. Intermediate checkpoint groups exclude the final checkpoint listed separately; a pattern does not imply that a checkpoint is available at every step.

For example, `sft_1_11000` is the checkpoint saved at training step 11,000 within SFT Phase 1, and is the final checkpoint of that phase. The numeric suffix is the step within the named stage or phase, not the cumulative step across all training. Thus, `sft_2_2500` refers to step 2,500 within SFT Phase 2.

For a partially released group, the available checkpoints and the remaining checkpoints are listed in the notes.

| Checkpoint | Branch / repository | Status | Remaining items / expected availability |
| --- | --- | --- | --- |
| Pretrain Intermediate Checkpoints | `pretrain_*` | Available | N/A |
| Pretrain Final Checkpoint | `pretrain_1100000` | Available | N/A |
| Midtrain Stage 1 Intermediate Checkpoints | `mid_1_*` | Available | N/A |
| Midtrain Stage 1 Final Checkpoint | `mid_1_55000` | Available | N/A |
| Midtrain Stage 2 Intermediate Checkpoints | `mid_2_*` | Available | N/A |
| Midtrain Stage 2 Final Checkpoint | `mid_2_25000` | Available | N/A |
| Midtrain Stage 3 Intermediate Checkpoints | `mid_3_*` | Available | N/A |
| Midtrain Stage 3 Final Checkpoint | `mid_3_5500` | Available | N/A |
| Midtrain Stage 4 Intermediate Checkpoints | `mid_4_*` | Available | N/A |
| Midtrain Stage 4 Final Checkpoint | `mid_4_10000` | Available | N/A |
| SFT Phase 1 Intermediate Checkpoints | `sft_1_*` | Available | N/A |
| SFT Phase 1 Final Checkpoint | `sft_1_11000` | Available | N/A |
| SFT Phase 2 Intermediate Checkpoints | `sft_2_*` | Available | N/A |
| SFT Phase 2 Final Checkpoint | `sft_2_2500` | Available | N/A |

> [!IMPORTANT]
> Note:
> - Released K2-Horizon Hugging Face checkpoints (e.g. [Huggingface](https://huggingface.co/IFM/K2-Horizon-375B-A23B/tree/main)) can be used for inference, evaluation, and downstream fine-tuning (including SFT).
> Training behavior in the bundled Hugging Face implementation may differ from native xLLM, including the auxiliary load-balancing loss.
> To continue the original pretraining with xLLM's training behavior, use the native xLLM checkpoint and xLLM runtime.

## Best Practices

1. **Reasoning effort: always `high`.** All reported results use high reasoning effort. Pass `{"chat_template_kwargs": {"reasoning_effort": "high"}}` on every request.  `medium` and `low` effort settings are not recommended except for research on reasoning efforts.
2. **Sampling parameters.** `temperature=1.0`, `top_p=0.95`.
3. **Serving.** Use the validated SGLang recipe above: BF16, TP=2, FlashAttention-3. Full recipes for every K2-Horizon size, with measured H200 latency and throughput, are in the [SGLang cookbook](https://docs.sglang.io/cookbook/autoregressive/IFM/K2-Horizon) and the [vLLM recipe](https://recipes.vllm.ai/IFM).
4. **Parsers.** Enable the `k2_horizon` reasoning parser for chat, and add the `k2_horizon` tool-call parser for agent use. Leave both off for plain completion-style generation.

## Citation

```bibtex
@misc{k2horizon2026,
  title  = {Introducing K2 Horizon: Frontier Performance, Radically Open},
  author = {{IFM Team}},
  year   = {2026},
  url    = {https://ifm.ai/blog/k2/},
}
```
```
