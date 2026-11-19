# third_party / Artificial Analysis article on Sarvam 105B and 30B (2 April 2026)

source_url: https://artificialanalysis.ai/articles/sarvam-105b-Sarvam-30b-everything-you-need-to-know
retrieval_date: 2026-11-19
exists: yes
retrieved: true

Verbatim extracts (publisher text, not edited). Notes by OneHill are marked NOTE.

```
K
All articles
April 2, 2026
Sarvam 105B and Sarvam 30B: India enters the open-weights race
See model page
India enters the open-weights AI race with its largest models pre-trained from scratch: Sarvam 105B and Sarvam 30B
SarvamAI's Sarvam 105B and Sarvam 30B score 18 and 12 on the Artificial Analysis Intelligence Index respectively. Announced at the India AI Impact Summit 2026 and open-sourced under Apache 2.0, both are Mixture-of-Experts models trained entirely in India using compute provided under the IndiaAI Mission. Both support reasoning and non-reasoning modes.
These are an improvement from Sarvam's previous model, Sarvam M (8 on Intelligence Index, 23.6B parameters), which was based on Mistral Small rather than pre-trained from scratch. Sarvam 105B has 106B total parameters with ~10B active per token and a 128K context window. Sarvam 30B has 32B total parameters with ~2.4B active per token and a 65K context window. Alongside the text models, Sarvam also announced Saaras v3 (Speech to Text) and Bulbul v3 (Text to Speech) with a focus on Indic languages.
Key takeaways in reasoning mode:
Sarvam 105B scores 18 on the Intelligence Index.
 Among ~100B-class open-weights reasoning models, it trails GLM-4.5-Air (23), INTELLECT-3 (22), Mistral Small 4 (27), and gpt-oss-120B (High, 33). All four peers also activate more parameters per token
Sarvam 30B scores 12 on the Intelligence Index.
 Among ~30B-class open-weights reasoning models, it trails GLM-4.7-Flash (30), Nemotron Cascade 2 30B A3B (28), Qwen3 30B A3B 2507 (22), and Qwen3 32B (17). Sarvam 30B activates fewer parameters than these peers
Sarvam 105B's relative strength is in select agentic tasks
. Its agentic index of 25 places it ahead of INTELLECT-3 (20) and GLM-4.5-Air (21) despite trailing both on overall intelligence. Its GDPval index of 773 also edges ahead of GLM-4.5-Air (665). Both new models are a large step up from Sarvam M (Reasoning), which scored 8 on the Intelligence Index.
Compared to peers, both models score lower on TerminalBench Hard (Agentic Coding & Terminal Use) and AA-Omniscience
. Sarvam 105B scored 1.5% and Sarvam 30B scored 2.3% on TerminalBench Hard, compared to GLM-4.5-Air (20.5%) and INTELLECT-3 (9.1%). The AA-Omniscience Index is -60 for Sarvam 105B and -72 for Sarvam 30B. Both models have high hallucination rates relative to their accuracy, and both attempt to answer far more questions rather than abstaining, which drives the negative scores.
Key model details:
➤ 
Modality
: Text input and output only.
➤ 
Context window
: 128K tokens (Sarvam 105B) and 65K tokens (Sarvam 30B).
➤ 
Pricing
: Currently free on Sarvam's first-party API.
➤ 
License
: Apache 2.0.
➤ 
```

NOTE: Artificial Analysis is an independent benchmarking organisation. Its evaluation covers the March 2026 builds, not 105B-1711. Its statement that the models are 'pre-trained from scratch' repeats the publisher's account and is not an independent check of training provenance.
