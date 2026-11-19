# OpenAI open-weight siblings on Hugging Face - re-read 2026-11-19

- **doc_type:** model_card
- **source_url:** https://huggingface.co/openai/gpt-oss-safeguard-20b ; https://huggingface.co/openai/gpt-oss-safeguard-120b ; https://huggingface.co/openai/privacy-filter ; https://huggingface.co/openai/circuit-sparsity
- **retrieval_date:** 2026-11-19
- **exists:** yes
- **retrieved:** true

## gpt-oss-safeguard (20b and 120b)

- Created 2025-09-18. HF API: gated False, licence tag apache-2.0, `base_model_relation: finetune` of
  `openai/gpt-oss-20b` and `openai/gpt-oss-120b`. 20b last modified 2026-01-14, 120b 2025-10-29.
- Raw LICENSE in both repos is the Apache License 2.0 (11,358 bytes, header "Apache License Version 2.0,
  January 2004"). Raw USAGE_POLICY:

> We aim for our tools to be used safely, responsibly, and democratically, while maximizing your control over how you use them. By using OpenAI gpt-oss-safeguard-120b and gpt-oss-safeguard-20b, you agree to comply with all applicable law.

- Card text: "safety reasoning models built-upon gpt-oss ... classify text content based on safety policies
  that you provide ... intended for safety use cases. For other applications, we recommend using gpt-oss
  models." 20b is 21B total / 3.6B active, 120b is 117B total / 5.1B active. Trained on, and only to be
  used with, the harmony format. The card links the gpt-oss model card (arXiv 2508.10925) and a separate
  repo `github.com/openai/gpt-oss-safeguard` (Apache-2.0; LICENSE, USAGE_POLICY, docs, example policies).

## Other openai org artifacts created after the base release

| repo | created | gated | licence tag | note |
| --- | --- | --- | --- | --- |
| openai/privacy-filter | 2026-04-17 | False | apache-2.0 | 1.5B total / 50M active token classifier for PII masking; no LICENSE file in the repo, licence stated in the card header and highlights only |
| openai/circuit-sparsity | 2025-12-11 | False | apache-2.0 | research weights for one sparse model from a paper; LICENSE.MD and NOTICE.MD ("Copyright 2025 OpenAI", Apache-2.0) in repo; needs trust_remote_code |

Nothing from `openai` on Hugging Face was created after 2026-04-17 (listing sorted by createdAt, read
2026-11-19).
