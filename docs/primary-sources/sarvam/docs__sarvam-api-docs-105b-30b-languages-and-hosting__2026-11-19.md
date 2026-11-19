# docs / Sarvam API documentation: model pages, language sets, deprecation

source_url: https://docs.sarvam.ai/api/token-factory/models/sarvam-105b.md ; https://docs.sarvam.ai/api/getting-started/models.md ; https://docs.sarvam.ai/api/getting-started/models/sarvam-30b.md
retrieval_date: 2026-11-19
exists: yes
retrieved: true

Verbatim extracts (publisher text, not edited). Notes by OneHill are marked NOTE.

## Sarvam-105B model page (hosted API)
```
> Sarvam-105B - 105B parameter flagship multilingual language model delivering state-of-the-art performance on Indian language understanding, reasoning, and generation tasks.

**Sarvam-105B (Flagship Chat LLM)**

Sarvam AI's flagship Mixture-of-Experts reasoning model trained from scratch, with Multi-head Latent Attention (MLA) for efficient long-context inference. Matches or outperforms most open and closed-source frontier models of its class across knowledge, reasoning, and agentic benchmarks.

**Highlights:**

* **105B+ total parameters**: our most capable MoE model with Multi-head Latent Attention
* Pre-trained on **12 trillion tokens** across code, math, multilingual, and web data
* **98.6 on Math500**, **88.3 on AIME 25** (96.7 with tools), **49.5 on BrowseComp**
* State-of-the-art Indian language performance: wins 90% of pairwise comparisons
* Powers **Indus**, Sarvam's AI assistant for complex reasoning and agentic workflows
* OpenAI-compatible chat completions API | Apache 2.0 open-source

## At a Glance

|                       |                                                                                                                                                                                        |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Model ID**          | `sarvam-105b` (flagship) · [`sarvam-105b-conversations`](#conversational-variant) (conversational)                                                                                     |
| **What it does**      | Flagship chat LLM, complex reasoning, coding, and agentic workflows (105B+ MoE with MLA). The conversational variant is post-trained for real-time dialogue and voice-agent use cases. |
| **Languages**         | 10 most-spoken Indian languages + English; native script, romanized, and code-mixed input                                                                                              |
| **APIs**              | [Chat Completions](/api/token-factory/chat-completions) (`POST /v1/chat/completions`; `sarvam-105b` also on `/v2/chat/completions`, OpenAI-compatible, streaming supported)            |
| **Input limits**      | 128K-token context window (`sarvam-105b`); 32K-token context window (`sarvam-105b-conversations`), [all limits](#limits)                                                               |
| **Benchmarks**        | [Key Features](#key-features) and the [model blog](https://www.sarvam.ai/blogs/sarvam-30b-105b)                                                                                        |
| **Pricing**           | ₹10 input · ₹0.25 cached input · ₹25 output per 1M tokens, <mark>introductory pricing</mark> through the end of 2026 ([Pricing page](/api/getting-started/pricing))                    |
| **Best for**          | Multi-step reasoning, code generation, long-context document analysis, agentic tool use                                                                                                |

#### Flagship Indian Language Support

Wins 90% of pairwise comparisons across Indian language benchmarks and 84% on STEM, math, and coding. Trained extensively on native script, romanized, and code-mixed inputs across the 10 most-spoken Indian languages.

```

```
Model IDs: `sarvam-105b`, `sarvam-105b-conversations`
...
* Pre-training Data: 12T tokens
...
* License: Apache 2.0

**Sarvam-M (24B)** has been deprecated and is no longer available through the API.
```

## Known limitations table (the only one listed)
```
Thinking mode is on by default: On `sarvam-105b`, reasoning (`reasoning_effort`, default `low`) is enabled by default, and reasoning tokens count toward completion tokens
```

## Models page: language sets
```
| Sarvam-105B (Chat LLM) | 11 (10 Indian + English), `sarvam-105b` | Serverless |
| Sarvam-105B Conversations (Chat LLM) | 11 (10 Indian + English), `sarvam-105b-conversations` | Serverless |

### 11-language set (Bulbul v3, Mayura, Sarvam-105B)
Hindi hi-IN, Bengali bn-IN, Tamil ta-IN, Telugu te-IN, Gujarati gu-IN, Kannada kn-IN, Malayalam ml-IN, Marathi mr-IN, Punjabi pa-IN, Odia od-IN, English en-IN
```

## Sarvam-30B API page
```
> Sarvam-30B - 30B parameter multilingual language model optimized for Indian languages with strong reasoning, coding, and conversational capabilities. Deprecated; migrate to Sarvam-105B.

> **Warning**
>
> **Deprecated Model:** Sarvam-30B has been deprecated. Please migrate to [**Sarvam-105B**](/api/token-factory/models/sarvam-105b) for improved performance across all tasks. The information below is retained for reference only.

**Languages** | 10 most-spoken Indian languages + English; native script, romanized, and code-mixed input
```

NOTE: Sarvam's own API documentation lists 10 Indian languages plus English for Sarvam-105B, Sarvam-105B Conversations and the (deprecated) Sarvam-30B, while the Hugging Face cards and blog headline say 22 Indian languages. The hosted sarvam-105b-conversations variant is not on Hugging Face. The page does not say whether the hosted sarvam-105b is the March weights or the 1711 build.
