doc_type: model_card
entity: kimi-k2
variant/applies-to: Kimi-K2-Instruct and Kimi-K2-Base
source_url: https://huggingface.co/moonshotai/Kimi-K2-Instruct
retrieval_date: 2026-11-19
exists: yes
retrieved: true

## What the re-read found

[Licence statement - VERBATIM] "Both the code repository and the model weights are released under the [Modified MIT License](LICENSE)." Unchanged.
[Front matter] license: other; license_name: "modified-mit"; new_version: moonshotai/Kimi-K2-Instruct-0905. The new_version pointer was added on 2025-09-05 (commit 2a193634), so it predates the 2026-07-25 read but was not recorded in the entry. The tracked checkpoints (Kimi-K2-Base, Kimi-K2-Instruct) are therefore marked by their publisher as superseded by Kimi-K2-Instruct-0905.
[API metadata] Kimi-K2-Instruct: created 2025-07-11, last modified 2026-04-23, gated false, fp8 safetensors, 1.026T parameters. Kimi-K2-Base: created 2025-07-03, last modified 2026-01-30, gated false.
[Serving note on the card] "You can access Kimi K2's API on https://platform.moonshot.ai". That hosted line is now retired for new users, see docs__hosted-model-list__2026-11-19.md.

## Newer Moonshot repos on the verified org (Hugging Face API, createdAt)

Kimi-K3.1-Pro 2026-11-02; Kimi-K3 2026-06-13 (first public commit 2026-07-27); Kimi-K2.7-Code 2026-06-11; Kimi-K2.6 2026-04-14; Kimi-K2.5 2026-01-01; Kimi-K2-Thinking 2025-11-04; Kimi-Linear-48B-A3B-Base/Instruct 2025-10-30; Kimi-K2-Instruct-0905 2025-09-03. Kimi-K2.5, K2.6 and K2.7-Code are 1T total / 32B active MoE, 256K context, native multimodal (image-text-to-text), MoonViT vision encoder, native int4 quantisation per their cards, each "released under the Modified MIT License". Not folded into this entry.
