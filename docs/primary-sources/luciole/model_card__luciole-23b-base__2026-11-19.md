doc_type: model_card
entity: luciole
variant/applies-to: OpenLLM-France/Luciole-23B-Base (the base of the scored Instruct release; sibling release, NOT scored)
source_url: https://huggingface.co/OpenLLM-France/Luciole-23B-Base (raw README.md)
repo_sha_read: 258bab249eb0155d4ebc3a97e750a307f1994db3 (created 2026-02-17, last modified 2026-11-12)
retrieval_date: 2026-11-19
exists: yes
retrieved: true

## Governing clauses (verbatim extracts, README.md, 21,972 bytes)

[Front matter] "license: apache-2.0" ; languages "fr, en, it, de, es, pt, nl, ar" ; "datasets: OpenLLM-France/Luciole-Training-Dataset" ; training_progress "num_steps: 1170080, num_tokens: 4907671224320, context_length: 131072".

[Description and languages] "Luciole-23B-Base is a pretrained 23B parameter causal language model developed by LINAGORA and the OpenLLM-France consortium ... funded by BPI France through the France 2030 program. It was trained on the GENCI supercomputer Jean Zay, managed by IDRIS." "trained on around 5 trillion tokens of multilingual data, including English (41.9%), French (30.4%), German (3.8%), Spanish (3.5%), Italian (1.9%), Portuguese (1.3%), Dutch (1.0%), Arabic (0.5%), and a small subset of regional languages ... (0.4%)". "parallel data from a selection of languages (1.7%), as well as several programming languages (9.2%) and English mathematical data (3.5%)."

[Intended use] "trained solely to predict the most probable next word in a sequence. It is designed as the first brick in a more complex training pipeline". "not intended to generate text directly for end use cases. It must be fine-tuned first."

[Bias] "much of our French data comes from older works in the public domain that carry biases from other time periods. While we made efforts to reduce toxic and offensive content ... Luciole-23B-Base may still generate such content." "it is advised to fine-tune Luciole-23B-Base through instruction and preference tuning (DPO, RLHF, etc.)."

[Intermediate checkpoints] "Intermediate checkpoints are released under dedicated revision tags at regular intervals throughout training ... All checkpoints are available at: https://dl.labs.linagora.com/files/models/OpenLLM-France/Luciole-23B-Base/". (The Hugging Face refs API lists only the main branch and no tags; the Linagora URL is a JavaScript file browser whose listing could not be read.)

[Training data and code] "The training dataset used for the pretraining of Luciole-23B-Base is available at OpenLLM-France/Luciole-Training-Dataset." "The training code is available at https://github.com/OpenLLM-France/Luciole-Training. Training used version 2.3.1 of NVIDIA's NeMo framework". Phases: 3.5T tokens initial, 1T continued pretraining, 300B annealing "introducing some instruction-style and reasoning data", then two 50B-token context extensions to 32,768 and 131,072.

[Compute] "pre-trained on 256 - 512 H100 80GB GPUs (64 - 128 nodes) for about 576,587 GPU hours (1,186 hours) on the Jean Zay supercomputer". (6 x 23.2B x 4.9T tokens is about 6.8e23 FLOPs, a OneHill calculation, below the 1e25 systemic-risk threshold.)

[Architecture] "a custom adaptation of the Nemotron3-22B recipe (github.com/NVIDIA-NeMo/NeMo/.../nemotron3_22b.py). It has 23.2 billion free parameters": vocabulary 128,000; 40 blocks; 48 heads; 8 KV heads; hidden 6144; FFN 36864; relu2. Initialiser range 0.009 in the hyperparameter table. The card does not use the words "from scratch" and names no initialising checkpoint.

[Training logs and evaluation] Training logs CSV per phase and evaluation figures are in the repo under metadata/. Baselines: Gaperon-1125-24B, EuroLLM-22B-2512, Mistral-Small-24B-Base-2501. RULER long-context figure included.

[License section] "Copyright (c) 2025-2026 LINAGORA SAS. Luciole-23B-Base is developed by LINAGORA within the OpenLLM-France consortium (PROJET FRANCE2030 OpenLLM-France, funded by Bpifrance) and released under the Apache License 2.0."

[Technical report] "Technical report: coming soon."
