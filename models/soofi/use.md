# Use - Soofi (Soofi-S)

_What can it do and how do we use it well? Capabilities, context window, chat template,
languages, and native tool-use; structured output is a current gap._

<!-- item: capabilities -->
## Capabilities & modalities

Soofi-S is a **text-only** language model built for **German and English** generation, code, and
technical/agentic tasks in industrial and regulated settings. Per the pretraining report and
independent coverage (`ev-arxiv`, `ev-perf`), it is the **strongest fully-open model on aggregate
English and German benchmarks** - ahead of OLMo 3 32B, Apertus 70B, EuroLLM 22B and Alia 40B - and
wins the **code aggregates** in both languages among open base models, all while activating only
~3B of 30B parameters per token. Choose Soofi-S when European sovereignty, auditability, German-language
strength and long-context economics matter; it is a leading *open* model rather than a
frontier-vs-closed contender.

<!-- item: context-window -->
## Context window & long-context behaviour

Soofi-S supports contexts **up to 256k tokens**, and its hybrid Mamba-2 design keeps decode
throughput **flat from 4k to 256k** (a near-constant inference cache) - a genuine differentiator for
long-document and high-concurrency workloads. This item is marked *partial* because effective
long-context recall at full length is not independently benchmarked; treat 256k as the architectural
ceiling rather than a verified quality guarantee at full length.

<!-- item: chat-template -->
## Prompt format & chat template

The **Instruct-Preview** variant ships an **embedded Jinja chat template** (its default system
prompt carries only a knowledge cutoff and date - no identity text). Apply it rather than
hand-rolling role markers:

```python
messages = [
    {"role": "system", "content": "Du bist ein hilfreicher Assistent."},
    {"role": "user", "content": "Fasse das folgende Dokument zusammen ..."},
]
prompt = tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
```

With GGUF, run `llama-server --jinja` so the embedded template (identity **and** tools) is applied
verbatim. The **base** checkpoint has **no** chat template - it is a plain text-completion / fine-tuning
model and should not be prompted as a chat assistant.

<!-- item: languages -->
## Language coverage

Soofi-S is a genuine **bilingual German + English** model: German was **deliberately up-weighted** in
the ~27T-token training mix, and both languages are first-class supported targets (this is the
model's core design goal rather than incidental coverage). Other languages may appear but are not a
supported target - evaluate per-language before relying on Soofi-S outside German/English.

<!-- item: tool-use -->
## Function / tool calling

Soofi-S has a **native tool-call format embedded in the Instruct GGUF's Jinja template**. To use it
reliably, run under **`llama-server --jinja`**, which applies the model's own identity-and-tools
template verbatim. Be aware that **Ollama's template intentionally omits the tool portion**, so
tool calling there falls back to prompt scaffolding - this is why the item is marked *partial*: the
capability exists and is documented, but its behaviour depends on which runtime template your stack
applies.

<!-- structured-output is a `gap` item - no native JSON/schema-constrained output is documented for
     Soofi-S; constrained decoding is a serving-layer feature (vLLM/llama.cpp grammars). See gap_reason. -->
