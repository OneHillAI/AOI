doc_type: license
entity: minicpm5
variant/applies-to: every checkpoint of the MiniCPM5-1B release, plus the MiniCPM5-2B sibling release, plus older MiniCPM generations (for contrast)
source_url: https://huggingface.co/api/models/openbmb/<repo> (cardData.license) and https://huggingface.co/openbmb/<repo>/raw/main/README.md
retrieval_date: 2026-11-19
exists: yes
retrieved: true

## Per-checkpoint licence (Hugging Face card metadata, read from the API on 2026-11-19)

openbmb/MiniCPM5-1B : license apache-2.0, gated false
openbmb/MiniCPM5-1B-SFT : license apache-2.0, gated false
openbmb/MiniCPM5-1B-Base : license apache-2.0, gated false
openbmb/MiniCPM5-1B-GGUF : license apache-2.0, gated false
openbmb/MiniCPM5-1B-MLX : license apache-2.0, gated false
openbmb/MiniCPM5-2B, -2B-SFT, -2B-Base, -2B-Midtrain, -2B-GGUF, -2B-MLX, -2B-GPTQ, -2B-DSpark, -2B-DSpark-GGUF : license apache-2.0, gated false (sibling release, see follow-ups)
openbmb/MiniCPM4-8B, MiniCPM4-0.5B, MiniCPM4.1-8B, MiniCPM3-4B : license apache-2.0
openbmb/MiniCPM-V-4.6, MiniCPM-V-4.7-1B, MiniCPM-V-4.7-35B-A3B, MiniCPM-o-4_5, MiniCPM-OCR-1.0, MiniCPM-SALA, BitCPM-CANN-*, UltraX-0.6B-Preview : license apache-2.0

## Older generations carry NO licence metadata on Hugging Face (read 2026-11-19)
openbmb/MiniCPM-2B-sft-bf16, MiniCPM-2B-dpo-bf16, MiniCPM-1B-sft-bf16, MiniCPM-2B-128k, MiniCPM-MoE-8x2B, MiniCPM-V, MiniCPM-V-2, MiniCPM-V-2_6, MiniCPM-Llama3-V-2_5, MiniCPM-Embedding, MiniCPM-Reranker : cardData.license is empty. (MiniCPM-S-1B-sft is apache-2.0.)
These older generations were governed by the custom General Model License; see license__older-generations-general-model-license__2026-11-19.md.

## Card text on the MiniCPM5-1B model card (verbatim)
YAML header: "license: apache-2.0"; "language: - en - zh".
Body: "## License / This repository and MiniCPM model weights are released under the [Apache-2.0](https://github.com/OpenBMB/MiniCPM/blob/main/LICENSE) License."
The MiniCPM5-1B-SFT, -Base, -MLX and -GGUF cards carry the same sentence (their cards are copies of the main card with the "you are here" marker moved).
