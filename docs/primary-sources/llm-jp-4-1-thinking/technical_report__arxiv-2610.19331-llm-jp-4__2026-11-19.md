# technical_report / arxiv-2610.19331-llm-jp-4

source_url: https://arxiv.org/abs/2610.19331 and https://arxiv.org/html/2610.19331v1
retrieval_date: 2026-11-19
exists: yes
retrieved: true

Verbatim extracts (publisher text, not edited). Notes by OneHill are marked NOTE.

NOTE: this is the LLM-jp-4 Technical Report (arXiv v1, 14 Oct 2026). It covers the 8B dense and 32B-A3B MoE models. The arXiv comment says: "Results for the LLM-jp-4 33B dense model are not included in this version and will be added in a future revision". It does not cover LLM-jp-4.1 (the 4.1 post-training is described only in the publisher blog and the model cards).

## Abstract page (https://arxiv.org/abs/2610.19331)
Title: LLM-jp-4 Technical Report. Submitted 14 Oct 2026. Authors: LLM-jp (Chaoran Liu, Daisuke Kawahara, Hideyuki Tachibana, Hirokazu Kiyomaru, Jun Suzuki, Koshi Eguchi, Kouta Nakayama, Qianying Liu, Rio Yokota, Ryo Takahashi, Sadao Kurohashi, Sosuke Hosokawa, Taishi Nakamura, Takashi Kodama, Yun-Ang Wu, Yusuke Miyao, Yusuke Oda).
```
This paper presents LLM-jp-4, a family of Japanese sovereign large language models (LLMs) developed with an emphasis on transparency, reproducibility, and practical usability.
LLM-jp-4 comprises an 8B dense model and a 32B-A3B mixture-of-experts model, both trained from scratch on approximately 12 trillion tokens.
To support independent verification and reproduction, we establish explicit criteria for selecting training data, external models, and software, and make the development process publicly available.
Evaluation results demonstrate substantial improvements over previous LLM-jp models and competitive performance against open-weight models of similar scale.
By documenting the development principles, training procedures, and empirical findings of LLM-jp-4, we aim to provide a reference for future sovereign AI development.
```
Comments: Results for the LLM-jp-4 33B dense model are not included in this version and will be added in a future revision

## Section 1 Introduction (openness claims)
```
We address these problems by developing LLMs from scratch and making the entire development process public.
The performance and behavior of an LLM are shaped throughout development, including training data, data processing, training objectives, and optimization methods.
Releasing the final model weights alone is insufficient for fully understanding how the model’s capabilities and properties emerge.
Making the entire development process public enables third parties to verify, reproduce, and compare results Biderman et al. (2023); Groeneveld et al. (2024); Apertus et al. (2025).
This openness provides a foundation for sovereign AI by enabling anyone to use, analyze, and further develop models while advancing scientific understanding of how training shapes their capabilities, biases, and safety properties.
This paper introduces LLM-jp-4, a family of LLMs developed to provide an open foundation for both sovereign AI in Japan and scientific research on LLMs worldwide.
In addition to the final model weights, we make the entire training process publicly available in a form that enables independent verification and reproduction.
To this end, we established strict selection criteria for the data, external models, and code used in training, taking into account legal and licensing requirements, as well as the feasibility of independent verification and reproduction.
The LLM-jp-4 family comprises an 8B dense model and a 32B-A3B mixture-of-experts (MoE) model.
Each model was trained from scratch on approximately 12 trillion tokens in total (Figure 1).
Our evaluations show that LLM-jp-4 substantially outperforms the previous generation of LLM-jp models and achieves performance comparable to strong open-weight LLMs on Japanese benchmarks.
In the following sections, we first describe the development principles of LLM-jp-4 and then present the training data, model architecture, training procedure, and evaluation results.
We explain how technical choices throughout development balance the goal of improving model performance with requirements for transparency, reproducibility, and legal compliance.
The LLM-jp-4 models are publicly available on Hugging Face under the Apache 2.0 license.11
 1
 https://huggingface.co/collections/llm-jp/llm-jp-4-models
```

## Section 2 Development principles, 2.1 dataset selection criteria and release levels
```
2 Development Principles
2.1 Dataset Selection Criteria
2.2 Criteria for External Models
2.3 Software Selection Criteria
2.4 Model License
3 Model Architecture
3.1 Tokenizer
4 Pre-training
4.1 Corpus
4.1.1 Corpus for Pre-training Phase 1
FineWeb Rescored
4.1.2 Corpus Mixture Optimization for Pre-training Phase 1
4.1.3 Corpus for Pre-training Phase 2
MegaMath-Web-Pro-Max-OSS
4.1.4 Corpus Mixture Optimization for Pre-training Phase 2
4.2 Training
4.2.1 Training Recipe
4.2.2 Learning-rate Schedule
4.2.3 Hyperparameter Selection
4.2.4 Training System
4.3 Evaluation
5 Mid-training
5.1 Corpus
5.1.1 Corpus Candidates Collection
5.1.2 Regeneration of LLM-jp-Corpus-Midtraining-v1
5.1.3 Corpus Mixture Optimization for Mid-training
5.2 Training Setup
5.3 Evaluation
6 Post-training
6.1 Chat Template
6.2 Supervised Fine-tuning (SFT)
6.2.1 Data Sources
6.2.2 Reasoning Data Generation
6.2.3 Training Setup
6.3 Direct Preference Optimization (DPO)
6.3.1 Preference Data Construction
6.3.2 Training Setup
7 Evaluation
7.1 Evaluation Benchmarks
7.2 Evaluation with llm-jp-eval v2.1.3
7.3 Evaluation with LLM-as-a-Judge
8 Conclusion
References
A Contribution Statement
B Regeneration of LLM-jp-Corpus-Midtraining-v1
C Preference Data Construction
 License: arXiv.org perpetual non-exclusive license
arXiv:2610.19331v1 [cs.CL] 14 Oct 2026
\jvol
vv
\jnumnn
2025
\docheadTechnical Paper
LLM-jp-4
LLM-jp
Chaoran Liu
††thanks: LLM-jp-4 was a team effort. Authors sorted alphabetically. Contribution statements can be found in Appendix.
Daisuke Kawahara
Hideyuki Tachibana
Hirokazu Kiyomaru
Jun Suzuki
Koshi Eguchi
Kouta Nakayama
Qianying Liu
Rio Yokota
Ryo Takahashi
Sadao Kurohashi
Sosuke Hosokawa
Taishi Nakamura
Takashi Kodama
Yun-Ang Wu
Yusuke Miyao
Yusuke Oda
Abstract
This paper presents LLM-jp-4, a family of Japanese sovereign large language models (LLMs) developed with an emphasis on transparency, reproducibility, and practical usability.
LLM-jp-4 comprises an 8B dense model and a 32B-A3B mixture-of-experts model, both trained from scratch on approximately 12 trillion tokens.
To support independent verification and reproduction, we establish explicit criteria for selecting training data, external models, and software, and make the development process publicly available.
Evaluation results demonstrate substantial improvements over previous LLM-jp models and competitive performance against open-weight models of similar scale.
By documenting the development principles, training procedures, and empirical findings of LLM-jp-4, we aim to provide a reference for future sovereign AI development.
1 Introduction
Despite the growing importance of large language models (LLMs), their development is concentrated in a small number of companies and regions, and the full development process is not publicly disclosed for many state-of-the-art models Wan et al. (2025); Sajadieh et al. (2026).
The concentration and closed nature of LLM development create problems for societal autonomy and scientific understanding.
First, dependence on specific external LLM developers may limit the ability of countries and regions to develop and operate AI systems that meet their own linguistic and social needs.
The idea of maintaining such autonomy has been discussed under the concept of sovereign AI Bondarenko et al. (2025).
Second, keeping the development process internal to a limited number of LLM developers makes it difficult for outside researchers to analyze and verify how the capabilities, limitations, and potential risks of these models arise.
This problem extends beyond any particular country or region, hindering the broader research community’s efforts to develop a scientific understanding of AI.
We address these problems by developing LLMs from scratch and making the entire development process public.
The performance and behavior of an LLM are shaped throughout development, including training data, data processing, training objectives, and optimization methods.
Releasing the final model weights alone is insufficient for fully understanding how the model’s capabilities and properties emerge.
Making the entire development process public enables third parties to verify, reproduce, and compare results Biderman et al. (2023); Groeneveld et al. (2024); Apertus et al. (2025).
This openness provides a foundation for sovereign AI by enabling anyone to use, analyze, and further develop models while advancing scientific understanding of how training shapes their capabilities, biases, and safety properties.
This paper introduces LLM-jp-4, a family of LLMs developed to provide an open foundation for both sovereign AI in Japan and scientific research on LLMs worldwide.
In addition to the final model weights, we make the entire training process publicly available in a form that enables independent verification and reproduction.
To this end, we established strict selection criteria for the data, external models, and code used in training, taking into account legal and licensing requirements, as well as the feasibility of independent verification and reproduction.
The LLM-jp-4 family comprises an 8B dense model and a 32B-A3B mixture-of-experts (MoE) model.
Each model was trained from scratch on approximately 12 trillion tokens in total (Figure 1).
Our evaluations show that LLM-jp-4 substantially outperforms the previous generation of LLM-jp models and achieves performance comparable to strong open-weight LLMs on Japanese benchmarks.
In the following sections, we first describe the development principles of LLM-jp-4 and then present the training data, model architecture, training procedure, and evaluation results.
We explain how technical choices throughout development balance the goal of improving model performance with requirements for transparency, reproducibility, and legal compliance.
The LLM-jp-4 models are publicly available on Hugging Face under the Apache 2.0 license.11
 1
 https://huggingface.co/collections/llm-jp/llm-jp-4-models
Figure 1: Overview of the training pipeline of LLM-jp-4. Training proceeds through three stages: pre-training, mid-training, and post-training. Pre-training uses LLM-jp Corpus v4 to acquire broad knowledge (Phase 1; 6.3T tokens), followed by LLM-jp Corpus v4.1 with increased proportions of math and code (Phase 2; 4.2T tokens). Mid-training mixes LLM-jp Corpus Midtraining v2 with the pre-training corpus to improve question-answering capabilities (Phase 1; 0.8T tokens) and extend the maximum context length from 4K to 64K tokens via 16K (Phase 2; 0.4T tokens). Post-training aligns the models as thinking models through SFT and DPO. The bottom panels show the learning-rate schedule and maximum context length throughout training.
2 Development Principles
Transparency and reproducibility are key principles in the development of LLM-jp-4.
These principles are essential for supporting independent LLM development in Japan and for providing a foundation that enables third parties to verify the development process and build on it through further research and development.
For this purpose, LLM-jp-4 requires that the development process remain reproducible by third parties when selecting data, external models, and software.
Specifically, we limit these resources to those that are available to third parties or for which third parties can construct equivalent resources based on publicly available information about their sources, acquisition methods, processing procedures, and other relevant details.
These selection criteria are designed to satisfy legal requirements, including Japanese copyright law, and to be consistent with the Open Source AI Definition (OSAID) published by the Open Source Initiative22
 2
 https://opensource.org/33
 3
 https://opensource.org/ai/open-source-ai-definition.
2.1 Dataset Selection Criteria
We apply the reproducibility and legal compliance requirements described above to all datasets used for training LLM-jp-4.
In addition, we require that not only our use of a dataset but also its original construction process comply with applicable legal and licensing requirements, including Japanese copyright law.
LLM-jp assigns a release level to each dataset subset to explicitly manage the scope in which it can be used.
The release level consists of five levels, as shown in Table 1.
For training the publicly released LLM-jp-4 models, we use only data classified as L1 through L3, which permits use for public model training.
```
Table 1 (release levels, as extracted from the HTML): L1 = internal-model training yes, public-model training yes, retrieval yes, redistribution yes. L2 = yes, yes, yes, redistribution no. L3 = yes, yes, retrieval no, redistribution no. LX = internal-model training only. LZ = none.

## 2.2 to 2.4 external models, software, model licence
```
2.2 Criteria for External Models
2.3 Software Selection Criteria
2.4 Model License
```

## 4.1.1 pre-training Phase 1 corpus (FineWeb-Rescored rationale)
```
The pre-training corpus for Phase 1 was constructed with a target size of approximately 20 trillion tokens, taking the scale of the Llama 3 pre-training corpus (15 trillion tokens) Grattafiori et al. (2024) as a reference.
The corpus covers Japanese, English, Chinese, and Korean, as well as code.
Because Japanese capability is a particular priority for a sovereign LLM developed in Japan, we collected Japanese data as broadly as possible, prioritizing corpus size.
We also performed deduplication across the entire Japanese corpus, as duplication in pre-training corpora is known to negatively affect model performance (Lee et al., 2022).
Table 4 lists the subcorpora included in Phase 1.
All subcorpora satisfy the requirements for use in model training under the release levels defined in Section 2.1.
FineWeb Rescored
Phase 1 primarily uses existing datasets, but FineWeb-Rescored was newly constructed for LLM-jp-4.
FineWeb-Rescored reproduces the construction procedure of FineWeb-Edu Penedo et al. (2024).
FineWeb-Edu is a Web corpus derived from Common Crawl by selecting documents judged to have high educational value, and its use in pre-training has been reported to substantially improve performance on STEM tasks.
However, Llama-3-70B-Instruct Grattafiori et al. (2024) was used to construct the classifier for document selection.
Directly adopting FineWeb Edu could therefore introduce restrictions arising from the Llama 3 license55
 5
 https://developer.meta.com/ai/llama3/license/, such as naming requirements for derivative models or the need for a separate agreement with Meta depending on the scale of use.
We considered such restrictions inconsistent with our development policy and therefore reproduced the FineWeb-Edu construction procedure using an open-source LLM in place of Llama-3-70B-Instruct.
We followed the original FineWeb-Edu construction procedure, changing only the LLM used for annotation.
First, we used Qwen3-32B Yang et al. (2025), released under the Apache 2.0 license, to annotate the same subset of 450K FineWeb documents that had been annotated by Llama-3-70B-Instruct during the construction of FineWeb-Edu, assigning each document a label reflecting its educational value.
We used the same annotation prompt as FineWeb-Edu.
We then fine-tuned a pre-trained BERT-based embedding model66
 6
 https://huggingface.co/Snowflake/snowflake-arctic-embed-m using the annotations produced by Qwen3-32B as training data.
Finally, we applied the fine-tuned classifier to all 24.5 billion documents in FineWeb to estimate the educational value of each document.
This process used 128 H200 GPUs and took approximately 1.5 days.
```
Table 4 rows relevant to redistribution (extracted from the HTML table): Ja Ceek.jp News, News, L3, 12.5B tokens; Ja NWJC, Web, L2, 25.7B tokens; every other Japanese subcorpus L1. NOTE (OneHill): Ja Common Crawl 217.4B and FineWeb-2 ja 216.1B tokens.

## 4.2 training configuration availability
```
Training comprised two consecutive phases aligned with the corpus development described above.
Phase 1 used the broad-coverage mixture and ended after approximately 6.3T tokens.
Phase 2 initialized from the corresponding Phase 1 checkpoint and added approximately 4.2T tokens from the revised mixture, which places greater emphasis on mathematical and code data.
Each model therefore received approximately 10.5T pre-training tokens in total.
The two models processed the same number of tokens with different numbers of optimizer updates.
With a sequence length of 4,096, the dense model used global batch sizes of 512 and 2,048 sequences in Phases 1 and 2, respectively, resulting in 3,000,000 updates in Phase 1 and 500,000 updates in Phase 2.
The MoE model used global batch sizes of 1,024 and 2,048 in Phases 1 and 2, respectively, resulting in 1,500,000 and 500,000 updates.
In both cases, the phase-wise token count is the product of the number of steps, global batch size, and sequence length: 6.3T tokens in Phase 1 and 4.2T tokens in Phase 2.
Thus, differences in update counts reflect the selected batch sizes rather than differences in the amount of training data.
Table 7 summarizes the model and optimization settings.
The complete training configurations are publicly available for the dense model88
 8
 Phase 1: https://github.com/llm-jp/scripts/tree/main/pretrain/scripts/v4-8b-phase1, and the MoE model99
 9
 https://github.com/llm-jp/scripts/tree/main/pretrain/scripts/v4-32b-a3.8b-phase1.
The --train-iters values in the stable-run configurations are operational upper bounds; the step counts reported here are the checkpoints actually used at the phase boundaries.
```

## 4.2.4 training system
```
We implemented training with Megatron-LM on the ABCI H200 GPU cluster. Model computation used bfloat16 arithmetic, while Transformer Engine provided optimized attention kernels. To reduce optimizer-state memory and communication overhead, we used Megatron-LM’s distributed optimizer and overlapped gradient reduction and parameter gathering with computation. For the MoE model, grouped matrix multiplications and fused token permutation were enabled to improve the efficiency of expert computation, and router logits were computed in float32 for numerical stability.
```

## 6.2 SFT data sources: licence-agreement dataset and release statement
```
For SFT, we collect prompts from multiple instruction data sources and construct a dataset by augmenting each prompt with a reasoning process and a final answer.
For portions of the resulting SFT dataset whose licenses permit redistribution, we release the data as llm-jp-4-thinking-sft-data1111
 11
 https://huggingface.co/datasets/llm-jp/llm-jp-4-thinking-sft-data.
```
```
Ichikara-instruction is a manually created Japanese instruction–response dataset.
We use it for training LLM-jp-4 under a license agreement that permits us to release models trained on the data, including for commercial use.
In this work, we use three subsets: ichikara-instruction (ver004-002), ichikara2 (ver002-001), and ichikara-multiturn (ver002-002).
```

## 6.3 DPO safety-data selection
```
We used two types of evaluation prompts: a general helpfulness judge prompt and a safety judge prompt.
For most data sources, we used the helpfulness judge prompt, which assigns an integer helpfulness score from 1 to 10 based on the usefulness, relevance, correctness, depth, creativity, and specificity of the response.
For AnswerCarefully Self-Instruct, we instead used the safety judge prompt for safety alignment, assigning an integer safety score from 1 to 5.
Both judge prompts explicitly instructed the judge not to penalize differences in reasoning length arising from different reasoning effort levels, and to base the evaluation primarily on the helpfulness or safety of the final answer.
The helpfulness and safety judge prompts used in our experiments are shown in Appendix C.
To construct preference pairs, we selected the highest-scoring candidate response to each prompt as the chosen response and the lowest-scoring candidate as the rejected response.
When multiple responses shared the same score, we selected one chosen response from among the highest-scoring responses and up to two rejected responses from among the lowest-scoring responses using a fixed random seed.
For helpfulness data, we retained only examples for which the highest score was greater than 6 and the difference between the highest and lowest scores was at least 2.
For safety data, we required the highest score to be greater than 3 and the score difference to be at least 1.
In addition, to mitigate length bias arising from differences in final-answer length between the chosen and rejected responses, we excluded pairs for which the ratio of their token lengths exceeded 1.5.
```

## 7 evaluation set-up and results (publisher benchmarks; judge model is gpt-5.4)
```
We evaluate the English and Japanese capabilities of LLM-jp-4 from two perspectives: automatically scored benchmarks with ground-truth answers and conversational evaluation using LLM-as-a-Judge.
For the automatically scored benchmarks, we compare LLM-jp-4 with llm-jp-3.1-8x13b-instruct4, the flagship model of the previous-generation LLM-jp-3 series, as well as Qwen3-8B Yang et al. (2025) and gpt-oss-20b OpenAI et al. (2025), open-weight models developed by other organizations with relatively similar parameter scales.
For the LLM-as-a-Judge evaluation, we compare LLM-jp-4 with gpt-oss-20b OpenAI et al. (2025) and additionally include GPT-4o and GPT-5.4 as reference models.
```
```
For all LLM-as-a-Judge evaluations, we use gpt-5.4-2026-03-05 as the judge model and report the average score over three independent inference and evaluation runs.
For datasets used in both post-training and evaluation, we used only their training splits for post-training and their test splits for evaluation.
```
```
LLM-jp-4 substantially improves upon llm-jp-3.1-8x13b-instruct4, the flagship model of the previous generation.
The average Japanese score increases from 0.307 for llm-jp-3.1-8x13b-instruct4 to 0.590 for the 8B dense model and 0.605 for the 32B-A3B MoE models.
In particular, the 32B-A3B model achieves Japanese performance comparable to Qwen3-8B (0.608) and gpt-oss-20b (0.604).
Figure 6 shows the scores by task on the English subset of llm-jp-eval v2.1.3.
LLM-jp-4 also shows substantial improvements over the previous-generation model on the English subset.
The average English score increases from 0.354 for llm-jp-3.1-8x13b-instruct4 to 0.634 for the 8B dense model and 0.650 for the 32B-A3B MoE model.
Although these scores remain below those of Qwen3-8B (0.714) and gpt-oss-20b (0.704), they represent substantial improvements over the previous generation.
Figure 7 shows the results on challenging benchmarks requiring knowledge and reasoning.
The improvements over the previous generation are particularly pronounced on these tasks.
On JMMLU, llm-jp-4-32b-a3b-thinking achieves a score of 0.820, compared with 0.590 for llm-jp-3.1-8x13b-instruct4.
On Japanese GPQA Diamond, the score likewise improves from 0.310 for llm-jp-3.1-8x13b-instruct4 to 0.540 for llm-jp-4-32b-a3b-thinking.
However, gaps remain relative to the external baselines on challenging science and mathematics tasks.
On GPQA Diamond (EN), llm-jp-4-32b-a3b-thinking scores 0.520, below Qwen3-8B (0.560) and gpt-oss-20b (0.670).
On AIME 2024/2025, llm-jp-4-32b-a3b-thinking achieves scores of 0.400/0.300; although this represents a substantial improvement over the previous generation, it still falls short of Qwen3-8B and gpt-oss-20b.
Scores on HLE are low across all models, and the results indicate substantial room for further improvement in LLM-jp-4.
7.3 Evaluation with LLM-as-a-Judge
```
```
Table 16 presents the LLM-as-a-Judge evaluation results on MT-Bench, AnswerCarefully, and llm-jp-instructions.
With reasoning effort set to medium, llm-jp-4-8b-thinking achieves scores of 7.54 on MT-Bench (JA), 7.79 on MT-Bench (EN), 3.69 on AnswerCarefully, and 3.54 on llm-jp-instructions.
With low reasoning effort, the corresponding scores are 7.23, 7.54, 3.58, and 3.50, respectively, indicating that the medium setting yields particularly clear improvements on MT-Bench and AnswerCarefully.
With medium reasoning effort, llm-jp-4-32b-a3b-thinking achieves scores of 7.82 on MT-Bench (JA), 7.86 on MT-Bench (EN), 3.70 on AnswerCarefully, and 3.61 on llm-jp-instructions, achieving higher average scores than the 8B model on all four benchmarks.
For comparison, gpt-oss-20b with medium reasoning effort scores 7.33 on MT-Bench (JA), 7.85 on MT-Bench (EN), 3.55 on AnswerCarefully, and 3.16 on llm-jp-instructions.
Thus, llm-jp-4-32b-a3b-thinking outperforms gpt-oss-20b on Japanese MT-Bench, AnswerCarefully, and llm-jp-instructions, while achieving comparable performance on English MT-Bench.
```
