# Use - Mistral (research / non-production licence)

_What can it do? Capabilities, context window, chat template, languages, tool use, and
structured output live here._

<!-- item: capabilities -->
## Capabilities & modalities

Strong instruct (Ministral 8B, Mistral Large 2), code (Codestral), and multimodal image+text
(Pixtral Large) capability - among Mistral's most capable models, usable in research/
non-production settings.

<!-- item: context-window -->
## Context window & long-context behaviour

128K on the instruct/multimodal models, 32K on Codestral per the cards. OneHill has not
independently measured effective long-context recall, so treat these as declared windows.

<!-- item: chat-template -->
## Prompt format & chat template

Mistral instruct templates (the newer models use the tekken tokenizer). Use
`apply_chat_template` and confirm the tokenizer per model - it changed across generations.

<!-- item: languages -->
## Language coverage

Strong European-language coverage (a Mistral strength) alongside English; per-language depth
varies by model.

<!-- item: tool-use -->
## Function / tool calling

The instruct models support function / tool calling via the Mistral schema. Confirm and test
per serving stack.

<!-- item: structured-output -->
## Structured / JSON-constrained output

Mistral documents JSON / structured-output modes on its platform. Self-hosted, constrained
decoding is a serving-layer feature (vLLM grammars), not a model guarantee.
