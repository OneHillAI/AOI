# model_card / llm-jp-4.1-33b-thinking

source_url: https://huggingface.co/llm-jp/llm-jp-4.1-33b-thinking (raw README.md)
retrieval_date: 2026-11-19
exists: yes
retrieved: true

Verbatim extracts (publisher text, not edited). Notes by OneHill are marked NOTE.

## Front matter and header
```
---
license: apache-2.0
language:
- en
- ja
programming_language:
- C
- C++
- C#
- Go
- Java
- JavaScript
- Lua
- PHP
- Python
- Ruby
- Rust
- Scala
- TypeScript
pipeline_tag: text-generation
library_name: transformers
inference: false
---
```

## Overview
```
LLM-jp-4.1 is a series of large language models developed by the [Research and Development Center for Large Language Models](https://llmc.nii.ac.jp/) at the [National Institute of Informatics](https://www.nii.ac.jp/en/).

This repository provides the **llm-jp-4.1-33b-thinking** model.
For an overview of the LLM-jp-4.1 models across different parameter sizes, please refer to:
  - [LLM-jp-4.1 Models](https://huggingface.co/collections/llm-jp/llm-jp-41-models)

Base models are trained with pre-training and mid-training only.
Post-trained models are aligned using supervised fine-tuning (SFT) and direct preference optimization (DPO), without reinforcement learning.

For more details on the training procedures and evaluation results, please refer to our [technical blog](https://llm-jp.nii.ac.jp/blog/llm-jp-4-1/) (in Japanese).

For practical usage examples and detailed instructions on how to use the models, please also refer to our [cookbook](https://github.com/llm-jp/llm-jp-4-cookbook).

To support the continued development of LLM-jp, we would greatly appreciate it if you could share how you utilize LLM-jp outcomes via the [survey form](https://forms.gle/AvbNXTNT2ADsssHq5).
```

## Model details (architecture and context length)
```
## Model Details

- **Model type:** Transformer-based Language Model
- **Architectures:**

Dense model:
|Params|Layers|Hidden size|Heads|Context length|Embedding parameters|Non-embedding parameters|Total parameters|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|8B|32|4,096|32|65,536|805,306,368|7,784,894,464|8,590,200,832|
|33B|64|5,120|40|65,536|1,006,632,960|32,212,915,200|33,219,548,160|

MoE model:
|Params|Layers|Hidden size|Heads|Routed Experts|Activated Experts|Context length|Embedding parameters|Non-embedding parameters|Activated parameters|Total parameters|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|32B-A3B|32|2,560|40|128|8|65,536|503,316,480|31,635,712,512|3,827,476,992|32,139,028,992|
```

## Training
```
## Training

### Pre-training

This model was trained through a multi-stage pipeline consisting of pre-training and mid-training phases, using a total of 11.7T tokens.

![v4_pretraining_overview](https://cdn-uploads.huggingface.co/production/uploads/649e389a53777d8950704588/CMoeH-gyBDuYkBYLyWBR1.png)

The corpora used for pre-training and mid-training are publicly available at the following links:
- [Pre-training](https://gitlab.llm-jp.nii.ac.jp/datasets/llm-jp-corpus-v4.1)
- [Mid-training](https://gitlab.llm-jp.nii.ac.jp/datasets/llm-jp-corpus-midtraining-v2)

> [!NOTE]
> Although most of the corpora have been released, some portions are excluded from public release due to licensing constraints.

### Post-training

We have fine-tuned the pre-trained checkpoint using SFT and further aligned it with DPO.

The datasets used for post-training are also publicly available at the following links:
- [SFT](https://huggingface.co/datasets/llm-jp/llm-jp-4.1-thinking-sft-data)
- [DPO (for llm-jp-4.1-8b-thinking model)](https://huggingface.co/datasets/llm-jp/llm-jp-4.1-8b-thinking-dpo-data)
- [DPO (for llm-jp-4.1-32b-a3b-thinking model)](https://huggingface.co/datasets/llm-jp/llm-jp-4.1-32b-a3b-thinking-dpo-data)
- [DPO (for llm-jp-4.1-33b-thinking model)](https://huggingface.co/datasets/llm-jp/llm-jp-4.1-33b-thinking-dpo-data)
```

## Evaluation (llm-jp-judge table, safety benchmark AnswerCarefully)
```
### [llm-jp-judge](https://github.com/llm-jp/llm-jp-judge)

We evaluated the models using an LLM-as-a-Judge framework on the following benchmarks:

- MT-Bench (JA/EN): A benchmark for measuring multi-turn conversational task-solving ability.
- [AnswerCarefully](https://huggingface.co/datasets/llm-jp/AnswerCarefully): A benchmark for evaluating safety in Japanese. We used 336 questions from the v2.0 test set.
- [llm-jp-instructions](https://huggingface.co/datasets/llm-jp/llm-jp-instructions): A set of human-created single-turn question-answer pairs. We used 400 questions from the test set.

We used `gpt-5.4-2026-03-05` as the judge. For models that support `reasoning_effort`, it was set to `medium`.

The scores represent the average values obtained from three rounds of inference and evaluation.
For more details, please refer to the [evaluation code](https://github.com/llm-jp/llm-jp-judge).


| Model Name | MT-Bench (JA) | MT-Bench (EN) | AnswerCarefully | llm-jp-instructions |
|:-----------|--------------:|--------------:|----------------:|--------------------:|
| gpt-4o-2024-08-06 | 7.29 | 7.69 | 4.00 | 4.07 |
| gpt-5.4-2026-03-05 | 8.87 | 8.89 | 4.43 | 4.82 |
| [gpt-oss-20b](https://huggingface.co/openai/gpt-oss-20b) | 7.33 | 7.85 | 3.55 | 3.16 |
| [llm-jp-4-8b-thinking](https://huggingface.co/llm-jp/llm-jp-4-8b-thinking) | 7.54 | 7.79 | 3.69 | 3.54 |
| [llm-jp-4.1-8b-thinking](https://huggingface.co/llm-jp/llm-jp-4.1-8b-thinking) | 7.58 | 7.67 | 3.92 | 3.67 |
| [llm-jp-4-32b-a3b-thinking](https://huggingface.co/llm-jp/llm-jp-4-32b-a3b-thinking) | 7.82 | 7.86 | 3.70 | 3.61 |
| [llm-jp-4.1-32b-a3b-thinking](https://huggingface.co/llm-jp/llm-jp-4.1-32b-a3b-thinking) | 7.69 | 7.85 | 3.91 | 3.79 |
| [llm-jp-4-33b-thinking](https://huggingface.co/llm-jp/llm-jp-4-33b-thinking) | 8.00 | 8.24 | 3.79 | 3.79 |
| [llm-jp-4.1-33b-thinking](https://huggingface.co/llm-jp/llm-jp-4.1-33b-thinking) | 7.76 | 7.98 | 4.08 | 3.83 |
```

## Tool calling
```
### Tool Calling

We evaluated the models on the following tool calling benchmarks:

- [BFCL](https://gorilla.cs.berkeley.edu/leaderboard.html)
- [tau2-bench](https://github.com/sierra-research/tau2-bench)

For BFCL, we evaluated the models using only the categories available up to v3, so the web search and memory categories introduced in v4 are excluded.
For tau2-bench, we used Azure's `gpt-5.1-2025-11-13` as both the user simulator and the NL-assertion judge, and the scores represent the average values obtained from two rounds of inference and evaluation.
For all LLM-jp models, `reasoning_effort` was set to `medium`.

The figure below shows the scores on each benchmark.

![tool-calling results](https://cdn-uploads.huggingface.co/production/uploads/694a80a07f331c43f52eaaa6/sroa-NbpkyoXVeMcv5S1V.png)
```

## Risks and Limitations (the use-guidance wording)
```
## Risks and Limitations

The models released here are research and development models and are not intended for direct use in production services.
Although the models have undergone post-training for instruction following and safety, they may still generate inaccurate, inappropriate, or otherwise undesirable outputs.
Users should carefully evaluate the models for their intended use cases.
```

## License and acknowledgements
```
## License

[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)


## Acknowledgements

To develop this model, we used the NINJAL Web Japanese Corpus (whole-NWJC) from the National Institute for Japanese Language and Linguistics (NINJAL).
```

NOTE: the 8B and 32B-A3B 4.1 cards (https://huggingface.co/llm-jp/llm-jp-4.1-8b-thinking and https://huggingface.co/llm-jp/llm-jp-4.1-32b-a3b-thinking) carry the same Risks and Limitations text and the same licence line. Verified by diff on 2026-11-19: the Risks section is identical in all three 4.1 cards.
```
## Risks and Limitations

The models released here are research and development models and are not intended for direct use in production services.
Although the models have undergone post-training for instruction following and safety, they may still generate inaccurate, inappropriate, or otherwise undesirable outputs.
Users should carefully evaluate the models for their intended use cases.
```
