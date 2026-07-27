# Use - DeepSeek (V3 / R1)

_What can it do and how do we use it well? Capabilities, context window, prompt/chat
template, languages, tool-use, structured output._

<!-- item: capabilities -->
## Capabilities & modalities

DeepSeek is text-only. Its headline strengths are **reasoning and coding**: R1 exposes an
explicit reasoning mode (it "thinks" before answering) and performs strongly on
public reasoning leaderboards, while V3 is a competitive general instruct model. The
R1-Distill checkpoints carry much of the reasoning behaviour into smaller dense models.
The distinctive behavioural limit to design around is **topic censorship** on certain
political topics - capability is high, but neutrality is not guaranteed.

<!-- item: context-window -->
## Context window & long-context behaviour

V3/R1 provide a **long context window**, documented on the model card. Because the exact
window can vary by checkpoint and release, confirm the value in the specific checkpoint's
`config.json` rather than assuming a fixed figure. Long-context quality degrades in the
usual ways at the extremes; test retrieval/summarisation at your target length before
relying on it. (Coverage marked partial: the model card states "long" with no
verified exact token count.)

<!-- item: chat-template -->
## Prompt format / chat template

Use the **DeepSeek chat template** shipped in the tokenizer config on the model card -
apply it via `tokenizer.apply_chat_template(...)` rather than hand-building prompts. The
key operational detail is R1's **`<think>` reasoning tags**: the model emits its
chain-of-thought inline, so your application must parse and strip (or deliberately surface)
the reasoning span before returning the final answer to users. Follow the model card's
usage recommendations on system-prompt handling per variant.

<!-- item: languages -->
## Multilingual coverage

**English and Chinese are the strongest** languages. Other languages are supported but
less thoroughly evaluated, so validate quality on your target languages before adoption.
(Coverage marked partial: strong EN/ZH is well-attested, broader multilingual performance
is not independently characterised here.)

<!-- tool-use and structured-output are `gap` items in entry.yaml - their gap_reasons
     render as callouts. Function/tool-calling for the self-hosted weights is not cleanly
     documented (differs V3 vs R1; described mainly for the hosted API), and there is no
     model-native JSON mode - schema-constrained decoding is a serving-layer feature
     (vLLM/SGLang/outlines). -->
