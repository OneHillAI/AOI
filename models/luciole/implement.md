# Implement - Luciole 1.1 Instruct (23B, 8B, 1B)

_Installation, hardware, serving, safe-deployment controls, quantisation, fine-tuning and integration._

<!-- item: install -->
## Install & run

The 23B and 1B load with transformers through the native Nemotron class, so no repository code is needed. Pin a revision and check the shard hashes against the Hugging Face LFS values (`ev-card-instruct`, `ev-hf-platform`).

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
name = "OpenLLM-France/Luciole-23B-Instruct-1.1"
tok = AutoTokenizer.from_pretrained(name)   # pin revision=<commit sha>
model = AutoModelForCausalLM.from_pretrained(name, torch_dtype="bfloat16", device_map="auto")
```

For Ollama, download an official GGUF file and the Modelfile from the GGUF repo, edit the `FROM` path, then run `ollama create -f Modelfile Luciole`. The Modelfile sets a 32,000-token context and temperature 0.2.

The 8B repo ships `configuration_nemotron_h.py` and `modeling_nemotron_h.py`. Read them before executing and run them in a sandbox (`ev-hf-platform`).

<!-- item: hardware -->
## Hardware & VRAM requirements

The publisher gives file sizes and no requirements table (`ev-hf-platform`, `ev-card-instruct`).

| Artefact | 23B | 8B | 1B |
|---|---|---|---|
| bf16 safetensors | 46.4 GB | not measured | 2.6 GB |
| GGUF BF16 | 46.4 GB | 16.2 GB | 3.2 GB |
| GGUF Q8_0 | 24.7 GB | 8.6 GB | 1.7 GB |
| GGUF Q5_K_M | 16.7 GB | 5.8 GB | 1.2 GB |
| GGUF Q4_K_M | 14.5 GB | 5.0 GB | 1.0 GB |
| FP8 (compressed-tensors) | 24.8 GB | listed in the org | listed in the org |

Add memory for the KV cache. A 131k context needs far more memory than the weights alone, and the publisher gives no figure. FP8 needs Hopper, Ada Lovelace or Blackwell GPUs.

<!-- item: serving -->
## Serving stacks

| Stack | Status |
|---|---|
| vLLM | documented with `--enable-auto-tool-choice --tool-call-parser hermes`; the Thinking card needs a recent vLLM (0.24 or later) and `--reasoning-parser qwen3` |
| Ollama | official GGUF and Modelfile |
| llama.cpp | official GGUF, parsed by Hugging Face as architecture nemotron with a 131,072 context |
| transformers | native Nemotron class for 23B and 1B; repository code for the 8B hybrid |
| Hosted providers | none; the Hugging Face inference provider mapping is empty |

<!-- item: safe-deployment -->
## Safe-deployment controls & Deployment Ceiling

Applying the [safe-deployment playbook](../../methodology/safe-deployment-playbook.md):

- Supply chain: pin the revision, verify the LFS hashes of every shard, and add the Apache-2.0 text and the LINAGORA SAS notice to anything you redistribute.
- Model layer: no safety evaluation, acceptable-use policy or guard model ships. Run your own misuse tests in each target language, since post-training was almost entirely English.
- Tool calling: the card marks it as work in progress. Test it on your tools before use.
- Input and output layers: add your own guardrails and logging.
- Evaluation: the only published results are the publisher's instruction-following and maths benchmarks.

Deployment Ceiling: T1 (internal assistant, human reads every output), conditional. No safety evidence supports customer-facing T2 use. The ceiling moves up when a safety evaluation is published and your own tests pass.

<!-- item: quantization -->
## Available quantizations

OpenLLM-France publishes GGUF (BF16, Q8_0, Q5_K_M, Q4_K_M) and FP8 builds of the 1B, 8B and 23B Instruct models, all Apache-2.0 under the same copyright notice (`ev-siblings`). The card says to prefer the official GGUF files for Ollama. No quality-loss figures are published, so test Q4_K_M on your task.

<!-- item: fine-tuning -->
## Fine-tuning & adaptation

The card recommends further training for specific use cases and longer-sequence training to extend context (`ev-card-instruct`). The training repository holds NeMo and NeMo-RL recipes and per-model cards for the Instruct and Thinking runs (`ev-code-repo`). The SFT and DPO data is public, with per-source tables (`ev-posttrain-data`).

The published recipe is SFT on 2.6M thinking samples and 2.1M non-thinking samples for four epochs at a 2e-5 peak learning rate, then DPO on 284K pairs with beta 5. The recipes target the Jean Zay cluster and Slurm, so expect to adapt them. The finetune folder has no README on the main branch.

<!-- item: integration -->
## API / OpenAI-compatible integration

vLLM serves an OpenAI-compatible endpoint. The card shows a chat request with the OpenAI Python client and a tool-calling request with a `tools` list. Calls return in `message.tool_calls` (`ev-card-instruct`). Ollama exposes its own API.
