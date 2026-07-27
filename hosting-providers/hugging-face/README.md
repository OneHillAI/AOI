# Hugging Face Hub - OneHill Hosting-Provider Dossier

> **Score: 79.2/100 · Grade B** · Type: hub · safetensors default: promoted · Signing: GPG commit-signing only (not weight signing)
> Last verified: 2026-07-25
>
> _The best-provisioned public model hub - verified orgs, layered scanning, enforced gating - but its biggest self-hosting risk is what you load, not what you download: pickle is flagged-not-blocked and the loader surface has live RCE history._

**Hard flags:** none

---

## At a glance

| Dimension | Score | One-line reason |
|---|---|---|
| Provenance & Integrity | 4/5 | Verified orgs + layered scanning + checksums + revision pinning + enforced gating; no default weight signing |
| Format & Loader Safety | 4/5 | safetensors promoted & audited, but pickle allowed and trust_remote_code / config-injection CVEs exist |
| License Surfacing & Governance | 4/5 | Actually enforces click-through gating (Llama, Gemma) at the download/API layer |
| Security Track Record | 3/5 | Repeated real malicious-upload / typosquat incidents, offset by fast (~24h) removals |
| Transparency & Trust Signals | 4/5 | Rich, mostly honest signals; download counts / likes / lineage are gameable |
| Ecosystem & Portability | 5/5 | The de facto standard; plain git+LFS, fully portable |

## 1. How weights are distributed & installed

Every model is a git repository backed by git-LFS. You can `git clone` it, but in
practice almost everyone pulls through the `huggingface_hub` client or
`transformers.from_pretrained()`, which resolve a repo and revision and stream the LFS
blobs into a local cache. Storage is content-addressed and the client verifies file
hashes on download, so what lands on disk matches what the repo advertises. Revisions are
addressable by commit hash, which is the single most important lever for a reproducible,
pinned pull.

## 2. Provenance - verified orgs, signing, scanning, checksums, gating

This is where Hugging Face is genuinely best-in-class among public hubs. Named labs
(Meta, Google, Mistral, and others) carry a blue **verified-org** badge, giving you a
real identity anchor. Uploads pass through a layered, automated scanning pipeline:
**Picklescan** and **ProtectAI ModelScan/Guardian** for malicious pickles, **ClamAV** for
general malware, **TruffleHog** for leaked secrets, and a **JFrog** proprietary scanner
that parses embedded code. Files come with **SHA/etag checksums**, revisions can be
**pinned to a commit hash**, and gated models (Llama, Gemma) enforce a **click-through
license acceptance** - optionally a per-user access request - at the download/API layer.

Two caveats keep this at 4, not 5. First, "signing" here is **GPG commit-signing** that
produces a "Verified" badge when a publisher uploads their key - it attests the git
committer, not the model weights, and is not applied by default. There is no default
cryptographic signing of the weights themselves. Second, scanning **marks but does not
block**: a file flagged "unsafe" or "suspicious" stays downloadable.

## 3. Format & loader safety

Hugging Face promotes **safetensors** as the default safe format, and safetensors was
independently audited by **Trail of Bits (2023)** with no critical RCE flaw found - a
strong, non-publisher validation. But pickle checkpoints (`.bin`/`.pt`/`.ckpt`) are still
permitted and only flagged, so an unwary `torch.load` from an unverified repo can execute
code. The loader surface has concrete, recent CVE history: `trust_remote_code=True` runs
repo-shipped Python by design, and **CVE-2026-4372** achieved RCE through config
injection (`_attn_implementation_internal`) that **bypassed `trust_remote_code=False`** in
Transformers < 5.3.0 (patched in 5.3.0). Picklescan itself was bypassed by **CVE-2025-1716**
(the nullifAI 7z technique) and four further Sonatype-reported bypasses in 2025.

## 4. Security track record

The hub has repeatedly hosted malicious content. **PoisonGPT (2023)** laundered a poisoned
model through a typosquatted "EleuterAI" org. **nullifAI (Feb 2025, ReversingLabs)** evaded
Picklescan with 7z compression and shipped a reverse shell. **JFrog** reported **~100+**
backdoored models across 2024-25. In 2026 the **Open-OSS "privacy-filter" typosquat**
(HiddenLayer) hid an infostealer in `loader.py` and reached top-trending with **200k+
downloads**, and a fake OpenAI repo reached **~244k** downloads before removal. The
counterweight is a comparatively strong response: layered scanning, JFrog/ProtectAI
partnerships, removals typically within ~24h, a hardened picklescan after nullifAI, and
SOC 2 / ISO 27001 for HF's own operations. The structural gap remains - open uploads plus
gameable signals keep the typosquat surface open.

## 5. Pulling from it safely - the practical guideline

- **Prefer safetensors.** Never `torch.load` a pickle from an unverified author in an
  unsandboxed process.
- **Pin the commit, not `main`.** Pass an explicit `revision=<commit-hash>` so you get a
  reproducible artifact, not whatever HEAD happens to be.
- **Verify the SHA256** of every downloaded file against the repo's advertised hashes.
- **Do not pass `trust_remote_code=True`** for code from anyone but a verified org you
  trust; and **keep `transformers >= 5.3.0`** to close the config-injection RCE.
- **Scan before serving** and load inside a sandbox (no network, least privilege).
- **Ignore the vanity signals.** Download counts, likes and the self-declared `base_model`
  lineage are gameable - rely on the verified-org badge, the scan status, and your own
  hash/scan verification. Record source, revision, format and result in your AI-BOM.

## 6. Sources & evidence

- Trail of Bits safetensors security review (third-party) - no critical RCE flaw.
- The Hacker News / ReversingLabs - nullifAI, PoisonGPT, picklescan bypass (CVE-2025-1716).
- HiddenLayer - Open-OSS "privacy-filter" typosquat, 200k+ downloads.
- Hugging Face - JFrog partnership & scanner, gated-model docs, safetensors, SOC 2 / ISO 27001 (publisher).

---

_Scored against [provider rubric v1.0](../../methodology/provider-scoring-rubric.md).
Data: [`data.yaml`](data.yaml)._
