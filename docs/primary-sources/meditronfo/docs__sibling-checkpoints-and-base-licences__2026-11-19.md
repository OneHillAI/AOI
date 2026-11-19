# docs / sibling-checkpoints-and-base-licences

source_url: https://huggingface.co/api/models?author=EPFLiGHT
retrieval_date: 2026-11-19
retrieved_by: curl, text read in full or in the extracts marked below
note: Hugging Face API listing of the EPFLiGHT organisation and the licence tags of sibling MeditronFO checkpoints. Used only to define the scope of this entry and to list follow-ups.

Verbatim extracts follow. Nothing below is paraphrased unless it is under a heading that says OneHill note.

```
- EPFLiGHT/Meditron3-8B | created 2024-07-11 | gated=None | ['license:llama3.1']
- EPFLiGHT/Meditron3-70B | created 2024-07-12 | gated=None | ['license:llama3.1']
- EPFLiGHT/Meditron3-Gemma2-2B | created 2025-01-16 | gated=None | ['license:gemma']
- EPFLiGHT/Meditron3-Qwen2.5-7B | created 2025-01-16 | gated=None | ['license:apache-2.0']
- EPFLiGHT/Meditron3-Gemma2-9B | created 2025-01-16 | gated=None | ['license:gemma']
- EPFLiGHT/Meditron3-Phi4-14B | created 2025-01-16 | gated=None | ['license:mit']
- EPFLiGHT/Meditron3-Qwen2.5-14B | created 2025-02-18 | gated=None | ['license:apache-2.0']
- EPFLiGHT/Gemma-3-27B-MeditronFO | created 2026-05-08 | gated=None | ['license:gemma']
- EPFLiGHT/EuroLLM-22B-MeditronFO | created 2026-05-08 | gated=None | ['license:apache-2.0']
- EPFLiGHT/Apertus-70B-MeditronFO | created 2026-05-08 | gated=None | ['license:apache-2.0']
- EPFLiGHT/Apertus-8B-MeditronFO | created 2026-05-08 | gated=None | ['license:apache-2.0']
- EPFLiGHT/OLMo-2-32B-MeditronFO | created 2026-05-08 | gated=None | ['license:apache-2.0']
- EPFLiGHT/EuroLLM-9B-MeditronFO | created 2026-05-08 | gated=None | ['license:apache-2.0']
- EPFLiGHT/Gemma-3-27B-MeditronFO-Amharic | created 2026-05-26 | gated=None | []
```

EPFLiGHT/Gemma-3-27B-MeditronFO card front matter and licence line (verbatim):
```
---
license: gemma
language:
- en
library_name: transformers
pipeline_tag: text-generation
tags:
- medical
- clinical
- healthcare
- meditron
- fully-open
- medical-llm
base_model: google/gemma-3-27b-it
base_model_relation: finetune
datasets:
- EPFLiGHT/fully-open-meditron
---

# Gemma-3-27B-MeditronFO

<div align="center">
<img src=https://raw.githubusercontent.com/EPFLiGHT/MeditronFO/3caab22b7efaf9e56e2894bac65dab6d3a31aaa0/
[...]
<b>License</b>: <a href="https://ai.google.dev/gemma/terms" target="_blank">gemma</a> | <b>Authors</b>: <a href="https://www.light-laboratory.org/" target="_blank">LiGHT</a>
```

The Gemma card still carries the tag `fully-open` although the project page labels it open-weight.

Base-model reads on 2026-11-19: swiss-ai/Apertus-*-Instruct-2509 gated=False; allenai/OLMo-2-0325-32B-SFT Apache-2.0 (card front matter read); utter-project/EuroLLM-9B-Instruct gated=auto (card and raw files return HTTP 401, licence tag apache-2.0 from the API); utter-project/EuroLLM-22B-Instruct, the base named on EPFLiGHT/EuroLLM-22B-MeditronFO, returns an error from the API (HTTP 401, not readable); utter-project/EuroLLM-22B-2512 shows licence tag apache-2.0.

