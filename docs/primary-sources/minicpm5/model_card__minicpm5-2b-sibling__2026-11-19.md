doc_type: model_card
entity: minicpm5
variant/applies-to: openbmb/MiniCPM5-2B (SIBLING RELEASE, not scored in this entry; read only to apply the scope rule)
source_url: https://huggingface.co/openbmb/MiniCPM5-2B (raw README) ; https://huggingface.co/api/models/openbmb/MiniCPM5-2B
retrieval_date: 2026-11-19
exists: yes
retrieved: true (header and highlights; the SVG radar chart markup was skipped)

## Verbatim extracts
"license: apache-2.0", gated false, language en and zh.
"We are releasing MiniCPM5-2B, the second model in the MiniCPM5 series, following MiniCPM5-1B. It is a dense 2B Transformer that scales up the same training recipe".
Dataset list in the YAML header: Ultra-FineWeb, UltraX-Preview, Ultra-FineWeb-L3, UltraData-Math, UltraData-Code, UltraData-SFT-2605, UltraData-SFT-Agent-2609, UltraData-RL-2609. This differs from the 1B card (4 datasets), so the 2B has a different, larger disclosed data set, including a released RL dataset (UltraData-RL-2609) the 1B does not have.
GitHub README: 2B released 2026-09-07, with checkpoints -2B, -SFT, -Midtrain, -Base, -GGUF, -MLX, -GPTQ, -DSpark. HF repo created 2026-09-06.

## Scope reading
Same licence (Apache-2.0) as the 1B, but a different release date, a different disclosed data composition and a different post-training recipe (a critic-based RL algorithm from JustRL II). Under the scope rule an entry is one release with uniform provenance and openness, so the 2B is a separate entry (follow-up), not folded into this one.
