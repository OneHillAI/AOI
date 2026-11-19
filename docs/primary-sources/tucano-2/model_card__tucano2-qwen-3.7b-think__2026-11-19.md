doc_type: model_card
entity: tucano-2
variant/applies-to: Tucano2-qwen-3.7B-Think
source_url: https://huggingface.co/Polygl0t/Tucano2-qwen-3.7B-Think
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

**[Tucano2-qwen-3.7B-Think](https://huggingface.co/Polygl0t/Tucano2-qwen-3.7B-Think)** is an instruction-tuned Portuguese language model built on top of **Tucano2-qwen-3.7B-Base**. It has been trained using a combination of one round of supervised fine-tuning (SFT) and one round of Anchored Preference Optimization (APO).

Tucano2-qwen-3.7B-Think is a reasoning model, which means it has been fine-tuned to generate CoT-style (Chain-of-Thought) traces in its responses. These reasoning traces are always encapsulated within the special tokens `<think>` and `</think>`.

**All datasets, source code, and training recipes used to develop the Tucano2 series are fully open and reproducible.**

## Details

- **Architecture:** a Transformer-based model ([`qwen3`](https://huggingface.co/docs/transformers/main/en/model_doc/qwen3))
- **Size:** 3,759,341,056 parameters
- **Context length:** 4,096 tokens
- **Dataset(s):**
  - [Polygl0t/gigaverbo-v2-sft](https://huggingface.co/datasets/Polygl0t/gigaverbo-v2-sft)
  - [Polygl0t/gigaverbo-v2-preferences](https://huggingface.co/datasets/Polygl0t/gigaverbo-v2-preferences)
- **Training time**: ~ 1.5 hours
- **Emissions:** 13.30 KgCO2 (Germany)
- **Total energy consumption:** 29 kWh

This repository has the [source code](https://github.com/Polygl0t/llm-foundry) used to train this model. The full configuration used for training is available in the following config files:

- Single stage Supervised Fine-Tuning (linear warmup with cosine decay): [training_config_sft.yaml](training_config_sft.yaml)
- Single stage Anchored Preference Optimization (linear warmup with cosine decay): [training_config_apo.yaml](training_config_apo.yaml)
- Training Logs (loss, lr, rewards, etc.): [train_logs_apo.parquet](train_logs_apo.parquet), [train_logs_sft.parquet](train_logs_sft.parquet)

[Intended Uses]
## Intended Uses

The primary intended use Tucano2-qwen-3.7B-Think is to serve as foundations for research and development involving Portuguese language modeling. You may also fine-tune and adapt Tucano2-qwen-3.7B-Think for deployment if your use follows the Apache 2.0 license. If you decide to use Tucano2-qwen-3.7B-Think as a basis for your fine-tuned model, please conduct your own risk and bias assessment.

[Limitations]
## Limitations

Like almost all other language models trained on large text datasets scraped from the web, the Tucano2-qwen-3.7B-Think shows behavior that does not make it an out-of-the-box solution to many real-world applications, especially those requiring factual, reliable, and nontoxic text generation. Tucano2-qwen-3.7B-Think is subject to the following:

- **Hallucinations:** Tucano2-qwen-3.7B-Think can produce content that can be mistaken as true facts, but are misleading or entirely false, i.e., hallucination.

- **Biases and Toxicity:** Tucano2-qwen-3.7B-Think inherits the social and historical stereotypes from the data used to train it. Given these biases, the model can produce toxic content, i.e., harmful, offensive, or detrimental to individuals, groups, or communities.

- **Language Limitations:** Tucano2-qwen-3.7B-Think is primarily designed to interact with Portuguese. Other languages might challenge its comprehension, leading to potential misinterpretations or errors in response.

- **Repetition and Verbosity:** Tucano2-qwen-3.7B-Think may get stuck on repetition loops (especially if the repetition penalty during generations is set to a meager value) or produce verbose responses unrelated to the prompt it was given.

Hence, even though Tucano2-qwen-3.7B-Think is released with a permissive license, we urge users to perform their risk analysis on them if they intend to use them for real-world applications.

[Evaluations, aggregate table]
## Evaluations

The table below compares the Tucano2 (Think variant) series against other reasoning models of similar size. We divide our evaluations into two sets:

- **Knowledge & Reasoning:** ARC-Challenge, ENEM, BLUEX, OAB Exams, BELEBELE, MMLU, GSM8K-PT
- **Instruction Following:** IFEval-PT

The NPM (Normalized Performance Metric) provides a balanced view of model performance across tasks, accounting for each task's inherent difficulty by normalizing its evaluation score relative to its random baseline.

We do not include coding benchmarks in this table because the Think models were not trained on coding data during post-training and thus perform poorly on them. For coding skills, we recommend using the Instruct models instead, which were trained with coding data and perform much better on coding benchmarks.

|                             | Total Avg. | Knowledge & Reasoning (NPM) | Instruction Following |
| --------------------------- | ---------- | --------------------------- | --------------------- |
| **Tucano2-qwen-3.7B-Think** | 51.27      | 54.07                       | 31.67                 |
| SmolLM3-3B                  | 48.58      | 46.28                       | 64.67                 |
| Qwen3-4B                    | 46.35      | 40.97                       | 84                    |
| Qwen3-1.7B                  | 36.54      | 32                          | 68.33                 |
| **Tucano2-qwen-1.5B-Think** | 27.54      | 26.67                       | 33.67                 |
| Qwen3-0.6B                  | 24.11      | 19.22                       | 58.33                 |
| **Tucano2-qwen-0.5B-Think** | 14.41      | 12.52                       | 27.67                 |

[Acknowledgements and License]
## Aknowlegments

Polyglot is a project funded by the Federal Ministry of Education and Research (BMBF) and the Ministry of Culture and Science of the State of North Rhine-Westphalia (MWK) as part of TRA Sustainable Futures (University of Bonn) and the Excellence Strategy of the federal and state governments.

We also gratefully acknowledge the granted access to the [Marvin cluster](https://www.hpc.uni-bonn.de/en/systems/marvin) hosted by [University of Bonn](https://www.uni-bonn.de/en) along with the support provided by its High Performance Computing & Analytics Lab.

## License

Tucano2-qwen-3.7B-Think is licensed under the Apache License, Version 2.0. For more details, see the [LICENSE](LICENSE) file.
