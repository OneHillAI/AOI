# Use - Jais 3 (0.9B, 3.7B, 7B, 32B, MoVA-36B-A4B, 375B-A23B)

_Capabilities, context window, chat template, languages, tool use and structured output._

<!-- item: capabilities -->
## Capabilities & modalities

Jais 3 is a family of text reasoning and agentic models for Arabic and English. The report says they plan multi-step tasks, call tools and Model Context Protocol servers, operate a terminal, search the web, and read, edit and produce PDF, spreadsheet and presentation files in Arabic (`ev-report-release`). They also follow Arabic-specific instruction constraints such as hamza, diacritics and morphology.

Sizes: dense 0.9B, 3.7B, 7B and 32B, a 36B mixture of experts with Mixture-of-Value Attention (about 4B active, 100 experts in the config) and a 375B mixture of experts (about 23B active, 192 experts) (`ev-hub`).

The report says the 3.7B and 7B lead every agentic benchmark against models of their size, and that the 32B and 375B trail Qwen3.8 models on most of them (`ev-report-eval`). All figures are the publisher's own. Speech is a separate model (Jais-ASR) and is not covered.

<!-- item: context-window -->
## Context window & long-context behaviour

The configuration sets `max_position_embeddings` to 524,288 for the 3.7B, 7B, 32B, MoVA-36B-A4B and 375B-A23B, and to 131,072 for the 0.9B (`ev-hub`). The report says the long context comes from K2 Horizon mid-training (`ev-report-lineage`).

The report scores the 3.7B at 68 on AA-LCR-Ar, an Arabic long-context benchmark with inputs of about 100K tokens, and says most Arabic-focused baselines could not run it (`ev-report-eval`). No result is reported near 512K tokens. Test your own long inputs and plan KV-cache memory (see implement.md).

<!-- item: chat-template -->
## Prompt format & chat template

Each repository ships `chat_template.jinja`. Reasoning depth is chosen per request through `chat_template_kwargs`, and the card says all reported results use `reasoning_effort="high"` (`ev-card-32b`). Low effort is not recommended except for research on reasoning effort.

The template accepts `tool_call_format` (`json`, `xml` or `xml_typed`, default `xml`) and `tool_presentation_format` (`json`, `xml` or `markdown`, default `markdown`). It raises an error for the misspelt names `tool_presentation`, `tool_calling_format` and `tool_format`. Enable the `k2_horizon` reasoning parser for chat and add the `k2_horizon` tool-call parser for agent use. Leave both off for plain completion.

Sampling from the card: temperature 0.2 by default, 1.0 for English thinking and 0.7 for Arabic thinking, with `top_p` 0.95 and `top_k` 20.

<!-- item: languages -->
## Language coverage

The cards tag Arabic and English. Arabic coverage is Modern Standard Arabic, the regional dialects and Arabizi, the Latin-script form of informal Arabic (`ev-card-32b`, `ev-report-dialect`).

Dialect evidence in training has four parts (`ev-report-data`, `ev-report-dialect`). Parallel dialect text comes from English conversations translated by GLM-5 and Jais 2 and judge-filtered. Arabizi covers Gulf, Egyptian, Levantine and Darija forms (25.1B tokens). Country-knowledge questions cover the 22 Arab League states, about 70% in the country's dialect. Translation and transliteration data covers seven dialects. The public sample's web subset is labelled 89.5% MSA, 6.7% Moroccan, 2.5% Egyptian and 1.0% Najdi (`ev-data-sample`).

Dialect evidence in evaluation: QADI dialect identification, Dialectal-Arabic-MMLU in Egyptian, Saudi, Moroccan, Syrian and Emirati, FLORES+ translation across eight dialects, and Darija and Egyptian transliteration. All runs are the publisher's own. Languages other than Arabic and English are out of scope on the cards.

<!-- item: tool-use -->
## Function / tool calling

Tool calling goes through the `k2_horizon` tool-call parser on vLLM or SGLang, with an XML default and JSON and typed-XML options (`ev-card-32b`). The card includes an Arabic function-calling example with a loop that executes tool calls.

The report evaluates agentic tasks on eleven benchmarks and says only two are in Arabic. Coding, tool use and deep search are tested in English only (`ev-report-eval`). Sandbox every tool and test the parser before an unattended run.
