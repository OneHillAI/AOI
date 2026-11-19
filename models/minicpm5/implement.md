# Implement - MiniCPM5-1B

_Installation, hardware, serving, safe-deployment controls, quantisation, fine-tuning and integration._

<!-- item: install -->
## Install & run

Pull the weights from the Hub and pin the revision. The card's three routes (`ev-card`):

```bash
pip install "vllm>=0.21" && vllm serve openbmb/MiniCPM5-1B --port 8000
pip install "sglang[srt]>=0.5.12" && python -m sglang.launch_server --model-path openbmb/MiniCPM5-1B --port 30000
pip install -U "transformers>=5.6" accelerate torch   # then AutoModelForCausalLM.from_pretrained("openbmb/MiniCPM5-1B")
```

For laptops and phones use the official GGUF with llama.cpp (the GGUF card documents `llama serve -hf openbmb/MiniCPM5-1B-GGUF`, which downloads Q4_K_M) or the official MLX 4-bit on Apple Silicon. The version floors are recent; older vLLM and transformers releases may not load it. Verify the LFS sha256 against the repository listing (`ev-repo-files`).

<!-- item: hardware -->
## Hardware & VRAM requirements

The publisher gives file sizes, not device benchmarks (`ev-repo-files`, `ev-github`): BF16 safetensors 2.16 GB; GGUF F16 2.17 GB, Q8_0 1.15 GB, Q4_K_M 0.69 GB (the cookbook rounds this to 657 MB); MLX 4-bit 0.61 GB. The KV cache is small because there are only 2 key-value heads. By arithmetic from config.json (24 layers x 2 heads x 128 head dim x 2 tensors x 2 bytes) it is 24,576 bytes per token, about 3.2 GB at the full 131,072 tokens in 16-bit. On a small device cap the context; the cookbook's llama-server example uses `-c 8192`. No RAM, speed or battery figures for named phones or boards are published, so measure on your target.

<!-- item: serving -->
## Serving stacks

The model is a standard `LlamaForCausalLM`, and the card says "no custom kernels, no model-code fork" are needed (`ev-card`). The card and repository provide cookbooks for Transformers, vLLM, SGLang (recommended for tool calling), llama.cpp, Ollama, LM Studio, MLX, ArcLight, LiteRT-LM (a `.litertlm` runtime for Android, iOS, desktop and IoT) and vLLM Ascend (`ev-github`). The card also lists FlagOS multi-chip builds for Nvidia, Hygon, Metax, Iluvatar, Zhenwu, Mthreads, Kunlunxin, Ascend and ARM-v9, published under the separate FlagRelease org. The ollama.com library page for minicpm5 does not exist (404); the cookbook uses a local Modelfile (`ollama create minicpm5-1b -f Modelfile`).

<!-- item: safe-deployment -->
## Safe-deployment controls & Deployment Ceiling

Deployment Ceiling: T1 (internal assistant), conditional. Humans read the output, and the deployer writes the acceptable-use policy, because the publisher provides neither a policy nor a safety evaluation (`ev-card`). T2 and above need controls the deployer must build:

- Use the final MiniCPM5-1B checkpoint and not Base for any assistant. SFT-only is a research stage.
- Run safety and refusal tests in the languages served, and add input and output guardrails or a separate classifier. None is released with the model.
- Treat tool calls as untrusted model output: parse with SGLang's `minicpm5` parser or the repo's tool parser, validate arguments and allow-list actions.
- Pin the revision and verify the sha256. Avoid unreviewed community conversions, some of which are named "Uncensored".
- Test long-context behaviour, because no long-context result is published for the 1B.

<!-- item: quantization -->
## Available quantizations

Official: GGUF in F16, Q8_0 and Q4_K_M, and an MLX 4-bit conversion (`ev-repo-files`). The repository also ships AWQ, GPTQ and bitsandbytes quantisation scripts with an evaluation script (`ev-github`). The later 2B release adds official GPTQ and speculative-decoding drafts; the 1B has none of those from the publisher. The card gives no quality-loss numbers for the 1B quantisations beyond the cookbook description of Q8_0 as "very small quality drop vs F16". Many community quantisations exist (MLX, AWQ, NVFP4, ONNX, MNN, LiteRT-LM); they are not publisher-verified.

<!-- item: fine-tuning -->
## Fine-tuning & adaptation

Apache-2.0 allows fine-tuning and redistribution. The Base and SFT-only checkpoints are published alongside the final one. Cookbooks and agent skills cover TRL with PEFT (LoRA and SFT), LLaMA-Factory, ms-swift, unsloth and xtuner; the repository also has finetune scripts including an MLX trainer (`ev-card`, `ev-github`). The desk-pet demo uses LoRA persona switching. The public pretraining datasets allow continued pre-training on the published mix. The SFT dataset needs a Hub login and gate acceptance (`ev-sft-dataset`). RL and OPD are described but their pipelines are not released.

<!-- item: integration -->
## API / OpenAI-compatible integration

`vllm serve` and the SGLang server both expose `/v1/chat/completions`. For tool calling the card says SGLang is recommended: start it with `--tool-call-parser minicpm5` (or `auto`) and the model's XML-style calls come back as OpenAI-compatible `tool_calls` (`ev-card`). The card gives mode-specific sampling: temperature 0.9 and top_p 0.95 for Think, 0.7 and 0.95 for No Think.
