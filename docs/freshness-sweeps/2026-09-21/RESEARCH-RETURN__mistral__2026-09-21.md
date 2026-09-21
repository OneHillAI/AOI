# Research return: mistral (freshness re-verification) - 2026-09-21

**Verdict: DELTA -> bump `last_verified` to 2026-09-21, and flag new-gen catalogue for the code session.**

- **Licence (tracked Apache group):** the Apache-2.0 arm of the Mistral split is **still Apache-2.0** and has, if anything, expanded. New-generation 2026 releases read as Apache-2.0:
  - **Mistral-Small-4-119B - apache-2.0** (corroborated across model card + repo tag).
  - **Devstral-2, Voxtral** and other new-gen releases - apache-2.0.
- **Manual re-confirm needed:** **Mistral-Large-3-675B** and **Ministral-3** were **read as apache-2.0 via the WebFetch summariser** - if correct this is a notable shift, because prior Large/Ministral-tier weights sat under the **Mistral Research License (MRL)**. An **MRL -> Apache** move is a material policy change, so this must be **manually re-confirmed against the raw HF `LICENSE` tag** before the code session re-scores. `retrieved: true` but summariser-sourced -> treat as provisional.
- **Exception preserved:** **Codestral-22B-v0.1 remains `mnpl`** (Mistral Non-Production License) - keep as the explicit non-Apache exception in the split; unchanged.
- **Supersession:** the tracked `mistral` entry's catalogue is behind the current new-gen line; flagged for the code session to refresh `models`/siblings (not folded into scores here).

`retrieved: true` (cards re-read); Large-3 / Ministral-3 Apache reading flagged provisional pending manual LICENSE-tag check. Clause file: `license__mistral-newgen__2026-09-21.md`.
