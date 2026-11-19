# license LICENSE-MODEL, DeepSeek-V3 (original), re-read 2026-11-19

source_url: https://huggingface.co/deepseek-ai/DeepSeek-V3/raw/main/LICENSE-MODEL (byte-identical to https://raw.githubusercontent.com/deepseek-ai/DeepSeek-V3/main/LICENSE-MODEL) | exists: yes | retrieved: true

Also read: .../raw/main/LICENSE-CODE (MIT, "Copyright (c) 2023 DeepSeek"), and the model card section 7 ("This code repository is licensed under the MIT License. The use of DeepSeek-V3 Base/Chat models is subject to the Model License. DeepSeek-V3 series (including Base and Chat) supports commercial use."). There is no plain LICENSE file in the repo (HTTP 404 on /raw/main/LICENSE for both DeepSeek-V3 and DeepSeek-V3-Base). The HF card metadata carries no licence tag.

Result: the MIT-code / DeepSeek-License-weights split is still real. Text is DeepSeek License Agreement, Version 1.0, 23 October 2023, unchanged in structure.

Clauses not previously extracted in this folder:

- Section 7, Updates and Runtime Restrictions: "To the maximum extent permitted by law, DeepSeek reserves the right to restrict (remotely or otherwise) usage of the Model in violation of this License." Scope is use in violation of the licence, not a general revocation; the grant in Section 2 stays "perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable".
- Section 4.a: the Attachment A use restrictions "MUST be included as an enforceable provision by You in any type of legal agreement" governing use or distribution of the Model or Derivatives of the Model.
- "Derivatives of the Model" is defined to include "distillation methods entailing the use of intermediate data representations or methods based on the generation of synthetic data by the Model", so distilled or synthetic-data-trained models inherit the Attachment A restrictions.
- Section 14, Governing Law and Jurisdiction: "This agreement will be governed and construed under PRC laws without regard to choice of law principles... The courts located in the domicile of Hangzhou DeepSeek Artificial Intelligence Fundamental Technology Research Co., Ltd. shall have exclusive jurisdiction of any dispute arising out of this agreement."
- Attachment A also lists, beyond the items already recorded: "To generate or disseminate inappropriate content subject to applicable regulatory requirements", and a ban on exploiting vulnerabilities of a specific group of persons by age, social, physical or mental characteristics.
