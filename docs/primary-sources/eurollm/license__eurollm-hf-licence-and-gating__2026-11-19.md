# EuroLLM licence and gating re-read, 2026-11-19

Sources: Hugging Face model API (`https://huggingface.co/api/models/utter-project/<repo>`), the
raw `README.md` of each ungated repo, and the rendered model page of the gated 9B-Instruct repo.
Retrieved 2026-11-19. None of the repos contains a standalone `LICENSE` file in its file listing
(checked against the `siblings` list of each repo). The licence statement is the card front
matter plus the card line "License: Apache License 2.0."

| repo | licence (card metadata) | card text | gated (API) | context (card / config) |
|---|---|---|---|---|
| utter-project/EuroLLM-9B | apache-2.0 | n/a (gated, raw 401) | auto | 4,096 (tracked) |
| utter-project/EuroLLM-9B-Instruct | apache-2.0 | "License: Apache License 2.0." (rendered page) | auto, profile sharing: username and email | 4,096 (card table) |
| utter-project/EuroLLM-1.7B | apache-2.0 | n/a | none | 4,096 |
| utter-project/EuroLLM-1.7B-Instruct | apache-2.0 | "**License:** Apache License 2.0." | none | 4,096 (card table) |

Gate text on the 9B-Instruct page, verbatim: "You need to agree to share your Hugging Face
information to access this model. This repository is publicly accessible, but you have to accept
the conditions to access its files and content." The gate is auto-approved (`gated: auto`); it
shares the account username and email with the publisher and adds no licence term. The 1.7B
repos carry no gate.

Result for the tracked 9B and 1.7B line: Apache-2.0 unchanged and uniform. Gating is not uniform
(9B repos auto-gated, 1.7B not gated). Card limitation text, 9B: "EuroLLM-9B has not been aligned to
human preferences, so the model may generate problematic outputs (e.g., hallucinations, harmful
content, or false statements)." 1.7B: same sentence for EuroLLM-1.7B-Instruct.

## Successor repos in the same org (not folded into the tracked entry)

| repo | created | licence (card metadata) | gated | context (config.json) |
|---|---|---|---|---|
| EuroLLM-9B-2512 | 2025-06-07 | apache-2.0 | none | 32,768 |
| EuroLLM-9B-Instruct-2512 | 2026-01-26 | apache-2.0 | none | 32,768 |
| EuroLLM-22B-2512 | 2025-11-24 | apache-2.0 | none | 32,768 |
| EuroLLM-22B-Instruct-2512 | 2025-12-05 | apache-2.0 | none | 32,768 |
| EuroMoE-2.6B-A0.6B-2512 / -Instruct-2512 | 2025-06-09 / 2025-12-15 | apache-2.0 | none | 32,768 (Mixtral arch) |
| EuroLLM1.5-9B-Base | 2026-07-06 (updated 2026-11-16) | apache-2.0 | none | 164,000 |
| EuroLLM1.5-9B-SFT | 2026-08-29 (updated 2026-11-03) | none declared (no licence in card metadata) | none | 40,960 |
