doc_type: docs
entity: minicpm5
variant/applies-to: the datasets the MiniCPM5-1B card names as its training corpus and post-training data
source_url: https://huggingface.co/datasets/openbmb/Ultra-FineWeb ; /Ultra-FineWeb-L3 ; /UltraData-Math ; /UltraData-SFT-2605 ; RL sets listed below
retrieval_date: 2026-11-19
exists: yes
retrieved: partly (three pretraining dataset cards read in full; the SFT dataset card is gated and NOT read)

## openbmb/Ultra-FineWeb (card read, raw README 200)
Licence metadata and text: "license: apache-2.0"; "This project is released under the Apache 2.0. Please note that since Ultra-FineWeb is built using multiple datasets, users should check the LICENSE of each dataset individually to ensure proper usage and compliance." gated: false. Repo contains a LICENSE file.
Content: "approximately 1T tokens" English and "approximately 120B tokens" Chinese, filtered from FineWeb and Chinese FineWeb sources (IndustryCorpus2, MiChao, WuDao, SkyPile, WanJuan, ChineseWebText, TeleChat, CCI3). Card: "Ultra-FineWeb serves as a core pre-training web dataset for the MiniCPM4 Series and MiniCPM5 Series models." and, in the 2026.05.25 news line, "Ultra-FineWeb serves as the core pre-training web dataset for MiniCPM5-1B." Also released: the fastText classifier (openbmb/Ultra-FineWeb-classifier) and Ultra-FineWeb-L1 (2026-08-20 news line: built from Common Crawl snapshots up to CC-MAIN-2025-51).

## openbmb/Ultra-FineWeb-L3 (card read)
"license: apache-2.0", gated false, LICENSE file present. "it leverages MiniCPM4 and Qwen3 to perform Q&A Pair Generation and Multi-style Rewriting, producing 400B+ English tokens and 200B+ Chinese tokens." and "it serves as key training data for the decay phase of MiniCPM5-1B." Acknowledgements list the L3 refinement models: MiniCPM4 Series, Qwen3 Series (the card elsewhere says "Qwen-30B-A3"). So the synthetic pretraining tier was generated with a third-party model family.

## openbmb/UltraData-Math (card read)
"license: apache-2.0", "This project is licensed under the Apache 2.0 license." gated false. "290B+ tokens across three progressive tiers (L1 170.5B, L2 33.7B, L3 88B)". Says it "has been applied to the mathematical pre-training of the MiniCPM Series models." L2 selection "Uses proprietary large models to annotate seed data" (the annotating models are not named). Card YAML still has the placeholder "arxiv: xxxx.xxxxx" but the text cites arXiv 2602.09003.

## openbmb/UltraData-SFT-2605 (card NOT read)
Hub API metadata: "gated": "auto" (login and accepting the gate required), license apache-2.0, 1,510 files, tags sft, reasoning, math, code, language en, zh, size_categories 10M<n<100M, createdAt 2026-05-21, lastModified 2026-05-28. The raw README returned: "Access to dataset openbmb/UltraData-SFT-2605 is restricted. You must have access to it and be authenticated to access it. Please log in." exists: yes, retrieved: false for the card text. The model card's claim "the SFT data is released as UltraData-SFT-2605" is therefore confirmed only as "a dataset of that name exists, is tagged Apache-2.0 and sits behind an automatic Hugging Face access gate"; its contents, sources and provenance statement were not read. Nothing is scored on its content.

## RL datasets named on the model card (Hub API metadata only, cards not read)
BytedTsinghua-SIA/DAPO-Math-17k: apache-2.0, ungated. THU-KEG/LongWriter-Zero-RLData: apache-2.0, ungated. google-research-datasets/nq_open: cc-by-sa-3.0 (ShareAlike), ungated. mandarjoshi/trivia_qa: licence metadata "unknown", ungated.
Not released or not named: the "synthesized verifiable RLVR data" and the "pair-wise RLHF signals" (no dataset link on the card).

## Reading
Public and Apache-2.0-tagged on the Hub: Ultra-FineWeb, Ultra-FineWeb-L3, UltraData-Math (read), UltraData-SFT-2605 (gated, unread). The Ultra-FineWeb card itself warns that source-dataset licences must be checked individually. Whether these three pretraining sets are the whole pretraining corpus is the publisher's statement ("The training corpus is released alongside the model as ...") and was not independently verifiable: no token count for MiniCPM5-1B pretraining and no code-data source is stated on the card.
