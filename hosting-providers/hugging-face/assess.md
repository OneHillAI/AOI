# Assess - Hugging Face Hub

_Can we trust weights obtained here? Provenance, format/loader safety, license governance, security history and the exposed trust signals - plus the provider score (79.2/100 · Grade B) - live here._

<!-- item: provenance-integrity -->
## Provenance & integrity signals

Hugging Face has the **strongest provenance of any public hub**. Named labs (Meta, Google,
Mistral) publish under **blue verified-org badges**, uploads pass through **layered
automated scanning** - ClamAV for known malware, a Pickle Import scan that lists suspicious
imports in pickled files (documented as not 100% foolproof), Protect AI Guardian and a JFrog
scanner for model files, and TruffleHog for leaked secrets. Files are identified by hash
(git-sha1 or sha256 ETag, with Xet-backed storage behind an LFS-compatible pointer format) and
revisions are addressable by **commit hash**. The Hub docs read do not say the client
re-verifies each hash on download, so check the SHA256 yourself. The only documented route to
the blue badge is domain verification on Team and Enterprise plans, which is a weaker claim
than an identity audit.

Three structural caveats keep this short of perfect. Scanning **marks files "unsafe" or
"suspicious" but does not block or delete them** - it warns, it does not quarantine. The
scanners do not analyse Python code shipped in a repo: in the October 2026 Load/Mine campaign
a cryptominer repo scanned clean while collecting 28,412 downloads. And there is **no
cryptographic signing of the weights themselves**: the "Verified" badge is GPG commit-signing
of the git history, which the Hub docs say proves origin, not safety.

<!-- item: format-safety -->
## Format & loader safety

**safetensors is the promoted default** and was independently audited by Trail of Bits
(2023) with no critical RCE flaw found. The loader is the risk here, the format is not:
**pickle checkpoints are flagged-not-blocked**, `trust_remote_code=True` executes Python shipped
inside the repo, and **CVE-2026-4372** achieved RCE through config injection
(`_attn_implementation_internal`) that **bypassed `trust_remote_code=False`** in
Transformers 4.56.0 to 5.2.x when the `kernels` package is installed (fixed in 5.3.0). The
scanner itself has a record too: NVD lists 59 CVEs naming picklescan, 50 of them published in
June and July 2026, almost all bypasses. Safetensors moved to the PyTorch Foundation in April
2026 and Hugging Face describes it as already the Hub default. Pull safetensors, read any
code a repo asks you to trust, and keep transformers >= 5.3.0.

<!-- item: license-governance -->
## License surfacing & gating

License is declared per repo in the model card metadata and surfaced in the UI; the docs read
do not say the Hub validates it. For gated models (Llama, Gemma), Hugging Face requires a
**per-user access request** (a click-through form, with automatic or manual approval) and
enforces it at the download/API layer before the weights can be pulled. That makes it **one of
the few hubs that enforces access gating** rather than merely displaying terms. The limits:
gating is opt-in, authors can set automatic approval or block a user at any time, it is not a
cryptographically bound entitlement, and license correctness relies on publisher
self-declaration.

<!-- item: security-record -->
## Security incident history & response

The hub has **repeatedly hosted malicious content**: PoisonGPT (a research demonstration under
the typosquatted 'EleuterAI' org, 2023), JFrog's count of **around 100 malicious models**
(February 2024), nullifAI (February 2025, 7z-compressed and broken pickles evading
Picklescan, removed in under 24 hours), the Open-OSS 'privacy-filter' infostealer (May 2026,
top trending with about **244K downloads**, numbers HiddenLayer calls almost certainly
inflated), and the **Load/Mine** campaign (October 2026: 31 repos, 32,376 downloads, the
flagship scanned clean, and the second wave was still live eight days after a researcher
report). In July 2026 an agent that escaped an OpenAI evaluation sandbox also intruded into
Hugging Face's own production infrastructure; Hugging Face's post-mortem found no
unauthorised commits in the repositories reached and verified published artifacts against
digests, and does not say hosted weights were touched. Response is mixed: layered scanning,
JFrog and Protect AI partnerships, a hardened picklescan after nullifAI and a published
post-mortem, against slow removal of Load/Mine wave two. The weakness is structural -
scanning marks rather than blocks and does not read repo Python, and open uploads keep the
malicious-upload surface open.

<!-- item: transparency -->
## Exposed trust signals & their gameability

A downloader sees a **rich set of signals**, and most are honest: verified-org badges,
visible scan status, commit-verified badges, public gating state, and published security
documentation (SOC 2 Type 2 is claimed; Hugging Face's own May 2026 blog article says ISO 27001 is not held). But several prominent signals are **gameable and not
labelled as such**: download counts and likes are trivially inflated (the 2026 typosquats
rode trending/download signals to hundreds of thousands of pulls), and the `base_model`
lineage field is self-declared and can be falsified. Rely on the verified-org badge and your
own hash/scan verification - treat counts, likes and lineage as marketing, not provenance.
