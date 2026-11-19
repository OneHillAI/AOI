doc_type: model_card
entity: tucano-2
variant/applies-to: Tucano2-qwen-3.7B-Instruct
source_url: https://huggingface.co/Polygl0t/Tucano2-qwen-3.7B-Instruct
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
  - Polygl0t/gigaverbo-v2-sft
  - Polygl0t/gigaverbo-v2-preferences
pipeline_tag: text-generation

[Model Summary and Details]
## Model Summary

**[Tucano2-qwen-3.7B-Instruct](https://huggingface.co/Polygl0t/Tucano2-qwen-3.7B-Instruct)** is an instruction-tuned Portuguese language model on top of **Tucano2-qwen-3.7B-Base**. It has been trained using a combination of one round of supervised fine-tuning (SFT) and one round of Anchored Preference Optimization (APO).

Despite its compact size, the model delivers strong performance across a wide range of Portuguese benchmarks and supports tasks such as **retrieval-augmented generation**, **function calling and tool use**, **summarization**, and **structured output generation**, among others.

**All datasets, source code, and training recipes used to develop the Tucano2 series are fully open and reproducible.**

## Details

- **Architecture:** a Transformer-based model ([`qwen3`](https://huggingface.co/docs/transformers/main/en/model_doc/qwen3))
- **Size:** 3,759,341,056 parameters
- **Context length:** 4,096 tokens
- **Dataset(s):**
  - [Polygl0t/gigaverbo-v2-sft](https://huggingface.co/datasets/Polygl0t/gigaverbo-v2-sft)
  - [Polygl0t/gigaverbo-v2-preferences](https://huggingface.co/datasets/Polygl0t/gigaverbo-v2-preferences)
- **Training time**: ~ 140 hours
- **Emissions:** 110 KgCO2 (Germany)
- **Total energy consumption:** 290 kWh

This repository has the [source code](https://github.com/Polygl0t/llm-foundry) used to train this model. The full configuration used for training is available in the following config files:

- Single stage Supervised Fine-Tuning (linear warmup with cosine decay): [training_config_sft.yaml](training_config_sft.yaml)
- Single stage Anchored Preference Optimization (linear warmup with cosine decay): [training_config_apo.yaml](training_config_apo.yaml)
- Training Logs (loss, lr, rewards, etc.): [train_logs_apo.parquet](train_logs_apo.parquet), [train_logs_sft.parquet](train_logs_sft.parquet)

[Intended Uses]
## Intended Uses

The primary intended use Tucano2-qwen-3.7B-Instruct is to serve as foundations for research and development involving Portuguese language modeling. You may also fine-tune and adapt Tucano2-qwen-3.7B-Instruct for deployment if your use follows the Apache 2.0 license. If you decide to use Tucano2-qwen-3.7B-Instruct as a basis for your fine-tuned model, please conduct your own risk and bias assessment.

[Limitations]
## Limitations

Like almost all other language models trained on large text datasets scraped from the web, the Tucano2-qwen-3.7B-Instruct shows behavior that does not make it an out-of-the-box solution to many real-world applications, especially those requiring factual, reliable, and nontoxic text generation. Tucano2-qwen-3.7B-Instruct is subject to the following:

- **Hallucinations:** Tucano2-qwen-3.7B-Instruct can produce content that can be mistaken as true facts, but are misleading or entirely false, i.e., hallucination.

- **Biases and Toxicity:** Tucano2-qwen-3.7B-Instruct inherits the social and historical stereotypes from the data used to train it. Given these biases, the model can produce toxic content, i.e., harmful, offensive, or detrimental to individuals, groups, or communities.

- **Language Limitations:** Tucano2-qwen-3.7B-Instruct is primarily designed to interact with Portuguese. Other languages might challenge its comprehension, leading to potential misinterpretations or errors in response.

- **Repetition and Verbosity:** Tucano2-qwen-3.7B-Instruct may get stuck on repetition loops (especially if the repetition penalty during generations is set to a meager value) or produce verbose responses unrelated to the prompt it was given.

Hence, even though Tucano2-qwen-3.7B-Instruct is released with a permissive license, we urge users to perform their risk analysis on them if they intend to use them for real-world applications.

[Evaluations, aggregate table]
## Evaluations

The table below compares the Tucano2 (Instruct variant) series against other chat models of similar size. We divide our evaluations into three sets:

- **Knowledge & Reasoning:** ARC-Challenge, ENEM, BLUEX, OAB Exams, BELEBELE, MMLU, GSM8K-PT
- **Instruction Following:** IFEval-PT
- **Coding:** HumanEval

The NPM (Normalized Performance Metric) provides a balanced view of model performance across tasks, accounting for each task's inherent difficulty by normalizing its evaluation score relative to its random baseline.

|                                | Total Avg. | Knowledge & Reasoning (NPM) | Instruction Following | Coding |
| ------------------------------ | ---------- | --------------------------- | --------------------- | ------ |
| **Tucano2-qwen-3.7B-Instruct** | 53.64      | 56.22                       | 41.67                 | 47.56  |
| Jurema-7B                      | 53.03      | 50.66                       | 47                    | 75.61  |
| Qwen2.5-3B-Instruct            | 51.71      | 47.34                       | 63.33                 | 70.73  |
| Qwen3-4B                       | 51.36      | 42.33                       | 79.33                 | 86.59  |
| Gemma-3-Gaia-PT-BR-4b-it       | 49.93      | 45                          | 70.33                 | 64.02  |
| SmolLM3-3B                     | 49.54      | 43.99                       | 69.67                 | 68.29  |
| Llama-3.2-3B-Instruct          | 45.82      | 43.08                       | 62.67                 | 48.17  |
| Qwen2.5-1.5B-Instruct          | 41.39      | 40.25                       | 42                    | 48.78  |
| **Tucano2-qwen-1.5B-Instruct** | 37.54      | 39.61                       | 34.33                 | 26.22  |
| Qwen3-1.7B                     | 36.3       | 28.24                       | 65                    | 64.02  |
| **Tucano2-qwen-0.5B-Instruct** | 26.08      | 27.77                       | 30                    | 10.37  |
| Qwen3-0.6B                     | 22.21      | 15.13                       | 55                    | 39.02  |
| Llama-3.2-1B-Instruct          | 20.14      | 15.37                       | 44.33                 | 29.27  |
| Qwen2.5-0.5B-Instruct          | 17.8       | 14.98                       | 31                    | 24.39  |
| Tucano-2b4-Instruct            | 3.78       | 2.71                        | 15                    | 0      |
| Tucano-1b1-Instruct            | 2.59       | 1.42                        | 13.33                 | 0      |
| TeenyTinyLlama-460m-Chat       | 0.07       | -1.68                       | 12.33                 | 0      |

[Acknowledgements and License]
## Aknowlegments

Polyglot is a project funded by the Federal Ministry of Education and Research (BMBF) and the Ministry of Culture and Science of the State of North Rhine-Westphalia (MWK) as part of TRA Sustainable Futures (University of Bonn) and the Excellence Strategy of the federal and state governments.

We also gratefully acknowledge the granted access to the [Marvin cluster](https://www.hpc.uni-bonn.de/en/systems/marvin) hosted by [University of Bonn](https://www.uni-bonn.de/en) along with the support provided by its High Performance Computing & Analytics Lab.

## License

Tucano2-qwen-3.7B-Instruct is licensed under the Apache License, Version 2.0. For more details, see the [LICENSE](LICENSE) file.
