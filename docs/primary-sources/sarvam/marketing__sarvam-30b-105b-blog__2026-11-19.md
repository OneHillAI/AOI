# marketing / Open-Sourcing Sarvam 30B and 105B (blog, dated 6 March 2026)

source_url: https://www.sarvam.ai/blogs/sarvam-30b-105b
retrieval_date: 2026-11-19
exists: yes
retrieved: true

Verbatim extracts (publisher text, not edited). Notes by OneHill are marked NOTE.

Doc type is marketing (publisher blog). Every statement below is a publisher claim. No technical report, paper or arXiv entry was found for these models (searched 2026-11-19).

```
We're releasing Sarvam 30B and Sarvam 105B as open-source models. Both are reasoning models trained from scratch on large-scale, high-quality datasets curated in-house across every stage of training: pre-training, supervised fine-tuning, and reinforcement learning. Training was conducted entirely in India on compute provided under the IndiaAI mission. These models represent a true full-stack effort. Beyond datasets, we optimized tokenization, model architecture, execution kernels, scheduling, and inference systems to make deployment efficient across a wide range of hardware, from flagship GPUs to personal devices like laptops. Both models are already in production.
```

```
Sarvam 105B is available on Indus. Both models are accessible via our API at the API dashboard. Weights can be downloaded from AI Kosh ( 30B, 105B ) and Hugging Face ( 30B, 105B ). If you want to run inference locally with Transformers, vLLM, and SGLang, please refer to the Hugging Face models page for sample implementations.
```

```
All stages of the training pipeline were developed and executed in-house. This includes the model architecture, data curation and synthesis pipelines, reasoning supervision frameworks, and reinforcement learning infrastructure. Building everything from scratch gave us direct control over data quality, training dynamics, and capability development across every stage of training, which is a core requirement for a sovereign stack.
```

```
Our 30B and 105B models were trained on large datasets, with 16T tokens for the 30B and 12T tokens for the 105B. The pre-training data spans code, general web data, specialized knowledge corpora, mathematics, and multilingual content. After multiple ablations, the final training mixture was balanced to emphasize reasoning, factual grounding, and software capabilities. We invested significantly in synthetic data generation pipelines across all categories. The multilingual corpus allocates a substantial portion of the training budget to the 10 most-spoken Indian languages.
```

```
For safety fine-tuning, we developed a dataset covering both standard and India-specific risk scenarios. This effort was guided by a unified taxonomy and an internal model specification inspired by public frontier model constitutions. To surface and address challenging failure modes, the dataset was further augmented with adversarial and jailbreak-style prompts mined through automated red-teaming. These prompts were paired with policy-aligned, safe completions for supervised training.
```

```
To evaluate Indian language capabilities, we developed a new benchmark using a pairwise comparison framework with an LLM-as-judge protocol. A key goal of this benchmark is to reflect how language is actually used in India today. This means evaluating each language in two script styles, native script representing formal written usage and romanized Latin script representing colloquial usage commonly seen in messaging and online communication. The benchmark is organized into four domains: general chat, STEM, mathematics, and coding. It originates from 110 English source prompts, with 50 covering general chat and 20 each for STEM, mathematics, and coding. Each prompt is translated into 22 scheduled Indian languages and provided in both native and romanized script. Evaluating correctness for complex reasoning prompts directly in low-resource languages can be noisy and inconsistent. To address this, we generated high-quality reference answers in English using Claude Opus 4, which are used only to evaluate the usefulness dimension, covering relevance, completeness, and correctness, for answers generated in Indian languages. The evaluation uses a pairwise comparison methodology with Gemini 3 as the judge model. The judge evaluates responses across four dimensions: fluency, language/script correctness, usefulness, and verbosity. The evaluation dataset and corresponding prompts are available
```

```
Sarvam 105B wins on average 90% across all benchmarked dimensions and on average 84% on STEM. math, and coding. Sarvam 30B wins on average 89% of comparisons across all benchmarked dimensions and 87% on STEM, mathematics, and coding.
```

```
The Sarvam tokenizer is optimized for efficient tokenization across all 22 scheduled Indian languages, spanning 12 different scripts, directly reducing the cost and latency of serving in Indian languages. It outperforms other open-source tokenizers in encoding Indic text efficiently, as measured by the fertility score, which is the average number of tokens required to represent a word. It is significantly more efficient for low-resource languages such as Odia, Santali, and Manipuri (Meitei) compared to other tokenizers. The chart below shows the average fertility of various tokenizers across English and all 22 scheduled languages.
```

```
Sarvam 30B and Sarvam 105B represent a significant step in building high-performance, open foundation models in India. By combining efficient Mixture-of-Experts architectures with large-scale, high-quality training data and deep optimization across the entire stack, from tokenizer design to inference efficiency, both models deliver strong reasoning, coding, and agentic capabilities while remaining practical to deploy. A defining strength of the Sarvam model family is its investment in the Indian AI ecosystem, reflected in strong performance across Indian languages, tokenization optimized for diverse scripts, and safety and evaluation tailored to India-specific contexts. Combined with Apache 2.0 open-source availability, these models serve as foundational infrastructure for sovereign AI development.
```

```
These models were trained using compute provided through the IndiaAI Mission, under the Ministry of Electronics and Information Technology, Government of India. Nvidia collaborated closely on the project, contributing libraries used across pre-training, alignment, and serving. We're also grateful to the developers who used earlier Sarvam models and took the time to share feedback. We're open-sourcing these models as part of our ongoing work to build foundational AI infrastructure in India.
```

NOTE: blog 30B table row 'AIME 25 (w/ tools)' reads 80.0 (96.7) while the Hugging Face 30B card reads 88.3 (96.7); the blog's own prose says 'On AIME 25, it achieves 88.3 Pass@1'. The blog table is therefore inconsistent with its own text. The blog 105B table lists 34.46 in the Qwen3-Next SWE-Bench cell where the card lists 60.9. Per-language results for the 22-language benchmark appear only as charts; no per-language numbers are available as text. The blog names the 10 most-spoken Indian languages as the pre-training emphasis, not all 22.
