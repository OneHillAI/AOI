# model_card / Jais-3-32B (representative card for the six Jais-3 weights repos)

source_url: https://huggingface.co/inception42/Jais-3-32B (raw: https://huggingface.co/inception42/Jais-3-32B/raw/main/README.md)
retrieval_date: 2026-11-19
doc_type: model_card
exists: yes
retrieved: true
tag: publisher
repo sha at retrieval: c87efc1f6d94b1f5152ba1d2220aa68cdcb5f4ed (last modified 2026-11-12)

NOTE (OneHill): the benchmark table (HTML) and the inline CSS are omitted below; everything else is the raw README text. The card has YAML front matter `license: apache-2.0` and NO "License" section in the body. It contains the sentence "Code repository | Coming soon" in the Artifact Index, while the technical report (Table 41) lists three GitHub code repositories; see technical_report and docs__github-code-repos files.

## Raw README (verbatim)
```
---
pipeline_tag: text-generation
library_name: transformers
model_name: Jais-3-32B
language:
- ar
- en
tags:
- jais-3
- 32B
- dense
- reasoning
license: apache-2.0
---

# Jais-3-32B

Jais-3-32B is the large dense member of the Jais-3 family: a 32B-class decoder-only model with a 512K context window.

> [!TIP]
> Other formats are available in the [IFM/Jais-3](https://huggingface.co/collections/IFM/jais-3-6abba9df4f1173ec7ce2929d) collection:
> - Quantization: [IFM/Jais-3-32B-FP8](https://huggingface.co/IFM/Jais-3-32B-FP8)
> - GGUF for llama.cpp and Ollama: [IFM/Jais-3-32B-GGUF](https://huggingface.co/IFM/Jais-3-32B-GGUF)
> - MLX for Apple silicon:
>   - [IFM/Jais-3-32B-MLX-4bit](https://huggingface.co/IFM/Jais-3-32B-MLX-4bit)
>   - [IFM/Jais-3-32B-MLX-8bit](https://huggingface.co/IFM/Jais-3-32B-MLX-8bit)
>   - [IFM/Jais-3-32B-MLX-bf16](https://huggingface.co/IFM/Jais-3-32B-MLX-bf16)

<p align="center">
  <a href="https://huggingface.co/inception42/Jais-3-32B/resolve/main/assets/jais-3-32b-benchmarks.png" target="_blank">
    <img src="assets/jais-3-32b-benchmarks.png" alt="Jais-3-32B benchmark results" width="100%">
  </a>
</p>

## Benchmark Results

<!-- TABLE:START -->
[BENCHMARK TABLE HTML OMITTED]
<!-- TABLE:END -->

> [!NOTE]
> Starred (\*) benchmarks have been audited for sample quality. Items with ambiguous questions, invalid answer options, or indefensible gold labels were excluded, since they can penalize a correct answer or reward a lucky guess. Scores on these benchmarks are reported on the cleaned sets. The audit methodology, the excluded samples and the verified benchmarks are available in the [IFM/Arabic-Benchmark-Auditing](https://huggingface.co/collections/IFM/arabic-benchmark-auditing-6ac7711f28fbb54bc6c8caaa) collection.

> [!NOTE]
> Benchmarks marked with ^ will be released by IFM soon.


## Quickstart

### Serving


vLLM (`vllm>=0.30.0`) · [vLLM recipe](https://recipes.vllm.ai/IFM/Jais-3-32B):

```shell
vllm serve inception42/Jais-3-32B \
  --trust-remote-code \
  --model-impl vllm \
  --dtype bfloat16 \
  --tensor-parallel-size 2 \
  --reasoning-parser k2_horizon \
  --enable-auto-tool-choice \
  --tool-call-parser k2_horizon
```
Use an exact branch name from the inventory with vLLM's `--revision` option.

SGLang (`sglang>=0.5.20`) · [SGLang recipe](https://docs.sglang.io/cookbook/autoregressive/IFM/Jais-3):

```shell
sglang serve \
  --model-path inception42/Jais-3-32B \
  --tp 2 \
  --dtype bfloat16 \
  --attention-backend fa3 \
  --reasoning-parser k2_horizon \
  --host 0.0.0.0 \
  --port 30000 \
  --tool-call-parser k2_horizon
```

### API Usage
> [!TIP]
> Recommended settings: `reasoning_effort="high"`, the sampling hyperparameters in the table below, and at least 32,768 output tokens.
> Reasoning depth is selected per request through `chat_template_kwargs`. Thinking is returned in `reasoning_content` and the answer in `content`.

| Parameter | Default | Thinking mode, English | Thinking mode, Arabic |
|---|---|---|---|
| `temperature` | 0.2 | 1.0 | 0.7 |
| `top_p` | 0.95 | 0.95 | 0.95 |
| `top_k` | 20 | 20 | 20 |



<div class="tabsA">
<input type="radio" name="tabsA" id="a1" checked>
<input type="radio" name="tabsA" id="a2">
<div class="barA"><label for="a1">Reasoning Example</label><label for="a2">Tool Calling Example</label></div>
<div class="pA p1">

```python
from openai import OpenAI
client = OpenAI(base_url="http://localhost:30000/v1", api_key="EMPTY")
response = client.chat.completions.create(
    model="inception42/Jais-3-32B",
    messages=[{"role": "user", "content": "لدينا عددان مجموعهما 50 وحاصل ضربهما 600. ما هما العددان؟ اشرح خطوات الحل."}],
    temperature=0.7,
    top_p=0.95,
    max_tokens=32768,
    extra_body={"top_k": 20, "chat_template_kwargs": {"reasoning_effort": "high"}},
)
message = response.choices[0].message
print("Reasoning:", getattr(message, "reasoning_content", None))
print("Answer:", message.content)
```

</div>
<div class="pA p2">

```python
import json
from datetime import datetime
from zoneinfo import ZoneInfo
from openai import OpenAI
client = OpenAI(base_url="http://localhost:30000/v1", api_key="EMPTY")
TIMEZONES = {"أبوظبي": "Asia/Dubai", "الرياض": "Asia/Riyadh", "القاهرة": "Africa/Cairo", "لندن": "Europe/London"}

def get_current_time(city: str) -> dict:
    if city not in TIMEZONES:
        return {"error": f"مدينة غير معروفة: {city}"}
    return {"city": city, "time": datetime.now(ZoneInfo(TIMEZONES[city])).strftime("%H:%M")}

tools = [{
    "type": "function",
    "function": {
        "name": "get_current_time",
        "description": "يعيد الوقت الحالي في مدينة معينة",
        "parameters": {
            "type": "object",
            "properties": {"city": {"type": "string", "description": "اسم المدينة بالعربية"}},
            "required": ["city"],
        },
    },
}]
available_tools = {"get_current_time": get_current_time}
messages = [{"role": "user", "content": "كم الساعة الآن في القاهرة؟"}]
for _ in range(5):  # call the model, run any requested tools, repeat until it answers
    message = client.chat.completions.create(
        model="inception42/Jais-3-32B",
        messages=messages,
        tools=tools,
        temperature=0.7,
        top_p=0.95,
        max_tokens=32768,
        extra_body={
            "top_k": 20,
            "chat_template_kwargs": {"reasoning_effort": "high", "tool_call_format": "xml"},
        },
    ).choices[0].message
    messages.append(message)
    if not message.tool_calls:
        break
    for call in message.tool_calls:
        tool = available_tools.get(call.function.name)
        arguments = json.loads(call.function.arguments)
        result = tool(**arguments)
        messages.append({"role": "tool", "tool_call_id": call.id,
                         "content": json.dumps(result, ensure_ascii=False)})

print(message.content)
```

</div>
</div>

Our model supports multiple tool-call formats, which can be changed with `chat_template_kwargs`. The supported values are `json`, `xml`, and `xml_typed`. The default is `xml`. Keep `--tool-call-parser k2_horizon` enabled to parse the selected format.


### Transformers

Validated with Transformers 5.15.0, PyTorch 2.13.0, Safetensors 0.8.0.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
model_id = "inception42/Jais-3-32B"
tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_id, device_map="auto", dtype="bfloat16", low_cpu_mem_usage=True, trust_remote_code=True
)
inputs = tokenizer("لدينا عددان مجموعهما 50 وحاصل ضربهما 600. ما هما العددان؟ اشرح خطوات الحل.", return_tensors="pt").to(model.device)
inputs.pop("token_type_ids", None)
outputs = model.generate(**inputs, max_new_tokens=32768, temperature=0.7, top_p=0.95, top_k=20, do_sample=True)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

## Release Artifacts

The table below lists the release artifacts for **Jais-3-32B**.

### Artifact Index

| Artifact | Link |
| --- | --- |
| Model card | [Hugging Face](https://huggingface.co/inception42/Jais-3-32B) |
| Training logs | [W&B](https://forge.coreweave.com/wandb/mbzuai-llm/Jais-3-32B) |
| Blog post | [Jais 3: Introducing Arabic-centric Agentic AI](https://ifm.ai/blog/jais3/) |
| Checkpoints | [Checkpoint inventory](#checkpoint-inventory) |
| Technical report | [Jais 3 Technical Report](https://ifm.ai/jais/tech-report) |
| Code repository | Coming soon |

### Checkpoint Inventory

**Model repository:** [inception42/Jais-3-32B](https://huggingface.co/inception42/Jais-3-32B)

Branch names below refer to this repository.

| Checkpoint | Branch / repository |
| --- | --- |
| CPT Checkpoint | `CPT` |
| Cooldown Checkpoint | `Cooldown` |
| FTPO Checkpoint | `FTPO` |
| SFT Checkpoint | `SFT` |

## Best Practices

1. **Reasoning effort: always `high`.** All reported results use high reasoning effort. Pass `{"chat_template_kwargs": {"reasoning_effort": "high"}}` on every request. No reasoning (`{"reasoning_effort": "low"}`) is not recommended except for research on reasoning efforts.
2. **Sampling parameters.** Use the values in the table above: `temperature=0.2`, `top_p=0.95`, `top_k=20` by default. In thinking mode, set `temperature=1.0` for English and `temperature=0.7` for Arabic. Keep `min_p=0.0`, `presence_penalty=0.0` and `repetition_penalty=1.0`.
3. **Serving.** Use the validated SGLang recipe above: BF16, TP=2 on a single H100 node, FlashAttention-3.
4. **Parsers.** Enable the `k2_horizon` reasoning parser for chat, and add the `k2_horizon` tool-call parser for agent use. Leave both off for plain completion-style generation.

## Intended Use and Limitations

**Intended use:** The model is designed for Arabic and English assistant and agentic applications, including reasoning and tool-use tasks, as well as for research and experimentation.

**Out of scope:** The model should not be used in ways that violate applicable laws or regulations. The following uses are also considered out of scope:

- **Harmful or malicious use:** generating hateful, extremist, discriminatory, or deliberately misleading content, or using the model to support illegal or harmful activities.
- **Sensitive information:** using the model to generate, expose, or infer personal, confidential, or otherwise sensitive information about individuals or organizations.
- **Unsupported languages:** applications that depend on reliable performance in languages other than Arabic or English.
- **High-stakes decisions:** relying on the model to make medical, legal, financial, or safety-critical decisions without appropriate human oversight.

**Limitations:** The model can produce inaccurate or made-up content and may reflect biases present in its training data. Evaluate it for your use case and add safeguards before deploying it.

## Citation

```bibtex
@misc{ifm2026jais3introducingarabiccentric,
      title={Jais 3: Introducing Arabic-centric Agentic AI},
      author={Team IFM and Haonan Li and Hadi Abdine and Nikhil Ranjan and Mohamed Anwar and Ahmad Chamma and Amr Mohamed and Ahmed Frikha and Dani Bouch and Maaz Maqsood and George Ibrahim and Mostafa Awad and Nurkhan Laiyk and Hasan Iqbal and Abhishek Maiti and Bilal Bouardi and Shivam Chauhan and Ahmer Tabassum and Owais Aijaz and Omar Arbi and Neha Sengupta and Aaryamonvikram Singh and Abdelhakim Freihat and Sarath Chandran and Rahul Pal and Mohammed Bellam and Sajid Siddiki and Sarah AlBarri and Debopriyo Banerjee and Ali El Filali and Samta Kamboj and Rifo Genadi and Ahmed Attia and Go Inoue and Shuonan Dong and Amine Khelif Khelif and Evan Dufraisse and Florian Valade and Tapas Sen and Guowei He and Sunil Sahu and Onkar Pandit and Kareem Magdy and Sheikh Khalid bin Khalifa Al Nahyan and Samujjwal Ghosh and Zainul Abedien and Ahmed Quraishi and Larry Murray and Avraham Sheinin and Natalia Vassilieva and Preslav Nakov and Guokan Shang and Xuguang Hector Ren and Zhengzhong Liu and Eric Xing},
      year={2026},
      eprint={2611.10224},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2611.10224},
}
```

```
