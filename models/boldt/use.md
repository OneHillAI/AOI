# Use - Boldt-DC (350M and 1B base models)

_Capabilities, context window, chat template, languages, tool use and structured output._

<!-- item: capabilities -->
## Capabilities & modalities

Text only. Both models continue German text. Reported scores sit at the low end for knowledge and reading tasks: MMLU 29.29 and 31.06, ARC-Easy 52.87 and 57.30 (`ev-card-1b`, `ev-paper`). There is no instruction following, retrieval or code claim. Fine-tune before use in an assistant or a RAG pipeline.

<!-- item: context-window -->
## Context window & long-context behaviour

The context is 2,048 tokens. The config's `max_position_embeddings` and the tokenizer's `model_max_length` agree, and the publisher makes no long-context claim (`ev-card-1b`, `ev-card-350m`).

<!-- item: chat-template -->
## Prompt format & chat template

There is no chat template. The cards say to use plain text completion. End of text is `<|endoftext|>` (id 0) and padding is `<|pad|>` (id 1) (`ev-card-1b`, `ev-card-350m`).

<!-- item: languages -->
## Language coverage

German only. The models were trained on the `deu_Latn` split of FineWeb-2 with a German 32k BPE tokenizer. The paper studied German alone and tests no other language (`ev-paper`, `ev-dataset`). The cards claim no English or other-language ability, and none has been measured.

<!-- tool-use is a `gap` item: base models, no tool-calling capability documented. -->

<!-- structured-output is a `gap` item: base models, no structured-output capability documented. -->
