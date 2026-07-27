# Implement - Soofi (Soofi-S)

_How do we deploy and run it? Install, hardware, serving, quantization, fine-tuning, and the
safe-deployment controls & Deployment Ceiling (**T2, conditional - and preview-caveated**)._

<!-- item: install -->
## Install & run

Soofi-S ships as bf16 safetensors on the verified `Soofi-Project` org, plus first-party GGUF
builds. Because it is a **custom hybrid Mamba-2/MoE**, the transformers path needs
`trust_remote_code=True`. Always pin an exact revision.

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

The MoE **activates only ~3B of 30B** parameters per token, so *decode* is cheap, but the **full
~30B weight set** must be resident. In **bf16** that is roughly 60 GB, so plan for **multi-GPU** or
a **first-party GGUF / 3-bit** quantization to fit a single high-VRAM card. The standout property
is long-context economics: the hybrid Mamba-2 design keeps the inference cache **near-constant** as
context grows, so serving up to **256k** tokens does not blow up VRAM the way a dense
transformer's KV cache would. Size for the largest variant you intend to serve and budget headroom.

<!-- item: serving -->
## Serving stacks

Because Soofi-S is a **custom architecture**, runtime support is still maturing - check your stack's
version before committing:

| Stack | Use it for |
|---|---|
| **llama.cpp / llama-server** | GGUF inference; `--jinja` applies the embedded chat/tool template verbatim |
| **vLLM** | High-throughput + OpenAI-compatible API (needs `--trust-remote-code`; confirm hybrid-arch support) |
| **Ollama** | Local single-command runs (note: its template omits the native tool format) |
| **transformers** | Prototyping and fine-tuning (`trust_remote_code=True`) |

This is why Operational Readiness scores **4** rather than 5: the breadth is there, but the custom
Mamba-2/MoE and cross-runtime tool-template quirks demand more care than a plain Llama-class model.

<!-- item: safe-deployment -->
## Safe-deployment controls & Deployment Ceiling

Applying the [safe-deployment playbook](../../methodology/safe-deployment-playbook.md), the
model-specific gate rows are:

- **Supply chain:** pin the exact `Soofi-Project` revision hash and verify checksums; prefer
  safetensors (`trust_remote_code=True` runs vendor modelling code - review it).
- **Model layer:** deploy the **Instruct-Preview** variant, never the base checkpoint; set
  conservative decoding defaults.
- **Input/output layers:** add input/output guardrails and your **own** guard classifier for any
  customer-facing path - Soofi-S ships no companion guard model and its safety features are
  documented as **incomplete**; add prompt-injection defences and treat retrieved/tool content as
  untrusted.
- **Compliance:** archive the (readily available) per-source training-content summary and copyright
  posture in your AI-BOM.

**Deployment Ceiling: T2 (customer-facing, human-reviewed) - conditional, and preview-caveated.**
With the Instruct-Preview variant plus input/output guardrails and prompt-injection defences,
Soofi-S can *in principle* reach customer-facing, human-reviewed use - but because it is an early
preview with incomplete safety hardening, **pilot it internally first**. Its standout strengths are
**European sovereignty, auditability and long-context economics**. T3+ (bounded autonomous)
additionally needs a deterministic action-policy engine, per-action human approval for irreversible
operations, and external guard tooling beyond what this release provides.

<!-- item: quantization -->
## Available quantizations

The `Soofi-Project` org publishes **first-party GGUF** builds for the preview variants and an
**EntQuant 3-bit** build, so quantized inference does not depend solely on community efforts. This
is unusually good coverage for a preview - but re-check quality against the bf16 base for your
workload before relying on an aggressive (e.g. 3-bit) quant in production.

<!-- item: fine-tuning -->
## Fine-tuning & adaptation

Soofi-S is strong here because the **training stack is open**: `soofi-project/Soofi-Pretraining`
and `soofi-trainer` provide the pre-/mid-training code and configs, and the released **intermediate
checkpoints** plus **per-source data accounting** let you reproduce or extend training rather than
only fine-tune the final weights. The base is explicitly built for fine-tuning. For most adopters,
standard **SFT/LoRA** via `transformers` / TRL on the safetensors checkpoints is the practical path;
teams needing deeper control can use the released trainers directly. Note the EU AI Act provider
implications of placing a derivative on the market (see Assess).

<!-- item: integration -->
## API / OpenAI-compatible integration

Serve Soofi-S behind **vLLM's** or **llama-server's OpenAI-compatible endpoint** for drop-in
integration with existing OpenAI-client code:

```bash
llama-server -m soofi-s-instruct-preview.Q4_K_M.gguf --jinja --port 8000
# then point any OpenAI SDK at http://localhost:8000/v1
```

Use `--jinja` (llama.cpp) so the model's **embedded chat/tool template** is applied verbatim - that
is what makes native tool calling work; some runtimes (e.g. Ollama) strip the tool portion, so
verify the template your endpoint actually applies.
