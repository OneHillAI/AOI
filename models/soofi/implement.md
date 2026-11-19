# Implement - Soofi (Soofi-S)

_Installation, hardware, serving, safe-deployment controls, quantisation, fine-tuning and integration._

<!-- item: install -->
## Install & run

Soofi-S ships as bf16 safetensors on the verified `Soofi-Project` org, plus first-party GGUF
builds, but every repo is manually gated. Request access and wait for publisher approval before
any file downloads; the card describes a closed beta for selected partners. The custom hybrid
Mamba-2/MoE needs `trust_remote_code=True` on the transformers path. Pin an exact revision.

```python
# Hugging Face transformers
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "Soofi-Project/Soofi-S-Instruct-Preview"   # deploy the post-trained variant
rev = "<pinned-commit-sha>"                              # pin the revision, don't float on main
tok = AutoTokenizer.from_pretrained(model_id, revision=rev, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_id, revision=rev, trust_remote_code=True)
```

```bash
# llama.cpp / llama-server (first-party GGUF) - use --jinja for the native tool template
./llama-server -m soofi-s-instruct-preview.Q4_K_M.gguf --jinja

# Ollama (community/first-party GGUF)
ollama run soofi-s-instruct

# vLLM (OpenAI-compatible server) - confirm your vLLM version supports the hybrid arch
vllm serve Soofi-Project/Soofi-S-Instruct-Preview --revision <sha> --trust-remote-code
```

Prefer safetensors; verify per-file checksums after download.

<!-- item: hardware -->
## Hardware & VRAM requirements

The MoE activates only ~3B of 30B parameters per token, so decode is cheap, but the full ~30B
weight set must be resident. In bf16 that is roughly 60 GB, so plan for multi-GPU or a
first-party GGUF or 3-bit quantization to fit a single high-VRAM card. The hybrid Mamba-2 design
keeps the inference cache near-constant as context grows, so serving up to 256k tokens does not
blow up VRAM the way a dense transformer's KV cache would. Size for the largest variant to serve
and budget headroom.

<!-- item: serving -->
## Serving stacks

Runtime support for the custom architecture is still maturing, so check the stack's version
before committing:

| Stack | Use it for |
|---|---|
| llama.cpp / llama-server | GGUF inference; `--jinja` applies the embedded chat/tool template verbatim |
| vLLM | High-throughput + OpenAI-compatible API (needs `--trust-remote-code`; confirm hybrid-arch support) |
| Ollama | Local single-command runs (note: its template omits the native tool format) |
| transformers | Prototyping and fine-tuning (`trust_remote_code=True`) |

Operational Readiness scores 4. The breadth is there, but the custom Mamba-2/MoE and
cross-runtime tool-template quirks need more care than a plain Llama-class model.

<!-- item: safe-deployment -->
## Safe-deployment controls & Deployment Ceiling

Apply the [safe-deployment playbook](../../methodology/safe-deployment-playbook.md). The
model-specific gate rows are:

- Supply chain: pin the exact `Soofi-Project` revision hash and verify checksums; prefer
  safetensors. `trust_remote_code=True` runs vendor modelling code, so review it.
- Model layer: deploy the Instruct-Preview variant, never the base checkpoint, and set
  conservative decoding defaults.
- Input/output layers: add guardrails and your own guard classifier for any customer-facing path,
  because Soofi-S ships no companion guard model and its safety features are documented as
  incomplete. Add prompt-injection defences and treat retrieved and tool content as untrusted.
- Compliance: archive the per-source training-content summary and copyright posture in your
  AI-BOM; the source data is readily available.

Deployment Ceiling: T2 (customer-facing, human-reviewed), conditional and preview-caveated. With
the Instruct-Preview variant, input/output guardrails and prompt-injection defences, Soofi-S can
in principle reach customer-facing, human-reviewed use. It is an early preview with incomplete
safety hardening, so pilot it internally first. Its strengths are European sovereignty,
auditability and long-context economics. T3+ (bounded autonomous) also needs a deterministic
action-policy engine, per-action human approval for irreversible operations and external guard
tooling beyond what this release provides.

<!-- item: quantization -->
## Available quantizations

The `Soofi-Project` org publishes first-party GGUF builds for the preview variants and an
EntQuant 3-bit build, so quantized inference does not depend solely on community efforts.
Coverage is good for a preview. Test quality against the bf16 base for your workload before
relying on an aggressive (e.g. 3-bit) quant in production.

<!-- item: fine-tuning -->
## Fine-tuning & adaptation

Soofi-S is built for fine-tuning, but the rights are not there yet. The training code is public
(`soofi-project/Soofi-Pretraining`, with no licence file; `soofi-trainer`, MIT) and the
per-source data accounting documents the recipe, so the project could in principle be reproduced
or extended. The weights and the intermediate Megatron checkpoint are manually gated, and no
licence in force grants adaptation or redistribution of derivatives. Confirm the terms of your
access approval before fine-tuning. With access, standard SFT/LoRA via `transformers` / TRL on
the safetensors checkpoints is the practical path. Placing a derivative on the market carries EU
AI Act provider implications (see Assess).

<!-- item: integration -->
## API / OpenAI-compatible integration

Serve Soofi-S behind the OpenAI-compatible endpoint of vLLM or llama-server for drop-in
integration with existing OpenAI-client code:

```bash
llama-server -m soofi-s-instruct-preview.Q4_K_M.gguf --jinja --port 8000
# then point any OpenAI SDK at http://localhost:8000/v1
```

Use `--jinja` (llama.cpp) so the model's embedded chat/tool template is applied verbatim, which
is what makes native tool calling work. Some runtimes (e.g. Ollama) strip the tool portion, so
verify the template your endpoint applies.
