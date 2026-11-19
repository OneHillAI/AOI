# docs / indivibe evaluation dataset card

source_url: https://huggingface.co/datasets/sarvamai/indivibe (raw README.md)
retrieval_date: 2026-11-19
exists: yes
retrieved: true

Verbatim extracts (publisher text, not edited). Notes by OneHill are marked NOTE.

```
---
configs:
  - config_name: chat
    data_files:
      - split: test
        path: chat/test.parquet
  - config_name: code
    data_files:
      - split: test
        path: code/test.parquet
  - config_name: math
    data_files:
      - split: test
        path: math/test.parquet
  - config_name: stem
    data_files:
      - split: test
        path: stem/test.parquet
language:
  - as
  - bn
  - brx
  - doi
  - gu
  - hi
  - kn
  - ks
  - kok
  - mai
  - ml
  - mni
  - mr
  - ne
  - or
  - pa
  - sa
  - sat
  - sd
  - ta
  - te
  - ur
license: cc-by-4.0
task_categories:
  - text-generation
pretty_name: indivibe
size_categories:
  - 1K<n<10K
---

# indivibe

## Overview

To rigorously evaluate the Indic capabilities of Sarvam models across all 22 scheduled languages, we developed a new Indic benchmark and evaluated models using a pairwise comparison framework with an LLM-as-judge protocol. A key goal of this benchmark is to reflect how language is actually used in India today. In practice, this means evaluating each language in two script styles: native script (formal written usage) and romanized Latin script (colloquial usage commonly seen in messaging and online communication).

We organize the benchmark into four domains: general chat, STEM, mathematics, and coding. The benchmark originates from 110 English source prompts: 50 general chat and 20 each for STEM, mathematics, and coding. Each prompt is translated into all 22 scheduled Indian languages and provided in both native and romanized script, yielding 220 prompts per language and 4,840 prompts in total (22 languages × 2 scripts × 110 prompts).

The general chat domain covers creative writing, cultural knowledge, everyday advice, emotional support, and light reasoning. The STEM, mathematics, and coding domains are designed to more directly evaluate multilingual reasoning and technical problem-solving.

Because all languages use translations of the same underlying source prompts, models are evaluated on semantically equivalent tasks across every language and script, enabling fair cross-lingual comparison while allowing independent analysis of conversational and reasoning performance by domain.

## Dataset Subsets

| Subset | Prompts per language | Total prompts | Description |
|--------|---------------------|---------------|-------------|
| **chat** | 100 (50 native + 50 romanized) | 2,200 | Creative writing, cultural knowledge, everyday advice, emotional support, and light reasoning |
| **code** | 40 (20 native + 20 romanized) | 880 | Algorithms, data structures, web development, security, DevOps, and more |
| **math** | 40 (20 native + 20 romanized) | 880 | Algebra, geometry, calculus, probability, number theory, and more |
| **stem** | 40 (20 native + 20 romanized) | 880 | Physics, chemistry, biology, engineering, economics, and more |

## Schema

| Column | Type | Description |
|--------|------|-------------|
| `prompt` | string | The evaluation prompt in the target language and script |
```

NOTE: the dataset holds prompts only (110 English source prompts translated into 22 languages in two scripts). The card names no judge model, no results and no evaluation code. The blog says the judge is Gemini 3 and the reference answers were written by Claude Opus 4.
