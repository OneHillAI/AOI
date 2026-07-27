# Hosting / Distribution Providers

> **Status: hidden from the published site (July 2026).** These entries are migrated to the
> v2 four-domain format and still validate in CI, but the hosting **section is not currently
> rendered on the website** while we settle how hosting/distribution should be presented.
> Re-enable by adding a `hosting-providers` source to `site/src/lib/entries.ts` (a
> `listEntries('hosting-providers', ...)` call with the hosting dimension map) and rendering
> it in the custom library pages under `site/src/pages/library`.

Where model weights live and how you install them. The defining risk here is different
from inference: **you download an artifact and execute it.** So these entries lead with
provenance, format safety, and self-hosting risk - scored on the
[provider rubric](../methodology/provider-scoring-rubric.md) hosting profile, grounded in
the [supply-chain risk framework](../methodology/supply-chain-risk.md).

## How to read an entry

- **Provenance & integrity** - verified orgs, malware/pickle scanning, cryptographic
  signing, checksums, revision pinning, license gating.
- **Format & loader safety** - safetensors vs pickle, `trust_remote_code`, GGUF
  template/config-injection, and the loader CVEs you must patch.
- **Security track record** - real malicious-upload and typosquatting incidents, and how
  fast they were handled.

## The exemplar set (v0.1)

| Entry | Type | Provenance strength | Format posture | The one thing to remember |
|---|---|---|---|---|
| [`hugging-face`](hugging-face/) | Hub | Strongest (verified orgs + layered scanning + gating) | safetensors default; pickle flagged-not-blocked | Best tooling, but *pin the revision & verify* - typosquats and pickle bypasses are real. |
| [`ollama`](ollama/) | Local runner | Weak (no verified-org identity, no documented scanning/signing) | GGUF (data-only, avoided the main CVE) | Convenient, but **bring your own provenance discipline**. |
| [`llama-cpp-gguf`](llama-cpp-gguf/) | Serving engine / format | Inherits your source; none native | GGUF is safe *data*, but loaders had SSTI/heap CVEs | Pin `llama-cpp-python ≥ 0.2.72` and **inspect the chat template**. |

## The universal minimum bar (applies to all of them)

Regardless of host, before you run a downloaded model:

1. **Pull from the canonical, verified source** - check the *exact* namespace spelling
   (typosquatting is a proven attack).
2. **Pin the exact revision/commit** - never track a moving `main`.
3. **Verify the checksum** (and signature, if offered).
4. **Prefer safetensors/GGUF**; never `torch.load` a pickle from an untrusted source in
   an unsandboxed process.
5. **Scan the artifact** with a model-malware scanner; keep the report.
6. **Patch your loaders** (`transformers ≥ 5.3.0`, `llama-cpp-python ≥ 0.2.72`) and avoid
   `trust_remote_code` from unverified repos.
7. **Inspect GGUF chat templates** before serving - template injection runs at inference
   time.

> **Content-addressed ≠ authentic.** A SHA256-addressed blob guarantees *integrity* (the
> bytes didn't change) but not *authenticity* (that the right party produced them). Only
> a signature tied to an identity gives you the latter.

Adding an entry: copy [`../templates/hosting-provider/`](../templates/hosting-provider/).
