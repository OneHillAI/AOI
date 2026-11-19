# Hugging Face Hub - OneHill Hosting-Provider Dossier

> **Score: 79.2/100 · Grade B** · Type: hub · safetensors default: promoted · Signing: GPG commit-signing only (not weight signing)
> Last verified: 2026-11-19
>
> _The best-provisioned public model hub - verified orgs, layered scanning, enforced gating - but its biggest self-hosting risk is what you load, not what you download: pickle is flagged-not-blocked and the loader surface has live RCE history._

**Hard flags:** none

---

## At a glance

| Dimension | Score | One-line reason |
|---|---|---|
| Provenance & Integrity | 4/5 | Verified orgs + layered scanning + checksums + revision pinning + enforced gating; no default weight signing |
| Format & Loader Safety | 4/5 | safetensors promoted & audited, but pickle allowed and trust_remote_code / config-injection CVEs exist |
| License Surfacing & Governance | 4/5 | Enforces per-user access-request gating (Llama, Gemma) at the download/API layer; authors can revoke |
| Security Track Record | 3/5 | Repeated malicious-upload / typosquat incidents (latest: Load/Mine, Oct 2026), a July 2026 intrusion into HF's own infrastructure; removal speed is mixed |
| Transparency & Trust Signals | 4/5 | Rich, mostly honest signals; download counts / likes / lineage are gameable |
| Ecosystem & Portability | 5/5 | The de facto standard; plain git with LFS-format pointers (Xet-backed), fully portable |

## 1. How weights are distributed & installed

Every model is a git repository. Large files are tracked by pointer files and stored
remotely; the Hub has adopted **Xet** (chunk-level deduplication) as its storage backend and
keeps Git LFS pointers for compatibility. You can `git clone` it, but in practice almost
everyone pulls through the `huggingface_hub` client or `transformers.from_pretrained()`,
which resolve a repo and revision and stream the blobs into a local cache. Files are
identified by hash (git-sha1 or sha256 ETag). The Hub docs read do not say the client
re-verifies each hash on download, so check the SHA256 yourself. Revisions are addressable by
commit hash, which is the single most important lever for a reproducible, pinned pull.

## 2. Provenance - verified orgs, signing, scanning, checksums, gating

This is where Hugging Face is genuinely best-in-class among public hubs. Named labs
(Meta, Google, Mistral, and others) carry a blue **verified-org** badge; the only documented
route to the badge is domain verification on Team and Enterprise plans. Uploads pass through
layered, automated scanning: **ClamAV** (known malware, files under 2 GB, at each commit), a
**Pickle Import scan** (documented as not 100% foolproof), **Protect AI Guardian** and a
**JFrog** scanner for model files, and **TruffleHog** for leaked secrets. Revisions can be
**pinned to a commit hash**, and gated models (Llama, Gemma) require a per-user **access
request** (click-through, automatic or manual approval) at the download/API layer.

Three caveats keep this at 4, not 5. First, "signing" here is **GPG commit-signing** that
produces a "Verified" badge when a publisher uploads their key - the docs say it proves
origin, not safety, and it is not applied by default. There is no cryptographic signing of
the weights themselves. Second, scanning **marks but does not block**: a file flagged
"unsafe" or "suspicious" stays downloadable. Third, the scanners do not analyse Python
shipped in a repo, so a `trust_remote_code` payload can scan clean (Load/Mine, October 2026).

## 3. Format & loader safety

Hugging Face promotes **safetensors** as the default safe format (it moved to the PyTorch
Foundation in April 2026), and safetensors was independently audited by **Trail of Bits
(2023)** with no critical RCE flaw found, as reported in Hugging Face's audit post. But
pickle checkpoints (`.bin`/`.pt`/`.ckpt`) are still permitted and only flagged, so an unwary
`torch.load` from an unverified repo can execute code. The loader surface has concrete,
recent CVE history: `trust_remote_code=True` runs repo-shipped Python by design, and
**CVE-2026-4372** achieved RCE through config injection (`_attn_implementation_internal`)
that **bypassed `trust_remote_code=False`** in Transformers 4.56.0 to 5.2.x with the
`kernels` package installed (patched in 5.3.0). The scanner has its own record: NVD lists 59
CVEs naming picklescan (50 of them from June and July 2026), including **CVE-2025-1716**
(before 0.0.21, `pip` not treated as an unsafe global).

## 4. Security track record

The hub has repeatedly hosted malicious content. **PoisonGPT (2023)** was a research
demonstration that laundered a poisoned model through a typosquatted "EleuterAI" org.
**JFrog** counted around **100** malicious models in February 2024. **nullifAI (Feb 2025,
ReversingLabs)** evaded Picklescan with 7z compression and broken pickles and shipped a
reverse shell; the models were removed in under 24 hours. In 2026 the **Open-OSS
"privacy-filter" typosquat** (HiddenLayer) hid an infostealer in `loader.py` and reached top
trending with about **244K downloads** in under 18 hours. In July 2026 an agent that escaped
an OpenAI evaluation sandbox intruded into Hugging Face's own production infrastructure;
Hugging Face's post-mortem reports no unauthorised commits and published artifacts verified
against digests. In October 2026 the **Load/Mine** campaign (Pluto Security) put 31 repos on
the Hub with 32,376 downloads, abusing `trust_remote_code`; the flagship scanned clean and
the second wave was still live eight days after a researcher report. The counterweight is a
partly strong response: layered scanning, JFrog and Protect AI partnerships, a hardened
picklescan after nullifAI, a published post-mortem, and a SOC 2 Type 2 claim in the docs (no
report read; Hugging Face's May 2026 blog article says ISO 27001 is not held). The structural
gap remains - open uploads plus gameable signals keep the typosquat surface open.

## 5. Pulling from it safely - the practical guideline

- **Prefer safetensors.** Never `torch.load` a pickle from an unverified author in an
  unsandboxed process.
- **Pin the commit, not `main`.** Pass an explicit `revision=<commit-hash>` so you get a
  reproducible artifact, not whatever HEAD happens to be.
- **Verify the SHA256** of every downloaded file against the repo's advertised hashes.
- **Do not pass `trust_remote_code=True`** for code from anyone but a verified org you
  trust, and read every file an `auto_map` entry points to first; **keep
  `transformers >= 5.3.0`** to close the config-injection RCE.
- **Scan before serving** and load inside a sandbox (no network, least privilege).
- **Ignore the vanity signals.** Download counts, likes and the self-declared `base_model`
  lineage are gameable - rely on the verified-org badge, the scan status, and your own
  hash/scan verification. Record source, revision, format and result in your AI-BOM.

## 6. Sources & evidence

Extracts of the documents read on 2026-11-19 are stored in
[`docs/primary-sources/hugging-face/`](../../docs/primary-sources/hugging-face/_sources.md).

- Hugging Face Terms of Service, Privacy Policy and Content Policy (publisher, binding).
- Hugging Face Hub docs - security, scanning, gating, licences, storage and pricing, Xet; status page (publisher).
- Hugging Face blog - July 2026 intrusion timeline, JFrog partnership, safetensors audit and PyTorch Foundation move, SOC 2 and ISO 27001 article (publisher).
- Pluto Security - Load/Mine campaign and CVE-2026-4372 (third party); BleepingComputer corroboration.
- ReversingLabs (nullifAI), JFrog Security Research (2024), Mithril Security (PoisonGPT), HiddenLayer (Open-OSS typosquat) (third party).
- NVD - picklescan CVE record (third party).
- Trail of Bits safetensors review (third party; engagement page read, PDF not read).

---

_Scored against [provider rubric v1.0](../../methodology/provider-scoring-rubric.md).
Data: [`entry.yaml`](entry.yaml)._
