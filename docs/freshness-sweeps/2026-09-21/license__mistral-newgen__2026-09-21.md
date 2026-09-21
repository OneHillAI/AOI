doc_type: license
entity: mistral
source_url: https://huggingface.co/mistralai (Mistral-Small-4, Mistral-Large-3, Ministral-3, Devstral-2, Voxtral cards) ; per-repo LICENSE tags
document_effective_date: 2026 new-generation releases
retrieval_date: 2026-09-21
exists: yes
retrieved: partial - see per-item flags
tag: publisher

## What moved
Mistral's 2026 new-generation catalogue has advanced past what the `mistral` entry tracks. Licence reads this pass:

- **Mistral-Small-4-119B - apache-2.0.** Corroborated across model card + repo licence tag. retrieved: true.
- **Devstral-2 - apache-2.0.** retrieved: true (card).
- **Voxtral - apache-2.0.** retrieved: true (card).
- **Mistral-Large-3-675B - read apache-2.0 (PROVISIONAL).** Sourced via the WebFetch summariser, not a raw LICENSE-file read. If correct, this is a policy shift, because prior Large-tier weights sat under the **Mistral Research License (MRL)**. retrieved: false for the raw licence tag -> MUST be manually re-confirmed against the HF repo `LICENSE` before the code session re-scores.
- **Ministral-3 - read apache-2.0 (PROVISIONAL).** Same caveat as Large-3: summariser-sourced; prior Ministral-tier sat under MRL. retrieved: false for the raw tag -> manual re-confirm required.

## Preserved exception (unchanged)
- **Codestral-22B-v0.1 - mnpl (Mistral Non-Production License).** Still the explicit non-Apache exception in the split. retrieved: true. Unchanged.

## Note for the code session
The Apache-2.0 arm of the split is intact and expanding. The open question is whether Large-3 / Ministral-3 have genuinely moved MRL -> Apache. Do NOT re-score `use_modify` on that basis until the raw LICENSE tags are eyeballed - an MRL to Apache reclassification is materially score-moving and must not rest on a summariser read.
