# qwen - primary-source clauses (2026-07-25, re-verified 2026-11-19)

## _sources.md (index)
```
doc_type | source_url | retrieval_date | exists | retrieved | notes
license | https://huggingface.co/Qwen/Qwen3-235B-A22B (+3 checkpoints) | 2026-07-25 | yes | true | mainstream Qwen3 = apache-2.0 (0.6B..480B checked)
license | https://huggingface.co/Qwen/Qwen2.5-72B-Instruct ; Qwen-72B | 2026-07-25 | yes | true | Tongyi Qianwen community license; MAU>100M clause; "Built with Qwen"
technical_report | https://arxiv.org/abs/2505.09388 | 2026-07-25 | yes | true | Qwen3 Technical Report
privacy_policy | https://www.alibabacloud.com/help/en/legal/latest/alibaba-cloud-international-website-privacy-policy | 2026-07-25 | yes | true | GENERAL Alibaba Cloud policy; retention, SCC transfers, Singapore storage; SILENT on AI training
docs | https://www.alibabacloud.com/help/en/model-studio/faq-about-alibaba-cloud-model-studio | 2026-07-25 | yes | true | Model Studio FAQ: "never uses your data for model training"; stores call data per law (no period stated); AES-256 in transit
terms | https://www.alibabacloud.com/help/en/model-studio/ | 2026-07-25 | unknown | false | SUPERSEDED 2026-11-19: the binding Product Terms (Sec 4.48) were located and read, see the 2026-11-19 terms row; the formal retention period, region and opt-out remain unstated there
license | https://huggingface.co/Qwen/Qwen3-235B-A22B/raw/main/LICENSE (+0.6B, 32B, Coder-480B) | 2026-11-19 | yes | true | raw LICENSE read: unmodified Apache-2.0, identical md5 across checkpoints; no MAU clause; file license__qwen3-apache-2.0__2026-11-19.md
license | https://huggingface.co/Qwen/Qwen2.5-72B-Instruct/raw/main/LICENSE | 2026-11-19 | yes | true | Tongyi Qianwen community licence re-read: Sec 4 MAU>100M, Sec 5.b Built with Qwen, Sec 5.a export controls; unchanged; file license__qwen2.5-72b-tongyi__2026-11-19.md
model_card | https://huggingface.co/Qwen/Qwen3-235B-A22B ; Qwen3-Coder-480B-A35B-Instruct ; HF API ; https://www.modelscope.cn/api/v1/models/Qwen/Qwen3-32B ; https://ollama.com/library/qwen3 | 2026-11-19 | yes | true | sizes 0.6B-32B dense (no 0.5B), 235B-A22B, Coder-480B-A35B; context 32,768 native / 131,072 YaRN (235B), 262,144 native (Coder); ModelScope record via API (org web page is a JS shell); file model_card__qwen3-sizes-context-modelscope__2026-11-19.md
terms | https://www.alibabacloud.com/help/en/legal/latest/alibaba-cloud-international-website-product-terms-of-service | 2026-11-19 | yes | true | Product Terms Sec 4.48 Model Studio (Last Updated Oct 19, 2026): binding no-training-without-consent; NO retention period, region or opt-out stated; file terms__alibaba-cloud-product-terms-model-studio-4.48__2026-11-19.md
docs | https://www.alibabacloud.com/help/en/model-studio/faq-about-alibaba-cloud-model-studio | 2026-11-19 | yes | true | FAQ re-read: no-training sentence unchanged; "will store data" sentence no longer present; now points to Product Terms; file docs__ModelStudio-FAQ__2026-11-19.md
privacy_policy | https://www.alibabacloud.com/help/en/legal/latest/alibaba-cloud-international-website-privacy-policy | 2026-11-19 | yes | true | Last Updated Sep 04, 2026; retention, SCC (Art 46), DPF, Singapore storage (Philippines addendum) unchanged; silent on AI training; file privacy_policy__alibaba-cloud-international__2026-11-19.md
technical_report | https://arxiv.org/abs/2505.09388 | 2026-11-19 | yes | true | abstract page re-read: submitted 14 May 2025, 29 to 119 languages and dialects, all Qwen3 models under Apache 2.0 (full PDF not re-read)
```

## license Qwen3 (mainstream) - apache-2.0
source_url: huggingface.co/Qwen/Qwen3-235B-A22B (+Qwen3-32B, Qwen3-0.6B, Qwen3-Coder-480B-A35B-Instruct) | exists: yes | retrieved: true
[Metadata] all four checkpoints (0.6B..480B) display "License: apache-2.0". No MAU threshold on these.

## license Tongyi Qianwen (Qwen-72B, Qwen2.5-72B-Instruct) - NOT Apache-2.0
source_url: huggingface.co/Qwen/Qwen2.5-72B-Instruct (+/raw/main/LICENSE) | exists: yes | retrieved: true
[Sec 4 MAU - VERBATIM] "If you are commercially using the Materials, and your product or service has more than 100 million monthly active users, you shall request a license from us."
[Sec 5.b] display "Built with Qwen"/"Improved using Qwen". [Sec 5.a] export controls (China/US/other).
NOTE: per-checkpoint - mainstream Qwen3 is Apache-2.0; do not generalise.

## technical_report Qwen3
source_url: https://arxiv.org/abs/2505.09388 | exists: yes | retrieved: true
[Title] "Qwen3 Technical Report" - thinking/non-thinking modes, thinking budget, 119 languages (tail paraphrased by fetch; re-verify verbatim).

## privacy_policy (general Alibaba Cloud)
source_url: alibabacloud.com/help/en/legal/latest/alibaba-cloud-international-website-privacy-policy | exists: yes | retrieved: true
[Sec F Retention] "ongoing legitimate business need." [Sec D Transfer] SCCs (GDPR Art.46); EU-US/UK/Swiss DPF. [PH Addendum] "Your personal data will be stored in Singapore." [AI training] NOT addressed - MARK FOR CODE SESSION.

## docs (Model Studio FAQ) - hosted no-training commitment
source_url: alibabacloud.com/help/en/model-studio/faq-about-alibaba-cloud-model-studio | exists: yes | retrieved: true
[Data privacy - VERBATIM] "Alibaba Cloud strictly protects data privacy and never uses your data for model training." [Storage] Model Studio "will store data generated from model and application calls" (no retention period stated). [Security] data "encrypted with AES-256" in transit.
NOTE: grounds the hosted-Qwen **no-training** posture (doc_type: docs). The FAQ points to the formal Model Studio Service Agreement for the binding retention/region/opt-out specifics - see the terms row.

## terms (Model Studio Service Agreement) - specifics still unread
exists: unknown | retrieved: false
The FAQ (docs row above) grounds the no-training commitment, but the formal **Model Studio Service Agreement** - exact retention period, storage region, and opt-out mechanics - was not directly reachable this round. Keep retrieved:false for those binding specifics only. RE-DO with a headless browser when reachable.
