doc_type: model_card
entity: morena
variant/applies-to: vamboai/morena-1.5b-instruct (instruct checkpoint)
source_url: https://huggingface.co/vamboai/morena-1.5b-instruct (raw: https://huggingface.co/vamboai/morena-1.5b-instruct/raw/main/README.md)
repo_sha_read: b9bebd76c5725e570d6186ba400eff87f3a2382b (last modified 2026-10-14T07:57:43Z)
retrieval_date: 2026-11-19
exists: yes
retrieved: true

## Governing clauses (verbatim extracts from README.md, 7,861 bytes, read in full)

[Front matter] "license: apache-2.0" ; "language: [sn, sw, ha, yo, ig, zu, xh, rw, tn, af, nr, pcm, en]" ; "tags: [african-languages, from-scratch, instruct, isheanesu-misi, vambo-ai]" ; "inference: false" ; "base_model: vamboai/morena-1.5b-base". The `datasets:` list names: HuggingFaceFW/fineweb-edu, HuggingFaceFW/fineweb-2, codeparrot/codeparrot-clean, codeparrot/github-code-clean, open-web-math/open-web-math, EleutherAI/proof-pile-2, castorini/wura, allenai/MADLAD-400, castorini/afriberta-corpus, vamboai/fikira, ise-uiuc/Magicoder-OSS-Instruct-75K, m-a-p/CodeFeedback-Filtered-Instruction, vamboai/morena-sft-corpus.

[From scratch - PUBLISHER CLAIM] "MORENA, Sesotho and Setswana for a king, a lord or a chief, is a 1.5B-parameter decoder trained from scratch for twelve Latin-script African languages plus English, French and code. This is the instruction-tuned model described in the paper *MORENA: An African Foundation Model*."

[Languages, with the evidence the card gives] Language list in the "The MORENA family" section: "Twelve languages: Shona, Swahili, Hausa, Yoruba, Igbo, isiZulu, isiXhosa, Kinyarwanda, Setswana, Afrikaans, isiNdebele and Nigerian Pidgin, plus English, French and code. isiNdebele (ISO code nbl) has no FLORES+ or MasakhaNEWS coverage and is evaluated on NCHLT transcripts only." Per-language evidence on the card: translation measured for only five languages ("English into 5 African languages", FLORES+ chrF++ 45.8); Belebele "mean over 10 African languages, 0.24 Yoruba to 0.43 Afrikaans, 0.25 chance"; safety "13 languages"; weakest safety languages "Igbo 75%, Yoruba 82%, Setswana 83%, isiXhosa 87%".

[Headline numbers, publisher-measured] "African bits per byte, mean of 12 (lower is better) 1.441" (Lugha-Llama-8B 1.423, gemma-3-12b-it 2.159, gemma-3-1b-pt 2.335); "Translation, FLORES+ chrF++, English into 5 African languages, 3-shot 45.8 (45.1 to 46.5)" (MADLAD-400-3B 37.8, Lugha-Llama-8B 36.8); "5 African languages into English 48.7 (47.5 to 49.7)" (MADLAD-400-3B 53.6, Lugha-Llama-8B 52.4); "Belebele reading comprehension, released checkpoint 0.309"; "Retrieval QA ... 0.325 (0.297 to 0.355) / 0.73" with "0.25 chance"; "Grounded generation, fully faithful to given facts 23% (22 of 96, 15.6 to 32.3)"; "Tool calling, correct tool / valid JSON (marker prefilled) 98.1% / 100%"; "Safety, share of all 3,341 attempts handled well, 13 languages, 11 categories 89.0% (87.8 to 90.0)"; "Degenerate output 1.3%"; "Refused harmful requests, share of all attempts 91.5%"; "Benign requests answered well 58.9% (53.3 to 64.2)".

[Judge disclosure] "Every number above is a model (google/gemma-3-12b-it) judging a model; no native speaker has yet rated an answer."

[Limitations, publisher's own words] "The model fails to answer 41% of ordinary benign requests well, most of them by refusing; an earlier version once refused to recommend a dry cleaner, citing 'illegal substances or services'. That specific failure is fixed, but the broader over-refusal problem is not. Tool calling is measured with the tool marker prefilled; left to decide for itself the model almost never calls one. Multiple-choice comprehension in African languages is at chance for this model and for every model under 12B measured."

[Checkpoint selection] "It misses that rule on privacy by 0.1 points, on drugs by 1.0 and on violence by 2.6, and on degeneracy, which is 1.3%."

[Chat format] "Single reserved tokens mark turns: `<reserved_0>` opens a user turn and `<reserved_1>` an assistant turn (token ids 3 and 4). `load_example.py` in this repo shows a full prompt. Do not use `<|user|>`-style strings; they are not in the vocabulary and produce degenerate output."

[Files] "`model.safetensors` (bf16), `config.json`, `tokenizer.json`, `modeling_morena.py` (reference implementation, plain PyTorch, no transformers dependency), `load_example.py`, `SHA256SUMS`. A GGUF build for llama.cpp is in `vamboai/morena-1.5b-instruct-gguf`."

[Training] "251.7B tokens of pretraining, 63B tokens of mid-training (315B tokens seen in total; see MORENA 1.5B base), then 4,500 steps of supervised fine-tuning with loss masking and a 500-step safety anneal." "Nine languages were machine-translated from English documents: this is 24% of pretraining tokens seen and 28% including mid-training (57.1B tokens on disk, 21% of the 271B on disk)." "Release lineage: 12,834 A100 GPU-hours, an estimated twenty-five to forty thousand dollars at $2 to $3 per A100-hour". "Architecture: 28 layers x 2048, GQA 16/4, SwiGLU 6144, RoPE theta 500,000, 4,096 context, tied embeddings." "Tokenizer: 65,536-entry byte-fallback BPE trained on the target mix."

[Family] Table lists MORENA 1.5B base (1.485B), 1.5B instruct (1.485B), 0.5B mini (503M, "pruned and distilled from the 1.5B base"), 0.5B mini instruct, 0.2B nano (209M).

[Author, compute] "Isheanesu Misi, Vambo AI. Trained on CINECA Leonardo, with support from the AI Hub for Sustainable Development."

[Licence section] "Apache 2.0. Commercial use is permitted, including fine-tuning and redistributing derivatives, under the terms of the licence. The training corpus is not released with these weights."
