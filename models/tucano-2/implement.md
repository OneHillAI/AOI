# Implement - Tucano 2 (Qwen-derived 0.5B, 1.5B and 3.7B; Base, Instruct and Think)

_Installation, hardware, serving, safe-deployment controls, quantisation, fine-tuning and integration._

<!-- item: install -->
## Install & run

The models load with the standard transformers classes, with no remote code. Pin a revision hash and record the LFS sha256 of each safetensors shard (`ev-card-instruct`, `ev-configs`).

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
model_id = "Polygl0t/Tucano2-qwen-3.7B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")
messages = [{"role": "user", "content": "Qual é a capital de Cabo Verde?"}]
prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
```

The cards set temperature 0.1, top_k 50, top_p 1.0 and repetition_penalty 1.2, and `generation_config.json` sets `max_new_tokens` to 1024.

<!-- item: hardware -->
## Hardware & VRAM requirements

The publisher gives file sizes and training cost, not a requirements table (`ev-hf-platform`).

| Model | bf16 weights |
|---|---|
| 3.7B Base, Instruct, Think | 7.77 GB (Base), 7.52 GB (Instruct, Think) in two shards |
| 1.5B | 3.02 GB |
| 0.5B | 0.98 GB |

A third party served the 3.7B Instruct in bf16 with vLLM on an RTX 3080 (about 9.6 GiB usable). The setup used a 4,096 context, a 1 GiB KV cache and 8.7 GiB of VRAM. Speed was 79.4 tokens per second for one request and 436.7 at concurrency 8 (`ev-community`). OneHill has not measured memory or speed.

<!-- item: serving -->
## Serving stacks

| Stack | Status |
|---|---|
| transformers | documented on every card (`ev-card-instruct`) |
| vLLM | run by a third party with the unmodified Instruct weights (`ev-community`) |
| MLX | community 4-bit build of the 3.7B Instruct (`ev-community`) |
| llama.cpp, Ollama, TGI | no documented support or GGUF; the Qwen3 architecture is standard, but OneHill has not tested it |
| Hosted providers | none listed by Hugging Face (`ev-hf-platform`) |

<!-- item: safe-deployment -->
## Safe-deployment controls & Deployment Ceiling

Apply the [safe-deployment playbook](../../methodology/safe-deployment-playbook.md).

- Supply chain: pin the revision and record the LFS hashes, since no checksum file or signature ships.
- Model layer: use the Instruct or Think models only. The Base models have no safety tuning and the cards bar deployment of them.
- Evaluation: run your own Portuguese safety, bias and toxicity tests. No safety evaluation is published.
- Input and output layers: add guardrails. No guard model or acceptable-use policy ships.
- Context: keep prompts and context under 4,096 tokens.
- Licence hygiene: add the Apache-2.0 text to anything you redistribute, and record the mixed GigaVerbo-v2 source licences in your AI-BOM.

Deployment Ceiling: T1 (internal assistant, a human reads every output), conditional. The evidence read does not support customer-facing T2 use because no safety evaluation exists.

<!-- item: quantization -->
## Available quantizations

The publisher ships none. A community MLX 4-bit build of the 3.7B Instruct exists (`pessini/Tucano2-qwen-3.7B-Instruct-MLX-4bit`, Apache-2.0). Quality loss in Portuguese is unmeasured, so test your own tasks before using it.

<!-- item: fine-tuning -->
## Fine-tuning & adaptation

The repos publish the SFT and APO configs, training logs and the llm-foundry trainer, so you can rerun or adapt the post-training stages (`ev-configs`, `ev-code`). The Instruct SFT run uses 5 epochs at a peak learning rate of 5e-5 with assistant-only loss and a batch of 524,288 tokens. The APO run uses 5 epochs at 5e-6, `apo_zero` loss and beta 0.5, on 28,437 preference pairs. The Base repos keep intermediate checkpoints as branches every 2,500 steps for the 3.7B model. The SFT and Preferences datasets are Apache-2.0 and ungated. Check the CC-BY-NC question in the corpus licence before using GigaVerbo-v2 for commercial continued pretraining.

<!-- item: integration -->
## API / OpenAI-compatible integration

There is no hosted endpoint. A third-party recipe serves the 3.7B Instruct through vLLM's OpenAI-compatible chat completions route (`ev-community`). The chat template carries a tools block in Portuguese, so pass tools through the template and not as free text.
