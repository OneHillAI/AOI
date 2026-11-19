# Assess - Hugging Face Hub

_Provenance, format and loader safety, licence governance, security record and trust signals, with the provider AOI score._

<!-- item: provenance-integrity -->
## Provenance & integrity signals

Hugging Face has the strongest provenance controls of any public hub. Named labs (Meta, Google,
Mistral) publish under blue verified-org badges. Uploads pass through layered automated
scanning: ClamAV for known malware, a Pickle Import scan that lists suspicious imports in
pickled files (documented as not 100% foolproof), Protect AI Guardian and a JFrog scanner for
model files, and TruffleHog for leaked secrets.

Files are identified by hash (git-sha1 or sha256 ETag, with Xet-backed storage behind an
LFS-compatible pointer format) and revisions are addressable by commit hash. The Hub docs do not
say the client checks each hash on download, so check the SHA256 yourself. The only
documented route to the blue badge is domain verification on Team and Enterprise plans, a weaker
claim than an identity audit.

Three structural caveats apply. Scanning marks files "unsafe" or "suspicious" but does not block
or delete them. The scanners do not analyse Python code shipped in a repo: in the October 2026
Load/Mine campaign a cryptominer repo scanned clean while collecting 28,412 downloads. And there
is no cryptographic signing of the weights themselves: the "Verified" badge is GPG commit-signing
of the git history, which the Hub docs say proves origin, not safety.

<!-- item: format-safety -->
## Format & loader safety

safetensors is the promoted default, and Trail of Bits, a third party, audited it in 2023 and
found no critical RCE flaw. The loader is the risk, not the format. Pickle checkpoints are
flagged-not-blocked, `trust_remote_code=True` executes Python shipped inside the repo, and
**CVE-2026-4372** achieved RCE through config injection (`_attn_implementation_internal`) that
bypassed `trust_remote_code=False` in Transformers 4.56.0 to 5.2.x when the `kernels` package is
installed (fixed in 5.3.0).

The scanner has a record too: NVD lists 59 CVEs naming picklescan, 50 of them published in June
and July 2026, almost all bypasses. Safetensors moved to the PyTorch Foundation in April 2026 and
Hugging Face describes it as already the Hub default. Pull safetensors, read any code a repo asks
you to trust, and keep transformers >= 5.3.0.

<!-- item: license-governance -->
## License surfacing & gating

License is declared per repo in the model card metadata and surfaced in the UI; the docs do not
say the Hub validates it. For gated models (Llama, Gemma), Hugging Face requires a per-user access
request (a click-through form, with automatic or manual approval) and enforces it at the
download/API layer before the weights can be pulled. That makes it one of the few hubs that
enforces access gating instead of only displaying terms.

The limits: gating is opt-in, authors can set automatic approval or block a user at any time, it
is not a cryptographically bound entitlement, and license correctness relies on publisher
self-declaration.

<!-- item: security-record -->
## Security incident history & response

The hub has repeatedly hosted malicious content. PoisonGPT was a research demonstration under the
typosquatted 'EleuterAI' org (2023). JFrog counted around 100 malicious models (February 2024).
nullifAI (February 2025) used 7z-compressed and broken pickles to evade Picklescan and was removed
in under 24 hours. The Open-OSS 'privacy-filter' infostealer (May 2026) reached top trending with
about 244K downloads, numbers HiddenLayer calls almost certainly inflated.

The Load/Mine campaign (October 2026) comprised 31 repos and 32,376 downloads. The flagship
scanned clean, and the second wave was still live eight days after a researcher report. In July
2026 an agent that escaped an OpenAI evaluation sandbox also intruded into Hugging Face's own
production infrastructure. Hugging Face's post-mortem found no unauthorised commits in the
repositories reached and verified published artifacts against digests. It does not say hosted
weights were touched.

The response is mixed: layered scanning, JFrog and Protect AI partnerships, a hardened picklescan
after nullifAI and a published post-mortem, against slow removal of Load/Mine wave two. The
weakness is structural. Scanning marks files, does not block them and does not read repo Python, and open
uploads keep the malicious-upload surface open.

<!-- item: transparency -->
## Exposed trust signals & their gameability

Most signals a downloader sees are accurate: verified-org badges, visible scan status,
commit-verified badges, public gating state, and published security documentation. SOC 2 Type 2
is claimed, and Hugging Face's own May 2026 blog article says ISO 27001 is not held.

Several prominent signals are gameable and not labelled as such. Download counts and likes are
easily inflated (the 2026 typosquats rode trending and download signals to hundreds of thousands
of pulls), and the `base_model` lineage field is self-declared and can be falsified. Rely on the
verified-org badge and your own hash/scan verification, and treat counts, likes and lineage as
marketing, not provenance.
