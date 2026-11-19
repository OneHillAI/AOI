# Implement - Gemma 4 (E2B, E4B, 12B, 26B A4B, 31B)

_Installation, hardware, serving, safe-deployment controls, quantisation, fine-tuning and integration._

<!-- item: install -->
## Install & run

The weights are ungated, so no Hugging Face login or approval is needed (`ev-hf-inventory`).
Pin an exact revision and verify the LFS checksums after download.

```python
# Hugging Face transformers (from the model card)
from transformers import AutoProcessor, AutoModelForMultimodalLM

MODEL_ID = "google/gemma-4-31B-it"      # or -26B-A4B-it, -12B-it, -E4B-it, -E2B-it
processor = AutoProcessor.from_pretrained(MODEL_ID, revision="<pinned-commit-sha>")
model = AutoModelForMultimodalLM.from_pretrained(
    MODEL_ID, revision="<pinned-commit-sha>", dtype="auto", device_map="auto"
)
```

```bash
# Ollama (tags e2b, e4b, 12b, 26b, 31b)
ollama run gemma4
```

For llama.cpp or LM Studio use the official `-qat-q4_0-gguf` repositories; for vLLM or SGLang
use `-qat-w4a16-ct` (`ev-docs-overview`, `ev-ollama`). The model card says to use the latest
Transformers release (`ev-card-31b`).

<!-- item: hardware -->
## Hardware & VRAM requirements

Google's overview page gives approximate weight-load memory including 20 percent overhead
(`ev-docs-overview`):

| Size | BF16 | 8-bit | Q4_0 |
|---|---|---|---|
| 31B dense | 69.9 GB | 34.9 GB | 17.5 GB |
| 26B A4B (all 25.2B parameters resident) | 57.7 GB | 28.8 GB | 14.4 GB |
| 12B Unified | 26.7 GB | 13.4 GB | 6.7 GB |
| E4B | 17.9 GB | 8.9 GB | 4.5 GB |
| E2B | 11.4 GB | 5.7 GB | 2.9 GB |

The E2B and E4B also have mobile builds (E2B 1.1 GB, E4B 2.5 GB in the table's mobile column). These figures cover weights only. The KV cache at 128K to 256K context comes on top, and fine-tuning needs far more. The launch blog says the 31B BF16 weights fit one 80 GB H100
(`ev-blog`). The 26B A4B runs at roughly 4B-parameter speed but needs memory for all 26B.

<!-- item: serving -->
## Serving stacks

| Stack | Used for |
|---|---|
| Transformers | Reference loading, prototyping, fine-tuning |
| vLLM / SGLang | High-throughput serving with the official w4a16 compressed-tensors builds |
| llama.cpp / LM Studio | Local and CPU use with the official q4_0 GGUF builds |
| Ollama | Single-command local runs for all five sizes (`ev-ollama`) |
| LiteRT-LM | Mobile builds named by Google (`ev-docs-overview`) |

Speculative decoding uses the matching `-assistant` drafter with a quantised main model
(`ev-docs-overview`). The launch blog lists further day-one stacks (MLX, NVIDIA NIM, Unsloth, Docker and others). That list is a publisher claim and is unchecked (`ev-blog`).

<!-- item: safe-deployment -->
## Safe-deployment controls & Deployment Ceiling

The model-specific gate rows follow the [safe-deployment playbook](../../methodology/safe-deployment-playbook.md):

- Pull from the verified `google` organisation only, pin the revision and verify checksums. Prefer Google's own QAT repositories to community quants.
- Deploy an instruction-tuned checkpoint. Use the card's sampling settings (temperature 1.0, top_p 0.95, top_k 64) and strip thinking content from history.
- Add your own guardrails and a guard classifier. No Gemma 4 guard model has been identified, and the publisher safety evidence is qualitative (`ev-tech-report`).
- No Prohibited Use Policy binds the weights, so enforce your own at the application layer.
- Test image, audio and video paths separately. Limits are 30 seconds of audio and 60 seconds of video at one frame per second (`ev-card-31b`).
- Record in the AI-BOM that the training summary states user data from Google products and Gemini 3 synthetic data were used (`ev-eu-summary`).

Deployment Ceiling: T2 (customer-facing, human-reviewed), conditional. With an instruction-tuned checkpoint, your own guardrails and per-language, per-modality evaluation, Gemma 4 reaches customer-facing, human-reviewed use. T3 and above need a deterministic action-policy engine and independent safety evidence that does not yet exist for this release.

<!-- item: quantization -->
## Available quantizations

Google publishes official quantisation-aware-trained checkpoints in the `google` organisation,
all Apache-2.0 and ungated (`ev-docs-overview`, `ev-hf-inventory`, `ev-tech-report`):

- `-qat-q4_0-gguf` for llama.cpp and LM Studio (all five sizes);
- `-qat-w4a16-ct` compressed-tensors for vLLM and SGLang (E2B, E4B, 12B, 31B);
- `-qat-mobile-ct` and `-qat-mobile-transformers` for edge devices;
- `-qat-q4_0-unquantized` half-precision QAT weights for converting to other formats such as
  MLX, plus `-assistant` drafters for speculative decoding.

Test quality for your language and task after any quantisation.

<!-- item: fine-tuning -->
## Fine-tuning & adaptation

Fine-tune the base or `-it` checkpoints with Transformers or Google's JAX library (`ev-gemma-lib`). The 12B Unified model is encoder-free, so the whole model can be tuned in one pass (`ev-card-31b`). Fine-tuning needs the right end token: base models end with `<eos>`, instruction-tuned models with `<turn|>` (`ev-tech-report`).

Modifications may be licensed on the deployer's own terms, but redistribution requires shipping the Apache-2.0 text, marking changed files and keeping notices (`ev-license`). A Gemma 3 derivative, by contrast, has to carry the Gemma Terms and the Prohibited Use Policy (see Assess, license item). Placing a derivative on the EU market may make the deployer its provider under the AI Act.

<!-- item: integration -->
## API / OpenAI-compatible integration

The named servers (vLLM, SGLang, Ollama, LM Studio, llama.cpp server) expose chat endpoints, but OpenAI-compatible serving of Gemma 4 is not documented in a primary document, so coverage is partial. Test tool-call round trips and thinking-mode output through the gateway. The chat template drives tool calls and thinking blocks, and it has had several fixes since release (`ev-hf-scan`). Keep thinking content out of conversation history except on tool-call turns (`ev-card-31b`).
