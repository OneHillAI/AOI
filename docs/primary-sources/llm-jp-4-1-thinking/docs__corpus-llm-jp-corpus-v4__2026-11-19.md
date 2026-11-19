# docs / corpus-llm-jp-corpus-v4

source_url: https://gitlab.llm-jp.nii.ac.jp/datasets/llm-jp-corpus-v4 (raw README.md)
retrieval_date: 2026-11-19
exists: yes
retrieved: true

Verbatim extracts (publisher text, not edited). Notes by OneHill are marked NOTE.

NOTE (OneHill): public GitLab project (API visibility: public, created 2025-05-15, last activity 2026-04-24). Only the README was fetched. Sections below are the structure tree and the redistribution and exclusion notes; the per-subcorpus licence list is in the same README (Aozora Bunko CC BY 4.0; ja_cc and FineWeb-2 ODC-BY plus Common Crawl terms of use; Wikipedia CC BY-SA 3.0; Dolma ODC-BY; MathPile Commercial CC BY-SA 4.0; The Stack v1 "Each repository follows its own license"; and so on).

## Structure
```
## Dataset Structure

The dataset is organized as follows. Each language and sub-corpus is stored in its own directory, with multiple `jsonl.gz` files in each directory.

```
. (Total File Size : 33TB) (Total token # : 19.5T)
├── ja (688B)
│   ├── ja_aozorabunko (0.1B)
│   ├── ja_cc (223B)
│   │   ├── level0
│   │   ├── level1
│   │   └── level2
│   ├── ja_e-gov (0.08B)
│   ├── ja_fineweb-2 (236B)
│   ├── ja_kaken (0.9B)
│   ├── ja_kokkai_giji (0.8B)
│   ├── ja_nwc2010 (16B)
│   ├── ja_patent (68B)
│   ├── ja_sip_comprehensive_html (11B)
│   ├── ja_sip_comprehensive_pdf (30B)
│   │   ├── pdf2text
│   │   └── surya
│   ├── ja_warp_html (0.8B)
│   ├── ja_warp_pdf (58B)
│   │   ├── e0
│   │   └── e0.2
│   └── ja_wiki (1B)
├── en (17.8T)
│   ├── en_dolma (155B)
│   │   ├── books (5B)
│   │   ├── pes2o (63B)
│   │   ├── reddit (83B)
│   │   └── wiki (4B)
│   ├── en_dolmino (1.5B)
│   │   └── stackexchange (1.5B)
│   ├── en_finemath (10B)
│   │   └── 4plus (10B)
│   ├── en_fineweb (17.6T)
│   │   ├── eduscore2 (6.2T)
│   │   └── rest (11.4T)
│   ├── en_gsm8k (0.003B)
│   ├── en_mathpile (9B)
│   ├── en_olmo (49B)
│   │   ├── algebraicstack (13B)
│   │   ├── arxiv (22B)
│   │   └── openwebmath (13B)
│   └── en_wiki (5B)
├── ko (52B)
│   ├── ko_fineweb2 (52B)
│   └── ko_wiki (0.3B)
├── zh (789B)
│   ├── zh_fineweb2 (788B)
│   └── zh_wiki (0.8B)
└── code (218B)
    ├── code_olmo-starcoder (104B)
    └── code_stack (114B)
```

( ) : Number of tokens counted with llm-jp-tokenizer v3

Each jsonl file consists of a `text` key with the text content and a `meta` key containing additional information such as a document ID and a URL.
```

## Redistribution and exclusion notes
```
Copyright for each document in this dataset belongs, in principle, to the original author of the document. This dataset is intended for use in pretraining large language models, and is distributed from a server located in Japan to comply with Japanese copyright law. Usage, including redistribution, is permitted within the scope of each license, but please note that Japanese copyright law may not apply if redistributed from servers outside Japan.

The original LLM-jp Corpus v4 includes the following two Japanese sub-corpora. However, they are not included in this dataset because they cannot be redistributed. For information on how to obtain them, please contact each site directly.
- A Japanese corpus extracted and filtered using Uzushio from [NINJAL Web Japanese Corpus (NWJC)](https://masayu-a.github.io/NWJC/)
- A Japanese corpus extracted and filtered using Uzushio from [Ceek.jp News](https://news.ceek.jp/)

In developing the LLM-jp-4 model series, we excluded the following sub-corpora from pre-training.
- en_fineweb: We did not use this sub-corpus because its split is based on an educational score assigned using Llama-3-70B-Instruct, which prevents release of the resulting model under an OSS license. Instead, we reproduced this sub-corpus using Qwen3-32B (Apache 2.0) and used the reproduced version for pre-training. The reproduced sub-corpus is available at [https://gitlab.llm-jp.nii.ac.jp/datasets/llm-jp-corpus-v4.1/-/tree/main/en/en_fineweb-rescored](https://gitlab.llm-jp.nii.ac.jp/datasets/llm-jp-corpus-v4.1/-/tree/main/en/en_fineweb-rescored).
- en_finemath: We did not use this sub-corpus because its construction process relies on Llama-3.1-70B-Instruct, which likewise prevents release of the resulting model under an OSS license.
- ja_sip_comprehensive_pdf/surya: We did not use this sub-corpus because the extracted text was of insufficient quality.
```
