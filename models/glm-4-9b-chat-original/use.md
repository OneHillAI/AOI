# Use - GLM-4-9B-Chat (original, glm-4 licence)

_What can it do? Capabilities, context window, chat template, languages, tool use, and
structured output live here._

<!-- item: capabilities -->
## Capabilities & modalities

A text chat / instruct 9B with general assistant and coding ability - capable for its mid-2024
vintage, dated by 2026.

<!-- item: context-window -->
## Context window & long-context behaviour

128K on GLM-4-9B-Chat; an advertised 1M-token context on GLM-4-9B-Chat-1M (memory-intensive in
practice). OneHill has not independently measured effective long-context recall, so treat the
figures as declared windows.

<!-- item: chat-template -->
## Prompt format & chat template

Ships a 2024-era GLM chat template - use `apply_chat_template` and confirm behaviour on your
serving stack, as the convention is older than the current GLM line.

<!-- item: languages -->
## Language coverage

Chinese and English are strongest; per-language depth varies and is not exhaustively
documented.

<!-- item: tool-use -->
## Function / tool calling

GLM-4-9B-Chat documented some tool-calling support at release, but the convention is older than
the current line. Confirm and test per serving stack.

<!-- item: structured-output -->
## Structured / JSON-constrained output

No model-documented native JSON/schema-constrained output guarantee. Constrained decoding is
available at the serving layer (vLLM grammars), a runtime feature of the server.
