doc_type: technical_report
entity: kimi-k3
variant/applies-to: Kimi K3 technical report, "Kimi K3: Open Frontier Intelligence"
source_url: https://github.com/MoonshotAI/Kimi-K3/blob/main/k3_tech_report.pdf (read as raw.githubusercontent.com/MoonshotAI/Kimi-K3/main/k3_tech_report.pdf, 1,795,670 bytes, 47 pages)
retrieval_date: 2026-11-19
exists: yes
retrieved: true

The PDF was re-downloaded and its text streams extracted locally (no OCR). The load-bearing section is unchanged.

[Section 6.2.2, refusal point - VERBATIM] "Frontier models from Anthropic and OpenAI refuse cyber-related tasks, making a comparable evaluation infeasible; we therefore exclude them from this suite."
[Tier 1, VERBATIM] "the model identified hundreds of candidate vulnerabilities. Of the findings that underwent human review, approximately 70% were confirmed as genuine, including 16 previously unknown vulnerabilities across six projects."
[Tier 2, VERBATIM] "solving 14 of 36 tasks (38.9%) versus 8 of 36 (22.2%) for GLM-5.2."
[Summary, VERBATIM] "At Tier 2, it completes end-to-end exploits against user-space targets."
[Third-party reference inside the report - VERBATIM] "An independent joint assessment by the UK AI Security Institute and NIST's Center for AI Standards and Innovation (CAISI) [125] reaches conclusions consistent with ours." The report adds that K3 scored 32% against 24% for GLM-5.2 on ExploitBench and achieved arbitrary code execution on 0 of 41 tasks. That assessment was cited by the publisher and was not itself read.
[Safety training] A text search of the extracted report finds no safety-tuning, red-team, guard-model or harmlessness section. The word "refus" appears only in the benchmark-comparison footnotes (other vendors' refusals) and a WorldVQA note.
[Not stated] total training tokens and absolute pretraining FLOPs (only relative scaling-law FLOPs; Figure 7 reports a 2.5x scaling-efficiency gain over Kimi K2).
