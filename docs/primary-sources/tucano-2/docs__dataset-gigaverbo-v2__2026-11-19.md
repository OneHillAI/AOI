doc_type: docs
entity: tucano-2
variant/applies-to: Polygl0t/gigaverbo-v2 (pretraining corpus, ~320B tokens)
source_url: https://huggingface.co/datasets/Polygl0t/gigaverbo-v2
retrieval_date: 2026-11-19
exists: yes
retrieved: true

## Extracts (VERBATIM from the dataset card README.md)


[Front matter] license: other ; gated: false (Hugging Face API) ; 302 parquet files; HEAD request on edu_high/train-00000-of-00056.parquet returned HTTP 200, content-length 1,277,623,206 (not downloaded).

[Dataset Summary]
### Dataset Summary

> **Update Notice (27.09.2026):** This dataset has been updated with a better split of the annotators' scores.

This repository contains a large corpus of Portuguese text (~320 billion tokens), which has been filtered and annotated using classifiers for educational content and toxicity. The dataset is intended for training language models and other NLP applications in Portuguese. GigaVerbo is part of the Polyglot project, which aims to develop multilingual resources and models for underrepresented languages.

The corpus is organized into four subsets, split according to the predicted educational quality and toxicity of each document:

| Subset       | Criterion                                   | Description                                                                 |
| ------------ | ------------------------------------------- | --------------------------------------------------------------------------- |
| `edu_high`   | `edu_int_score` ≥ 4 and `toxic_int_score` ≤ 3 | Highly educational, non-toxic documents (**default** subset).              |
| `edu_medium` | `edu_int_score` = 3 and `toxic_int_score` ≤ 3 | Moderately educational, non-toxic documents.                               |
| `edu_low`    | `edu_int_score` ≤ 2 and `toxic_int_score` ≤ 3 | Documents with little to no educational value.                  |
| `nsfw`       | `toxic_int_score` ≥ 4                        | Documents flagged as toxic / not safe for work (any educational score).    |

This allows users to easily build quality-based data mixtures (e.g., upsampling `edu_high` during annealing phases) without having to filter the full corpus themselves.

[Statistics table]
#### Statistics

| Subset       | Files   | Rows            | Size          | Tokens              | % of Tokens | Mean Tokens / Doc | Median Tokens / Doc |
| ------------ | ------- | --------------- | ------------- | ------------------- | ----------- | ----------------- | ------------------- |
| `edu_high`   | 56      | 16,245,599      | 70.96 GB      | 27,877,708,607      | 8.69%       | 1,716             | 854                 |
| `edu_medium` | 77      | 70,973,605      | 223.66 GB     | 88,984,480,724      | 27.75%      | 1,254             | 592                 |
| `edu_low`    | 146     | 284,889,372     | 469.97 GB     | 200,825,926,813     | 62.63%      | 705               | 298                 |
| `nsfw`       | 23      | 2,892,095       | 7.25 GB       | 2,987,598,133       | 0.93%       | 1,033             | 461                 |
| **Total**    | **302** | **375,000,671** | **771.84 GB** | **320,675,714,277** | **100%**    | —                 | —                   |

- **Total of EDU (`edu_high` + `edu_medium`) tokens**: 116,862,189,331
- **Total of Non-EDU (`edu_low`) tokens**: 200,825,926,813
- **Total of non-toxic (`edu_high` + `edu_medium` + `edu_low`) tokens**: 317,688,116,144

[Source Data, licences]
### Source Data

We sourced data from a variety of existing datasets available on Hugging Face. These datasets offer a mix of curated and semi-curated content, providing a solid foundation for our corpus to start (see the table below). Unlike web crawls, these datasets often come with some level of quality control, allowing us to bypass some of the initial cleaning steps (e.g., cleaning of HTML tags). However, we also recognized the need to supplement these datasets with more extensive web-crawled data to ensure sufficient coverage and diversity, especially when it comes to adding timely data from recent snapshots of CommonCrawl.

- **Cutoff Date:** December 2025

| Source Type  | Dataset / Crawl                                                                                                                | License(s)                                                                                                                      |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| Common Crawl |                                                                                                                                | [ODC-By v1.0](https://opendatacommons.org/licenses/by/1-0/), [CommonCrawl's Terms of Use](https://commoncrawl.org/terms-of-use) |
|              | [CC-MAIN-2025-30](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-30/index.html)                                          |                                                                                                                                 |
|              | [CC-MAIN-2025-38](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-38/index.html)                                          |                                                                                                                                 |
|              | [CC-MAIN-2025-33](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-33/index.html)                                          |                                                                                                                                 |
|              | [CC-MAIN-2025-26](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-26/index.html)                                          |                                                                                                                                 |
|              | [CC-MAIN-2024-51](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-51/index.html)                                          |                                                                                                                                 |
|              | [CC-MAIN-2023-50](https://data.commoncrawl.org/crawl-data/CC-MAIN-2023-50/index.html)                                          |                                                                                                                                 |
|              | [CC-MAIN-2023-23](https://data.commoncrawl.org/crawl-data/CC-MAIN-2023-23/index.html)                                          |                                                                                                                                 |
|              | [CC-MAIN-2022-49](https://data.commoncrawl.org/crawl-data/CC-MAIN-2022-49/index.html)                                          |                                                                                                                                 |
|              | [CC-MAIN-2021-49](https://data.commoncrawl.org/crawl-data/CC-MAIN-2021-49/index.html)                                          |                                                                                                                                 |
|              | [CC-MAIN-2020-50](https://data.commoncrawl.org/crawl-data/CC-MAIN-2020-50/index.html)                                          |                                                                                                                                 |
| Hugging Face |                                                                                                                                |                                                                                                                                 |
|              | [HuggingFaceFW/fineweb-2](https://huggingface.co/datasets/HuggingFaceFW/fineweb-2)                                             | [ODC-By v1.0](https://opendatacommons.org/licenses/by/1-0/), [CommonCrawl's Terms of Use](https://commoncrawl.org/terms-of-use) |
|              | [HuggingFaceFW/finepdfs](https://huggingface.co/datasets/HuggingFaceFW/finepdfs)                                               | [ODC-By v1.0](https://opendatacommons.org/licenses/by/1-0/), [CommonCrawl's Terms of Use](https://commoncrawl.org/terms-of-use) |
|              | [HPLT/HPLT2.0_cleaned](https://huggingface.co/datasets/HPLT/HPLT2.0_cleaned)                                                   | [cc0-1.0](https://choosealicense.com/licenses/cc0-1.0/)                                                                         |
|              | [HPLT/hplt_monolingual_v1_2](https://huggingface.co/datasets/HPLT/hplt_monolingual_v1_2)                                       | [cc0-1.0](https://choosealicense.com/licenses/cc0-1.0/)                                                                         |
|              | [legacy-datasets/mc4](https://huggingface.co/datasets/legacy-datasets/mc4)                                                     | [ODC-By v1.0](https://opendatacommons.org/licenses/by/1-0/), [CommonCrawl's Terms of Use](https://commoncrawl.org/terms-of-use) |
|              | [thegoodfellas/mc4-pt-cleaned](https://huggingface.co/datasets/thegoodfellas/mc4-pt-cleaned)                                   | [ODC-By v1.0](https://opendatacommons.org/licenses/by/1-0/), [CommonCrawl's Terms of Use](https://commoncrawl.org/terms-of-use) |
|              | [eduagarcia/LegalPT_dedup](https://huggingface.co/datasets/eduagarcia/LegalPT_dedup)                                           | [cc-by-4.0](https://choosealicense.com/licenses/cc-by-4.0/)                                                                     |
|              | [eduagarcia/CrawlPT_dedup](https://huggingface.co/datasets/eduagarcia/CrawlPT_dedup)                                           | [cc0-1.0](https://choosealicense.com/licenses/cc0-1.0/)                                                                         |
|              | [oscar-corpus/OSCAR-2201](https://huggingface.co/datasets/oscar-corpus/OSCAR-2201)                                             | [cc0-1.0](https://choosealicense.com/licenses/cc0-1.0/)                                                                         |
|              | [recogna-nlp/UltrachatBR](https://huggingface.co/datasets/recogna-nlp/UltrachatBR)                                             | [MIT](https://choosealicense.com/licenses/mit/)                                                                                 |
|              | [unicamp-dl/quati](https://huggingface.co/datasets/unicamp-dl/quati)                                                           | [cc-by-4.0](https://choosealicense.com/licenses/cc-by-4.0/)                                                                     |
|              | [thegoodfellas/blogset-br](https://huggingface.co/datasets/thegoodfellas/blogset-br)                                           | [Apache 2.0](https://choosealicense.com/licenses/apache-2.0/)                                                                   |
|              | [uonlp/CulturaX](https://huggingface.co/datasets/uonlp/CulturaX)                                                               | [ODC-By v1.0](https://opendatacommons.org/licenses/by/1-0/), [CommonCrawl's Terms of Use](https://commoncrawl.org/terms-of-use) |
|              | [graelo/wikipedia](https://huggingface.co/datasets/graelo/wikipedia)                                                           | [cc-by-sa-3.0](https://spdx.org/licenses/CC-BY-SA-3.0)                                                                          |
|              | [pablo-moreira/gpt4all-j-prompt-generations-pt](https://huggingface.co/datasets/pablo-moreira/gpt4all-j-prompt-generations-pt) | [Apache 2.0](https://choosealicense.com/licenses/apache-2.0/)                                                                   |
|              | [carolina-c4ai/corpus-carolina](https://huggingface.co/datasets/carolina-c4ai/corpus-carolina)                                 | [cc-by-4.0](https://choosealicense.com/licenses/cc-by-4.0/)                                                                     |
|              | [csebuetnlp/xlsum](https://huggingface.co/datasets/csebuetnlp/xlsum)                                                           | [cc-by-nc-sa-4.0](https://spdx.org/licenses/CC-BY-NC-SA-4.0)                                                                    |
|              | [MBZUAI/Bactrian-X](https://huggingface.co/datasets/MBZUAI/Bactrian-X)                                                         | [cc-by-nc-4.0](https://spdx.org/licenses/CC-BY-NC-4.0/)                                                                         |
|              | [bigscience-data/roots_pt_wikiquote](https://huggingface.co/datasets/bigscience-data/roots_pt_wikiquote)                       | [cc-by-sa-3.0](https://spdx.org/licenses/CC-BY-SA-3.0)                                                                          |
|              | [heloisy/cosmos_qa_ptbr](https://huggingface.co/datasets/heloisy/cosmos_qa_ptbr)                                               | [cc-by-4.0](https://choosealicense.com/licenses/cc-by-4.0/)                                                                     |
|              | [Gustrd/dolly-15k-libretranslate-pt](https://huggingface.co/datasets/Gustrd/dolly-15k-libretranslate-pt)                       | [cc-by-sa-3.0](https://spdx.org/licenses/CC-BY-SA-3.0)                                                                          |
| Other        |                                                                                                                                |                                                                                                                                 |
|              | [BDTD](https://bdtd.ibict.br/vufind/)                                                                                          | [cc-by-4.0](https://choosealicense.com/licenses/cc-by-4.0/)                                                                     |
|              | [Baixe Livros](https://www.baixelivros.com.br/dominio-publico/)                                                                | [Public Domain](https://creativecommons.org/public-domain/)                                                                     |

[Licensing Information]
### Licensing Information

Please refer to the individual licenses of the source datasets used to create this corpus, as listed in the "Source Data" section above. The combined dataset does not have a single unified license, and users should ensure compliance with the terms of each source dataset when utilizing this corpus.

[Per-source token counts, from .assets/report_gigaverbo_v2_default.json (default subsets edu_high + edu_medium + edu_low)]
xlsum (CC-BY-NC-SA-4.0): 0.014B tokens. Bactrian-X (CC-BY-NC-4.0): 0.008B tokens. Total default subsets: 317,688,116,144 tokens. The NC sources are about 0.007% of the corpus tokens. Neither the card nor the paper says whether these documents entered the sampled pretraining mixture.
