doc_type: docs
entity: boldt
variant/applies-to: the other Boldt releases, which are NOT scored in this entry (follow-ups)
source_url: https://huggingface.co/Boldt/Boldt-1B ; https://huggingface.co/Boldt/Boldt-1B-IT-Preview ; https://huggingface.co/Boldt/Boldt-Phased-350M-200BT ; https://huggingface.co/Boldt/Boldt-MKC-350M-100BT ; https://huggingface.co/Boldt/fineweb2-de-edu-classifier (and siblings)
retrieval_date: 2026-11-19
exists: yes
retrieved: true (cards read; weights not downloaded)

## Why they differ from the scored release (verbatim extracts)
[Boldt-1B, base] Apache-2.0 in front matter, no LICENSE file. "Boldt-1B builds upon the foundation of Boldt-DC-1B by adding 6B tokens of premium German news data, collected continuously since 2022 via the Fundus library. To support complex downstream tasks, it also features a doubled context window of 4096 tokens." Training data: "German Dense-Core subset (FineWeb-2) + 6B tokens high-quality Fundus news data". The news corpus is not published and no licence or publisher terms for the articles are stated (the paper says the articles stem "from the time period between 2022 and February 2026, with smaller numbers of articles going back to 1994"). Different training data, so a different provenance and legal position.
[Boldt-1B-IT-Preview] Apache-2.0 in front matter, no LICENSE file, base_model Boldt/Boldt-1B. "fine-tuned on a curated mixture of 95k German instruction-output pairs": Aya German subset (about 200 pairs), SmolTalk2 German subset ("We adjusted 52k prompts ... and regenerated outputs using Qwen-3.6-27B"), 7k prompts from the r/FragReddit subreddit with Qwen-3.6-27B outputs, 19k synthetic QA pairs from a dump of r/FragReddit posts using Qwen-3.6-27B, and 17k NER tasks. "Preview status. ... It has not undergone systematic safety evaluation and should not be used in production settings without further assessment." The Qwen3.6-27B card declares Apache-2.0 (front matter; LICENSE file not read). The Reddit data terms were not read.
[Research checkpoints, 15 repos] Example: Boldt-Phased-350M-200BT. Front matter Apache-2.0; tags "research-checkpoint"; "released for reproducibility and for studying how different data-filtering choices affect pre-training". Boldt-MKC-350M-100BT is trained on epfml/FineWeb2-HQ (an external subset). The Sorted, Coherence, Edu, IV, Random checkpoints use the other filter subsets.
[Classifiers, 3 repos] No README, no licence declared in metadata, no LICENSE file; trained on Llama-3.3-70B-Instruct labels (see the Llama terms file).
[Evaluation datasets] Boldt/arc_de, hellaswag_de, lambada_openai_de, obqa_de: public; the API reports no licence in the card metadata; machine-translated from English benchmarks with Tower+ 72B (paper).
