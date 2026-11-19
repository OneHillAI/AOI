# Use - Luciole 1.1 Instruct (23B, 8B, 1B)

_Capabilities, context window, chat template, languages, tool use and structured output._

<!-- item: capabilities -->
## Capabilities & modalities

Text only. The post-training data covers maths, science, coding, general chat, RAG and translation (`ev-card-instruct`, `ev-posttrain-data`). The publisher's figure shows strong instruction following, with the best ifeval and ifeval-fr scores of the five models compared (`ev-bench`).

Maths and general chat trail Mistral-Small-3.2 in the same figure. The card says code and maths need additional training. All numbers are the publisher's.

<!-- item: context-window -->
## Context window & long-context behaviour

The configuration sets `max_position_embeddings` to 131,072. The base model reached that window through two 50-billion-token extension phases, to 32,768 and then 131,072 tokens (`ev-card-base`). Post-training used 16,384-token sequences, and the card says the Instruct model was trained on shorter sequences than its base (`ev-card-instruct`).

The base card reports RULER results. No long-context result is published for the Instruct models. Test your own long prompts before relying on the window.

<!-- item: chat-template -->
## Prompt format & chat template

The template follows the ChatML layout, which the card says is inspired by Qwen3-1.7B. A default system prompt reads "You are a helpful AI assistant named Luciole, trained by LINAGORA and OpenLLM France." Turns look like this (`ev-card-instruct`):

```
<|im_start|>system
You are a helpful AI assistant named Luciole, trained by LINAGORA and OpenLLM France.<|im_end|>
<|im_start|>user
Who was Molière?<|im_end|>
<|im_start|>assistant
```

Use `tokenizer.apply_chat_template(..., add_generation_prompt=True)`, which reads `chat_template.jinja`. The end token is `<|im_end|>` (id 261 in `generation_config.json`).

<!-- item: languages -->
## Language coverage

The Instruct cards list French and English. Post-training data is almost entirely English, with French from Nemotron multilingual maths (80K in the thinking mix), Paradocs and Croissant translation sets, and about 2,000 hard-coded identity prompts. The safety pairs cover English, French, German, Spanish and Italian (`ev-posttrain-data`).

The base card lists the pretraining shares: English 41.9%, French 30.4%, German 3.8%, Spanish 3.5%, Italian 1.9%, Portuguese 1.3%, Dutch 1.0%, Arabic 0.5%, and 0.4% for regional languages and French creoles (`ev-card-base`). The Base model was evaluated on German, Spanish, Italian, Portuguese, Dutch and Arabic. The Instruct card makes no claim for those languages.

<!-- item: tool-use -->
## Function / tool calling

vLLM's hermes parser turns tool calls into `message.tool_calls`. The training mix includes xlam, hermes, When2Call and smolagents data (`ev-posttrain-data`). The card warns that tool use is work in progress and links BFCL v4 charts on the 1B repo (`ev-card-instruct`). Treat tool calling as unproven on your tools until you test it.

<!-- structured-output is a `gap` item - no JSON or schema-constrained output is documented. -->
