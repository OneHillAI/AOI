# docs / post-training-datasets-sft-dpo

source_url: https://huggingface.co/datasets/llm-jp/llm-jp-4.1-thinking-sft-data ; https://huggingface.co/datasets/llm-jp/llm-jp-4.1-33b-thinking-dpo-data
retrieval_date: 2026-11-19
exists: yes
retrieved: true (AnswerCarefully licence: exists yes, retrieved false, HTTP 401 gated)

Verbatim extracts (publisher text, not edited). Notes by OneHill are marked NOTE.

NOTE (OneHill): Hugging Face API for llm-jp/llm-jp-4.1-thinking-sft-data and the three 4.1 DPO datasets: gated=false, parquet files listed, no licence tag in the hub metadata (licences are stated per subset in the card). AnswerCarefully (llm-jp/AnswerCarefully) is gated "manual" and carries licence:other; its LICENSE and README returned HTTP 401 without login, so its terms were NOT read. ac-self-inst is gated "auto", licence:other.

## llm-jp-4.1-thinking-sft-data: card body (OneHill selected the Overview and Data Sources and Notes sections)
```
## Overview

This dataset is a supervised fine-tuning (SFT) dataset used to train `llm-jp-4.1-*-thinking` models.

This dataset is constructed from prompts and conversations collected from multiple data sources. For most subsets, reasoning processes and final responses used for LLM-jp-4.1 SFT were generated or augmented using [gpt-oss-120b](https://huggingface.co/openai/gpt-oss-120b).
For the tool-calling and agentic data derived from NVIDIA Nemotron datasets, the original conversations and trajectories were generated using multiple language models. See the "Nemotron Agentic Mix" section below for details.

The splits `reasoning_low`, `reasoning_medium`, and `reasoning_high` correspond to different reasoning effort settings used when generating responses with gpt-oss-120b.

To support the continued development of LLM-jp, we would greatly appreciate it if you could share how you utilize LLM-jp outcomes via the [survey form](https://forms.gle/AvbNXTNT2ADsssHq5).

## Data Sources and Licenses

`llm-jp-4.1-*-thinking` are constructed based on the following data sources.
Since each dataset has its own license, please ensure compliance with the respective licenses when using this dataset.
Some subsets cannot be redistributed due to licensing restrictions and are therefore not included.

| Dataset                                                                                                                                                                                                                                        | License                                                         | Notes                                                   |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- | ------------------------------------------------------- |
| [ac_002](https://huggingface.co/datasets/llm-jp/AnswerCarefully)                                                                                                                                                                               | answer-carefully-dataset-tou                                    | Not included due to redistribution restrictions         |
| [daring_anteater](https://huggingface.co/datasets/nvidia/Daring-Anteater)                                                                                                                                                                      | CC BY 4.0                                                       | -                                                       |
| [flan](https://huggingface.co/datasets/allenai/dolmino-mix-1124)                                                                                                                                                                               | ODC-BY                                                          | -                                                       |
| [ichikara](https://liat-aip.sakura.ne.jp/wp/llm%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E6%97%A5%E6%9C%AC%E8%AA%9E%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%A9%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%87%E3%83%BC%E3%82%BF%E4%BD%9C%E6%88%90/) | -                                                               | Requires paid license, not included                     |
| [jaster_v1.4.1](https://github.com/llm-jp/llm-jp-eval/tree/v1.4.1)                                                                                                                                                                             | CC BY-SA 4.0, CC BY-SA 3.0, CC BY 4.0, BSD-3, Apache-2.0, MIT   | -                                                       |
| [llmjp_extraction_wiki_ja_v0.x](https://huggingface.co/datasets/llm-jp/extraction-wiki-ja)                                                                                                                                                     | Apache-2.0                                                      | -                                                       |
| [llmjp_magpie_sft_v1.0](https://huggingface.co/datasets/llm-jp/magpie-sft-v1.0)                                                                                                                                                                | Apache-2.0                                                      | -                                                       |
| llmc_math_dataset                                                                                                                                                                                                                              | -                                                               | To be released                                          |
| [logical_math_coding_wizard8x22b](https://huggingface.co/datasets/llm-jp/wizardlm8x22b-logical-math-coding-sft-ja)                                                                                                                             | Apache-2.0                                                      | -                                                       |
| [multiturn_calm3](https://huggingface.co/datasets/kanhatakeyama/AutoMultiTurnByCalm3-22B)                                                                                                                                                      | Apache-2.0, CC BY-SA 3.0, CC0, CC BY 4.0                        | -                                                       |
| [nemotron_post_v2_stem](https://huggingface.co/datasets/nvidia/Nemotron-Post-Training-Dataset-v2)                                                                                                                                              | CC BY 4.0                                                       | -                                                       |
| [nemotron_post_v3_chat](https://huggingface.co/datasets/nvidia/Nemotron-Instruction-Following-Chat-v1)                                                                                                                                         | CC BY 4.0                                                       | -                                                       |
| [nemotron_post_v3_if](https://huggingface.co/datasets/nvidia/Nemotron-Instruction-Following-Chat-v1)                                                                                                                                           | CC BY 4.0                                                       | -                                                       |
| [nemotron_post_v3_math](https://huggingface.co/datasets/nvidia/Nemotron-Math-v2)                                                                                                                                                               | CC BY-SA 4.0                                                    | -                                                       |
| [random_to_fixed_multiturn_calm3](https://huggingface.co/datasets/kanhatakeyama/ramdom-to-fixed-multiturn-Calm3)                                                                                                                               | Apache-2.0                                                      | -                                                       |
| synthetic_if_ja                                                                                                                                                                                                                                | -                                                               | To be released                                          |
| self_system_question                                                                                                                                                                                                                           | CC BY 4.0                                                       | Model-related questions     |
| [synthetic_jp_en_coding](https://huggingface.co/datasets/llm-jp/Synthetic-JP-EN-Coding-Dataset)                                                                                                                                                | Apache-2.0                                                      | -                                                       |
| system_prompt_question                                                                                                                                                                                                                         | CC BY 4.0                                                       | Model identity and metadata |
| [nemotron3_sft_chat_v3](https://huggingface.co/datasets/nvidia/Nemotron-SFT-Instruction-Following-Chat-v3) | CC BY 4.0, ODC-BY | - |
| [nemotron3_sft_science_vendor](https://huggingface.co/datasets/nvidia/Nemotron-SFT-Science-v2) | CC BY-SA 4.0 | - |
| [table_gpt_train_large](https://huggingface.co/datasets/LipengCS/Table-GPT) | MIT | - |
| [nemotron3_sft_multilingual_v2_math_ko_stackoverflow](https://huggingface.co/datasets/nvidia/Nemotron-SFT-Multilingual-v2) | CC BY-SA 4.0 | - |
| [nemotron3_sft_multilingual_v2_math_ja_stackoverflow](https://huggingface.co/datasets/nvidia/Nemotron-SFT-Multilingual-v2) | CC BY-SA 4.0 | - |
| nemotron_agentic_mix_v0.1.1 | CC BY 4.0 | Derived from [NVIDIA Nemotron-Agentic-v1](https://huggingface.co/datasets/nvidia/Nemotron-Agentic-v1) and [NVIDIA Nemotron-SFT-Agentic-v2](https://huggingface.co/datasets/nvidia/Nemotron-SFT-Agentic-v2) |
| nemotron_agentic_mix_v0.1.1_ja | CC BY 4.0 | Japanese translation of `nemotron_agentic_mix_v0.1.1` generated using `gpt-oss-120b` |
```
```
## Notes

* This dataset contains reasoning processes and responses generated by a large language model (`gpt-oss-120b`).
* Generated content may include errors, inaccuracies, biases, or harmful outputs.
```

## llm-jp-4.1-33b-thinking-dpo-data: card body, overview and the excluded rows
```
## Overview

This dataset is a Direct Preference Optimization (DPO) dataset used to train [llm-jp-4.1-33b-thinking](https://huggingface.co/llm-jp/llm-jp-4.1-33b-thinking).

It is constructed by pairing multiple candidate responses for a given prompt and selecting preferred (chosen) and non-preferred (rejected) responses. The splits `reasoning_low`, `reasoning_medium`, and `reasoning_high` correspond to different reasoning effort settings used during response generation.

The fields `chosen_analysis`, `chosen_final`, `rejected_analysis`, and `rejected_final` are generated using a model trained via supervised fine-tuning (SFT). These responses are then evaluated by [gpt-oss-120b](https://huggingface.co/openai/gpt-oss-120b), which determines the preferred (chosen) and non-preferred (rejected) responses.

To support the continued development of LLM-jp, we would greatly appreciate it if you could share how you utilize LLM-jp outcomes via the [survey form](https://forms.gle/AvbNXTNT2ADsssHq5).
```
Excluded-subset rows from the DPO source table: ac_self_inst "answer-carefully-dataset-tou" "Not included due to redistribution restrictions"; ichikara "Requires paid license, not included"; llmc_math_dataset "To be released".
