# Use - Hugging Face Hub

_Available models, supported formats and downstream integration._

<!-- item: catalog-scope -->
## Catalogue scope & publishers

Hugging Face is the de facto default public registry for open-weight models. Named labs (Meta,
Google, Mistral and many others) publish under verified orgs, alongside a vast open-upload
community. Security researchers repeatedly target it because nearly everyone pulls from it,
which confirms its position as the ecosystem's centre of gravity.

<!-- item: formats-supported -->
## Formats supported

The Hub hosts safetensors (the promoted, data-only default), legacy pickle checkpoints (still
allowed but flagged-not-blocked), and repos that ship executable code paths consumed via
`trust_remote_code` or config. Prefer safetensors, and avoid untrusted pickle files or
repo-shipped Python from unverified authors.

<!-- item: integration -->
## Downstream integration

First-class client tooling (`huggingface_hub` and `transformers` `from_pretrained()`) makes the
Hub the default source most downstream stacks pull from, by convention and not by contractual
lock-in. Artifacts are plain git with LFS-format pointers, so they stay portable to any mirror
or local store. Per-stack integration specifics are not catalogued.
