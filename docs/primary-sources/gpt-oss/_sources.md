# gpt-oss - primary-source clauses (2026-07-25)

## _sources.md (index)
```
doc_type | source_url | retrieval_date | exists | retrieved | notes
license | https://github.com/openai/gpt-oss | 2026-07-25 | yes | true | plain Apache-2.0 boilerplate confirmed
model_card | https://huggingface.co/openai/gpt-oss-120b | 2026-07-25 | yes | true | HF card metadata "License: apache-2.0" - corroborates the GitHub LICENSE
technical_report | https://arxiv.org/abs/2508.10925 | 2026-07-25 | yes | true | model card doubling as report
terms | https://github.com/openai/gpt-oss/blob/main/USAGE_POLICY | 2026-07-25 | yes | true | single-paragraph policy (confirmed complete)
security | https://cdn.openai.com/pdf/419b6906-9da6-406c-a19d-1bb078ac7637/oai_gpt-oss_model_card.pdf | 2026-07-25 | yes | true | malicious-fine-tuning eval + SAG conclusion
security | https://metr.org/blog/2025-10-23-gpt-oss-methodology-review/ | 2026-07-25 | yes | true | METR third-party methodology review
```

## license Apache-2.0
source_url: github.com/openai/gpt-oss (raw LICENSE) | exists: yes | retrieved: true
[LICENSE] standard Apache License 2.0 (Jan 2004) boilerplate; copyright line left as template placeholder. No bespoke restrictions in the file; use restrictions live in USAGE_POLICY.

## technical_report (model card)
source_url: https://arxiv.org/abs/2508.10925 | exists: yes | retrieved: true
[Title] "gpt-oss-120b & gpt-oss-20b Model Card" [Abstract] "...two open-weight reasoning models...efficient mixture-of-expert transformer architecture...trained using large-scale distillation and reinforcement learning." Releases "all model weights, inference code, tools, and tokenizers under an Apache 2.0 license."

## terms - USAGE_POLICY (full text)
source_url: github.com/openai/gpt-oss/blob/main/USAGE_POLICY | exists: yes | retrieved: true
"We aim for our tools to be used safely, responsibly, and democratically, while maximizing your control over how you use them. By using OpenAI gpt-oss-120b and gpt-oss-20b, you agree to comply with all applicable law." (Confirmed complete, not truncated.)

## security - safety report + METR
source_url: cdn.openai.com/.../oai_gpt-oss_model_card.pdf ; metr.org/blog/2025-10-23-gpt-oss-methodology-review/ | exists: yes | retrieved: true
[Method] adversarial fine-tuning on bio/cyber data to simulate worst case; external reviewers METR, SecureBio, Daniel Kang. [Finding] default "does not reach...High capability in any of the three Tracked Categories"; SAG concluded even robust fine-tuning "did not reach High capability in Biological and Chemical Risk or Cyber risk." [METR] "OpenAI at least partially addressed each of our 6 high-urgency items"; flagged no published High-capability criteria.
