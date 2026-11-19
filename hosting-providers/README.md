# Hosting and distribution providers

Where model weights live and how they are installed. A downloaded artifact is executed, so entries lead with provenance, format safety and self-hosting risk, scored on the hosting profile of the [provider rubric](../methodology/provider-scoring-rubric.md) and grounded in the [supply-chain risk framework](../methodology/supply-chain-risk.md).

The entries (`hugging-face`, `ollama`, `llama-cpp-gguf`) are validated in CI but are not rendered on the website. Rendering them needs a `hosting-providers` source in `site/src/lib/entries.ts` and matching pages under `site/src/pages/library`.

## How to read an entry

- Provenance and integrity: verified organisations, malware and pickle scanning, signing, checksums, revision pinning and licence gating.
- Format and loader safety: safetensors against pickle, `trust_remote_code`, GGUF template and config injection, and the loader CVEs to patch.
- Security track record: malicious uploads and typosquatting incidents, and how fast they were handled.

## Before running a downloaded model

1. Pull from the canonical, verified source and check the exact namespace spelling. Typosquatting is a proven attack.
2. Pin the exact revision or commit. Never track a moving `main`.
3. Verify the checksum, and the signature where one is offered.
4. Prefer safetensors or GGUF. Never `torch.load` a pickle from an untrusted source in an unsandboxed process.
5. Scan the artifact with a model-malware scanner and keep the report.
6. Patch the loaders (`transformers` 5.3.0 or later, `llama-cpp-python` 0.2.72 or later) and avoid `trust_remote_code` from unverified repositories.
7. Inspect GGUF chat templates before serving. Template injection runs at inference time.

A SHA256-addressed blob proves integrity, meaning the bytes did not change. It does not prove authenticity. Only a signature tied to an identity shows who produced the bytes.

## Adding an entry

Copy [`../templates/hosting-provider/`](../templates/hosting-provider/).
