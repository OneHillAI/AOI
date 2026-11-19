# Use - Gemma 4 (E2B, E4B, 12B, 26B A4B, 31B)

_Capabilities, context window, chat template, languages, tool use and structured output._

<!-- item: capabilities -->
## Capabilities & modalities

Gemma 4 is a multimodal family that reads text and images (all sizes), video as frames, and audio (E2B, E4B and 12B only) and writes text (`ev-card-31b`). It has a configurable thinking mode, coding ability, native function calling and a native system role.

Audio is limited to 30 seconds and video to 60 seconds at one frame per second. Image detail is set with a visual token budget of 70, 140, 280, 560 or 1120: use low budgets for classification and video, high budgets for OCR and small text.

The sizes differ a lot. On the publisher's table the 31B scores 84.3 percent on GPQA Diamond and 2150 on Codeforces Elo, the E4B 58.6 percent and 940, and the E2B 43.4 percent and 633. The 26B A4B activates 3.8B parameters per token and is the fast choice, the 31B is the quality choice, and the 12B Unified takes audio without a separate encoder. Independent capability evidence is mixed (see Assess, evaluation item).

<!-- item: context-window -->
## Context window & long-context behaviour

E2B and E4B support 128K tokens; the 12B, 26B A4B and 31B support 256K (`ev-card-31b`). The models interleave sliding-window attention (512 tokens for the small models, 1024 for the others) with global layers.

Long-context retrieval is publisher-reported and falls with size: on 8-needle 128K retrieval the 31B scores 66.4 percent, the 26B A4B 44.1, the 12B 43.4, the E4B 25.4 and the E2B 19.1. Do not assume a small model can use its full window; chunk and retrieve, and test your own documents. Memory for the KV cache grows with context (`ev-docs-overview`).

<!-- item: chat-template -->
## Prompt format & chat template

Gemma 4 uses standard `system`, `user` and `assistant` roles. Use the template (`apply_chat_template`) instead of hand-rolling role markers (`ev-card-31b`). The card sets these rules:

- Switch thinking on by putting the `<|think|>` token at the start of the system prompt; remove it to switch thinking off. Thinking output is delimited as `<|channel>thought ... <channel|>` before the answer.
- With thinking off, every size except E2B and E4B still emits an empty thought block.
- Do not put earlier turns' thinking content back into history, except on tool-call turns.
- Put image content before the text and audio content after the text.
- Use temperature 1.0, top_p 0.95 and top_k 64.
- Instruction-tuned models end a turn with `<turn|>`; base models end with `<eos>` (`ev-tech-report`).

The template in the repositories has had several fixes (tool-call loops, turn closure, null handling, reasoning preservation), so pin the revision under test (`ev-hf-scan`).

<!-- item: languages -->
## Language coverage

The card says Gemma 4 is pre-trained on more than 140 languages and supports 35 plus out of the box (`ev-card-31b`). The publisher reports MMMLU of 88.4 percent for the 31B, 86.3 for the 26B A4B, 83.4 for the 12B, 76.6 for the E4B and 67.4 for the E2B.

These are aggregate figures, and no per-language safety evaluation has been identified. Run your own for each target language, and expect the small models to be weakest.

<!-- item: tool-use -->
## Function / tool calling

Native function calling is documented in the model card as structured tool use for agentic workflows, and the chat template renders tool declarations and tool results (`ev-card-31b`). Ollama lists the tools capability for gemma4 (`ev-ollama`).

The publisher reports a Tau2 average over three of 76.9 percent for the 31B, 68.2 for the 26B A4B, 69.0 for the 12B, 42.2 for the E4B and 24.5 for the E2B. Keep thinking content on tool-call turns, and test tool-result rendering for images, since a repository discussion dated 18 November 2026 reports a template problem there (`ev-hf-scan`).

<!-- item: structured-output -->
## Structured / JSON-constrained output

The launch blog claims native structured JSON output (`ev-blog`), but the model card documents function calling and no JSON-schema mode (`ev-card-31b`), so coverage is partial. For guaranteed schemas, use constrained decoding at the serving layer (for example grammars in vLLM or llama.cpp) and validate outputs.
