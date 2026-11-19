doc_type: technical_report
entity: boldt
variant/applies-to: the Boldt model series (base models trained for the paper, including Boldt-DC-350M and Boldt-DC-1B)
source_url: https://arxiv.org/abs/2604.28075 (HTML v3, 23 Oct 2026: https://arxiv.org/html/2604.28075); proceedings: https://aclanthology.org/2026.emnlp-main.1473/ (EMNLP 2026, pages 33690-33710)
retrieval_date: 2026-11-19
exists: yes
retrieved: true (arXiv HTML text read; ACL Anthology page confirmed, PDF not parsed)

## Governing clauses (verbatim extracts)

[Authors and affiliation] "Ansar Aynetdinov, Patrick Haller, Alan Akbik", "Affiliation: Humboldt-Universität zu Berlin". Acknowledgments: DFG Emmy Noether grant "Eidetic Representations of Natural Language" (project 448414230); HPC resources from NHR@FAU (project c107fa). Paper licence on arXiv: CC BY 4.0.

[From scratch - PUBLISHER CLAIM, in a document] "By training language models from scratch on these filtered subsets, we isolate the impact of each semantic property on downstream performance". Appendix B gives the architecture, initialisation is not discussed; no base checkpoint is named anywhere in the paper. Tokenizer: "we train dedicated BPE tokenizers (vocabulary size 32,000) for each subset".

[Abstract, claims] "We release our German language models (called Boldt), as well as our cleaned evaluation benchmarks to the research community. Our experiments indicate that they achieve state-of-the-art results despite training on 10-360x fewer tokens than comparable models."

[Data] "Our data pipeline is built upon the German split of the FineWeb2 (FW2-DE) dataset". Three classifier tiers (Coherence, Information Value, Educational Quality); "Dense-Core ... the intersection of these three filters".

[Annotation recipe, Appendix A] "We first used an LLM to score 500k randomly sampled FW2-DE documents ... For Educational Quality, we use the prompt defined by Lozhkov et al. (2024), while for Coherence and Information Value we define our own prompt, provided in Figure 6." "The LLM that we use for initial annotation is Llama-3.3-70B-Instruct." "We then fine-tuned three respective snowflake-arctic-embed-m-v2.0 ... regression models on the annotated 500k sample". "We report their performance on the holdout test set in Table 6 and release them to the public" (Coherence micro F1 84.32, Information Value 78.45, Educational Quality 75.61).

[Training setup, Appendix B] 350M: 24 layers, hidden 1024, FFN 4096; 1B: 16 layers, hidden 2048, FFN 8192; context 2048. Cosine schedule, peak LR 5e-4, AdamW (0.9, 0.95), weight decay 0.1, batch 0.5M tokens, bf16. "We rely on Huggingface's Nanotron (v0.4), Datatrove (v0.5), and TRL (v0.25.1) libraries ... All pre-trianing runs were conducted on 8xA100 and 4xH100 Nvidia GPUs". No GPU-hour or energy figure is given. No training configs or code repository are linked.

[Release, section 6] "We release our trained models, called Boldt, together with the filtered FineWeb2 subsets they were trained on, as well as the updated benchmarks from our evaluation suite to the research community. In addition to all the base models we trained as part of our experiments, we release an additional pre-trained model: Boldt-1B. A 1B parameter model trained on a combination of Dense-Core and a corpus of 6B tokens of news data in German obtained using the Fundus library". Footnote link: https://huggingface.co/Boldt.

[Evaluation] Benchmarks: Global MMLU (German, used unchanged, 0 re-translated), ARC-Challenge, ARC-Easy, HellaSwag, LAMBADA, OpenBookQA, "re-translated ... using the state-of-the-art machine translation Tower+ 72B model". Table 9 / Table 5: Boldt-DC-350M avg 40.16; Boldt-DC-1B 44.05 (MMLU 31.06, ARC-C 35.99, ARC-E 57.30, HellaSwag 48.69, LAMBADA 42.80, OBQA 48.48); LLaMmlein-1B 40.78; Gemma-3-1B 39.77; Llama-3.2-1B 37.90. Reference-model token counts marked with an asterisk. The paper does not describe a benchmark decontamination check, and all results are the authors' own.

[Licences, Appendix C] FineWeb2 "released under the ODC-By 1.0 license and is subject to CommonCrawl's Terms of Use"; SmolTalk2 Apache 2.0; snowflake-arctic-embed-m-v2.0 Apache 2.0; "Llama-3.3-70B-Instruct, used for initial data annotation and as one of the LLM-as-a-judge evaluators, is governed by the Llama 3.3 Community License Agreement."

[Safety / limitations] "We do not evaluate our models for toxic content generation, demographic biases, or harmful stereotypes." "Our experiments are limited to models up to 1B parameters trained on at most 200B tokens." "While this work does not provide direct empirical evidence that our findings generalize to other languages ... We leave the validation of our findings across different language families to future work." Language scope: "Our investigation focuses exclusively on German".
