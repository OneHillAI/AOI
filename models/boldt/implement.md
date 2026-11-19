# Implement - Boldt-DC (350M and 1B base models)

_Installation, hardware, serving, safe-deployment controls, quantisation, fine-tuning and integration._

<!-- item: install -->
## Install & run

Load the weights with transformers and use plain text completion (`ev-card-1b`, `ev-card-350m`).

Call `AutoTokenizer.from_pretrained` and `AutoModelForCausalLM.from_pretrained` with `Boldt/Boldt-DC-1B` or `Boldt/Boldt-DC-350M`. Then call `generate` on a German prompt such as "Berlin ist eine Stadt, wo".

The Boldt-DC-1B card's own sample loads `Boldt/Boldt-1B`, a different model trained with news data and a 4,096 context. Use the repo name above. Always load the tokenizer from the same repo.

<!-- item: hardware -->
## Hardware & VRAM requirements

The bf16 weights are 0.94 GB for the 350M model (468M parameters) and 2.41 GB for the 1B model (1.205B parameters). With a 2,048-token context the KV cache is small, so both run on a laptop GPU or CPU. This is OneHill's inference from file sizes. The publisher gives no VRAM, latency or throughput figure. The paper names training hardware (8xA100 and 4xH100) and no GPU-hours (`ev-hf-platform`, `ev-paper`).

<!-- item: serving -->
## Serving stacks

The cards document transformers only. The config is a standard `LlamaForCausalLM`, which common runtimes read, but the publisher makes no statement for vLLM, llama.cpp or Ollama and nobody has tested them for this entry. No inference provider hosts the models (`ev-hf-platform`).

<!-- quantization is a `gap` item: no quantised build of either DC model exists. -->

<!-- item: safe-deployment -->
## Safe-deployment controls & Deployment Ceiling

Deployment Ceiling: T0 (sandbox and research), conditional. These are base models with no safety tuning and no safety evaluation, so keep them behind a human reviewer.

- Run your own toxicity, bias and factuality tests before any wider use.
- Add input and output guardrails; no guard model or acceptable-use policy ships.
- Add the Apache-2.0 text and a notice when you redistribute, since no LICENSE file ships.
- Pin the repo revision and check the LFS SHA256; nothing is signed.
- Confirm which repo your code loads (see Install).

<!-- item: fine-tuning -->
## Fine-tuning & adaptation

The paper fine-tunes both base models on the German SmolTalk2 subset with TRL: batch size 32, peak learning rate 5e-5, 3% warmup, loss on completions only, one H100 (`ev-paper`). Third parties have published German chat and embedding fine-tunes of the DC models (`ev-hf-platform`). No configs or fine-tuning guide ship, and the Boldt-1B-IT-Preview sibling was tuned on a different base and data mix (`ev-siblings`).

<!-- integration is a `gap` item: no hosted endpoint or OpenAI-compatible serving guidance exists. -->
