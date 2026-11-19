# Implement - Mistral AI (open-weight family)

_Installation, hardware, serving, safe-deployment controls, quantisation, fine-tuning and integration._

<!-- item: install -->
## Install & run

Mistral checkpoints are standard safetensors on the verified `mistralai` org, and Mistral ships
an official inference library. Always pin an exact revision.

```python
# Hugging Face transformers.
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "mistralai/Mistral-Small-3.2-24B-Instruct-2506"  # Pick the exact variant to deploy.
rev = "<pinned-commit-sha>"                                    # Pin the revision; do not float on main.
tok = AutoTokenizer.from_pretrained(model_id, revision=rev)
model = AutoModelForCausalLM.from_pretrained(model_id, revision=rev)
```

```bash
# Official Mistral inference library.
pip install mistral-inference

# Ollama.
ollama run mistral-small

# vLLM (OpenAI-compatible server).
vllm serve mistralai/Mistral-Small-3.2-24B-Instruct-2506 --revision <sha>

# llama.cpp (community GGUF).
./llama-cli -m mistral-small-3.2.Q4_K_M.gguf -p "Hello"
```

Prefer safetensors, verify per-file checksums after download and confirm the model's licence.

<!-- item: hardware -->
## Hardware & VRAM requirements

Mistral 7B and Nemo 12B run comfortably on a single modern GPU, and a 24 GB card handles them
at full or near-full precision. Mistral Small 3.x (24B) fits a 24 GB card with modest
quantization. Mixtral 8x7B needs more VRAM than its ~13B active parameters suggest, because
all experts must be resident. Mixtral 8x22B and Mistral Large 2 (123B) need multi-GPU or heavy
quantization for latency-sensitive serving.

Size for the largest checkpoint to be served, and budget extra headroom for the KV cache at
128K context lengths.

<!-- item: serving -->
## Serving stacks

The checkpoints are plain safetensors with standard architectures, so mainstream runtimes load
them without custom code, and Mistral ships a first-party library.

| Stack | Use it for |
|---|---|
| mistral-inference | Mistral's official reference inference |
| vLLM | High-throughput serving and OpenAI-compatible API |
| TGI | Hugging Face-native production serving |
| llama.cpp | CPU, edge and GGUF quantized inference |
| Ollama | Local single-command runs |
| transformers | Prototyping and fine-tuning |

This breadth is a large part of why Operational Readiness scores 4. It stops short of 5 only
on the narrower official quantization programme.

<!-- item: safe-deployment -->
## Safe-deployment controls & Deployment Ceiling

The model-specific gate rows from the
[safe-deployment playbook](../../methodology/safe-deployment-playbook.md) are below.

- Supply chain: pin the exact `mistralai` revision hash and verify checksums. Prefer
  safetensors, which is already the default (no pickle load).
- Model layer: deploy the instruct variant, never the base checkpoint, and set conservative
  decoding defaults.
- Input and output layers: add input/output guardrails. The Mistral Moderation API (a
  fine-tuned Ministral 8B classifier) can serve as the companion filter, because Mistral ships
  no broadly distributed open guard-weight. Add prompt-injection defences and treat retrieved
  and tool content as untrusted.
- Compliance: confirm the per-model licence (Apache-2.0 or research-only MRL) before
  commercial deployment, and archive the copyright and training-content posture in the AI-BOM.

Deployment Ceiling: T2 (customer-facing, human-reviewed), conditional. With the instruct
variant, input/output guardrails, the Moderation classifier and prompt-injection defences,
Mistral reaches customer-facing, human-reviewed use. It is held at T2 because safety tuning is
lighter than at the largest labs and no broad independent red-team exists. T3+ (bounded
autonomous) additionally needs a deterministic action-policy engine, per-action human approval
for irreversible operations, and external guard tooling beyond what the release provides.

<!-- item: quantization -->
## Available quantizations

A broad community ecosystem of GGUF (llama.cpp, Ollama), AWQ, GPTQ and FP8 quantizations
circulates (bartowski, unsloth, lmstudio-community and others), and some official low-bit
releases exist. Coverage is partial because the first-party quantization programme is narrower
than the largest ecosystems and much of the breadth is community-driven. Verify the source and
check quality before relying on a third-party quant in production.

<!-- item: fine-tuning -->
## Fine-tuning & adaptation

For the Apache-2.0 models, standard SFT, LoRA and QLoRA via `transformers`, PEFT, TRL, Axolotl
or Unsloth on the safetensors checkpoints is the practical path. The specialist variants
(Codestral, Mathstral, Devstral, Pixtral) show the family's adaptability.

Pre-training data and code are not published, so continued pre-training from scratch cannot be
reproduced. Only the released weights can be fine-tuned. Placing a derivative on the market has
EU AI Act provider implications (see Assess). An MRL model may not be fine-tuned for commercial
deployment without a negotiated licence.

<!-- item: integration -->
## API / OpenAI-compatible integration

Serve Mistral behind vLLM's OpenAI-compatible `/v1` server (or TGI or Ollama endpoints) for a
drop-in integration with existing OpenAI-client code, or use Mistral's hosted API (Mistral
Studio, formerly La Plateforme).

```bash
vllm serve mistralai/Mistral-Small-3.2-24B-Instruct-2506 --revision <sha> --port 8000
# Then point any OpenAI SDK at http://localhost:8000/v1.
```

No model-specific client is required for the self-hosted path. The chat-completions surface
behaves like any other OpenAI-compatible endpoint, so routing, retries and gateways carry over
unchanged.

Mistral's hosted API has different data terms from self-hosting. They come from the Privacy
Policy (3 Sep 2026), the help centre, the Commercial Terms (25 Sep 2026) and the DPA
(27 Jul 2026).

Training depends on the product. Vibe Free, Pro, Teams and Student plans train on inputs by
default unless the user opts out, and Vibe Enterprise is opted out by default. Mistral Studio
Free mode may train, and pay-as-you-go customers can opt out (the default is not stated). Labs
and Public Preview models may always train, whatever was opted out. The Commercial Terms (4.2)
allow training only on an opt-in, on feedback, as an Order Form allows, or on Labs and Preview
models. DPA clause 2.3 lets Mistral train as controller unless the customer has opted out.

Retention: the API keeps input and output for the time needed to generate the output and then
30 rolling days to monitor abuse (unless ZDR is active). The Agents API keeps them until the
account is terminated, and Vibe keeps them until the user deletes the conversation or the
account.

Residency: hosting is in the EEA by default. An explicit US API endpoint processes requests in
the US, with GDPR Article 46 safeguards (Standard Contractual Clauses) for non-EU
sub-processors. The Module 4 SCCs in the DPA apply only to customers outside the EEA.

Zero Data Retention (ZDR) is available only on pay-as-you-go, for stateless API endpoints.
Mistral approves it at its discretion, and it does not cover Vibe, agents, conversations,
libraries, batch files or Labs and Preview models.

Self-hosting the open weights avoids all of this, because data never leaves the deployer's
infrastructure.
