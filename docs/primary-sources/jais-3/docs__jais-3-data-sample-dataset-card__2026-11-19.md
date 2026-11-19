# docs / IFM/Jais-3-Data dataset card (published training-data sample)

source_url: https://huggingface.co/datasets/IFM/Jais-3-Data (raw README https://huggingface.co/datasets/IFM/Jais-3-Data/raw/main/README.md; API https://huggingface.co/api/datasets/IFM/Jais-3-Data)
retrieval_date: 2026-11-19
doc_type: docs
exists: yes
retrieved: true
tag: publisher

NOTE (OneHill): the dataset API reports gated false, private false, created 2026-10-06, last modified 2026-11-11, front matter licences odc-by and cc-by-4.0, and a file list of Parquet shards under cpt/ and sft/ plus MANIFEST_parquet.tsv. No data shard was downloaded. The four subsets are Arabic web text, style rewrites, web question-answer pairs and Arabic SFT conversations. The dialect corpora, translated reasoning data, Arabizi corpus, partner-supplied books and the agentic and file-manipulation trajectories described in the report are not among the four subsets.

## Raw README (verbatim, from the front matter to the end of the licence section)
```
---
license:
- odc-by
- cc-by-4.0
language:
- ar
pretty_name: Jais-3 Data
task_categories:
- text-generation
tags:
- jais-3
- training-data
- parquet
- arabic
configs:
- config_name: arabic-txt360-cc
  default: true
  data_files:
  - split: train
    path: cpt/arabic-txt360-cc/*.parquet
- config_name: arabic-txt360-style-rewrite
  data_files:
  - split: train
    path: cpt/arabic-txt360-style-rewrite/*.parquet
- config_name: arabic-cc-qa
  data_files:
  - split: train
    path: cpt/arabic-cc-qa/*.parquet
- config_name: arabic-txt360-3efforts-sft
  data_files:
  - split: train
    path: sft/arabic-txt360-3efforts-sft/*.parquet
---

# Jais-3 Data

## Dataset Description

Jais-3 Data is a 23.8 billion-token sample of the data used to train the Jais-3 family of
Arabic language models, released by the Institute of Foundation Models (IFM) at MBZUAI. It
covers about 10% of the continued-pretraining (CPT) and supervised-fine-tuning (SFT) tokens of
Jais-3 and is part of the [Jais 3 collection](https://huggingface.co/collections/IFM/jais-3).
It is intended for language-model training and research; the four subsets can be streamed
independently or combined with user-defined weights.

## Dataset Subsets

| Subset | Stage | Content | Records | Tokens | License |
| --- | --- | --- | ---: | ---: | --- |
| `arabic-txt360-cc` | CPT | Arabic web text from 83 Common Crawl dumps (CC-MAIN-2013-48 to CC-MAIN-2024-30) | 39,191,869 | 15.07 B | ODC-BY |
| `arabic-txt360-style-rewrite` | CPT | The same web text rewritten in formal, simple and funny styles | 12,379,664 | 4.42 B | ODC-BY |
| `arabic-cc-qa` | CPT | Web passages followed by generated question-answer pairs | 2,966,538 | 1.16 B | ODC-BY |
| `arabic-txt360-3efforts-sft` | SFT | Arabic conversations with and without reasoning traces | 2,811,750 | 3.20 B | CC BY 4.0 |

`arabic-txt360` marks data built with the [TxT360](https://huggingface.co/datasets/IFM/TxT360)
recipe applied to Arabic web text; `arabic-txt360-3efforts-sft` is the Arabic counterpart of
LLM360's TxT360-3efforts. None of the four is published separately. Each subset is a single
`train` split of Parquet shards under `cpt/` or `sft/`; `MANIFEST_parquet.tsv` lists the sha256,
record count, size and token count of every shard. About 2.0% of `arabic-cc-qa` passages also
appear in `arabic-txt360-cc`.

In `arabic-txt360-cc`, GlotLID labels 89.5% of documents Modern Standard Arabic, 6.7% Moroccan,
2.5% Egyptian and 1.0% Najdi Arabic; 7.7% are flagged code-switched. The rewrite subset is 49.0%
funny, 42.6% formal and 8.4% simple. In the SFT subset 33.0% of conversations carry a reasoning
trace, written mostly in English, across six categories: STEM, code, chat, math, teacher-as-assistant
and math dialogue.

## Data Fields

All subsets carry `text` or `messages` and `token_count`, the number of Jais-3 tokenizer tokens.

- `arabic-txt360-cc`: `meta` with `url`, `timestamp`, `cc-path`, `lang` and `lang_score` (fastText),
  `glotid` and `glotid_prob` (GlotLID), `is_code_switched`.
- `arabic-txt360-style-rewrite`: `source_style` (`formal`, `simple` or `funny`).
- `arabic-cc-qa`: `meta` with `url`, `timestamp`, `cc-path`, `detected_language`, `num_qa_pairs`
  (0 for the 5.0% of passages whose pairs were all rejected), `qa_token_ratio`, `skip_reason`.
- `arabic-txt360-3efforts-sft`: `messages` (turns with `role`, `content`, `think`, `think_faster`),
  `category`, `conv_index`, `n_turns`. Every assistant turn has exactly one of `think` (reasoning
  trace) or `think_faster` (empty string). About 9.9% of conversations start with a Jais-3 identity
  system prompt.

```python
from datasets import load_dataset
dataset = load_dataset("IFM/Jais-3-Data", "arabic-txt360-cc", split="train", streaming=True)
print(next(iter(dataset)))
```

## Data Provenance and Processing

This dataset has been collected, cleaned, and processed entirely by the IFM team.

The CPT subsets come from Common Crawl with Arabic language identification, quality filtering
and deduplication; the rewrite and question-answer subsets are derived from that web text. The
SFT subset is built from Arabic translations of prompts in LLM360's
[TxT360-3efforts](https://huggingface.co/datasets/LLM360/TxT360-3efforts), with model-generated
responses and reasoning traces. E-mail addresses and IPv4 addresses in all four subsets are
replaced by `[EMAIL]` and `[IP]`. The web-derived subsets cover Common Crawl dumps up to
CC-MAIN-2024-30 (July 2024).

## Limitations and Responsible Use

Large-scale training data can contain factual errors, duplicates, sensitive topics and unsafe
content; users are responsible for evaluation and filtering appropriate to their application.
To request the removal of content, open a discussion in this repository.

## License and Terms of Use

The three CPT subsets are licensed under the
[Open Data Commons Attribution License (ODC-BY) v1.0](https://opendatacommons.org/licenses/by/1-0/);
the underlying pages are subject to the [Common Crawl Terms of Use](https://commoncrawl.org/terms-of-use).
The SFT subset is licensed under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode) and is derived from
TxT360-3efforts by LLM360, released under the same license.

```
