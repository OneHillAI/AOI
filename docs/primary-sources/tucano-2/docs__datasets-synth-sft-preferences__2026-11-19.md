doc_type: docs
entity: tucano-2
variant/applies-to: Polygl0t/gigaverbo-v2-synth, -sft, -preferences
source_url: https://huggingface.co/datasets/Polygl0t/gigaverbo-v2-synth (and -sft, -preferences)
retrieval_date: 2026-11-19
exists: yes
retrieved: true

## Extracts (VERBATIM from each dataset card README.md)


[Access] gated: false for all three (Hugging Face API). HEAD requests (not downloaded): synth default/train-00000-of-00038.parquet HTTP 200, 912,834,097 bytes; sft code/train-00000-of-00001.parquet HTTP 200, 160,138,633 bytes; preferences harmfull-no-reasoning/train-00000-of-00001.parquet HTTP 200, 8,928,692 bytes. Front matter: sft license: apache-2.0; preferences license: apache-2.0; synth has no license key in its front matter but the card text and a LICENSE file (Apache License 2.0) state Apache-2.0.

[Synth - Dataset Summary]
### Dataset Summary

GigaVerbo-v2 Synth is a large synthetic Portuguese text corpus (~9.3 billion tokens) generated to complement the GigaVerbo-v2 web-sourced dataset. Inspired by approaches like Cosmopedia, this dataset was created to fill gaps in domains where web data is scarce or of lower quality, providing high-quality, diverse educational content. The dataset includes educational texts, tutorials, academic articles, blog posts, mathematical walkthroughs, programming tutorials, and synthetic conversations, designed specifically to enhance language model training for Portuguese.

[Synth - Statistics by Generator]
#### Statistics by Generator

| Generator                                                                | Examples       | Total Tokens      |
| ------------------------------------------------------------------------ | -------------- | ----------------- |
| [Qwen2.5-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-32B-Instruct) | 7,719,118      | 6,484,418,687     |
| [Qwen2.5-14B-Instruct](https://huggingface.co/Qwen/Qwen2.5-14B-Instruct) | 1,806,691      | 1,625,788,204     |
| [Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct)   | 1,711,737      | 1,211,544,076     |
| **Total**                                                                | **11,237,546** | **9,321,750,967** |

[Synth - Generation Pipeline and Licensing Information]
### Generation Pipeline

We employed three different Qwen2.5 models:

- **[Qwen2.5-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-32B-Instruct)** - Complex tasks (e.g., detailed mathematical reasoning)
- **[Qwen2.5-14B-Instruct](https://huggingface.co/Qwen/Qwen2.5-14B-Instruct)** - Intermediate tasks and generation
- **[Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct)** - Simpler tasks like summarization and rephrasing

All prompts used are available in the [ALL_PROMPTS](ALL_PROMPTS.md) file.
### Licensing Information

The dataset is released under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).

[SFT - Dataset Summary]
### Dataset Summary

GigaVerbo-v2 SFT is a large-scale instruction-tuning dataset designed for supervised fine-tuning of language models in Portuguese. The dataset comprises approximately 2.1 billion tokens (~4.4 GB) across 4 million instruction-following examples, organized into 12 distinct task categories. It is entirely composed of high-quality, LLM-generated data that has been carefully curated and filtered to ensure instruction-following quality. The dataset is intended for developing language models capable of diverse downstream applications, from code generation and reasoning tasks to retrieval-augmented generation.

[SFT - Source Data and Synthetic Data Generation]
### Source Data

#### Data Collection Process

The dataset construction process involved collecting an extensive set of prompts and instructions from multiple public sources, including existing instruction-tuning datasets and community contributions. These prompts originated in both English and Portuguese, and we standardized them by translating all English content to Portuguese using [Qwen2.5-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-32B-Instruct). This translation approach was carefully designed to preserve the original intent and context while maintaining fluency and naturalness in Portuguese. We paid particular attention to avoiding formatting inconsistencies that commonly arise during translation, such as problems with lists, code blocks, and LaTeX expressions.

#### Synthetic Data Generation

A significant portion of our dataset was generated synthetically using the Qwen2.5 series of models. The Qwen2.5 series was used to either directly generate instruction-following examples from the collected prompts or to augment existing examples with additional variations and reasoning traces.

#### Reasoning-Intensive Tasks

For reasoning-intensive tasks, we implemented a two-step generation process. First, we prompted the model to generate a high-quality response to the instruction. Then, we used a follow-up prompt to elicit a detailed reasoning trace that explained the model's thought process in arriving at the answer. This approach allowed us to create examples that not only provided correct answers but also included rich reasoning steps, which are crucial for training models on complex problem-solving tasks.

#### Chat Template Standardization

All of the data generated was formatted to fit a chat template we adapted from the Qwen3 series models. You can find the exact template used by our models ([Instruct](https://huggingface.co/Polygl0t/Tucano2-qwen-3.7B-Instruct/blob/main/chat_template.jinja) and [Think](https://huggingface.co/Polygl0t/Tucano2-qwen-3.7B-Think/blob/main/chat_template.jinja) variants) in the hyperlinks.

[SFT - Licensing Information]
### Licensing Information

GigaVerbo-v2 SFT is released under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).

[Preferences - Dataset Summary]
### Dataset Summary

GigaVerbo-v2 Preferences is a preference dataset designed for Direct Preference Optimization (DPO) and other direct alignment algorithms. The dataset comprises approximately 27.8 million tokens across 28,437 preference pairs, organized into 4 distinct subsets covering both quality-focused and safety-focused alignment. It is entirely composed of high-quality, LLM-generated data using Constitutional AI approaches, carefully designed to support the development of language models that are both helpful and safe. As a hybrid reasoning/non-reasoning dataset, GigaVerbo-v2 Preferences enables training models that can generate reasoning traces in Portuguese while also learning to refuse harmful instructions effectively.

[Preferences - Response Generation]
#### Response Generation

To generate the corresponding preferred (`chosen`) and less preferred (`rejected`) responses, we employed a _Constitutional AI_ approach. Distinct constitutions and steering strategies were used for each subset:

**Harmless Subset:**

- Preferred (`chosen`) responses were generated using [Qwen2.5-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct) with chain-of-thought reasoning.
- Less preferred (`rejected`) responses were produced using [Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct), also with step-by-step reasoning.
- This approach yields contrastive pairs that capture meaningful quality differences while preserving instruction-following consistency.
- The constitution used for both models is available [here](./REASONING_CONSTITUTION.md).

**Harmful Subset:**

- Preferred responses were generated using safety-oriented constitutions applied to [Qwen2.5-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct).
- Rejected samples consist of compliant (and therefore undesired) harmful completions generated by an [abliterated version of Qwen2.5-32B-Instruct](https://huggingface.co/huihui-ai/Qwen2.5-32B-Instruct-abliterated). An abliterated model is a variant known to comply with harmful instructions, providing realistic negative examples.
- Two distinct constitutions were used to steer the preferred and rejected responses, both available in the hyperlinks below:
  - Preferred responses constitution: [here](./HARMLESS_CONSTITUTION.md)
  - Rejected responses constitution: [here](./HARMFULL_CONSTITUTION.md)

[Preferences - Quality Assessment (the only quality or safety check described)]
#### Quality Assessment

To assess the quality and alignment of the generated preference pairs, we performed an automatic evaluation using an LLM-as-a-judge framework. We designed a custom evaluation prompt instructing Qwen2.5-32B-Instruct to assess each `chosen`–`rejected` pair with respect to their corresponding constitutions. Specifically, the model compared responses based on (i) adherence to constitutional principles, (ii) helpfulness, and (iii) reasoning quality. To control computational cost, we evaluated a random subset of 500 preference pairs from the filtered dataset.

Across all evaluated samples, the `chosen` responses were consistently rated as preferable to their corresponding `rejected` counterparts, providing quantitative evidence of the dataset’s overall quality and alignment. In addition, we conducted a manual inspection of 100 randomly selected filtered interactions to qualitatively examine the effectiveness of our generation and filtering pipeline. Together, these automatic and human evaluations increase our confidence in the reliability and alignment of the resulting preference pairs.

**Note.** Human judgments are inherently subjective and may vary across annotators and use cases. While we have taken multiple steps to ensure dataset quality, we encourage users to perform independent evaluations and consider the specific requirements of their downstream applications when using GigaVerbo-v2 Preferences.
