# Gemma 4 Technical Report (arXiv 2607.02770 v2)

source_url: https://arxiv.org/abs/2607.02770
retrieval_date: 2026-11-19
doc_type: technical_report
retrieved: true


arXiv:2607.02770, "Gemma 4 Technical Report", Gemma Team (Google DeepMind). Submitted 2 Jul 2026, v2 24 Jul 2026, 17 pages. HTML version read (https://arxiv.org/html/2607.02770, 254 KB). The PDF (https://arxiv.org/pdf/2607.02770, 742 KB) exists and was not separately read; the HTML is the same text. The report itself is licensed CC BY 4.0 (arXiv page); that licence covers the report, not the weights.

## Abstract

```
We introduce Gemma 4, a new generation of open-weight, natively multimodal language models in the Gemma model family. Designed to advance compute efficiency and reasoning, the Gemma 4 model suite features dense and Mixture-of-Experts architectures, ranging from 2.3B to 31B parameters. Alongside improved vision and audio encoders for all model sizes, we propose a unified, encoder-free architecture for our 12B model, which ingests raw audio and image patches. Furthermore, we integrate a thinking mode, enabling Gemma models to generate reasoning traces prior to responding. We improve inference speed, memory, and compute efficiency, as well as long-context abilities through critical design choices. Gemma 4 establishes a leap in performance across STEM, multimodal, and long-context benchmarks, and rivals larger, frontier open models in human-rated tasks.
```

## Licence statement (verbatim; the report states Apache 2.0 for the models)

```
In this technical report, we outline the different model architectures across model sizes as well as the pre-training and post-training recipe of Gemma 4. Through comprehensive benchmarks and human evaluations such as Arena (Chiang et al., 2024), we demonstrate that Gemma 4 operates at a level comparable to larger, frontier open-source models across text, image, and audio modalities. We release the Gemma 4 models under an Apache 2.0 license, empowering developers and researchers everywhere to build upon, customize, and extend these capabilities.
```

## Pre-training data and filtering (what is disclosed)

```
2.4 Pre-training
We follow a similar pre-training as Gemma 3.
Training data. Our pre-training dataset is a large-scale, diverse collection of data from a wide range of domains and modalities, including web documents, code, images, and audio (for E2B, E4B and 12B), with a cutoff date of January 2025.
Figure 1: The autoregressive MTP drafter (blue blocks on the right) is fed activations and KV cache from the main model (gray blocks).
```

```
Filtering. We filter data to decontaminate benchmarks, and to reduce the risk of unwanted or unsafe utterances and the risk of recitation.
```

Not disclosed in the report text read: token counts, compute (FLOPs), dataset composition by source, the training code, or the evaluation harness. A search of the HTML text for "trillion" found no hit.

## Post-training

```
Pre-trained models are turned into instruction-tuned models with a similar post-training approach as in Gemma 3. A significant difference is the addition of a thinking mode, where the model can output a reasoning trace before answering.
```

```
Data filtering. We carefully optimize the data used in post-training to maximize model performance. We filter examples that show certain personal information, unsafe or toxic model outputs, mistaken self-identification data, and duplicated examples. Including subsets of data that encourage better in-context attribution, hedging, and refusals to minimize hallucinations also improves performance on factuality metrics, without degrading model performance on other metrics.
```

## Quantisation-aware training and multi-token-prediction drafters

```
2.5 Quantization-Aware Training
We provide quantized models and encoders in different formats along with the raw checkpoints.
Based on the most popular open source quantization inference engines (e.g. llama.cpp) as well as efficient hardware support, we focus on two sets of weight representations:
- •
mobile quantization: per-channel low bitwidth weight (mix of int2 and int4) and activation quantization (int8).
```

```
We train a small autoregressive MTP drafter head with our models, used for speculative decoding. In our MTP procedure, the model’s last layer activations from the previous step and token embeddings are fed into the MTP head. The MTP head generates future tokens sequentially using a separate embedder and a 4-layer Transformer block that cross-attends to the KVs of the main model (Figure 1), thus eliminating the need for MTP prefill and supporting any draft length. The Transformer block has model dimension 256 for E2B and E4B, 1024 for 26B-A4B and 31B, three local, and one global attention layers.
```

## Arena human-preference ranking (publisher-reported, naming a third-party leaderboard)

```
Table 4: Leading open-weight models on Arena Text (Chiang et al., 2024) (as of June 19, 2026). Models are evaluated through blind side-by-side evaluations by human raters, and attributed scores based on the Elo rating system. The top closed model (gray) is included for scale. Gemma models rival much larger models, and Gemma 4 31B is the leading dense open model on the leaderboard.
```

## Section 5 Responsibility, Safety, Security

```
5 Responsibility, Safety, Security
As open models become central to enterprise infrastructure, provenance and security are paramount. Gemma 4 undergoes the same rigorous safety evaluations as Gemini models. Responsibility, safety, and security are of utmost importance in the development workflow, ensuring that these language models are designed from the ground up for responsible AI development.
5.1 Governance & Assessment
```

```
5.2 Safety Policies and Train-Time Mitigations
A key pillar of Gemma’s safety approach is aligning our fine-tuned models with Google’s AI principles and safety policies. These policies aim to prevent our generative models from producing harmful content, specifically:
- •
Content related to child sexual abuse material (CSAM) and exploitation;
- •
Dangerous content, e.g., promoting suicide, or instructing in activities that could cause real-world harm;
- •
Sexually explicit content;
- •
Hate speech, e.g., dehumanizing members of protected groups;
- •
```

```
5.3 Safety Evaluations
We conduct rigorous automated and human evaluations to understand the potential harms our models might cause. For all areas of safety testing, we saw major improvements in every category of content safety relative to previous Gemma models. Overall, Gemma 4 models significantly outperform Gemma 3 and 3n models in improving safety, while keeping unjustified refusals low.
Importantly, all testing was conducted without safety filters to accurately evaluate the model’s inherent capabilities and behaviors. For both text-to-text and image-to-text modalities, and across all model sizes, the models produced minimal policy violations. We balance development speed with targeted safety testing, upholding the commitments laid out in our Frontier Safety Framework (Google
DeepMind, 2024).
5.4 Ethical Considerations and Risk Mitigation
```

```
5.5 Our Approach to Responsible Open Models
Designing safe, secure, and responsible applications requires a system-level approach that mitigates risks associated with specific use cases and environments. We provide guidelines, mechanisms, and safeguards for content safety, and encourage developers to implement appropriate configurations based on their product policies. We will continue to adopt safety mitigations proportionate to potential risks, sharing these models with the community only when confident that the benefits significantly outweigh foreseeable risks.
```

Reading note by OneHill: the safety evaluation is described qualitatively. No violation rates, no per-category numbers, no named red-team, no CBRN, cyber or child-safety evaluation results and no jailbreak-resistance figures appear in the text read. A Frontier Safety Framework commitment is mentioned but its results are not reported here. No companion guard model for Gemma 4 is named in the report.
