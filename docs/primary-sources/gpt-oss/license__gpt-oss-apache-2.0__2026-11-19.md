# gpt-oss - LICENSE and USAGE_POLICY, re-read 2026-11-19

- **doc_type:** license
- **source_url:** https://raw.githubusercontent.com/openai/gpt-oss/main/LICENSE ; https://raw.githubusercontent.com/openai/gpt-oss/main/USAGE_POLICY ; https://huggingface.co/openai/gpt-oss-120b/raw/main/README.md
- **retrieval_date:** 2026-11-19
- **exists:** yes
- **retrieved:** true

## What was read

The raw LICENSE on GitHub (11,358 bytes) is the unmodified Apache License, Version 2.0, January 2004. The
appendix notice still carries the template placeholder "Copyright [yyyy] [name of copyright owner]". No
bespoke clause is present. The LICENSE shipped in the Hugging Face repos is the same file.

The raw USAGE_POLICY is a single paragraph, unchanged:

> We aim for our tools to be used safely, responsibly, and democratically, while maximizing your control over how you use them. By using OpenAI gpt-oss-120b and gpt-oss-20b, you agree to comply with all applicable law.

Correction: the publisher spells "maximizing" with a z. The quotation in entry.yaml evidence `ev-usage-policy`
had the British spelling "maximising"; it was corrected to the verbatim text on 2026-11-19. The meaning is
unchanged. The 2026-07-25 _sources.md extract already had the verbatim spelling.

## Hugging Face API, same day

| repo | gated | licence tag | created | last modified |
| --- | --- | --- | --- | --- |
| openai/gpt-oss-120b | False | apache-2.0 | 2025-08-04 | 2025-08-26 |
| openai/gpt-oss-20b | False | apache-2.0 | 2025-08-04 | 2025-08-26 |

Both repos contain LICENSE, USAGE_POLICY, safetensors shards and an `original/` folder. config.json
reports max_position_embeddings 131072 (128K), 128 experts (120b) and 32 experts (20b), 4 experts per
token, MXFP4 quantisation. The card README states 117B total / 5.1B active (120b) and 21B total / 3.6B
active (20b). The organisation page reports `isVerified: True` for `openai`.

## Newer OpenAI open-weight artifacts on the same org (not folded)

Listing `openai` models by creation date (2026-11-19) shows nothing created after 2026-04-17. No gpt-oss
successor exists. See `model_card__gpt-oss-safeguard__2026-11-19.md` for the siblings.
