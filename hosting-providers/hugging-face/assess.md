# Assess - Hugging Face Hub

_Can we trust weights obtained here? Provenance, format/loader safety, license governance, security history and the exposed trust signals - plus the provider score (79.2/100 · Grade B) - live here._

<!-- item: provenance-integrity -->
## Provenance & integrity signals

Hugging Face has the **strongest provenance of any public hub**. Named labs (Meta, Google,
Mistral) publish under **blue verified-org badges**, uploads pass through **layered
automated scanning** - Picklescan and ProtectAI ModelScan/Guardian for malicious pickles,
ClamAV for general malware, TruffleHog for leaked secrets, and a JFrog proprietary scanner
that parses embedded code - and storage is content-addressed so the client verifies file
hashes on download, with revisions addressable by **commit hash**.

Two structural caveats keep this short of perfect. Scanning **marks files "unsafe" or
"suspicious" but does not block or delete them** - it warns, it does not quarantine. And
there is **no default cryptographic signing of the weights themselves**: the "Verified"
badge is GPG commit-signing of the git history, attesting the committer, not the model.

<!-- item: format-safety -->
## Format & loader safety

**safetensors is the promoted default** and was independently audited by Trail of Bits
(2023) with no critical RCE flaw found. The loader is the risk here, the format is not:
**pickle checkpoints are flagged-not-blocked**, `trust_remote_code=True` executes Python shipped
inside the repo, and **CVE-2026-4372** achieved RCE through config injection
(`_attn_implementation_internal`) that **bypassed `trust_remote_code=False`** in
Transformers < 5.3.0. Pull safetensors, avoid remote code from unverified authors, and keep
transformers >= 5.3.0.

<!-- item: license-governance -->
## License surfacing & gating

License is declared per repo and surfaced in the model card and UI. For gated models (Llama,
Gemma), Hugging Face **actually enforces a click-through acceptance** - plus an optional
per-user access request - at the download/API layer before the weights can be pulled. That
makes it **one of the few hubs that enforces EULA gating** rather than merely displaying
terms. The limits: enforcement is per-user click-through rather than a cryptographically
bound entitlement, and license correctness relies on publisher self-declaration.

<!-- item: security-record -->
## Security incident history & response

The hub has **repeatedly hosted malicious content**: PoisonGPT (typosquatted 'EleuterAI'
org, 2023), nullifAI (2025, 7z-compressed pickles evading Picklescan, leading to
CVE-2025-1716), JFrog's report of **~100+ backdoored models**, and 2026 typosquats - the
Open-OSS 'privacy-filter' infostealer reached top-trending with **200k+ downloads** and a
fake OpenAI repo accumulated ~244k. Response is comparatively strong: **~24h removals**,
hardened picklescan after nullifAI, and formal partnerships with JFrog and ProtectAI. The
weakness is structural - scanning marks rather than blocks, and open uploads keep the
malicious-upload surface open.

<!-- item: transparency -->
## Exposed trust signals & their gameability

A downloader sees a **rich set of signals**, and most are honest: verified-org badges,
visible scan status, commit-verified badges, public gating state, and published security
documentation (SOC 2 / ISO 27001). But several prominent signals are **gameable and not
labelled as such**: download counts and likes are trivially inflated (the 2026 typosquats
rode trending/download signals to hundreds of thousands of pulls), and the `base_model`
lineage field is self-declared and can be falsified. Rely on the verified-org badge and your
own hash/scan verification - treat counts, likes and lineage as marketing, not provenance.
