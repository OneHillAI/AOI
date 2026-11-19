# Soofi GitHub repos and public artifacts, re-read 2026-11-19

Sources: https://github.com/soofi-project/Soofi-Pretraining (raw README.md, LICENSE and
LICENSE.md probes, GitHub API), `https://api.github.com/orgs/soofi-project/repos`, Hugging Face
dataset `Soofi-Project/SOOFI-S-Base-eval-scores`. exists: yes, retrieved: true.

Soofi-Pretraining README, verbatim: "The current code release contains the complete codebase
used for training Soofi S a 30B model based on Nvidia's Nemotron 3 Nano architecture." It lists
preprocessing (`src/preprocessing`: corpus construction, filtering, tokenization, mixture
assembly), pretraining and three annealing and long-context midtraining stages. Final line:
"Open model weights coming soon." The repo was last pushed 2026-07-15 and the README is
unchanged from the July read. `LICENSE` and `LICENSE.md` return HTTP 404 and the GitHub API
reports no licence: the training code is published but carries no licence grant.

Other org repos (GitHub API): `soofi-trainer` (MIT, pushed 2026-06-01), `soofi-model-hosting`
(MIT, 2026-07-02), `edc-mcp` (MIT), `aas-hybrid-mcp` (MIT, pushed 2026-11-12). These are
tooling, not the model.

Hugging Face dataset `SOOFI-S-Base-eval-scores` (created 2026-07-14, not gated): card front
matter `license: cc-by-4.0`; pre-training evaluation scores for Soofi-S and Soofi-S-long-context.
This is the only openly licensed Soofi artifact found.

Hugging Face Space `Soofi-Project/Pretraining-Tech-Report` is a project page for the report.

Correction to the earlier entry: it said the training and evaluation code was "not yet
released". The training code is released (without a licence file). The Base card's reference
list names evaluation code at github.com/ellamind/base-eval (Apache-2.0 per the GitHub API,
pushed 2026-11-11) and github.com/ellamind/eval-hive (no licence reported, pushed 2026-11-18),
both outside the Soofi org.
