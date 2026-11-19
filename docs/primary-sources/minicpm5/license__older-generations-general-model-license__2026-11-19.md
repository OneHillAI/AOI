doc_type: license
entity: minicpm5
variant/applies-to: OLDER MiniCPM generations (MiniCPM 1B/2B/MoE, V-2, V-2.6 era), NOT MiniCPM5. Read to answer "which licence applies per generation".
source_url: https://raw.githubusercontent.com/OpenBMB/MiniCPM/main/docs/README-legacy.md (section "开源协议 LICENSE")
retrieval_date: 2026-11-19
exists: yes
retrieved: true
note: The General Model License file itself (github.com/OpenBMB/General-Model-License) was NOT fetched; only the README text that points to it was read.

## Verbatim extract (legacy README, section "Model LICENSE")
"* This repository is released under the [Apache-2.0](https://github.com/OpenBMB/MiniCPM/blob/main/LICENSE) License. 
* The usage of MiniCPM model weights must strictly follow [the General Model License (GML)](https://github.com/OpenBMB/General-Model-License/blob/main/...).
* The models and weights of MiniCPM are completely free for academic research.
* If you intend to utilize the model for commercial purposes, please reach out to cpm@modelbest.cn to obtain the certificate of authorization."

Chinese original of the same section: "MiniCPM 模型权重的使用则需要遵循 通用模型许可协议-来源说明-宣传限制-商业授权 ... 如需将模型用于商业用途，请联系cpm@modelbest.cn来获取书面授权，在登记后亦允许免费商业使用。"

## Reading
Earlier MiniCPM weights needed GML terms (source attribution, promotion limits, commercial authorisation by registration). The current README (README.md, "Current release: MiniCPM5-2B / MiniCPM5-1B") replaced this with a single Apache-2.0 statement covering "This repository and MiniCPM models". The MiniCPM5 checkpoints are therefore Apache-2.0 and the GML applies only to older generations.
