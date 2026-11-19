doc_type: model_card
entity: minicpm5
variant/applies-to: openbmb/MiniCPM5-1B (BF16 final release, post-trained with RL + OPD)
source_url: https://huggingface.co/openbmb/MiniCPM5-1B (raw README: https://huggingface.co/openbmb/MiniCPM5-1B/raw/main/README.md); repo sha ac83f813ba7da263c51a9f3ec37c2072597e54af, lastModified 2026-11-09T08:13:40Z, createdAt 2026-05-21T07:27:59Z
retrieval_date: 2026-11-19
exists: yes
retrieved: true

## Identity and architecture (verbatim)
"We are releasing **MiniCPM5-1B**, the first model in the **MiniCPM5** series. It is a dense 1B Transformer built for on-device, local deployment, and resource-constrained scenarios, reaching 1B-class open-source SOTA."
"**Architecture**: Standard `LlamaForCausalLM`"; "**Number of Parameters**: 1,080,632,832"; "**Number of Non-Embedding Parameters**: 679,552,512"; "**Number of Layers**: 24"; "**Number of Attention Heads (GQA)**: 16 for Q and 2 for KV"; "**Context Length**: 131,072"
"MiniCPM5-1B is designed for local assistants, coding agents, tool-use workflows, and reasoning scenarios where a compact model is preferred. The model keeps a small deployment footprint while providing native long-context support and both Think / No Think chat modes through the same checkpoint."
"**Hybrid Reasoning**: built-in `<think>` chat template, switch via `enable_thinking`."

## Model list (verbatim)
MiniCPM5-1B "BF16 final release (post-trained with RL + OPD)"; MiniCPM5-1B-SFT "BF16 SFT-only checkpoint (before RL / OPD)"; MiniCPM5-1B-Base "BF16 base checkpoint (pre-training only)"; MiniCPM5-1B-GGUF "GGUF for llama.cpp / Ollama / LM Studio"; MiniCPM5-1B-MLX "MLX / 4bit for Apple Silicon".

## Training recipe and data (verbatim)
"The training of MiniCPM5-1B is a full-stack practice of UltraData Tiered Data Management, covering three stages: base training, mid-training, and post-training."
"The training corpus is released alongside the model as Ultra-FineWeb, Ultra-FineWeb-L3, and UltraData-Math."
"We first use **200B tokens of deep-thinking SFT** and **200B tokens of hybrid-thinking SFT** ...; the SFT data is released as UltraData-SFT-2605. We then train specialized **RL teachers** for math, code, closed-book QA, writing, and related domains, and use **On-Policy Distillation (OPD)** to distill these teachers back into one release model."
"Reasoning RL is based on DAPO-Math-17k ... We also use TriviaQA, NQ-Open, LongWriter-Zero-RLData, synthesized verifiable RLVR data, and pair-wise RLHF signals to improve reliability, instruction following, and user experience."
"OPD reuses the in-domain prompts used to train each RL teacher as distillation data, so no additional data curation is required."
Not stated on the card: total pretraining token count, mid-training data composition (any code corpus is not named among the three released pretraining datasets), the synthesised RLVR data, the pairwise RLHF data, the teacher models used, any training-code repository, or a training compute figure.

## Evaluation claims (verbatim)
"We compare MiniCPM5-1B with strong open-source models in the same size class, including LFM2.5-1.2B-Thinking, Qwen3-0.6B/think and Qwen3.5-0.8B/think. ... within this comparison set, MiniCPM5-1B reaches 1B-class open-source SOTA, with its advantage most visible in tool use, code generation, and difficult reasoning." The numbers are in an image (see marketing__benchmarks__2026-11-19.md).

## Citation and report
The card's "MiniCPM Tech Report" link and BibTeX point to arXiv 2506.07900, which is the MiniCPM4 paper ("@article{minicpm4, title={Minicpm4: Ultra-efficient llms on end devices}"). No MiniCPM5-specific technical report is linked on the card.

## Tool calling, chat and sampling (verbatim)
"For tool / function calling, **SGLang is the recommended backend**. MiniCPM5-1B emits XML-style tool calls and SGLang's built-in `minicpm5` parser converts them to OpenAI-compatible `tool_calls` natively: python -m sglang.launch_server --model-path openbmb/MiniCPM5-1B --port 30000 --tool-call-parser minicpm5"
Recommended sampling: Think "temperature=0.9, top_p=0.95" with enable_thinking=True; No Think "temperature=0.7, top_p=0.95" with enable_thinking=False.
Install lines: "pip install "vllm>=0.21"", "pip install "sglang[srt]>=0.5.12"", "pip install -U "transformers>=5.6" accelerate torch"; "MiniCPM5-1B uses the standard LlamaForCausalLM architecture, so mainstream inference engines can load it directly: no custom kernels, no model-code fork."
Deployment matrix on the card: Transformers, vLLM, SGLang, llama.cpp, Ollama, LM Studio, MLX, ArcLight; fine-tuning: TRL + PEFT, LLaMA-Factory, ms-swift, unsloth, xtuner; multi-chip via FlagOS (Nvidia, Hygon, Metax, Iluvatar, Zhenwu, Mthreads, Kunlunxin, Ascend, ARM-v9) with FlagRelease repos under the FlagRelease org.

## Safety and limitations (verbatim, the whole section)
"## Limitations and Responsible Use / MiniCPM5-1B is a language model that generates content based on learned statistical patterns from training data. It may produce inaccurate, biased, or unsafe outputs, and generated content should be reviewed and verified before use in high-stakes settings. / Users are responsible for evaluating outputs, applying appropriate safeguards, and complying with applicable laws, regulations, and platform policies."
The card contains no safety evaluation, red-team result, refusal behaviour description, acceptable-use policy, guard model, or EU AI Act statement (searched for "safety", "harm", "refus", "guard", "alignment": only the limitations paragraph above matched).

## Languages
YAML header lists only "en" and "zh". No multilingual claim anywhere on the card; a Chinese README (README-cn.md) is provided. Training dataset cards (Ultra-FineWeb, L3, Math) are en and zh.

## Desktop pet (verbatim)
"We also ship OpenBMB/MiniCPM-Desk-Pet, a desktop pet driven locally by MiniCPM5-1B. It supports Apple Silicon / NVIDIA GPU / CPU paths ... and supports LoRA persona switching."
