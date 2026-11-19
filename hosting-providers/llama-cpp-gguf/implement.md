# Implement - llama.cpp / GGUF

_Obtaining and verifying weights, integrity checks, revision pinning and running locally._

<!-- item: obtain-weights -->
## Obtain & convert weights

llama.cpp is not a hub, so obtaining weights takes two steps. There are two routes:

- Obtain and convert the weights: pull the source weights elsewhere (usually Hugging Face), convert to GGUF with `convert_hf_to_gguf.py`, then quantize with `llama-quantize` (Q4_K_M, Q5_K_M, Q8_0, etc.).
- Pull a prebuilt GGUF from a community quantizer (bartowski, unsloth) who has already done the conversion and redistributes it on Hugging Face.

Either way the trust question is upstream. Prefer the model's canonical publisher or a reputable quantizer.

<!-- item: verify-integrity -->
## Verify integrity before serving

The format offers no native integrity guarantee, so verification is manual:

- Verify the SHA256 of the file against the exact source revision.
- Keep llama.cpp and `llama-cpp-python` current. `llama-cpp-python >= 0.2.72` closes the chat-template SSTI RCE (CVE-2024-34359). llama.cpp fixes are tracked by build tag (bNNNN) in NVD, and GGUF parser fixes shipped as recently as b11301 (October 2026) and in November 2026. Serving GGUF through SGLang needs >= 0.5.11 (CVE-2026-5760).
- Inspect the GGUF chat template and tokenizer config before serving. Template injection runs at inference time, on every prompt, so a clean load is not evidence of a clean file. Check the template against known-malicious signatures where feasible.

<!-- item: pin-revision -->
## Pin the source revision

Provenance is inherited from the source hub, so pin the exact source-hub revision of the GGUF that was converted or downloaded. A pinned revision (and not a floating tag) makes the artifact reproducible and hashable, so a later re-pull can be checked byte-for-byte against the reviewed file.

<!-- item: run-serve -->
## Run & serve locally

Run inference locally with `llama-cli`, or stand up an OpenAI-style HTTP endpoint with `llama-server`. The README also shows `llama cli` and `llama serve`, which can download a model with `-hf`. Do not expose `llama-server` or the RPC backend to untrusted networks; SECURITY.md advises against it. Given the loader's CVE history, sandbox the loader with no network access and least privilege, so that a crafted file or poisoned template has the smallest possible blast radius.
