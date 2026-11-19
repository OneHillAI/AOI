doc_type: license
entity: morena
variant/applies-to: all MORENA repos read (1.5B base, 1.5B instruct, 1.5B instruct GGUF, 0.5B mini, 0.5B mini instruct, 0.2B nano front matter or card)
source_url: https://huggingface.co/vamboai/morena-1.5b-instruct (README.md front matter and "Licence" section; repo tree via https://huggingface.co/api/models/vamboai/morena-1.5b-instruct/tree/main)
retrieval_date: 2026-11-19
exists: yes (as a declaration); no separate LICENSE file exists
retrieved: true (declaration and card clause read; Apache-2.0 text read separately below)

## What was read

[Declaration - VERBATIM] Front matter: "license: apache-2.0". Card section "Licence": "Apache 2.0. Commercial use is permitted, including fine-tuning and redistributing derivatives, under the terms of the licence."

[No licence file] The repo tree for vamboai/morena-1.5b-instruct lists exactly: .gitattributes, README.md, SHA256SUMS, config.json, load_example.py, model.safetensors, modeling_morena.py, poster.png, tokenizer.json, tokenizer_config.json. There is no LICENSE, NOTICE or COPYING file. GET /raw/main/LICENSE returned HTTP 404 for both the instruct and the base repo. The card names no copyright holder for the weights. Source files carry no licence header (grep for licen/copyright/apache/SPDX in modeling_morena.py returned nothing).

[Licence history in the repo] Commit titles on the instruct repo (HF API /commits/main): 2026-09-17T06:49:10Z "Release card: licence wording removed"; 2026-09-18T06:53:50Z "Licence: Apache 2.0, commercial use permitted"; 2026-09-18T06:57:45Z "Remove pre-release wording now that the repo is public". The licence was therefore declared on release day, after a window in which the card carried no licence wording. The metadata at 2026-11-19 is Apache-2.0.

[Gating] The HF API reports "gated": false for the instruct, base and mini-instruct repos.

[Companion datasets] vamboai/fikira (a published SFT component) is MIT, copyright "Vambo Technologies (trading as Vambo AI)". vamboai/morena-sft-corpus is listed in the card metadata but is not publicly readable (HTTP 401 on the web page and API).

## Apache-2.0 text (the licence the declaration points to)

source_url: https://www.apache.org/licenses/LICENSE-2.0.txt (retrieved 2026-11-19, 11,358 bytes)
"2. Grant of Copyright License. Subject to the terms and conditions of this License, each Contributor hereby grants to You a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable copyright license to reproduce, prepare Derivative Works of, publicly display, publicly perform, sublicense, and distribute the Work and such Derivative Works in Source or Object form."
"3. Grant of Patent License." (present; patent licence from each Contributor).
"4. Redistribution. You may reproduce and distribute copies of the Work or Derivative Works thereof in any medium ... provided that You give any other recipients of the Work or Derivative Works a copy of this License".
