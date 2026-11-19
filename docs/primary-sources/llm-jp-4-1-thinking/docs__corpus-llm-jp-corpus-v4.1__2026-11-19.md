# docs / corpus-llm-jp-corpus-v4.1

source_url: https://gitlab.llm-jp.nii.ac.jp/datasets/llm-jp-corpus-v4.1 (raw README.md)
retrieval_date: 2026-11-19
exists: yes
retrieved: true

Verbatim extracts (publisher text, not edited). Notes by OneHill are marked NOTE.

NOTE (OneHill): the GitLab project is public (API visibility: public, created 2026-02-18, last activity 2026-04-24) and the file listing for en/en_fineweb-rescored is readable without login (jsonl.gz parts). Only the README was fetched; no data files were downloaded. This corpus holds English web, English maths and code only. The Japanese, Chinese and Korean pre-training data are in LLM-jp Corpus v4 (separate file).

```
# LLM-jp Corpus v4.1

This repository contains LLM-jp Corpus v4.1, used as part of the corpus mixture for the pretraining of the LLM-jp-4 model series.

To support the continued development of LLM-jp, we would greatly appreciate it if you could share how you utilize LLM-jp outcomes via the [survey form](https://forms.gle/AvbNXTNT2ADsssHq5).

## Directory Structure

```
.
├── en (18T)
│   ├── en_fineweb-rescored (18T)
│   ├── en_megamath-web-pro-max-oss (67B)
└── code (720B)
    └── code_stack-v2 (720B)
```

( ) : Number of tokens counted with llm-jp-tokenizer v4

Each jsonl file consists of a `text` key with the text content and additional keys that contain information such as document IDs and URLs.

## Details and License of Each Sub-corpus

- en
  - en_fineweb-rescored
    - Texts sourced from [the FineWeb dataset](https://huggingface.co/datasets/HuggingFaceFW/fineweb). Each text is assigned an educational score following [the FineWeb-Edu methodology](https://arxiv.org/abs/2406.17557). We used [Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B) (Apache 2.0 license) to annotate a small subset of the data, then trained a lightweight model to annotate the full corpus.
    - License: [ODC-BY](https://creativecommons.org/licenses/by/4.0/) (Users must also comply with [Common Crawl terms of use](https://commoncrawl.org/terms-of-use).)
  - en_megamath-web-pro-max-oss
    - A mathematics-domain text corpus constructed by following [the MegaMath-Web-Pro-Max dataset](https://huggingface.co/datasets/OctoThinker/MegaMath-Web-Pro-Max). We used [gpt-oss-120b](https://huggingface.co/openai/gpt-oss-120b) (Apache 2.0 license) to annotate a subset of texts with mathematical relatedness scores, then trained a lightweight model to annotate the full corpus. We used gpt-oss-120b again to paraphrase the filtered texts.
    - License: [ODC-BY](https://creativecommons.org/licenses/by/4.0/) (Users must also comply with [Common Crawl terms of use](https://commoncrawl.org/terms-of-use).)
- code
  - code_stack-v2
    - Code sourced from [the Stack v2 dataset](https://huggingface.co/datasets/bigcode/the-stack-v2).
    - License: Each repository follows its own license

Copyright for each document in this corpus belongs, in principle, to the original author of the document.
This corpus is intended for use in pretraining large language models, and is distributed from a server located in Japan to comply with Japanese copyright law.
Usage, including redistribution, is permitted within the scope of each license, but please note that Japanese copyright law may not apply if redistributed from servers outside Japan.

## Change log

* [2026/04/14] The remaining portion of the `en_fineweb-rescored` sub-corpus was uploaded.
* [2026/03/31] Initial release; this release did not yet include the lower-scored portion of the `en_fineweb-rescored` sub-corpus.

## Contact

For requests to remove documents from the corpus or for other inquiries, please contact us at: llm-jp-corpus (at) nii.ac.jp
```
