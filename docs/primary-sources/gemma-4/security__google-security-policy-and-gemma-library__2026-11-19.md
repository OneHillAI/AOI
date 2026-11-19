# Google security reporting policy (organisation default) and the google-deepmind/gemma library README and licence

source_url: https://github.com/google/.github/blob/master/SECURITY.md ; https://github.com/google-deepmind/gemma
retrieval_date: 2026-11-19
doc_type: security
retrieved: true


Two documents about the surrounding code and about reporting.

## google-deepmind/gemma (JAX library "to use and fine-tune Gemma")

README (https://raw.githubusercontent.com/google-deepmind/gemma/main/README.md) opens: "Gemma is a family of open-weights Large Language Model (LLM) by Google DeepMind" and "This repository contains the implementation of the `gemma` PyPI package. A JAX library to use and fine-tune Gemma." Its example loads `gm.nn.Gemma4_E4B()` with `gm.ckpts.CheckpointPath.GEMMA4_E4B_IT`. Its LICENSE file (https://raw.githubusercontent.com/google-deepmind/gemma/main/LICENSE, 11,358 bytes) is the Apache License 2.0; its sections 1 to 9 match the Gemma 4 licence page exactly (see license__gemma-4-apache-2.0). The repository is the inference and fine-tuning library; the pre-training pipeline is not in it. Issues are reported on the repository's GitHub issue tracker (README).

## Google organisation security policy (not Gemma-specific)

https://github.com/google/.github/blob/master/SECURITY.md reads: "Please use https://g.co/vulnz to report security vulnerabilities. We use https://g.co/vulnz for our intake and triage. For valid issues we will do coordination and disclosure here on GitHub (including using a GitHub Security Advisory when necessary). The Google Security Team will process your report within a day, and respond within a week (although it will depend on the severity of your report)."

This is the default policy for Google GitHub repositories. No SECURITY.md was found in google-deepmind/gemma or google-gemma (HTTP 404 on raw URLs) and no Gemma 4 model card, Hugging Face repository or gemma.ai page read names a security contact for the weights. Whether g.co/vulnz accepts reports about model weights was not checked.
