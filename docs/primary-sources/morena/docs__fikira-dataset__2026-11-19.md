doc_type: docs
entity: morena
variant/applies-to: vamboai/fikira, the one released dataset that the paper names as part of the supervised fine-tuning corpus
source_url: https://huggingface.co/datasets/vamboai/fikira (raw README: https://huggingface.co/datasets/vamboai/fikira/raw/main/README.md; API https://huggingface.co/api/datasets?author=vamboai)
retrieval_date: 2026-11-19
exists: yes
retrieved: true

## Governing statements (verbatim)

"license: mit" ; "This dataset contains 50,000 reasoning examples across 10 African languages, synthetically generated as part of ongoing experiments at Vambo AI." Languages: Zulu, Xhosa, Shona, Swahili, Kinyarwanda, Amharic, Yoruba, Igbo, Hausa, Tunisian Arabic (5,000 each). The card does not name the model used to generate the examples. "Disclaimer: This dataset was synthetically generated and may contain inaccuracies, errors, or artifacts ... The content has not been fully validated by native speakers of all languages". "MIT License Copyright (c) 2025 Vambo Technologies (trading as Vambo AI)". Contributors: Isheanesu Nigel Misi (HF user thisisisheanesu) and Vambo AI. Public, not gated, created 2025-12-13.

Note: only Fikira (50,000 rows, 10 languages, of which 8 overlap the MORENA twelve) is public. The card metadata of the instruct model also lists vamboai/morena-sft-corpus; the dataset page and API return HTTP 401, so it is not publicly readable. The paper's SFT corpus is 4.23B tokens (p6), far larger than Fikira.
