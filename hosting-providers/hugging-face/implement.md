# Implement - Hugging Face Hub

_How do we obtain and verify weights? Pulling via git / huggingface_hub, verifying integrity, and pinning a revision live here; running/serving and resource sizing are documented gaps._

<!-- item: obtain-weights -->
## Obtaining weights (git / huggingface_hub)

Weights live in **per-model git repositories** whose large files sit in **Xet storage** with
Git LFS pointer files kept for compatibility. You can `git clone` a repo, but the common path
is the **`huggingface_hub` client and `transformers` `from_pretrained()`**, which resolve and
cache the artifacts for you. For **gated** repos (Llama, Gemma) you must first have an
approved access request and then authenticate with a user token, because the pull is enforced
at the download/API layer.

<!-- item: verify-integrity -->
## Verifying integrity (hashes & scan status)

Files are identified by hash (git-sha1 or sha256 ETag, plus Xet chunk hashes), which gives you
something to check the bytes against. The Hub docs read do not state that the client
re-verifies each hash on download, so do not assume it. The visible integrity surface
on the Hub is **scan status** - files flagged "unsafe"/"suspicious" by the layered scanners -
but remember this **warns rather than blocks**. Do not treat an absent flag as a clean bill
of health: verify the **SHA256** of downloaded files yourself and check scan status before
loading.

<!-- item: pin-revision -->
## Pinning a revision

Revisions are **addressable by commit hash**. Always pin an explicit commit rather than
tracking `main`, so a later force-push or malicious update cannot silently change the bytes
you load - the download/API layer resolves the pinned revision. Combined with your own hash
check, a pinned commit gives you a reproducible, tamper-evident pull.
