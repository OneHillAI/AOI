# Implement - MORENA 1.5B (base and instruct)

_How do we deploy and run it? Install, hardware, serving, quantization, fine-tuning, and the
safe-deployment controls and Deployment Ceiling (**T1, conditional**). No OneHill run has been
made; everything here is aggregated from the publisher's files._

<!-- item: install -->
## Install & run

The weights are not a transformers architecture, so `AutoModelForCausalLM` will not load them.
The publisher route is its own PyTorch file (`ev-card-instruct`, `ev-trainer`):

```bash
pip install torch safetensors tokenizers
# download model.safetensors, config.json, tokenizer.json, modeling_morena.py,
# load_example.py and SHA256SUMS from vamboai/morena-1.5b-instruct at a pinned revision
sha256sum -c SHA256SUMS          # confirm all five files before running anything
python load_example.py           # needs a CUDA GPU as written
```

`load_example.py` builds `Transformer(ModelConfig(**cfg["model"]), "sdpa")`, loads the weights
with `strict=True` and samples with a hand-written loop. The class has no `.generate()`. The
other route is the official GGUF (`vamboai/morena-1.5b-instruct-gguf`) with llama.cpp:

```bash
llama-completion -m morena-1.5b-instruct-f16.gguf \
  -p "<reserved_0>\nNdeipi guta guru reZimbabwe?\n<reserved_1>\n" -e -n 64 --temp 0
```

Pin the revision hash. The instruct repo was last modified on 2026-10-14 and the file
`modeling_morena.py` is code you will execute, so read it first and run it in a sandbox with no
network. `load_example.py` still opens with "preview weights"; the text is stale, not a different
checkpoint (`ev-hf-platform`).

<!-- item: hardware -->
## Hardware & VRAM requirements

The publisher gives sizes, not a requirements table (`ev-card-instruct`, `ev-paper`,
`ev-hf-platform`).

| Artefact | Size |
|---|---|
| model.safetensors (bf16, 1,484,900,352 parameters) | 2.97 GB |
| GGUF Q4_K_M / Q8_0 / f16 | 0.92 / 1.58 / 2.97 GB |

The paper reports 4.44 ms per character on one A100, measured on the previous instruct version
with the same architecture, and states that the GGUF builds run on a laptop CPU offline. The
4,096-token context keeps the KV cache small, but the reference loop has no KV cache at all, so it
recomputes the whole sequence per token and is only fit for short tests. OneHill has not measured
memory or speed.

<!-- item: serving -->
## Serving stacks

| Stack | Status |
|---|---|
| llama.cpp | official GGUF; Hugging Face parses it as architecture `llama`, context 4096 (`ev-hf-platform`); the publisher says logit equivalence was checked (not repeated here) |
| Publisher PyTorch code | works, no `generate()`, no KV cache |
| transformers, vLLM, TGI, Ollama | no documented support or model class |
| Hosted providers | none; the Hugging Face inference mapping is empty and the cards set `inference: false` |

Operational readiness is therefore 2. Anything beyond llama.cpp means converting the weights or
writing a model class, which is a project in its own right.

<!-- item: safe-deployment -->
## Safe-deployment controls & Deployment Ceiling

Applying the [safe-deployment playbook](../../methodology/safe-deployment-playbook.md):

- **Supply chain:** pin the revision, verify `SHA256SUMS` yourself (including the 2.97 GB weights
  file, which this entry did not download), and review `modeling_morena.py` before executing it.
- **Model layer:** use the instruct checkpoint only for experiments; the base checkpoint has no
  safety tuning. Expect refusals and degenerate output (1.3%).
- **Evaluation:** rate outputs with native speakers per language before any wider use. Every
  publisher safety number is one model judging another, and Igbo (75%) and Yoruba (82%) are the
  weakest languages.
- **Input and output layers:** add your own guardrails; no guard model, acceptable-use policy or
  jailbreak test ships.
- **Licence hygiene:** add the Apache-2.0 text to anything you redistribute, and record the open
  Gemma Terms question in your AI-BOM.

**Deployment Ceiling: T1 (internal assistant, human reads every output), conditional.** The
publisher says the instruct model is not yet an assistant, fails 41% of benign requests and has
no native-speaker review, so customer-facing T2 use is not justified by the evidence read.

<!-- item: quantization -->
## Available quantizations

The publisher ships GGUF for the instruct model (Q4_K_M, Q8_0, f16), the 0.5B mini and the 0.2B
nano (`ev-siblings`, `ev-hf-platform`). No GGUF is listed for the 1.5B base, and no GPTQ, AWQ or
MLX build was found. The cards say GGUF conversions were checked for logit equivalence with the
safetensors; quality loss at Q4_K_M in the African languages is unmeasured, so test your language.

<!-- item: fine-tuning -->
## Fine-tuning & adaptation

The base card recommends the base checkpoint for "fine-tuning, continued pretraining and domain
adaptation" (`ev-card-base`). The repo's `modeling_morena.py` is the publisher's trainer: FSDP2
sharding, Muon for hidden weights and AdamW for embeddings, warmup-stable-decay schedule,
document-packed sequences, an `--anneal` mode and a `--loss-mask` flag for SFT. It expects
`configs/*.json`, a mixture JSON and sharded data directories that are not published, and it
mentions a `TRAIN_README.md` that is absent, so you must write your own configs and data loader
inputs. The released SFT component is the Fikira dataset (50,000 synthetic rows, MIT); the SFT
corpus itself is not public. The paper's recipe for the instruct model, for example 4,500 steps at
2e-5 on batches of 256 with loss masked to assistant turns, is a useful starting point.

<!-- item: integration -->
## API / OpenAI-compatible integration

There is no hosted endpoint and no documented OpenAI-compatible server. llama.cpp can serve the
GGUF over its own HTTP server, but the publisher does not document that route and the prompt
format uses reserved tokens, so wrap it with the chat template from `tokenizer_config.json`
(see the Use domain) rather than relying on role-based JSON.
