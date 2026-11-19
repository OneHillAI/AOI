doc_type: license
entity: boldt
variant/applies-to: Boldt-DC-350M and Boldt-DC-1B (also true of every other Boldt model repo)
source_url: https://huggingface.co/api/models/Boldt/Boldt-DC-350M and .../Boldt-DC-1B (cardData.license); https://huggingface.co/Boldt/Boldt-DC-1B/raw/main/LICENSE
retrieval_date: 2026-11-19
exists: yes (as a front-matter declaration); no separate LICENSE file
retrieved: true (declaration read; no file to read)

## What was read
[Declaration - VERBATIM] Front matter of both cards: "license: apache-2.0". API cardData.license: "apache-2.0". Tags include "license:apache-2.0".

[No licence file] GET https://huggingface.co/Boldt/<repo>/raw/main/LICENSE returned HTTP 404 for all 19 Boldt model repos on 2026-11-19. The repo trees (API) list no LICENSE, NOTICE or COPYING file. Neither card body names a licence or a copyright holder.

[Paper statement, future tense] arXiv 2604.28075 Appendix C: "Our re-translated and cleaned versions of the German benchmarks, as well as the model weights we release, will be made available under licenses compatible with their upstream sources."

[Gating] API "gated": false for both repos. No access form.

[Upstream terms that touch the weights] Pretraining data: FineWeb-2 German, ODC-By 1.0 plus Common Crawl Terms of Use (see docs__fineweb2-and-dense-core-dataset__2026-11-19.md). Data selection used Llama-3.3-70B-Instruct labels (see terms__llama-3-3-community-licence__2026-11-19.md). The Apache-2.0 declaration does not mention either.
