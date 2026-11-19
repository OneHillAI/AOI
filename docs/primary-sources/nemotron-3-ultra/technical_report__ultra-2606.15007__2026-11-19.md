doc_type: technical_report
entity: nemotron-3-ultra
variant/applies-to: Nemotron 3 Ultra dedicated technical report (a newer document than the Nemotron 3 White Paper 2512.20856 the entry cited)
source_url: https://arxiv.org/abs/2606.15007 ; https://arxiv.org/html/2606.15007
document_effective_date: arXiv v1, 2026-06-12
retrieval_date: 2026-11-19
exists: yes
retrieved: true
tag: publisher

## What it is
"Nemotron 3 Ultra: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning", 570+ authors. 550B
total / 55B active, pre-trained on 20 trillion text tokens (15T diverse, then 5T high quality) in NVFP4, context extended to
1M tokens, post-trained with SFT, RL and multi-teacher on-policy distillation (MOPD). Abstract: base, post-trained and quantized
checkpoints "along with training data and recipe" are released.

## Safety content (the full extent, from a keyword read of the HTML)
1. SFT safety data: the Nemotron 3 Super safety blend is retained, with prompts from diverse sources and responses generated
   "conditioned on a response policy mapped to each prompt", and translated into six languages (German, Spanish, French,
   Japanese, Italian, Chinese) with Riva Translate 4B v1.1.
2. An "Agentic Safety Teacher" trained against indirect prompt injection (malicious instructions embedded in tool responses),
   four attack categories (unauthorized actions, data modification, denial of service, data exfiltration), built with an
   automated red-teaming loop (Nemotron 3 Super as attacker, Nemotron 3 Nano as defender) and a deterministic verifier.
3. RL environments include a safety environment.
No safety benchmark table, no jailbreak or red-team result on Ultra, no residual-risk disclosure and no independent evaluation
appears in the report. This is training-side safety work, not a published model-level safety evaluation.

## Compute
No GPU-hour or total training FLOP figure was found (searched FLOP, GPU hours, GB200, H100, B200, compute). Training hardware is
named as GB200. The 1e25 systemic-risk question stays undeterminable from disclosed figures.
