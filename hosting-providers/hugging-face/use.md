# Use - Hugging Face Hub

_What is available and in what formats? Catalogue scope, supported formats and downstream integration live here._

<!-- item: catalog-scope -->
## Catalogue scope & publishers

Hugging Face is the **de facto default public registry** for open-weight models. Named labs
- Meta, Google, Mistral and many others - publish under **verified orgs**, alongside a vast
**open-upload community**. That breadth is also why it is the ecosystem's centre of gravity:
security researchers repeatedly target it precisely because nearly everyone pulls from it, so
its scope is confirmed both by its verified publishers and by the attention it draws.

<!-- item: formats-supported -->
## Formats supported

The Hub hosts **safetensors** (the promoted, data-only default), legacy **pickle**
checkpoints (still allowed but flagged-not-blocked), and repos that ship **executable code
paths** consumed via `trust_remote_code` or config. For a safe pull, prefer safetensors and
avoid untrusted pickle files or repo-shipped Python from unverified authors.

<!-- item: integration -->
## Downstream integration

First-class client tooling - **`huggingface_hub` and `transformers` `from_pretrained()`** -
makes the Hub the default source most downstream stacks pull from, by convention rather than
contractual lock-in. Because artifacts are plain git + LFS, they remain portable to any
mirror or local store; the per-stack integration specifics were not individually catalogued
here.
