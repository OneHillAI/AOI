# docs / corpus-llm-jp-corpus-midtraining-v2

source_url: https://gitlab.llm-jp.nii.ac.jp/datasets/llm-jp-corpus-midtraining-v2 (raw README.md)
retrieval_date: 2026-11-19
exists: yes
retrieved: true

Verbatim extracts (publisher text, not edited). Notes by OneHill are marked NOTE.

NOTE (OneHill): public GitLab project (API visibility: public, created 2026-03-16, last activity 2026-06-10). Only the README was fetched. Of note: the `nemotron_pretraining_code_v2` sub-corpus (491B tokens) is under the "NVIDIA Data Access Agreement for Model Training", which is a custom agreement, not an open licence; the `llm-jp-IPT_v0.3.2` sub-corpus is "Various licenses" (responses generated with gpt-oss-120b).

```
# LLM-jp Corpus Midtraining v2

This dataset is a bilingual corpus (Japanese and English) designed for mid-training of large language models.
It was created by the Corpus Construction Working Group of [LLM-jp](https://llm-jp.nii.ac.jp/).
This corpus was used for training the LLM-jp-4 series of models.

To support the continued development of LLM-jp, we would greatly appreciate it if you could share how you utilize LLM-jp outcomes via the [survey form](https://forms.gle/AvbNXTNT2ADsssHq5).

## Dataset Structure and Details
The dataset is structured as follows. Each directory contains multiple jsonl.gz files.

```
. (Total File Size : 858GB)
├── en
│   ├── cosmopedia_v2 (22B)
│   ├── dolma3_dolmino_pool (4B)
│   ├── dolmino-mix-1124 (26B) 
│   ├── llama_nemotron_post_training_dataset (0.6B)
│   ├── llm-jp-IPT_v0.3.2 (52B)
│   ├── nemotron_instruction_following_chat_v1 (2B)
│   ├── nemotron_math_v2 (4B)
│   ├── nemotron_post_training_dataset_v1 (91B)
│   ├── nemotron_post_training_dataset_v2 (0.2B)
│   ├── nemotron_pretraining_code_v2 (491B)
│   ├── nemotron_pretraining_specialized_v1 (8B)
│   ├── stack_math_qa (1B)
│   └── swallow_code_v2 (63B)
└── ja
    ├── llm-jp-IPT_v0.3.2 (35B)
    └── nemotron_post_training_dataset_v2 (6B)
```

( ) : Number of tokens counted with llm-jp-tokenizer v4

Each jsonl file consists of the following fields:
- `ID`: data ID
- `text`: text content

## License
The sources and licenses of each dataset are listed below:

- `cosmopedia_v2`: odc-by 
  - https://huggingface.co/datasets/HuggingFaceTB/smollm-corpus
- `dolma3_dolmino_pool`: odc-by
  - https://huggingface.co/datasets/allenai/dolma3_dolmino_pool
- `dolmino-mix-1124`: odc-by
  - https://huggingface.co/datasets/allenai/dolmino-mix-1124
- `llama_nemotron_post_training_dataset`: CC BY 4.0
  - https://huggingface.co/datasets/nvidia/Llama-Nemotron-Post-Training-Dataset
- `llm-jp-IPT_v0.3.2`: Various licenses.
  - A dataset constructed by generating responses with gpt-oss-120b for the instructions in [llm-jp-corpus-midtraining-v1](https://gitlab.llm-jp.nii.ac.jp/datasets/llm-jp-corpus-midtraining-v1).
  - The license varies depending on each constituent dataset. Please refer to [this link](https://gitlab.llm-jp.nii.ac.jp/datasets/llm-jp-corpus-midtraining-v1) for details.
- `nemotron_instruction_following_chat_v1`: CC BY 4.0
  - https://huggingface.co/datasets/nvidia/Nemotron-Instruction-Following-Chat-v1
- `nemotron_math_v2`: CC BY-SA 4.0
  - https://huggingface.co/datasets/nvidia/Nemotron-Math-v2
- `nemotron_post_training_dataset_v1`: CC BY 4.0
  - https://huggingface.co/datasets/nvidia/Nemotron-Post-Training-Dataset-v1
- `nemotron_post_training_dataset_v2`: CC BY 4.0
  - https://huggingface.co/datasets/nvidia/Nemotron-Post-Training-Dataset-v2
- `nemotron_pretraining_code_v2`:  NVIDIA Data Access Agreement for Model Training
  - https://huggingface.co/datasets/nvidia/Nemotron-Pretraining-Code-v2
- `nemotron_pretraining_specialized_v1`: CC BY-SA 4.0, GFDL
  - https://huggingface.co/datasets/nvidia/Nemotron-Pretraining-Specialized-v1
- `stack_math_qa`: CC BY 4.0
  - https://huggingface.co/datasets/math-ai/StackMathQA
- `swallow_code_v2`: Apache-2.0
  - https://huggingface.co/datasets/tokyotech-llm/swallow-code-v2

Copyright for each document in this corpus belongs, in principle, to the original author of the document.
This corpus is intended for use in pretraining large language models, and is distributed from a server located in Japan to comply with Japanese copyright law.
Usage, including redistribution, is permitted within the scope of each license, but please note that Japanese copyright law may not apply if redistributed from servers outside Japan.

## Change log
- [2026/04/03] Initial release
```
