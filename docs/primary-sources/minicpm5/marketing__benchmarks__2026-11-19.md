doc_type: marketing
entity: minicpm5
variant/applies-to: MiniCPM5-1B (Thinking mode) publisher benchmark table
source_url: https://raw.githubusercontent.com/OpenBMB/MiniCPM/main/assets/minicpm5/public_leaderboard_en.png (image embedded on the HF model card under "Evaluation Results")
retrieval_date: 2026-11-19
exists: yes
retrieved: true (image viewed, numbers transcribed by hand)
status: PUBLISHER CLAIM. No third party reproduced these numbers. The table is an image, so it is not machine-searchable and no evaluation harness, prompt or sampling setup is given beside it.

## Table "Evaluation Results of MiniCPM5-1B" (all columns in Thinking mode)
Columns: MiniCPM5-1B | Qwen3-0.6B | Qwen3.5-0.8B | LFM2.5-1.2B
Average Score: 42.57 | 26.77 | 25.14 | 35.61
MMLU-Pro: 48.85 | 35.63 | 42.74 | 47.98
MMLU-Redux: 70.06 | 55.47 | 61.50 | 66.08
GPQA-Diamond: 26.26 | 25.42 | 30.98 | 34.85
SuperGPQA: 23.14 | 20.79 | 22.92 | 22.83
LCB-Pro 25Q2 (Easy): 22.68 | 4.12 | 0.00 | 6.19
OJBench: 7.33 | 0.86 | 0.43 | 1.94
LCB-v6 (@Avg3): 33.52 | 16.00 | 5.33 | 21.33
IFBench: 46.67 | 25.67 | 29.33 | 41.67
IFEval: 80.41 | 59.89 | 59.89 | 84.84
Multi-IF: 43.54 | 36.56 | 32.31 | 55.61
MultiChallenge: 19.48 | 18.97 | 23.97 | 23.28
AIME-2025 (@Avg16): 40.42 | 16.25 | 1.04 | 31.88
AIME-2026 (@Avg16): 40.42 | 12.29 | 0.21 | 31.67
HMMT Feb 2026 (@Avg16): 25.76 | 9.85 | 0.57 | 21.21
MATH-500: 91.60 | 72.60 | 30.40 | 89.00
BBH: 71.89 | 47.86 | 54.58 | 57.32
BBEH: 12.14 | 3.78 | 8.53 | 8.64
BFCLv4: 25.15 | 25.43 | 25.53 | 10.60
tau2-Bench Telecom-AA: 79.53 | 21.10 | 47.70 | 19.60

## Observations for the entry
- Only three comparison models, all thinking-mode, all smaller or equal in size. No Gemma, Llama, SmolLM, Phi, Granite or Qwen3-1.7B baseline.
- The card says the advantage is "most visible in tool use". On BFCLv4 the model (25.15) is below both Qwen baselines (25.43, 25.53); the tool-use lead rests on tau2-Bench Telecom-AA (79.53).
- It is behind LFM2.5-1.2B on GPQA-Diamond, IFEval, Multi-IF and MultiChallenge, and behind Qwen3.5-0.8B on GPQA-Diamond and MultiChallenge. "1B-class SOTA" is therefore true on the average (42.57 vs 35.61) but not on every row.
- Non-thinking mode numbers are not published on the card.
- AIME-2025 and AIME-2026 are both 40.42 (identical to two decimals), as transcribed from the image.
