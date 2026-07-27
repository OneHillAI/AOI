# Implement - Mistral AI (open-weight family)

_How do we deploy and run it? Install, hardware, serving, quantization, fine-tuning, and the
safe-deployment controls & Deployment Ceiling (**T2, conditional**)._

<!-- item: install -->
## Install & run

Mistral checkpoints are standard safetensors on the verified `mistralai` org, and Mistral also
ships an **official** inference library. Always pin an exact revision.

```python
# Hugging Face transformers
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "mistralai/Mistral-Small-3.2-24B-Instruct-2506"  # pick the exact variant you assessed
rev = "<pinned-commit-sha>"                                    # pin the revision, don't float on main
tok = AutoTokenizer.from_pretrained(model_id, revision=rev)
model = AutoModelForCausalLM.from_pretrained(model_id, revision=rev)
```

```bash
# Official Mistral inference library
pip install mistral-inference

# Ollama
ollama run mistral-small

# vLLM (OpenAI-compatible server)
vllm serve mistralai/Mistral-Small-3.2-24B-Instruct-2506 --revision <sha>

# llama.cpp (community GGUF)
./llama-cli -m mistral-small-3.2.Q4_K_M.gguf -p "Hello"
```

Prefer safetensors; verify per-file checksums after download, and confirm the model's licence.

<!-- item: hardware -->
## Hardware & VRAM requirements

- **Mistral 7B / Nemo 12B** run comfortably on a single modern GPU (a 24 GB card handles them at
  full or near-full precision).
- **Mistral Small 3.x (24B)** fits a 24 GB card with modest quantization.
- **Mixtral 8x7B** benefits from more VRAM despite ~13B active params (all experts must be
  resident); **Mixtral 8x22B** and **Mistral Large 2 (123B)** need multi-GPU or heavy
  quantization for latency-sensitive serving.

Size to the largest checkpoint you intend to serve, and budget extra headroom for the KV cache at
128K context lengths.

<!-- item: serving -->
## Serving stacks

Because the checkpoints are plain safetensors with standard architectures, mainstream runtimes
load them without custom code - and Mistral ships a first-party library:

| Stack | Use it for |
|---|---|
| **mistral-inference** | Mistral's official reference inference |
| **vLLM** | High-throughput serving + OpenAI-compatible API |
| **TGI** | Hugging Face-native production serving |
| **llama.cpp** | CPU / edge / GGUF quantized inference |
| **Ollama** | Local single-command runs |
| **transformers** | Prototyping and fine-tuning |

This breadth is a large part of why Operational Readiness scores 4; it stops short of 5 only on
the narrower *official* quantization program.

<!-- item: safe-deployment -->
## Safe-deployment controls & Deployment Ceiling

Applying the [safe-deployment playbook](../../methodology/safe-deployment-playbook.md), the
model-specific gate rows are:

- **Supply chain:** pin the exact `mistralai` revision hash and verify checksums; prefer
  safetensors (already the default - no pickle load).
- **Model layer:** deploy the **instruct** variant, never the base checkpoint; set conservative
  decoding defaults.
- **Input/output layers:** add input/output guardrails - the **Mistral Moderation API** (a
  fine-tuned Ministral 8B classifier) can serve as the companion filter, since Mistral ships no
  broadly-distributed open guard-weight; add prompt-injection defences and treat retrieved/tool
  content as untrusted.
- **Compliance:** confirm the per-model **licence** (Apache vs research-only MRL) before commercial
  deployment, and archive the copyright/training-content posture in your AI-BOM.

**Deployment Ceiling: T2 (customer-facing, human-reviewed) - conditional.** With the instruct
variant plus input/output guardrails, the Moderation classifier and prompt-injection defences,
Mistral reaches customer-facing, human-reviewed use. It is held at T2 rather than higher because
safety tuning is lighter than the largest labs and there is no broad independent red-team. T3+
(bounded autonomous) additionally needs a deterministic action-policy engine, per-action human
approval for irreversible operations, and external guard tooling beyond what the release provides.

<!-- item: quantization -->
## Available quantizations

A broad **community** ecosystem of **GGUF** (llama.cpp/Ollama), **AWQ/GPTQ** and **FP8**
quantizations circulates (bartowski, unsloth, lmstudio-community and others), and some official
low-bit releases exist. Coverage is marked *partial* because the **first-party** quantization
program is narrower than the largest ecosystems and much of the breadth is community-driven -
verify the source and re-check quality before relying on a third-party quant in production.

<!-- item: fine-tuning -->
## Fine-tuning & adaptation

For the **Apache-2.0** models, standard **SFT/LoRA/QLoRA** via `transformers` / PEFT / TRL /
Axolotl / Unsloth on the safetensors checkpoints is the practical path, and the specialist
variants (Codestral, Mathstral, Devstral, Pixtral) demonstrate the family's adaptability. Because
the **pre-training data and code are not published**, continued pre-training *from scratch* is not
reproducible - this is fine-tuning of released weights rather than full-pipeline reproduction. Note the
EU AI Act provider implications of placing a derivative on the market (see Assess), and remember
that an **MRL** model may not be fine-tuned for commercial deployment without a negotiated licence.

<!-- item: integration -->
## API / OpenAI-compatible integration

Serve Mistral behind **vLLM's OpenAI-compatible `/v1` server** (or TGI/Ollama endpoints) for a
drop-in integration with existing OpenAI-client code, or use Mistral's own **La Plateforme** API:

```bash
vllm serve mistralai/Mistral-Small-3.2-24B-Instruct-2506 --revision <sha> --port 8000
# then point any OpenAI SDK at http://localhost:8000/v1
```

No model-specific client is required for the self-hosted path - the chat-completions surface
behaves like any other OpenAI-compatible endpoint, so routing, retries and gateways carry over
unchanged.

**If you use Mistral's hosted API instead of self-hosting, its data terms differ and you should
read them.** Per Mistral's Privacy Policy and help centre:

- **Training on your inputs is on by default** on Le Chat and the API unless you opt out (the
  "allow your interactions to be used to train our models" control); training does **not** apply
  to **Team and Enterprise** plans.
- **Retention:** the API keeps input/output for the time needed to generate the output and then
  **~30 rolling days**; Le Chat keeps them until you delete the conversation or your account.
- **Residency:** EU hosting by default (servers in the EU); an explicit **US API endpoint** hosts
  data in the US, with GDPR Article 46 Standard Contractual Clauses for non-EU processors.
- **Zero Data Retention (ZDR)** can be activated for eligible accounts.

Self-hosting the open weights avoids all of the above - the data never leaves your infrastructure.
