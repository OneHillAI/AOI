# Mistral - Hugging Face licence tags and raw model cards (re-read 2026-11-19)

- **doc_type:** model_card
- **source_url:** https://huggingface.co/api/models/mistralai/<repo> and https://huggingface.co/mistralai/<repo>/raw/main/README.md
- **retrieval_date:** 2026-11-19
- **exists:** yes
- **retrieved:** true (raw card front matter and the card's own "License" section; not a summariser read)

This closes the September 2026 sweep's open item: Mistral Large 3 and Ministral 3 were read as Apache-2.0 through a summariser. They are now read from the raw card.

## Raw card front matter and licence section (verbatim)

| Repo | `license:` in card front matter | HF `gated` (API) | Card body licence text |
|---|---|---|---|
| Mistral-Large-3-675B-Instruct-2512 (sha 383ffea2c7) | `apache-2.0` | false | "This model is licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0.txt)." and feature bullet "Apache 2.0 License: Open-source license allowing usage and modification for both commercial and non-commercial purposes." |
| Mistral-Large-3-675B-Base-2512 | `apache-2.0` | false | not separately quoted |
| Ministral-3-8B-Instruct-2512 (sha 5b26027e7b) | `apache-2.0` | false | same two sentences as above |
| Ministral-3-3B-Instruct-2512, Ministral-3-14B-Instruct-2512 | `apache-2.0` | false | front matter only checked |
| Mistral-Small-4-119B-2603 (sha a11f36bebf) | `apache-2.0` | false | front matter only checked |
| Codestral-22B-v0.1 (sha 28b1c1a51d) | `license: other`, `license_name: mnpl`, `license_link: https://mistral.ai/licences/MNPL-0.1.md` | false | unchanged |
| Mistral-Large-Instruct-2411 | `license: other`, `license_name: mrl`, `license_link: https://mistral.ai/licenses/MRL-0.1.md` | false | unchanged |
| Ministral-8B-Instruct-2410 | `license: other`, `license_name: mrl` | false | unchanged |
| Pixtral-Large-Instruct-2411 | `license: other`, `license_name: mrl` | false | unchanged |
| Mistral-Large-Instruct-2407 (sha a286006d55) | API `cardData`: `license: other`, `license_name: mrl` | `auto` (click-through gate; raw README returns HTTP 401) | not readable unauthenticated |
| Mistral-Small-Instruct-2409 (not tracked) | `license: other`, `license_name: mrl` | false | unchanged |

The Large 3 and Ministral 3 repos contain no separate LICENSE file (HTTP 404 on LICENSE, LICENSE.md and LICENSE.txt); the licence is declared in the card front matter and the card's "License" section. The Apache-2.0 reading therefore rests on card metadata plus card prose, not on a licence file. The MRL cards (2411, Ministral 8B, Pixtral Large, Small 2409) still carry an `extra_gated_prompt` in the card text while the API reports `gated: false`; the raw README of each was fetched without authentication.

## Findings

- Mistral Large 3 (675B total, 41B active per the card) and Ministral 3 (3B, 8B, 14B) are genuinely Apache-2.0. The MRL-to-Apache move is real for these new-generation releases.
- No existing MRL or MNPL repo changed licence. The tracked MRL models (Ministral-8B-Instruct-2410, Mistral-Large-Instruct-2407 and 2411, Pixtral-Large-Instruct-2411) and Codestral-22B-v0.1 carry the same tags as on 2026-09-21.
- The `mistralai` org has published no new MRL-licensed repo since Pixtral-Large-Instruct-2411 (2024-11-14).
- Codestral-22B-v0.1 is still MNPL on Hugging Face. Mistral's docs now list "Codestral" (v25.08) as a "Premier" API-only model, not an open-weight download.

## Licence tags on other recent repos (tags from the HF API, 2026-11-19; see the new-entity file for the texts read)

- Mistral-Large-4-1T-A52B and its NVFP4 build, Timestral-5M/28M/123M/209M, Mistral-Medium-3.5-128B (and its EAGLE draft): `license: other`, each repo has a LICENSE file (see `license__new-entities-large4-timestral__2026-11-19.md`).
- Devstral-2-123B-Instruct-2512: `license: other`, LICENSE file is the Modified MIT with a monthly-revenue cap. Devstral-Small-2-24B-Instruct-2512 is `apache-2.0`. The September sweep's "Devstral-2 - apache-2.0" holds only for the 24B Small build.
- Voxtral-4B-TTS-2603: `cc-by-nc-4.0`.
- Apache-2.0 tags: Mistral-Small-4-119B-2603 and its NVFP4 and EAGLE builds, Leanstral-2603, Leanstral-1.5-119B-A6B, Shieldstral-1.0-3B, Voxtral-Mini-4B-Realtime-2602, LIDstral-Arabic (card tag), Voxtral-Mini-4B-Realtime-Arabic (no HF tag; card says Apache 2.0).
