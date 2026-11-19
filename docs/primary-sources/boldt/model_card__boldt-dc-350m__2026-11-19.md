doc_type: model_card
entity: boldt
variant/applies-to: Boldt/Boldt-DC-350M (base)
source_url: https://huggingface.co/Boldt/Boldt-DC-350M (raw: https://huggingface.co/Boldt/Boldt-DC-350M/raw/main/README.md)
repo_sha: a00c213b9e579da872149359ed505ef4d5b12786 (created 2026-05-02, last modified 2026-11-01)
retrieval_date: 2026-11-19
exists: yes
retrieved: true

## Governing clauses (verbatim extracts from README.md)

[Front matter] "license: apache-2.0" ; "language: - de" ; "pipeline_tag: text-generation" ; "library_name: transformers". The card body has no licence section and no copyright-holder line; the word "licence" or "license" appears only in the front matter.

[From scratch - PUBLISHER CLAIM] "**Boldt** is a series of German Small Language Models (SLMs) trained from scratch. Our inital release includes three models:" (the list under it names four models).

[Method] "Boldt models are trained for multiple epochs on a highly filtered dataset: the German ***Dense-Core*** subset of [FineWeb-2]. We isolated this subset using a combination of three hierarchical filters: Coherence ... Information Value ... Educational Quality".

[Usage] "**Note:** This is a base language model, not an instruction-tuned model. It is not optimized for chat or instruction following. For best results, use standard text completion rather than chat templates."

[Evaluation, publisher] "Boldt-350M while significantly smaller than the 1B models we compare with, still fares comparatively well, outperforming the much larger, multilingual Gemma-3-1B and Llama-3.2-1B models." Table row: "Boldt-DC-300M (this model) | 200B | 29.29 | 32.24 | 52.87 | 43.21 | 37.48 | 45.86 | 40.16" (MMLU, ARC-C, ARC-E, H-Swag, LAMBADA, OBQA, Avg). Gemma-3-1B average 39.77, Llama-3.2-1B 37.90, LLaMmlein-1B 40.78, Qwen3.5-0.8B-Base 37.97.

[Safety] "We have not conducted systematic model evaluations of toxicity, demographic biases, or harmful stereotypes. Quality filtering may reduce some risks relative to unfiltered web data, but cannot guarantee their absence, and repeated exposure during multi-epoch training could amplify rather than mitigate encoded biases. Users should exercise caution in sensitive use-cases without further evaluation."

## Card inconsistencies noted
- Says "three models" and lists four. Table row calls the model "Boldt-DC-300M" and the text says "Boldt-350M"; the repo and org README say 350M; the API counts 468,239,360 parameters (BF16).
- Card gives no hardware, training-compute, intended-use or out-of-scope section.

## Repo facts (API, 2026-11-19)
Files: .gitattributes, README.md, config.json, generation_config.json, logo.png, merges.txt, model.safetensors (936,503,664 bytes, LFS sha256 ba2964d0d2d3a21b...), special_tokens_map.json, tokenizer.json, tokenizer_config.json, vocab.json. No LICENSE file (GET /raw/main/LICENSE returned HTTP 404). config.json: LlamaForCausalLM, 24 layers, hidden 1024, FFN 4096, 16 heads, max_position_embeddings 2048, vocab_size 32000, bfloat16. Not gated.
