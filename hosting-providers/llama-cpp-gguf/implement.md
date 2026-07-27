# Implement - llama.cpp / GGUF

_How do we obtain and verify weights? Obtaining and converting, integrity verification,
revision pinning, and running/serving locally live here._

<!-- item: obtain-weights -->
## Obtain & convert weights

Because llama.cpp is **not a hub**, obtaining weights is a two-step affair. You either:

- **Obtain and convert yourself** - pull the source weights elsewhere (usually Hugging Face),
  convert to GGUF with `convert_hf_to_gguf.py`, then quantize with `llama-quantize`
  (Q4_K_M, Q5_K_M, Q8_0, etc.); or
- **Pull a prebuilt GGUF** from a community quantizer (bartowski, unsloth) who has already
  done the conversion and redistributes it on Hugging Face.

Either way the trust question is upstream: prefer the model's **canonical publisher** or a
**reputable quantizer**.

<!-- item: verify-integrity -->
## Verify integrity before serving

Since the format offers no native integrity guarantee, verification is manual and non-negotiable:

- **Verify the SHA256** of the file against the exact source revision you intended to pull.
- **Keep `llama-cpp-python >= 0.2.72`** to close the chat-template SSTI RCE (CVE-2026-5760).
- **Inspect the GGUF chat template / tokenizer config before serving.** Template injection runs
  at **inference time, on every prompt**, beyond the initial load, so a clean load is not
  sufficient evidence of a clean file. Check the template against known-malicious signatures
  where feasible.

<!-- item: pin-revision -->
## Pin the source revision

Because provenance is entirely inherited, **pin the exact source-hub revision** of the GGUF you
converted or downloaded. Pinning a revision (rather than a floating tag) makes the artifact
reproducible and hashable, so a later re-pull can be checked byte-for-byte against what you
originally reviewed.

<!-- item: run-serve -->
## Run & serve locally

Run inference locally with **`llama-cli`**, or stand up an OpenAI-style HTTP endpoint with
**`llama-server`**. Given the loader's CVE history, **sandbox the loader** - no network access
and least privilege - so that a crafted file or poisoned template has the smallest possible blast
radius.
