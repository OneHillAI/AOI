# Use - MORENA 1.5B (base and instruct)

_What can it do and how do we use it well? Capabilities, context window, chat template and
languages; structured output is a gap._

<!-- item: capabilities -->
## Capabilities & modalities

Text only. The measured strengths are African-language modelling (lowest bits per byte of 26
models in the paper) and English-to-African translation (chrF++ 45.8 across five languages,
3-shot), plus code and French inherited from the mixture. Weak spots are comprehension (Belebele
0.309, retrieval QA 0.325 against a 0.25 floor), grounded faithfulness (23%), English knowledge
(MMLU 0.284, deliberately traded away) and over-refusal. Use it where its tokenizer and
language modelling matter: the paper reports that African text costs 1.39 times fewer tokens than
under Gemma 3's vocabulary and 1.53 times fewer than under Llama 3.2's (`ev-paper`). All figures
are the publisher's own.

<!-- item: context-window -->
## Context window & long-context behaviour

4,096 tokens, stated on the card and the paper, and consistent across `config.json`
(`seq_len` 4096), `tokenizer_config.json` (`model_max_length` 4096) and the GGUF header read by
Hugging Face (`ev-card-instruct`, `ev-hf-platform`). No long-context training or evaluation is
described. Chunk or retrieve instead of stuffing documents, and note that retrieval QA is itself
near chance.

<!-- item: chat-template -->
## Prompt format & chat template

Turns are marked by single reserved tokens, `<reserved_0>` for the user (id 3) and
`<reserved_1>` for the assistant (id 4). `tokenizer_config.json` (added 2026-10-14) holds a Jinja
template that renders as follows: a BOS of `<eos>`, then an optional system message followed by a
newline, then `<reserved_0>`, a newline, the user text and a newline, then `<reserved_1>` and a
newline as the generation prompt. An assistant turn ends with `<eos>`. The card warns that
`<|user|>`-style strings "produce degenerate output", and the paper says that mistake once
invalidated an internal safety evaluation (`ev-card-instruct`, `ev-trainer`). The base checkpoint
has no chat format and should not be prompted as an assistant.

<!-- item: languages -->
## Language coverage

The cards name twelve African languages, plus English, French and code (`ev-card-instruct`,
`ev-paper`). The evidence the publisher gives differs by language, so do not read the list as
equal support.

| Language | Native-text or machine-translated pretraining | Held-out evaluation text | Translation scored | Safety weakness |
|---|---|---|---|---|
| Swahili | MT pool | FLORES+, MasakhaNEWS | yes (59.9 into) | no |
| Hausa | MT pool | FLORES+, MasakhaNEWS | yes (49.1 into) | no |
| Yoruba | no MT pool in Table 2 | FLORES+, MasakhaNEWS | yes (26.9 into) | 82% |
| Igbo | MT pool | FLORES+, MasakhaNEWS | no | 75% |
| isiZulu | MT pool | FLORES+, NCHLT | yes (48.0 into) | no |
| isiXhosa | MT pool | FLORES+, MasakhaNEWS, NCHLT | yes (45.1 into) | 87% |
| Shona | MT pool | FLORES+, MasakhaNEWS | no | no |
| Kinyarwanda | MT pool | FLORES+ | no | no |
| Setswana | MT pool | FLORES+, NCHLT | no | 83% |
| Afrikaans | MT pool | FLORES+, NCHLT | no | no |
| isiNdebele | none, plus under 40M synthetic tokens | NCHLT transcripts only | no | not listed |
| Nigerian Pidgin | none, plus under 40M synthetic tokens | MasakhaNEWS only | no | not listed |

Translation scores are chrF++ from English from the paper's per-language table; safety figures
are the weakest-four list in the paper. The paper's own text says only isiNdebele and Nigerian
Pidgin lack a machine-translated pool, but Table 2 lists none for Yoruba either. Press articles
repeat the language list from the publisher and add no evidence.

<!-- item: tool-use -->
## Function / tool calling

The instruct model reaches 98.1% correct tool and 100% valid JSON, but the paper says this is
"format compliance and tool selection given the decision to call a tool": the tool marker is
prefilled in the test. Left to decide on its own, the model almost never calls a tool
(`ev-card-instruct`, `ev-paper`). Treat tool use as unproven unless you prefill or constrain the
call yourself.

<!-- structured-output is a `gap` item - no general JSON or schema-constrained output is
     documented. See gap_reason. -->
