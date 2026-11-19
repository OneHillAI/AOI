# Use - Meta Llama 3.x (Llama 3.1 / 3.3 text line)

_Capabilities, context window, chat template, languages, tool use and structured output._

<!-- item: capabilities -->
## Capabilities & modalities

Llama is a strong generalist for reasoning, summarisation, instruction-following, multilingual
chat and coding. The dense 3.1/3.3 line is text-only; the natively multimodal Llama 4 generation
is the separate llama-4 entry. Capability scales with size: the 8B is a capable lightweight
worker, while 70B/405B and the large MoE models approach frontier quality for open weights.

The main usage caveat is legal: the 700M-MAU trigger and the attribution terms of the Community
License.

<!-- item: context-window -->
## Context window & long-context behaviour

Llama 3.1 and 3.3 provide a 128K-token context window. Llama 4 Scout extends this to a very long
(multi-hundred-K+) window via its mixture-of-experts architecture. As with all long-context
models, recall is strongest near the prompt boundaries and softens in the middle of very long
inputs. Structure retrieval and place the most important material deliberately.

<!-- item: chat-template -->
## Prompt format & chat template

Llama Instruct models use the Llama 3 chat template, built from special tokens that delimit roles
and turns (a begin-of-text marker, `<|start_header_id|>role<|end_header_id|>` headers, and an
`<|eot_id|>` end-of-turn token). Do not hand-assemble these strings. Apply the tokenizer's
built-in chat template so the exact tokens and system/user/assistant structure are correct:

```python
from transformers import AutoTokenizer
tok = AutoTokenizer.from_pretrained("meta-llama/Llama-3.1-8B-Instruct")
msgs = [{"role": "system", "content": "You are helpful."},
        {"role": "user", "content": "Hello!"}]
prompt = tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)
```

Template mismatches are a common cause of degraded output; see the Support troubleshooting
notes.

<!-- item: languages -->
## Multilingual coverage

Meta officially supports eight core languages for the Llama 3.1 line: English, German, French,
Italian, Portuguese, Hindi, Spanish, and Thai. The model has broader informal competence in other
languages from pretraining, but only the eight are officially validated and covered by the
intended-use terms. Evaluate production use outside them for the specific language.

<!-- item: tool-use -->
## Function / tool calling

From Llama 3.1 onward, tool/function calling is a documented, first-party capability. The model
cards describe built-in tool formats and custom (JSON) tool calls, and the tokenizer's chat
template supports passing tool/function definitions. Serving stacks (vLLM, TGI, Ollama) surface
this through OpenAI-compatible `tools`/`tool_calls` fields. Tool-calling reliability varies with
model size, so validate outputs and treat any tool-triggered content as untrusted.
