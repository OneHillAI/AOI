# Implement - Hugging Face Hub

_Obtaining and verifying weights, integrity checks, revision pinning and running locally._

<!-- item: obtain-weights -->
## Obtaining weights (git / huggingface_hub)

Weights live in per-model git repositories whose large files sit in Xet storage, with Git LFS
pointer files kept for compatibility. You can `git clone` a repo, but the common path is the
`huggingface_hub` client and `transformers` `from_pretrained()`, which resolve and cache the
artifacts. For gated repos (Llama, Gemma), get an approved access request first and then
authenticate with a user token, because the pull is enforced at the download/API layer.

<!-- item: verify-integrity -->
## Verifying integrity (hashes & scan status)

Files are identified by hash (git-sha1 or sha256 ETag, plus Xet chunk hashes), which gives you
something to check the bytes against. The Hub docs do not state that the client checks each
hash on download, so do not assume it.

The visible integrity surface is scan status, which shows files flagged "unsafe" or "suspicious"
by the layered scanners. It warns and does not block, and an absent flag is not proof the file is
clean. Verify the SHA256 of downloaded files yourself and check scan status before loading.

<!-- item: pin-revision -->
## Pinning a revision

Revisions are addressable by commit hash. Pin an explicit commit instead of tracking `main`, so a
later force-push or malicious update cannot silently change the bytes you load. The download/API
layer resolves the pinned revision. Combined with your own hash check, a pinned commit gives a
reproducible, tamper-evident pull.
