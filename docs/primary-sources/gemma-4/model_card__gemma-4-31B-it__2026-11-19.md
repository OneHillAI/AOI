# Gemma 4 model card (Hugging Face README, google/gemma-4-31B-it)

source_url: https://huggingface.co/google/gemma-4-31B-it/raw/main/README.md
retrieval_date: 2026-11-19
doc_type: model_card
retrieved: true


Raw README.md of google/gemma-4-31B-it (27,963 bytes) at repository sha 842da3794eaa0b77d5f08bae87a17459d91ff475. The 31B base, 12B, 26B A4B, E2B and E4B cards carry the same text with per-size notes (the 12B card adds a note that it is the 12B Unified model; the 31B base and E2B base cards were compared with their instruction-tuned cards using diff and differ only in the base_model field, the license header line and code snippets). Extracts below are verbatim.

## Front matter and header

```
---
library_name: transformers
license: apache-2.0
license_link: https://ai.google.dev/gemma/docs/gemma_4_license
pipeline_tag: image-text-to-text
base_model:
- google/gemma-4-31B
---
```

```
<p align="center">
    <a href="https://huggingface.co/collections/google/gemma-4" target="_blank">Hugging Face</a> |
    <a href="https://github.com/google-gemma" target="_blank">GitHub</a> |
    <a href="https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/" target="_blank">Launch Blog</a> |
    <a href="https://ai.google.dev/gemma/docs/core" target="_blank">Documentation</a>|
    <a href="https://arxiv.org/abs/2607.02770" target="_blank">Technical Report</a>
    <br>
    <b>License</b>: <a href="https://ai.google.dev/gemma/docs/gemma_4_license" target="_blank">Apache 2.0</a> | <b>Authors</b>: <a href="https://deepmind.google/models/gemma/" target="_blank">Google DeepMind</a>
</p>
```

## Release scope

```
Gemma is a family of open models built by Google DeepMind. Gemma 4 models are multimodal, handling text and image input (with audio supported on E2B, E4B, and 12B) and generating text output. This release includes open-weights models in both pre-trained and instruction-tuned variants. Gemma 4 features a context window of up to 256K tokens and maintains multilingual support in over 140 languages.

Featuring both Dense and Mixture-of-Experts (MoE) architectures, Gemma 4 is well-suited for tasks like text generation, coding, and reasoning. The models are available in five distinct sizes: **E2B**, **E4B**, **12B**, **26B A4B**, and **31B**. Their diverse sizes make them deployable in environments ranging from high-end phones to laptops and servers, democratizing access to state-of-the-art AI.
```

## Models overview tables (sizes, context, modalities)

```
### Dense Models

| Property | E2B | E4B | 12B Unified | 31B Dense |
| :---- | :---- | :---- | :---- | :---- |
| **Total Parameters** | 2.3B effective <br> (5.1B with embeddings) | 4.5B effective <br> (8B with embeddings) | 11.95B | 30.7B |
| **Layers** | 35 | 42 | 48 | 60 |
| **Sliding Window** | 512 tokens | 512 tokens | 1024 tokens | 1024 tokens |
| **Context Length** | 128K tokens | 128K tokens | 256K tokens  | 256K tokens  |
| **Vocabulary Size** | 262K | 262K | 262K | 262K |
| **Supported Modalities** | Text, Image, Audio | Text, Image, Audio | Text, Image, Audio | Text, Image |
| **Vision Encoder Parameters** | *~150M* | *~150M* | - | *~550M* |
| **Audio Encoder Parameters** | *~300M* | *~300M* | - | No Audio |
```

```
### Mixture-of-Experts (MoE) Model

| Property | 26B A4B MoE |
| :---- | :---- |
| **Total Parameters** | 25.2B |
| **Active Parameters** | 3.8B |
| **Layers** | 30 |
| **Sliding Window** | 1024 tokens |
| **Context Length** | 256K tokens |
| **Vocabulary Size** | 262K |
| **Expert Count** | 8 active / 128 total and 1 shared |
| **Supported Modalities** | Text, Image |
| **Vision Encoder Parameters** | *~550M* |
```

## Benchmark table (publisher-reported, instruction-tuned)

```
|  | Gemma 4  31B | Gemma 4  26B A4B | Gemma 4 12B Unified | Gemma 4  E4B | Gemma 4  E2B | Gemma 3  27B (no think) |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| MMLU Pro | 85.2% | 82.6% | 77.2% | 69.4% | 60.0% | 67.6% |
| AIME 2026 no tools | 89.2% | 88.3% | 77.5% | 42.5% | 37.5% | 20.8% |
| LiveCodeBench v6 | 80.0% | 77.1% | 72.0% | 52.0% | 44.0% | 29.1% |
| Codeforces ELO | 2150 | 1718 | 1659 | 940 | 633 | 110 |
| GPQA Diamond | 84.3% | 82.3% | 78.8% | 58.6% | 43.4% | 42.4% |
| Tau2 (average over 3) | 76.9% | 68.2% | 69.0% | 42.2% | 24.5% | 16.2% |
| HLE no tools | 19.5% | 8.7% | 5.2% | - | - | - |
| HLE with search | 26.5% | 17.2% | - | - | - | - |
| BigBench Extra Hard | 74.4% | 64.8% | 53.0% | 33.1% | 21.9% | 19.3% |
| MMMLU | 88.4% | 86.3% | 83.4% | 76.6% | 67.4% | 70.7% |
| **Vision** |  |  |  |  |  |  |
| MMMU Pro | 76.9% | 73.8% | 69.1% | 52.6% | 44.2% | 49.7% |
| OmniDocBench 1.5 (average edit distance, lower is better) | 0.131 | 0.149 | 0.164 | 0.181 | 0.290 | 0.365 |
| MATH-Vision | 85.6% | 82.4% | 79.7% | 59.5% | 52.4% | 46.0% |
| MedXPertQA MM | 61.3% | 58.1% | 48.7% | 28.7% | 23.5% | - |
| **Audio** |  |  |  |  |  |  |
| CoVoST | - | - | 38.5<sup>*</sup> | 35.54 | 33.47 | - |
| FLEURS (lower is better) | - | - | 0.069<sup>*</sup> | 0.08 | 0.09 | - |
| **Long Context** |  |  |  |  |  |  |
| MRCR v2 8 needle 128k (average) | 66.4% | 44.1%  | 43.4% | 25.4% | 19.1% | 13.5% |
```

## Core capabilities (function calling, context, languages)

```
* **Thinking** – Built-in reasoning mode that lets the model think step-by-step before answering.
* **Long Context** – Context windows of up to 128K tokens (E2B/E4B) and 256K tokens (12B, 26B A4B/31B).
* **Image Understanding** – Object detection, Document/PDF parsing, screen and UI understanding, chart comprehension, OCR (including multilingual), handwriting recognition, and pointing. Images can be processed at variable aspect ratios and resolutions.
* **Video Understanding** – Analyze video by processing sequences of frames.
* **Interleaved Multimodal Input** – Freely mix text and images in any order within a single prompt.
* **Function Calling** – Native support for structured tool use, enabling agentic workflows.
* **Coding** – Code generation, completion, and correction.
* **Multilingual** – Out-of-the-box support for 35+ languages, pre-trained on 140+ languages.
* **Audio** (E2B, E4B, and 12B only) – Automatic speech recognition (ASR) and speech-to-translated-text translation across multiple languages.
```

## Model data

```
### **Training Dataset**

Our pre-training dataset is a large-scale, diverse collection of data encompassing a wide range of domains and modalities, which includes web documents, code, images, audio, with a cutoff date of January 2025. Here are the key components:

* **Web Documents**: A diverse collection of web text ensures the model is exposed to a broad range of linguistic styles, topics, and vocabulary. The training dataset includes content in over 140 languages.
* **Code**: Exposing the model to code helps it to learn the syntax and patterns of programming languages, which improves its ability to generate code and understand code-related questions.
* **Mathematics**: Training on mathematical text helps the model learn logical reasoning, symbolic representation, and to address mathematical queries.
* **Images**: A wide range of images enables the model to perform image analysis and visual data extraction tasks.

The combination of these diverse data sources is crucial for training a powerful multimodal model that can handle a wide variety of different tasks and data formats.

### **Data Preprocessing**

Here are the key data cleaning and filtering methods applied to the training data:

* **CSAM Filtering**: Rigorous CSAM (Child Sexual Abuse Material) filtering was applied at multiple stages in the data preparation process to ensure the exclusion of harmful and illegal content.
* **Sensitive Data Filtering**: As part of making Gemma pre-trained models safe and reliable, automated techniques were used to filter out certain personal information and other sensitive data from training sets.
* **Additional methods**: Filtering based on content quality and safety in line with [our policies](https://ai.google/static/documents/ai-responsibility-update-published-february-2025.pdf).
```

## Ethics and safety, limitations

```
## **Ethics and Safety**

As open models become central to enterprise infrastructure, provenance and security are paramount. Developed by Google DeepMind, Gemma 4 undergoes the same rigorous safety evaluations as our proprietary Gemini models.

### **Evaluation Approach**

Gemma 4 models were developed in partnership with internal safety and responsible AI teams. A range of automated as well as human evaluations were conducted to help improve model safety. These evaluations align with [Google’s AI principles](https://ai.google/principles/), as well as safety policies, which aim to prevent our generative AI models from generating harmful content, including:

* Content related to child sexual abuse material and exploitation
* Dangerous content (e.g., promoting suicide, or instructing in activities that could cause real-world harm)
* Sexually explicit content
* Hate speech (e.g., dehumanizing members of protected groups)
* Harassment (e.g., encouraging violence against people)

### **Evaluation Results**

For all areas of safety testing, we saw major improvements in all categories of content safety relative to previous Gemma models. Overall, Gemma 4 models significantly outperform Gemma 3 and 3n models in improving safety, while keeping unjustified refusals low. All testing was conducted without safety filters to evaluate the model capabilities and behaviors. For both text-to-text and image-to-text, and across all model sizes, the model produced minimal policy violations, and showed significant improvements over previous Gemma models' performance.

## **Usage and Limitations**

These models have certain limitations that users should be aware of.
```

```
### **Limitations**

* **Training Data**
  * The quality and diversity of the training data significantly influence the model's capabilities. Biases or gaps in the training data can lead to limitations in the model's responses.
  * The scope of the training dataset determines the subject areas the model can handle effectively.
* **Context and Task Complexity**
  * Models perform well on tasks that can be framed with clear prompts and instructions. Open-ended or highly complex tasks might be challenging.
  * A model's performance can be influenced by the amount of context provided (longer context generally leads to better outputs, up to a certain point).
* **Language Ambiguity and Nuance**
  * Natural language is inherently complex. Models might struggle to grasp subtle nuances, sarcasm, or figurative language.
* **Factual Accuracy**
  * Models generate responses based on information they learned from their training datasets, but they are not knowledge bases. They may generate incorrect or outdated factual statements.
* **Common Sense**
  * Models rely on statistical patterns in language. They might lack the ability to apply common sense reasoning in certain situations.

### **Ethical Considerations and Risks**

The development of vision-language models (VLMs) raises several ethical concerns. In creating an open model, we have carefully considered the following:

* **Bias and Fairness**
  * VLMs trained on large-scale, real-world text and image data can reflect socio-cultural biases embedded in the training material. Gemma 4 models underwent careful scrutiny, input data pre-processing, and post-training evaluations as reported in this card to help mitigate the risk of these biases.
* **Misinformation and Misuse**
  * VLMs can be misused to generate text that is false, misleading, or harmful.
  * Guidelines are provided for responsible use with the model, see the [Responsible Generative AI Toolkit](https://ai.google.dev/responsible).
* **Transparency and Accountability**
  * This model card summarizes details on the models' architecture, capabilities, limitations, and evaluation processes.
  * A responsibly developed open model offers the opportunity to share innovation by making VLM technology accessible to developers and researchers across the AI ecosystem.

**Risks identified and mitigations**:

* **Generation of harmful content**: Mechanisms and guidelines for content safety are essential. Developers are encouraged to exercise caution and implement appropriate content safety safeguards based on their specific product policies and application use cases.
* **Misuse for malicious purposes**: Technical limitations and developer and end-user education can help mitigate against malicious applications of VLMs. Educational resources and reporting mechanisms for users to flag misuse are provided.
* **Privacy violations**: Models were trained on data filtered for removal of certain personal information and other sensitive data. Developers are encouraged to adhere to privacy regulations with privacy-preserving techniques.
* **Perpetuation of biases**: It's encouraged to perform continuous monitoring (using evaluation metrics, human review) and the exploration of de-biasing techniques during model training, fine-tuning, and other use cases.

### **Benefits**

At the time of release, this family of models provides high-performance open vision-language model implementations designed from the ground up for responsible AI development compared to similarly sized models.
```
