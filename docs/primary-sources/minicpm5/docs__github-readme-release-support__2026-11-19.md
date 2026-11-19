doc_type: docs
entity: minicpm5
variant/applies-to: OpenBMB/MiniCPM GitHub repository (code, cookbooks, release log, issue channels)
source_url: https://raw.githubusercontent.com/OpenBMB/MiniCPM/main/README.md ; https://api.github.com/repos/OpenBMB/MiniCPM ; .../contents/ ; .../contents/.github ; .../contents/docs/deployment/llama_cpp.md ; .../ollama.md
retrieval_date: 2026-11-19
exists: yes
retrieved: true

## Release log (verbatim)
"- [2026.05.19] MiniCPM5-1B is released: a compact 1B-class dense model for on-device and resource-constrained use, paired with deployment / fine-tuning Agent Skills."
"- 📌 [2026.09.07] MiniCPM5-2B is released: a compact 2B-class dense model for on-device and resource-constrained use ..."
Dates differ by source: GitHub README 2026-05-19; Ultra-FineWeb card news line 2026-05-25 ("MiniCPM5-1B is released!"); Artificial Analysis FAQ 2026-05-25; Hugging Face repos created 2026-05-21. The entry uses "May 2026".
Earlier cadence from the same log: MiniCPM-SALA 2026-02-11, MiniCPM4.1 2025-09-05, MiniCPM4 2025-06-06, MiniCPM3-4B 2024-09-05, MiniCPM-2B 2024-02-01.

## Publisher and institutions (verbatim)
"This project is developed by the following institutions: Modelbest Inc. (modelbest.cn); THUNLP (Tsinghua NLP); Gaoling School of Artificial Intelligence of RUC."
Repository: OpenBMB/MiniCPM, created 2024-01-29, last push 2026-11-09, not archived, Apache-2.0 per the API, 11,889 stars, 24 open issues, Discussions enabled. Hugging Face org: openbmb.

## Support channels
README: Discord and Feishu/Lark links. .github/ISSUE_TEMPLATE has bug_report.yaml, bad_case.yaml, feature_request.yaml and config.yaml. No SECURITY.md was found at SECURITY.md or .github/SECURITY.md (both HTTP 404) and no vulnerability-disclosure process is stated in the README. Legacy README gives cpm@modelbest.cn for commercial authorisation of the older generations.

## Hardware and runtime guidance (docs/deployment/llama_cpp.md, verbatim table rows)
"MiniCPM5-1B-F16.gguf | 2.1 GB | reference quality, uniform CPU/GPU performance"; "MiniCPM5-1B-Q8_0.gguf | 1.1 GB | very small quality drop vs F16, half the disk"; "MiniCPM5-1B-Q4_K_M.gguf | 657 MB | edge / mobile-class hardware, minimal VRAM". Example server flags in the cookbook: "-ngl 99 -c 8192 --jinja".
docs/deployment/ollama.md: "ollama run minicpm5-1b --temperature 0.9 --top-p 0.95" after "ollama create minicpm5-1b -f Modelfile" (a local Modelfile route; the ollama.com library page for minicpm5 returned 404 on 2026-11-19).
docs/deployment lists: arclight, litert, llama_cpp, lmstudio, mlx, ollama, sglang, transformers, vllm, vllm_ascend. The README table adds "LiteRT-LM | .litertlm on-device runtime: Android / iOS / desktop / IoT, CPU + GPU".
README fine-tuning table: TRL + PEFT, LLaMA-Factory, ms-swift, unsloth, xtuner.

## Code released in the repository (GitHub contents API, 2026-11-19)
finetune/ (finetune.py, lora_finetune.sh, sft_finetune.sh, mlx_finetune.py, sft_dpo_trainer, llama_factory_example, configs); quantize/ (awq_quantize.py, bnb_quantize.py, gptq_quantize.py, quantize_eval.py); tool_parsers/minicpm5xml_tool_parser.py; skills/ (minicpm5-deploy-* and minicpm5-finetune-* agent skills); docs/ (MiniCPM_4_Technical_Report.pdf, InfLLM-V2-paper.pdf, MiniCPM_SALA.pdf, BitCPM_CANN.pdf, deployment and finetune cookbooks). There is no MiniCPM5 technical report PDF and no pretraining, mid-training, RL or OPD training pipeline in the repository: the training-side code is fine-tuning for users, not the code that produced the release.
