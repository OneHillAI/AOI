doc_type: safety
entity: nemotron-3
variant/applies-to: Nemotron 3 Super and Nano safety subcards (safety.md), and the Nemotron 3.5 Content Safety guard model
source_url: https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16/blob/main/safety.md ; https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16/blob/main/safety.md ; https://huggingface.co/nvidia/Nemotron-3.5-Content-Safety
document_effective_date: repo commits 2026-08-24 and 2026-08-25; Content Safety 3.5 repo created 2026-05-22, card release date 06/02/2026
retrieval_date: 2026-11-19
exists: yes
retrieved: true
tag: publisher

## Super and Nano safety.md (VERBATIM table cells)
"We used a guard model for content safety to exclude potentially harmful data from training."
"We used a Gemma-3 4B-based guard model trained on Nemotron Content Safety Dataset v2 for content safety to exclude
potentially illegal or harmful content from the training."
"True. We use Nemotron Content Safety Dataset V2 and an internal safety dataset specialized for minority sexuality for
content safety evaluation to ensure the safety of this model."

## Reading
Both subcards state that content-safety evaluation is done on two datasets, but publish no scores, no jailbreak or
red-team result and no residual-risk disclosure for the Super or Nano base models. No published model-level safety
evaluation exists for these two models as of 2026-11-19. The score is unchanged (safety 3).

## Nemotron 3.5 Content Safety (the guard the September sweep cited)
A 4B guard model (text and optional image input, context up to 128K, 12 languages named on the card: English, Arabic,
German, Spanish, French, Hindi, Japanese, Thai, Dutch, Italian, Korean, Chinese). HF licence_name openmdw-license-agreement.
Repo created 2026-05-22, card Release Date 06/02/2026, so it predates the September sweep by months and is a companion
classifier, not a safety evaluation of Super or Nano. The card publishes guard benchmark scores (for example harmful F1
0.97 on Aya Redteaming), NVIDIA self-reported.
