doc_type: docs
entity: boldt
variant/applies-to: training data of Boldt-DC-350M and Boldt-DC-1B (Dense-Core subset) and its upstream corpus
source_url: https://huggingface.co/datasets/Boldt/fineweb2-de-dc (README.md and API); https://huggingface.co/datasets/HuggingFaceFW/fineweb-2 (README.md); https://huggingface.co/Snowflake/snowflake-arctic-embed-m-v2.0
retrieval_date: 2026-11-19
exists: yes
retrieved: true

## Boldt/fineweb2-de-dc dataset card (verbatim extracts)
[Front matter] "license: odc-by". Public, ungated, 183 files (parquet shards plus README.md and .gitattributes); no separate LICENSE file; last modified 2026-11-01.
[Contents] "It contains ~5% of FW2-DE" ; Documents 24,446,297 ; Tokens 28B ; "Source: German split of FineWeb2 (deu_Latn, ~496M documents)". Selection: coherence_score >= 3, iv_score >= 3, edu_score >= 3 (rounded). Scores come from the Boldt classifiers.
[Recipe] "Llama-3.3-70B-Instruct annotated 500k randomly sampled FW2-DE documents, truncated to 4096 tokens. Educational Quality uses the original FineWeb-Edu prompt. Coherence and Information Value use a joint prompt defined in the paper (Appendix A, Figure 6). Three regression heads on snowflake-arctic-embed-m-v2.0 were fine-tuned on these labels ... The classifiers then scored all ~500M FW2-DE documents. They are released here".
[Models trained on it] "Boldt/Boldt-DC-350M: 350M, 200B tokens (7.2 epochs); Boldt/Boldt-DC-1B: 1B, 200B tokens (7.2 epochs)"; also the 100BT, Phased variants and Boldt-1B (plus about 6B tokens of Fundus news).
[Licence] "This dataset is derived from FineWeb2. Like FineWeb2, it is released under the ODC-By 1.0 license and is subject to Common Crawl's Terms of Use."
[Not in the card] The 500k Llama labels, the classifier training script and the scoring pipeline code are not linked. The three sibling filter datasets (fineweb2-de-coherence, -iv, -edu) are also ODC-By and public.

## Classifier repos (Boldt/fineweb2-de-{coherence,iv,edu}-classifier)
API: no README (raw/main/README.md returns "Entry not found"), no licence in metadata (cardData null), no LICENSE file, not gated, files: config.json, model.safetensors (305,959,680 parameters), tokenizer files and two custom-code Python files named configuration_hf_alibaba_nlp_gte.py and modeling_hf_alibaba_nlp_gte.py. Created 2026-08-30. Base model (per paper): snowflake-arctic-embed-m-v2.0, whose Hugging Face card declares "license: apache-2.0" (raw LICENSE file: HTTP 404).

## FineWeb-2 dataset card (verbatim extracts)
"The 🥂 FineWeb2 dataset is fully reproducible, available under the permissive ODC-By 1.0 license". "The data was sourced from 96 CommonCrawl snapshots, spanning the summer of 2013 to April 2024". "The dataset is released under the Open Data Commons Attribution License (ODC-By) v1.0 license. The use of this dataset is also subject to CommonCrawl's Terms of Use." The card has a "Personal and Sensitive Information and opt-out" section.
