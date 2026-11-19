doc_type: technical_report
entity: tucano-2
variant/applies-to: all Tucano 2 models
source_url: https://arxiv.org/abs/2603.03543 (HTML rendering https://arxiv.org/html/2603.03543)
retrieval_date: 2026-11-19
exists: yes
retrieved: true

## Extracts (VERBATIM from the arXiv HTML rendering; abstract from the arXiv abstract page)


[Title and authors, arXiv abstract page] Tucano 2 Cool: Better Open Source LLMs for Portuguese. Corrêa, Nicholas Kluge; Sen, Aniket; Fatimah, Shiza; Falk, Sophia; Landgraf, Lennard; Kastner, Julia; Flek, Lucie. Submitted 2026/03/03. Subjects: Computation and Language (cs.CL); Artificial Intelligence (cs.AI).

[Abstract] We present Tucano 2, a fully open suite of large language models (LLMs) with 0.5-3.7 billion parameters, designed to address certain gaps in open-source development for Portuguese LLMs. [...] All artifacts associated with Tucano 2 are openly released, including training recipes, logs, and source code, ensuring that our work is reproducible, accessible, and extendable by the broader Portuguese NLP community.

[1 Overview, contribution list and released assets]
In this work, we introduce Tucano 2 , a new generation of open Portuguese LLMs that substantially extends our earlier efforts. We construct a large-scale, high-quality Portuguese corpus of approximately 320 billion tokens, enriched with educational and toxicity annotations and complemented by 9.3 billion synthetic tokens to mitigate domain gaps. To support data curation, we develop auxiliary datasets and train specialized annotation models for educational content, toxicity, and instruction quality. We further assemble a diverse supervised fine-tuning (SFT) corpus covering coding, tool use, structured outputs, mathematical problem solving, and chain-of-thought reasoning, and release a novel dual-reasoning preference dataset to further power direct alignment efforts. Leveraging these resources, we train a family of Portuguese LLMs with parameter counts ranging from 0.5B to 3.5B, using pretraining and continual pretraining regimes. Our models achieve strong gains over prior open Portuguese baselines and outperform similarly sized multilingual models across multiple Portuguese benchmarks. Finally, we release a comprehensive evaluation harness for Portuguese that supports assessment at both early and late training stages, including long-context settings.
 In summary, our main contributions are: 
 • 
 Large-scale Portuguese corpus. A 320B-token cleaned corpus with rich educational and toxicity annotations ( GigaVerbo-v2 ), plus 9.3B synthetic tokens for domain coverage ( GigaVerbo-v2 Synth ).
 • 
 Annotation and filtering models. Educational, toxicity, and instruction-quality classifiers trained from new auxiliary datasets and released for community use.
 • 
 Diverse SFT data. A large supervised fine-tuning collection spanning coding, tool calling, structured output, reasoning, and mathematics ( GigaVerbo-v2 SFT ).
 • 
 Dual-reasoning preference dataset. A new resource for preference optimization that captures complementary aspects of reasoning quality ( GigaVerbo-v2 Preferences ).
 • 
 Tucano 2 model family. Open Portuguese foundation models from 0.5B–3.5B parameters that outperform most prior Portuguese models of similar size ( Tucano 2 ).
 • 
 Portuguese evaluation suite. Benchmarks covering early- and late-stage training, including long-context evaluation.
 • 
 Fully open release. All datasets, models, training recipes, and evaluation code are publicly released under permissive licenses.
 This work is part of the broader Polyglot project. The methodology and findings presented here extend to additional language-specific studies conducted within the same framework, including Hindi (e.g., LilMoo ) and Bengali (e.g., LilTii ). For further details on these parallel efforts and associated resources, please refer to the Polyglot project page: huggingface.co/Polygl0t .
 Released Assets
 Base Models 
 Polygl0t/Tucano2-0.6B-Base 
 Polygl0t/Tucano2-qwen-0.5B-Base 
 Polygl0t/Tucano2-qwen-1.5B-Base 
 Polygl0t/Tucano2-qwen-3.7B-Base 
 Instruct Models 
 Polygl0t/Tucano2-qwen-0.5B-Instruct 
 Polygl0t/Tucano2-qwen-1.5B-Instruct 
 Polygl0t/Tucano2-qwen-3.7B-Instruct 
 Reasoning Models 
 Polygl0t/Tucano2-qwen-0.5B-Think 
 Polygl0t/Tucano2-qwen-1.5B-Think 
 Polygl0t/Tucano2-qwen-3.7B-Think 
 Auxiliary Models 
 Polygl0t/portuguese-bertimbau-edu-classifier 
 Polygl0t/portuguese-bertimbau-large-edu-classifier 
 Polygl0t/portuguese-bertimbau-toxicity-classifier 
 Polygl0t/portuguese-bertabaporu-large-toxicity-classifier 
 Polygl0t/portuguese-qwen3-4b-instruct-quality-classifier 
 Polygl0t/portuguese-qwen3-4b-instruct-quality-judge 
 Datasets 
    Polygl0t/gigaverbo-v2 
     Polygl0t/gigaverbo-v2-synth 
     Polygl0t/gigaverbo-v2-sft 
     Polygl0t/gigaverbo-v2-preferences 
     Polygl0t/portuguese-edu-qwen-annotations 
     Polygl0t/portuguese-toxicity-qwen-annotations 
     Polygl0t/portuguese-instruct-quality-qwen-annotations 
 Benchmarks 
    IFEval-PT 
     GSM8K-PT 
     RULER-PT 
 Code: 
    Polygl0t/llm-foundry 
     Polygl0t/lm-evaluation-harness

[Safety Considerations]
Safety Considerations 
 Like most large language models trained on web data, Tucano 2 should not be considered a turnkey solution for safety-critical or high-stakes applications. Despite extensive data curation and filtering, the model can generate hallucinated content that appears plausible but is factually incorrect. It may also reflect social and historical biases present in its training data, potentially producing toxic, harmful, or offensive outputs. Given that the model is primarily optimized for Portuguese, performance in other languages may be inconsistent, leading to misinterpretations. Additionally, the model may exhibit undesirable generation behaviors such as excessive verbosity or repetitive loops under certain decoding settings. Consequently, although Tucano 2 is released under a permissive license, we strongly recommend that users conduct appropriate risk assessments, apply additional safeguards, and perform domain-specific evaluation before deploying the model in real-world systems.

[3.2.4 Quality annotation (judge model and licence)]
We employ Qwen/Qwen2.5-32B-Instruct ( Yang et al., 2025b ) as an LLM judge to annotate document quality. This model was selected for its strong multilingual performance, support for the Portuguese language, and a permissive Apache-2.0 license, which enables open redistribution of the resulting annotations. We developed two evaluation protocols: an educational quality assessment inspired by FineWeb-Edu ( Penedo et al., 2024a ) , which ranks documents on a 5-point Likert scale according to their suitability for educational use (primary through secondary level), and a toxicity assessment that evaluates the presence of harmful, offensive, or inappropriate content on a similar 5-point scale. Both prompts elicit structured JSON responses to facilitate automated processing. The complete prompts are provided in Appendix  A .

[7.1 and 7.4, the from-scratch 0.6B base]
For the pretrained model in the Tucano 2 series, we used the 0.6B-parameter architecture ( Tucano2-0.6B-Base ) as our primary experimental platform. This scale enables rapid experimentation while remaining comparable to baseline models such as Qwen2.5-0.5B and Qwen3-0.6B-Base. Following our prior work with the original Tucano series  ( Corrêa et al., 2025b ) , we maintain a Llama-based architecture  ( Touvron et al., 2023 ) incorporating standard components: RMSnorm for normalization  ( Zhang and Sennrich, 2019 ) , RoPE positional embeddings  ( Su et al., 2023 ) , and SwiGLU activations  ( Shazeer, 2020 ) .
Unlike the single-stage warmup-decay recipe used in our original Tucano experiments, we designed a three-stage training curriculum inspired by OLMo2  ( Walsh et al., 2025 ) and SmolLM  ( Allal et al., 2025 ; Bakouch et al., 2025 ) . Each stage employs a specific phase of the WSD learning rate schedule  ( Hägele et al., 2024 ) , progressively refining the data mixture to upsample higher-quality subsets. Throughout all stages, we maintain a Portuguese-dominant mixture (63% overall) and supplement with high-quality English educational content (FineWeb-Edu  ( Penedo et al., 2024a ) , FineMath), synthetic data (Cosmopedia-v2  ( Allal et al., 2024 ) , GigaVerbo-v2 Synth ), and reasoning-focused datasets (OpenScience, Big Reasoning Traces, Math Meta Reasoning Filtered). The total training volume is approximately 408 billion tokens, distributed across 195,000 optimization steps.

[8 Continual pretraining: base models, tokenizer transplantation, data]
While Tucano2-0.6B-Base demonstrates strong Easy Set performance, Hard Set capabilities require substantially larger data volumes than feasible for from-scratch pretraining under constrained budgets. We adopt a continual pretraining strategy that adapts the Qwen3 base models to the Portuguese language. Using training-free OMP-based tokenizer transplantation, we replace the 151K Qwen3 vocabulary with our own 49K-token Portuguese-optimized tokenizer, reducing the embedding parameter count by 68% while preserving pretrained capabilities. We then continually pretrain three model variants (0.5B, 1.5B, 3.7B) on purely Portuguese data, with token counts ranging from 50 to 100B, using AdamW with cosine decay schedules. The resulting models achieve state-of-the-art Portuguese performance for their size range: Tucano2-qwen-3.7B-Base attains an aggregate NPM of 59.21, surpassing Qwen3-4B-Base (57.86) and Qwen2.5-7B (57.97), while using negligible additional compute (0.13% of total pretraining FLOPs). Complete hyperparameter configurations, data mixtures, and per-benchmark results are provided in Appendix  J .
We select the Qwen3 series (Base versions) as our starting point for three reasons. First, Qwen3 models consistently outperform other similarly sized baselines on our evaluation suite, particularly on Hard Set benchmarks (Section  7 ). Second, all Qwen3 models within our target size range are released under the Apache-2.0 license, enabling unrestricted modification and redistribution. Third, the Qwen3 architecture covers a broad parameter range, enabling a family of Portuguese-adapted models at multiple scales.
Using the mergekit-tokensurgeon utility  ( Goddard et al., 2025 ) , we transplant our 49K-token Portuguese-optimized tokenizer into three Qwen3 base models (0.6B, 1.7B, 4B). The vocabulary reduction from 151K to 49K removes approximately 68% of embedding parameters, yielding the Tucano2-qwen models: Tucano2-qwen-0.5B-Base (from Qwen3-0.6B-Base), Tucano2-qwen-1.5B-Base (from Qwen3-1.7B-Base), and Tucano2-qwen-3.7B-Base (from Qwen3-4B-Base). Post-transplantation evaluation reveals that the adapted models retain substantial performance on Hard Set benchmarks while exhibiting expected degradation on language-modeling-sensitive Easy Set tasks. Detailed transplantation results are provided in Appendix  J.1 .
8.4 Data Mixtures
 Unlike the multilingual mixtures used during from-scratch pretraining, continual pretraining employs purely Portuguese data. This deliberate shift maximizes Portuguese-specific adaptation within the constrained compute budget. Each mixture combines curated web text from GigaVerbo-v2 (education score 4) with synthetic data from GigaVerbo-v2 Synth , maintaining a web-to-synthetic ratio of approximately 60:40 for the 0.5B and 3.7B models and 70:30 for the 1.5B model. Full data mixture compositions are provided in Appendix  J.3 .

[9 Post-training: data construction, filtering, training]
Dataset construction.
 Prompts were sourced from multiple public instruction-tuning datasets in English and Portuguese, with all English content translated to Portuguese using Qwen2.5-32B-Instruct. Responses were generated synthetically using the Qwen2.5 model family, with model capacity matched to task complexity: Qwen2.5-7B-Instruct and Qwen2.5-14B-Instruct for simpler tasks (summarization, rewriting, translation) and Qwen2.5-32B-Instruct for complex tasks (reasoning, Math CoT). For reasoning-intensive tasks, we employed a two-stage pipeline: (1) Qwen2.5-7B-Instruct generated initial direct responses, then (2) Qwen2.5-32B-Instruct produced detailed reasoning traces appended in <think></think> format. A key finding during this process is that generating high-quality reasoning traces in Portuguese remains challenging. Experiments with Qwen3 and SmolLM3 revealed that these models frequently default to English during reasoning, produce inconsistent reasoning that trails off without conclusions, or switch languages mid-generation. This motivated our use of Qwen2.5-32B-Instruct and highlights an important ecosystem gap that our Think models aim to address.
To further align our models, we construct a preference dataset that spans both quality- and safety-focused alignment objectives. Prompts were sourced from UltraFeedback (diverse instruction-following) and HarmfulQA (adversarial/NSFW prompts), covering two core alignment challenges: (1) benign requests requiring helpful, well-reasoned responses, and (2) harmful requests requiring consistent refusal behavior.
 Response generation followed a Constitutional AI approach with distinct constitutions for each subset. For the harmless subset, chosen responses were generated by Qwen2.5-32B-Instruct with chain-of-thought reasoning, while rejected responses came from Qwen2.5-7B-Instruct. For the harmful subset, chosen (refusal) responses used safety-oriented constitutions applied to Qwen2.5-32B-Instruct, while rejected (compliant) responses were generated by an abliterated variant of Qwen2.5-32B-Instruct  ( Arditi et al., 2024 ) . After decontamination and quality filtering, the final dataset contains 28K preference pairs (28M tokens), with a balanced split between reasoning and non-reasoning formats. URLs to the used constitutions are provided in Appendix  L.3 and  L.4 .
Each base model (0.5B, 1.5B, 3.7B) was used to produce two chat variants:
 • 
 Instruct : trained on the full multi-task GigaVerbo-v2 SFT mixture + the non-reasoning part of GigaVerbo-v2 Preferences .
 • 
 Think : trained exclusively on reasoning-intensive tasks from both our post-training datasets.
 Both variants follow a two-stage recipe: SFT with assistant-only loss masking (5 epochs, context length 4,096, AdamW with cosine schedule), followed by Anchored Preference Optimization  ( D’Oosterlinck et al., 2024 ) using the apo_zero loss with (5 epochs). Full hyperparameter tables are provided in Appendix  L.5 .

[9.4.1 Instruct results, 9.4.3 long context]
Tucano2-qwen-3.7B-Instruct achieves the highest Total Average (53.64) and the highest Knowledge & Reasoning score (56.22) among all models in the 3–4B range, surpassing Qwen3-4B (42.33), SmolLM3-3B (43.99), and the Portuguese-specialized Gemma-3-Gaia-PT-BR-4b-it (45.00). These gains span multiple domain-specific benchmarks, like BLUEX, ENEM, OAB, ARC-Challenge, BELEBELE, and MMLU. Mathematical reasoning is a particular strength: on GSM8K-PT, Tucano2-qwen-3.7B-Instruct scores 53.81, outperforming both Qwen3-4B (39.88) and Gemma-3-Gaia-PT-BR-4b-it (51.29).
 However, Tucano2 models lag behind on Instruction Following (IFEval-PT) and Coding (HumanEval), where models such as Qwen3-4B (79.33 IF, 86.59 Code) maintain clear advantages. This gap reflects limitations in our data mixture. For instance, GigaVerbo-v2 SFT does not contain samples designed to ”benchmax” IFEval-style prompts, and has a limited volume of coding-specific training samples (4%). Figure  7 presents per-benchmark comparisons for the 3.7B Instruct model; comparisons at other scales are provided in Appendix  L.7 .
We evaluated all post-trained models on RULER-PT at context lengths of 1,024, 2,048, and 4,096 tokens. Tucano2 models fall substantially behind Qwen3 counterparts across all lengths, with the gap widening at longer contexts (Table  7 ). We attribute this primarily to the absence of long-context reasoning and retrieval samples in our SFT and preference data—tasks such as multi-key KV retrieval and common word extraction require robust long-range attention that must be explicitly cultivated during training. Addressing this limitation through long-context data augmentation and potential extensions of context length is a priority for future work. Detailed per-task RULER breakdowns are provided in Appendix  L.7.4 .

[Table 9, training tokens per run]
Tucano2-0.6: 670M, Base 408B. Tucano2-qwen-0.5: 490M, Base 50B, Instruct 4.5B, Think 250M. Tucano2-qwen-1.5: 1.5B, Base 100B, Instruct 4.5B, Think 250M. Tucano2-qwen-3.7: 3.7B, Base 50B, Instruct 4.5B, Think 250M.

[Conclusion and Limitations]
In this work, we presented Tucano 2 , a fully open suite of Portuguese large language models spanning 0.5B to 3.5B parameters, accompanied by the complete stack of artifacts required for reproducible development: large-scale pretraining corpora ( GigaVerbo-v2 , GigaVerbo-v2 Synth ), annotation and filtering models, supervised fine-tuning and preference datasets ( GigaVerbo-v2 SFT , GigaVerbo-v2 Preferences ), a Portuguese evaluation suite, and all training recipes and code—released under permissive licenses. Our pretraining and continual pretraining strategies demonstrate that carefully curated, language-specific data pipelines and efficient tokenization can yield models that outperform or match multilingual baselines. In particular, Tucano2-qwen-3.7B-Instruct achieves the highest Knowledge & Reasoning score among all models in the 3–4B parameter range, while Tucano2-qwen-3.7B-Think produces chain-of-thought reasoning entirely in Portuguese, a capability largely absent from prior open Portuguese models. Together, these contributions narrow persistent gaps in Portuguese NLP and provide a concrete, reproducible blueprint for community-driven LLM development in low-resource languages.
 Limitations and Future Work.
 Despite these advances, several limitations point toward important directions for future research. First, our synthetic data generation pipeline, while effective, accounted for the largest share of total energy consumption (73%), underscoring the need for more efficient, scalable generation methods that reduce costs without sacrificing diversity. Second, our post-training pipeline relies on SFT followed by Anchored Preference Optimization, but the preference dataset ( GigaVerbo-v2 Preferences ) remains relatively small (28K pairs). Scaling preference data by an order of magnitude and investigating reinforcement learning–based post-training methods—such as GRPO and other reward-driven optimization frameworks—could substantially improve alignment quality, particularly for reasoning and agentic capabilities. Moreover, introducing a “mid-training” stage that targets areas where we currently lack (e.g., long-context reasoning, code generation) could be an effective step before returning to post-training, as demonstrated by previous studies  ( Howard and Ruder, 2018 ; Copet et al., 2025 ; Xu et al., 2025 ; Bakouch et al., 2025 ) .
 Looking ahead, we identify several high-impact opportunities. On the data side, developing more diverse and challenging SFT samples—especially for multi-step reasoning, structured output generation, and tool use—would further close the gap to frontier models. Expanding the volume and diversity of reasoning-focused training data, including both native Portuguese and carefully translated mathematical and scientific corpora, is critical for advancing reasoning capabilities. Context extension techniques and the construction of high-quality long-context samples for post-training represent another promising axis, given the increasing importance of long-horizon tasks in practical applications. Finally, designing datasets and training protocols tailored for agentic settings—including multi-turn user–agent interactions, long-horizon planning, and dynamic tool orchestration—would position Portuguese LLMs to participate in the next wave of autonomous AI systems. We hope that the open release of all artifacts produced in this work will lower barriers to entry and catalyze sustained, community-driven progress for Portuguese and other low-resource languages.

[Authors Contribution, accountable entity]
The corresponding author is Nicholas Kluge Corrêa . He is a postdoc researcher at the Bonn-Aachen International Center for Information Technology (b-it) / CAISA Lab, as part of the Lamarr Institute for Machine Learning and Artificial Intelligence, University of Bonn (Bonn, NRW, Germany). His contact email is kluge@uni-bonn.de . N.K.C. contributed to the project’s idealization, development of the software stack, dataset curation, training, and evaluation of the models, as well as writing the article and documenting the repositories. N.K.C. is one of the Principal Investigators of this project.

[Acknowledgements]
Polyglot is a project funded by the Federal Ministry of Education and Research (BMBF) and the Ministry of Culture and Science of the State of North Rhine-Westphalia (MWK) as part of TRA Sustainable Futures (University of Bonn) and the Excellence Strategy of the federal and state governments.

[C.1 Data sources and licences of GigaVerbo-v2]
The table lists Common Crawl (ODC-By v1.0, CommonCrawl ToU), FineWeb-2, FinePDFs, mC4, mC4-pt-cleaned and CulturaX (ODC-By v1.0, CommonCrawl ToU), HPLT2.0, HPLT1.2, CrawlPT-dedup and OSCAR-2201 (CC0-1.0), LegalPT-dedup, Quati, Corpus-Carolina, Cosmos-QA-PTBR, BDTD (CC-BY-4.0), Wikipedia, Roots-Wiki-quote, Dolly-15k-PT (CC-BY-SA-3.0), Xlsum (CC-BY-NC-SA-4.0), Bactrian-X (CC-BY-NC-4.0), BlogSet-br, GPT4all (Apache 2.0), UltrachatBR (MIT), Baixe Livros (Public Domain).

[Not found] The paper reports no safety, jailbreak, toxicity or red-team evaluation of the post-trained models (searched the HTML text for safety, jailbreak, red-team, refus, harmful; the hits are the data construction and the Safety Considerations paragraph above). It does not mention the EU AI Act.
