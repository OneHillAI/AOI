# Research return: qwen (freshness re-verification) - 2026-09-21

**Verdict: DELTA (supersession) -> bump `last_verified` to 2026-09-21, and flag the newer generations.**

- **Licence:** unchanged for the tracked line - the in-scope **Qwen3** weights remain **Apache-2.0** and have **not** been reverted or re-licensed. No revision this pass.
- **Supersession - FLAG:** Qwen3 has been superseded by **Qwen3.5 / 3.6 / 3.8**, all read as **Apache-2.0**. The tracked Qwen3 entry is not wrong (still live, still Apache), but it no longer represents the current head of the line - flagged for the code session to decide whether to add newer siblings or update `models`.
- **Safety / availability:** repos live, ungated; no adverse finding.

`retrieved: true` - Qwen3 + Qwen3.5/3.6/3.8 cards/LICENSE re-read; all apache-2.0, tracked Qwen3 not reverted. No new clause file (supersession flagged).
