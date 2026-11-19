doc_type: model_card
entity: luciole
variant/applies-to: OpenLLM-France/Luciole-23B-Instruct-1.1 (the scored release; the 8B and 1B Instruct-1.1 cards differ only in sizes, one learning rate and one evaluation sentence)
source_url: https://huggingface.co/OpenLLM-France/Luciole-23B-Instruct-1.1 (raw: https://huggingface.co/OpenLLM-France/Luciole-23B-Instruct-1.1/raw/main/README.md)
repo_sha_read: 770af27b30611fc513d41cae28cb45e3ad9a79b3 (created 2026-07-07, last modified 2026-11-12)
retrieval_date: 2026-11-19
exists: yes
retrieved: true

## Governing clauses (verbatim extracts, README.md, 13,920 bytes)

[Front matter] "license: apache-2.0" ; "language: - fr - en" ; "base_model: - OpenLLM-France/Luciole-23B-Base" ; "datasets: - OpenLLM-France/Luciole-PostTraining-Dataset-1.1".

[What it is] "Luciole-23B-Instruct-1.1 is a fine-tuned and aligned version of Luciole-23B-Base, an open-source, multilingual causal language model created by OpenLLM-France. Luciole-23B-Instruct-1.1 was developed by LINAGORA and the OpenLLM-France consortium as a part of the OpenLLM France project, funded by BPI France through the France 2030 program."

[Training phases] "Training of Luciole-23B-Instruct-1.1 was conducted on Jean Zay in three phases: (i) a supervised fine-tuning (SFT) phase on instruction data with thinking traces, (ii) an SFT phase on instruction data without thinking traces, and (iii) a final preference alignment phase using Direct Preference Optimization (DPO). The training data covers topics in math, science, coding, general chat, RAG and translation."

[Status] "Note that Luciole-23B-Instruct-1.1 is only the first iteration of post-trained models based on Luciole-23B-Base. Development of the Luciole models is an active, ongoing project and further iterations, including models trained on higher proportions of French data, are planned. In the spirit of open-source, we share the model weights and training recipes to facilitate research and to provide open source building blocks for other training projects."

[Links on the card] "License: Apache 2.0" ; "Training repository: Luciole-Training (https://github.com/OpenLLM-France/Luciole-Training/tree/main/finetune)" ; "Training data: Luciole-PostTraining-Dataset-1.1" ; "Technical report: coming soon."

[Risks] "the model should be thoroughly tested for target use cases before being incorporated in industrial pipelines. Training has mostly focused on instruction following, and additional training would be necessary for tasks specifically focused on code generation or mathematical problem solving. It is also susceptible to hallucinations". "Luciole-23B-Instruct-1.1 was post-trained almost entirely on English data (in contrast to its base model ... which was trained on roughly 30% French data)." "Finally, Luciole-23B-Instruct-1.1 was trained on sequences of 16,384 tokens (in contrast to its base model, whose context window was extended to 131,000 tokens)."

[No safety statement] The Instruct card contains no section on safety evaluation, misuse, an acceptable-use policy or a guard model, and the word "safety" does not appear in it. (Contrast the Thinking card, which has a safety note; see model_card__luciole-23b-thinking-1-1.)

[Chat template] "chat template inspired from Qwen3-1.7B"; default system prompt "You are a helpful AI assistant named Luciole, trained by LINAGORA and OpenLLM France." Template uses <|im_start|> / <|im_end|>. (Template format only; no Qwen weights are named as a base.)

[Procedure table] SFT with thinking: 2.6M samples, 4 epochs; SFT without thinking: 2.1M samples, 4 epochs; DPO without thinking: 284K samples, 1 epoch, beta 5, max sequence length 16384.

[Interim checkpoints] "Links to the interim models: SFT with thinking, SFT without thinking" (https://dl.labs.linagora.com/files/models/OpenLLM-France/Luciole-23B-SFT-Thinking-1.1/ and .../Luciole-23B-SFT-1.1/; a JavaScript file browser, listing not readable).

[Evaluation] "Overall, Luciole-23B-Instruct-1.1 performs comparably with other open source instruct models of the same size. The model performs particularly well on instruction following benchmarks. Its performance on French language instruction following (ifeval-fr) is notable ..." Figure benchmark_eval.png (see docs__instruct-benchmark-figure).

[Serving] Ollama via the official GGUF files and a Modelfile; vLLM docker command with "--enable-auto-tool-choice --tool-call-parser hermes"; "Warning: Tool usage is still a work in progress, see BFCL v4 results".

[License section, added 2026-11-10 per commit history] "Copyright (c) 2025-2026 LINAGORA SAS. Luciole-23B-Instruct-1.1 is developed by LINAGORA within the OpenLLM-France consortium (PROJET FRANCE2030 OpenLLM-France, funded by Bpifrance) and released under the Apache License 2.0."

[Contact] "contact@openllm-france.fr" (not used).
