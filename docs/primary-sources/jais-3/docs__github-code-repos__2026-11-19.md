# docs / GitHub code repositories named by the Jais 3 report (ifm-ai)

source_url: https://github.com/ifm-ai/xllm ; https://github.com/ifm-ai/RL360 ; https://github.com/ifm-ai/gen-eval-arabic ; https://github.com/ifm-ai/JaisVoice (README and LICENSE from raw.githubusercontent.com, main branch; repository pages from github.com)
retrieval_date: 2026-11-19
doc_type: docs
exists: yes
retrieved: true
tag: publisher

NOTE (OneHill): the GitHub REST API was rate-limited (HTTP 403) during retrieval, so file trees come from the repository HTML pages and README text. The Jais-3 Hugging Face cards say "Code repository | Coming soon", while the technical report Table 41 names these repositories, and all four are public with an Apache-2.0 LICENSE. The xllm and RL360 READMEs describe the K2 Horizon training and RL stack; neither README mentions Jais 3, and no Jais-3 run configuration file was identified in the pages read. Whether the Jais-3 continual-pretraining, SFT and RLVR recipes can be reproduced from these repositories is unconfirmed.

## ifm-ai/xllm README (verbatim extracts)
```
xLLM: Efficient LLM training for extra-long contexts.
xLLM is a PyTorch-based framework for long-context language modeling, with
distributed training, online data preparation, evaluation, and model export
in one repository.
Model architectures | Transformer architectures, with dense, MoE, and MoVA components.
Distributed training | FSDP1/FSDP2, data parallelism, model parallelism, and context parallelism.
Online data pipeline | Parallel tokenization, asynchronous preparation, buffered shuffle, and bestfit packing.
Training to deployment | Checkpoint/resume, perplexity and task evaluation, Hugging Face export, and vLLM integration (via xBridges).
Quick Start: "Start a short, single-GPU training run with the K2 Horizon 0.9B configuration."
```
Top-level files: .gitignore, Dockerfile, LICENSE, README.md, docs, eval.py, examples, requirements.txt, setup.py, tests, train.py, xllm.

## ifm-ai/RL360 README (verbatim extracts)
```
Reinforcement Learning codebase used in the post-training pipeline for the [K2 Horizon](https://ifm.ai/blog/k2/) series.

It trains language models on tasks that involve writing code, using tools, and working in a sandbox. The example below uses our [K2 Horizon 7B](https://huggingface.co/IFM/K2-Horizon-7B) model. To see how to switch models, see the [Qwen example](#using-qwen3-8b).
```
Top-level files: .dockerignore, .gitignore, LICENSE, README.md, THIRD_PARTY_NOTICES, assets, components, docker, pyproject.toml, recipes, requirements.txt, src.

## ifm-ai/gen-eval-arabic README (verbatim extracts)
```
  $ python --version
  # should be >= 3.12 and < 3.15
  $ python -m venv jais3_venv
  $ source ./jais3_venv/bin/activate
  ```

2. Install the Python requirements (without dependencies)
```
Top-level files include eval.py, configs.py, hyperparams.yaml, judge_vllm.py, merge_results.py and the lm-evaluation-harness and mt-evaluation-harness submodules. Related repositories named in the report footnotes: github.com/ifm-ai/jais3-lm-evaluation-harness and github.com/ifm-ai/mt-evaluation-harness (not opened).

## ifm-ai/JaisVoice README (verbatim extracts)
```
<h1 align="center">Jais Voice</h1>

<p align="center">
  A private voice assistant for macOS that runs entirely on your Mac.<br>
  Hold a shortcut, speak in Arabic, French or English, and let it answer, browse or act for you.
</p>

- **2026-10-15**: 🎉 [Jais 3 is out](https://ifm.ai/blog/jais3/), six open Arabic-centric models from 0.9B to 375B parameters. The announcement includes [a demo video of Jais Voice](https://ifm.ai/blog/jais3/#capabilities) too !

```

## Security policy
SECURITY.md and .github/SECURITY.md returned HTTP 404 on xllm, RL360 and gen-eval-arabic. https://raw.githubusercontent.com/ifm-ai/.github/main/SECURITY.md returned 404. No security-reporting policy was found.
