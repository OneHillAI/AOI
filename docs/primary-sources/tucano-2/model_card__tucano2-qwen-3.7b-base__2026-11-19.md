doc_type: model_card
entity: tucano-2
variant/applies-to: Tucano2-qwen-3.7B-Base
source_url: https://huggingface.co/Polygl0t/Tucano2-qwen-3.7B-Base
retrieval_date: 2026-11-19
exists: yes
retrieved: true

## Extracts (VERBATIM from README.md; front matter keys kept: license, language, library_name, datasets)


[Front matter]
language:
  - pt
license: apache-2.0
library_name: transformers
datasets:
  - Polygl0t/gigaverbo-v2
  - Polygl0t/gigaverbo-v2-synth
pipeline_tag: text-generation

[Model Summary and Details]
## Model Summary

**[Tucano2-qwen-3.7B-Base](https://huggingface.co/Polygl0t/Tucano2-qwen-3.7B-Base)** is a decoder-only transformer continually pretrained from [Qwen3-4B-Base](https://huggingface.co/Qwen/Qwen3-4B-Base). Tucano2 is part of the [Polygl0t](https://huggingface.co/Polygl0t) initiative, which aims to advance language models for low-resource languages.

Tucano2-qwen-3.7B-Base shares the same tokenizer as **[Tucano2-0.6B-Base](https://huggingface.co/Polygl0t/Tucano2-0.6B-Base)**. Token embedding transplantation via _Orthogonal Matching Pursuit_ was used to adapt Qwen3-4B-Base to be more sensitive to the lexical, morphological, and orthographic properties of Portuguese.

The model was continually pretrained on approximately 50 billion tokens and achieves state-of-the-art performance across several benchmarks designed to evaluate Portuguese language models. **All data, source code, and recipes used to develop the Tucano2 series are open and fully reproducible.**

## Details

- **Architecture:** a Transformer-based model ([`qwen3`](https://huggingface.co/docs/transformers/main/en/model_doc/qwen3))
- **Size:** 3,759,341,056 parameters
- **Context length:** 4,096 tokens
- **Dataset(s):**
  - [Polygl0t/gigaverbo-v2](https://huggingface.co/datasets/Polygl0t/gigaverbo-v2)
  - [Polygl0t/gigaverbo-v2-synth](https://huggingface.co/datasets/Polygl0t/gigaverbo-v2-synth)
- **Language(s):** Portuguese
- **Batch size:** 1,048,576 tokens
- **Number of steps:** 50,000
- **GPU:** 8 NVIDIA A100-SXM4-80GB
- **Training time**: ~ 303 hours
- **Emissions:** 466 KgCO2 (Germany)
- **Total energy consumption:** 1223 kWh

This repository has the [source code](https://github.com/Polygl0t/llm-foundry) used to train this model. The full configuration used for training is available in the following config file:

- Single stage (linear warmup with cosine decay): [training_config.yaml](training_config.yaml)

[Intended Uses]
## Intended Uses

The primary intended use of Tucano2-qwen-3.7B-Base is to serve as a foundation for research and development involving Portuguese language modeling. Checkpoints saved during training are designed to provide a controlled setting for performing comparative experiments, specifically regarding the effects of continual pretraining on the performance of currently available benchmarks. You may also fine-tune and adapt Tucano2-qwen-3.7B-Base for deployment if your use follows the Apache 2.0 license. If you decide to use Tucano2-qwen-3.7B-Base as a basis for your fine-tuned model, please conduct your own risk and bias assessment.

## Out-of-scope Use

- Tucano2-qwen-3.7B-Base is **not intended for deployment**. It is not an out-of-the-box product and should not be used for human-facing interactions.
- Tucano2-qwen-3.7B-Base is for **the Portuguese language only** and is unsuitable for text generation tasks in other languages.
- Tucano2-qwen-3.7B-Base has **not been fine-tuned** for downstream tasks.

[Out-of-scope Use]
## Out-of-scope Use

- Tucano2-qwen-3.7B-Base is **not intended for deployment**. It is not an out-of-the-box product and should not be used for human-facing interactions.
- Tucano2-qwen-3.7B-Base is for **the Portuguese language only** and is unsuitable for text generation tasks in other languages.
- Tucano2-qwen-3.7B-Base has **not been fine-tuned** for downstream tasks.

[Limitations]
## Limitations

As almost all other language models trained on large text datasets scraped from the web, the Tucano2-qwen-3.7B-Base shows behavior that does not make it an out-of-the-box solution to many real-world applications, especially those requiring factual, reliable, and nontoxic text generation. Tucano2-qwen-3.7B-Base is subject to the following:

- **Hallucinations:** Tucano2-qwen-3.7B-Base can produce content that can be mistaken as facts, but is misleading or entirely false, i.e., hallucinations.

- **Biases and Toxicity:** Tucano2-qwen-3.7B-Base inherits the social and historical stereotypes from the data used to train it. Given these biases, the model can produce toxic content, i.e., harmful, offensive, or detrimental to individuals, groups, or communities.

- **Language Limitations:** Tucano2-qwen-3.7B-Base is primarily designed to interact with Portuguese. Other languages might challenge its comprehension, leading to potential misinterpretations or errors in response.

- **Repetition and Verbosity:** Tucano2-qwen-3.7B-Base may get stuck on repetition loops (especially if the repetition penalty during generations is set to a meager value) or produce verbose responses unrelated to the prompt it was given.

Hence, even though Tucano2-qwen-3.7B-Base is released under a permissive license, we urge users to perform their own risk analysis before using it for real-world applications.

[Evaluations, aggregate table]
## Evaluations

The table below compares the Tucano2 series against other base models of similar size. We divide our evaluations into two sets:

- **Easy Set**: CALAME, GlobalPIQA, LAMBADA, ARC-Challenge, HellaSwag
- **Hard Set**: ENEM, BLUEX, OAB Exams, BELEBELE, MMLU

The NPM (Normalized Performance Metric) provides a balanced view of model performance across tasks, accounting for each task's inherent difficulty by normalizing its evaluation score relative to its random baseline.

|                            | Total Avg. | Easy Set (NPM) | Hard Set (NPM) |
| -------------------------- | ---------- | -------------- | -------------- |
| **Tucano2-qwen-3.7B-Base** | 59.21      | 57.41          | 61             |
| Qwen2.5-7B                 | 57.97      | 54.12          | 61.83          |
| Qwen3-4B-Base              | 57.86      | 52.52          | 63.2           |
| SmolLM3-3B-Base            | 50.25      | 54.06          | 46.44          |
| Qwen2.5-3B                 | 50.16      | 47.69          | 52.62          |
| **Tucano2-qwen-1.5B-Base** | 47.9       | 47.97          | 47.82          |
| Curio-edu-7b               | 45.66      | 57.46          | 33.87          |
| Qwen3-1.7B-Base            | 44.48      | 40.94          | 48.03          |
| Curio-7b                   | 42.79      | 58.97          | 26.6           |
| Llama-3.2-3B               | 40.5       | 43.79          | 37.21          |
| granite-3.3-2b-base        | 39.97      | 45.31          | 34.63          |
| **Tucano2-qwen-0.5B-Base** | 35.36      | 39.93          | 30.79          |
| Qwen3-0.6B-Base            | 29.4       | 26.41          | 32.38          |
| Llama-2-7b-hf              | 29.36      | 42.69          | 16.03          |
| **Tucano2-0.6B-Base**      | 20.64      | 40.28          | 0.99           |
| Qwen2.5-0.5B               | 19.89      | 18.7           | 21.09          |
| Curio-1.1b                 | 19.23      | 39.16          | -0.69          |
| Tucano-2b4                 | 17.88      | 33.55          | 2.2            |
| Curio-edu-1b1              | 17.72      | 34.77          | 0.67           |
| Llama-3.2-1B               | 16.57      | 28.32          | 4.83           |
| Tucano-1b1                 | 15.44      | 29.12          | 1.76           |
| Tucano-630m                | 14.9       | 26.99          | 2.8            |
| Carvalho_pt-gl-1.3B        | 12.54      | 26.75          | -1.66          |
| TeenyTinyLlama-460m        | 11.18      | 19.65          | 2.72           |
| Tucano-160m                | 8.78       | 19.12          | -1.56          |
| TeenyTinyLlama-160m        | 7.72       | 15.75          | -0.31          |
| GlorIA-1.3B                | 5.93       | 27.27          | -15.42         |

[Acknowledgements and License]
## Aknowlegments

Polyglot is a project funded by the Federal Ministry of Education and Research (BMBF) and the Ministry of Culture and Science of the State of North Rhine-Westphalia (MWK) as part of TRA Sustainable Futures (University of Bonn) and the Excellence Strategy of the federal and state governments.

We also gratefully acknowledge the granted access to the [Marvin cluster](https://www.hpc.uni-bonn.de/en/systems/marvin) hosted by [University of Bonn](https://www.uni-bonn.de/en) along with the support provided by its High Performance Computing & Analytics Lab.

## License

Tucano2-qwen-3.7B-Base is licensed under the Apache License, Version 2.0. For more details, see the [LICENSE](LICENSE) file.
