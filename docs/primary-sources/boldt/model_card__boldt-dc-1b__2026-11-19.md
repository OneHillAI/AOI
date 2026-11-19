doc_type: model_card
entity: boldt
variant/applies-to: Boldt/Boldt-DC-1B (base)
source_url: https://huggingface.co/Boldt/Boldt-DC-1B (raw: https://huggingface.co/Boldt/Boldt-DC-1B/raw/main/README.md)
repo_sha: e50b6a3fe8ac0ca9575293347ee0ad898eb8dd7e (created 2026-05-02, last modified 2026-05-06)
retrieval_date: 2026-11-19
exists: yes
retrieved: true

## Governing clauses (verbatim extracts from README.md)

[Front matter] "license: apache-2.0" ; tags include "custom_code" (no custom code file exists in the repo) and "german". No licence section in the body.

[From scratch - PUBLISHER CLAIM] "**Boldt** is a series of German Small Language Models (SLMs) trained from scratch. Our initial release includes four models:" followed by Boldt-DC-350M, Boldt-DC-1B (this model), Boldt-1B, Boldt-1B-IT-Preview.

[Model] "**Boldt-DC-1B** represents the highly optimized 1-billion parameter foundation of this methodology, trained over multiple epochs on 200B tokens of our extreme-signal dataset." "Parameters: ~1 Billion ; Context Window: 2048 tokens ; Training Data: German Dense-Core subset (FineWeb-2) [200B tokens] ; Language: German".

[Usage] "This is a base language model, not an instruction-tuned model. It is not optimized for chat or instruction following." The code sample loads model_name = "Boldt/Boldt-1B", not Boldt-DC-1B (card error; a user following it gets the sibling with news data).

[Evaluation, publisher] "Despite being trained on substantially fewer tokens, the Boldt-1B family outperforms other 1B-class models on German tasks and performs competitively with much larger multilingual models." Row: "Boldt-DC-1B (this model) | 200B | 31.06 | 35.99 | 57.30 | 48.69 | 42.80 | 48.48 | 44.05". 1B-class comparison averages: LLaMmlein-1B 40.78, Gemma-3-1B 39.77, Llama-3.2-1B 37.90, Qwen3.5-0.8B-Base 37.97. Larger references: EuroLLM-1.7B 42.94, Qwen3-1.7B-Base 44.89, Buble-LM-2B 42.63, Gemma-2-2B 46.62, Gemma-4-E2B 50.08. The card links a "modernized German benchmark suite" and the paper. A chart (boldt_1b_evaluation.png) is in the repo.

[Safety] Same text as the 350M card: "We have not conducted systematic model evaluations of toxicity, demographic biases, or harmful stereotypes."

## Repo facts (API, 2026-11-19)
Files: README.md, boldt_1b_evaluation.png, config.json, generation_config.json, logo.png, merges.txt, model.safetensors (2,409,779,720 bytes, LFS sha256 fc584c7872bc3979...), special_tokens_map.json, tokenizer files. No LICENSE file (raw/main/LICENSE returned HTTP 404). config.json: LlamaForCausalLM, 16 layers, hidden 2048, FFN 8192, 16 heads, context 2048, vocab 32000, bfloat16; 1,204,881,408 parameters. Not gated. Hugging Face scan: scansDone false on this repo (Boldt-DC-350M: scansDone true), filesWithIssues empty on both.
