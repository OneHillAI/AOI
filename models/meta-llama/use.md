# Use - Meta Llama (Llama 3.x / Llama 4)

_What can it do and how do we use it well? Capabilities, context window, prompt/chat
template, languages, tool-use, structured output._

<!-- item: capabilities -->
## Capabilities & modalities

Llama is a strong **generalist**: reasoning, summarisation, instruction-following,
multilingual chat, and capable **coding**. The dense 3.1/3.3 line is text-only;
the **Llama 4** generation is natively **multimodal**, accepting images alongside text.
The key usage caveat is legal rather than technical: the multimodal Llama models are **not
licensed to EU-domiciled entities**, so EU adopters should restrict themselves to the
text-only checkpoints. Across the family, capability scales with size - the 8B is an
excellent lightweight worker, while 70B/405B and the large MoE models close in on frontier
quality for open weights.

<!-- item: context-window -->
## Context window & long-context behaviour

Llama 3.1 and 3.3 provide a **128K-token** context window. **Llama 4 Scout** extends this
dramatically to a **very long (multi-hundred-K+)** window via its mixture-of-experts
architecture. As with all long-context models, effective recall is strongest near the
prompt boundaries and softens in the middle of very long inputs, so structure retrieval
and place the most important material deliberately rather than relying on uniform recall.

<!-- item: chat-template -->
## Prompt format & chat template

Llama Instruct models use the **Llama 3 chat template**, built from special tokens that
delimit roles and turns (a begin-of-text marker, `<|start_header_id|>role<|end_header_id|>`
headers, and an `<|eot_id|>` end-of-turn token). Do **not** hand-assemble these strings -
apply the tokenizer's built-in chat template so the exact tokens and system/user/assistant
structure are correct:

```python
from transformers import AutoTokenizer
tok = AutoTokenizer.from_pretrained("meta-llama/Llama-3.1-8B-Instruct")
msgs = [{"role": "system", "content": "You are helpful."},
        {"role": "user", "content": "Hello!"}]
prompt = tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)
```

Template mismatches are one of the most common causes of degraded output - see the Support
troubleshooting notes.

<!-- item: languages -->
## Multilingual coverage

Meta officially supports **eight core languages** - English, German, French, Italian,
Portuguese, Hindi, Spanish, and Thai - for the Llama 3.1 line. The model has broader
*informal* competence in other languages from its pretraining, but only the eight are
officially validated and covered by the intended-use terms; production use outside them
should be evaluated for the specific language.

<!-- item: tool-use -->
## Function / tool calling

From **Llama 3.1** onward, tool/function calling is a documented, first-party capability.
The model cards describe both built-in tool formats and **custom (JSON) tool calls**, and
the tokenizer's chat template supports passing tool/function definitions. Serving stacks
(vLLM, TGI, Ollama) surface this through OpenAI-compatible `tools`/`tool_calls` fields.
Tool-calling reliability still varies with model size - validate outputs and treat any
tool-triggered content as untrusted.
