# Ollama - OneHill Hosting-Provider Dossier

> **Score: 48.4/100 · Grade D** · Type: local_runner · safetensors default: promoted (MLX builds, Apple Silicon only) · Signing: none shipped
> Last verified: 2026-11-19
>
> _A convenient local runner and registry on data-only formats. Users must bring their own provenance: there are no verified publishers, no scanning and no signing. The tool's own 2026 security record is poor, with a critical GGUF loader CVE, pull-path SSRF and updater CVEs, and several reporters saying the vendor did not respond._

**Hard flags:** none

Format & Loader Safety scores 3 because Ollama's own GGUF loader had CVE-2026-7482 (critical, fixed in 0.17.1). Security Track Record scores 2. The headline is 48.4 (D). CVE-2026-5760 is an SGLang flaw, not an Ollama one. Primary-source extracts are in [`docs/primary-sources/ollama/`](../../docs/primary-sources/ollama/_sources.md).

---

## At a glance

| Dimension | Score | One-line reason |
|---|---|---|
| Provenance & Integrity | 2/5 | No verified orgs, no scanning, signing only proposed (PR #11573 open); hashing proves integrity, not authorship |
| Format & Loader Safety | 3/5 | GGUF and MLX safetensors layers are data-only, but Ollama's own loader had CVE-2026-7482 and the template-injection surface remains |
| License Surfacing & Governance | 2/5 | Licence text shipped per model and viewable via `ollama show --license`, but no gating and Terms are silent on model licences |
| Security Track Record | 2/5 | Critical loader CVE, pull-path SSRF and Windows updater CVEs; vendor non-response on four records; no advisories or security page |
| Transparency & Trust Signals | 2/5 | Only namespace, library curation and the licence layer exposed; no trust centre, DPA or certification |
| Ecosystem & Portability | 4/5 | Huge ecosystem, MIT software, portable formats; Modelfile and manifest-list layout are Ollama-specific |

## 1. How weights are distributed & installed

Ollama distributes models through a content-addressable, OCI-like registry of manifests
and SHA256-addressed blobs. `ollama pull` fetches a manifest and its blobs and caches
them; `ollama run` serves the model on localhost. Since v0.40.0 (2026-09-25) a name can
resolve to a manifest list with two children: a llama.cpp GGUF build and an MLX
safetensors-derived build stored as one layer per tensor. The client prefers MLX, then
llama.cpp, then ggml on Apple Silicon, and llama.cpp first elsewhere. A client that does
not ask for the list (an older Ollama) is served the llama.cpp GGUF manifest.

Models already on disk are upgraded in the background by v0.40.2 and later, with the
original kept as a backup, and downgrading below 0.40 means re-pulling. Custom models
are built with a Modelfile and `ollama create`, and any user can push to ollama.com under a
username.

`:cloud` tags are different. A model such as `gemma4:cloud` is not downloaded: it runs
on Ollama's servers and needs an account. The binding Privacy Policy says cloud prompts
are processed transiently, "not stored beyond the time required to fulfill the request",
with "technical measures designed to minimize retention", and never used for training. The
Terms say Ollama does not use inputs or outputs to train AI models.

The cloud docs and the pricing page go further ("zero data retention", "never logged").
That is stronger than the binding text, and no ZDR agreement, DPA, sub-processor list or
certification is published. Hosting is described as primarily the United States, with Europe
overflow, by NVIDIA Cloud Providers. `OLLAMA_NO_CLOUD=1` keeps a local install fully local.

## 2. Provenance - verified orgs, signing, scanning, checksums, gating

Provenance is the weak spot. There is no verified-publisher identity, so trust rests on
namespace ownership alone. No GGUF-level malware scanning is documented, and no signing has
shipped: model signing (PR #11573) is open and was last updated on 2026-09-08. The Ollama
public key identifies an install to ollama.com, not a publisher.

The one integrity guarantee is that blobs are SHA256-addressed. That proves the bytes match
the manifest (integrity) and says nothing about who published them (authenticity). There is
no licence gating in the CLI flow.

## 3. Format & loader safety

GGUF and the safetensors-derived MLX layers are data-only: loading them does not execute
code the way pickle does. That keeps this dimension at 3 and not lower.

The record is not clean. CVE-2026-7482 ("Bleeding Llama") is a heap out-of-bounds read in
Ollama's own GGUF loader and quantiser (CVSS 9.1). A crafted GGUF sent to the unauthenticated
`/api/create` endpoint leaks process memory, which can be exfiltrated through `/api/push`.
NVD names 0.17.1 as the fixed version. CERT/CC lists a similar CVE-2026-5757 and says it
could not reach the vendor; Ollama has published no status for it.

A malicious GGUF Jinja2 chat template can still cause server-side template injection and
inference-time backdoors where the runner renders it. `ollama show` has reported
`template_source` since 0.40.7, so the origin of the template is visible.

CVE-2026-5760 is a chat-template RCE in SGLang (NVD, CERT/CC VU#915947). It is not an
Ollama or llama-cpp-python CVE, so it neither supports nor undermines Ollama's score.

## 4. Security track record

No malicious-model incident on ollama.com is known, but weak provenance tooling means
that absence is partly an absence of detection. The tool's own 2026 record is serious:

| CVE | What | Status |
|---|---|---|
| CVE-2026-7482 | GGUF loader heap read, memory leak via create and push | Fixed in 0.17.1 per NVD; release notes do not mention it |
| CVE-2026-5757 | Quantisation heap read (CERT/CC VU#518910) | No vendor status; may be the same flaw as 7482 |
| CVE-2026-85180 | SSRF through tensor-layer blob redirects on pull, 0.30.0 to 0.33.2 | Issue #17041 still open; current code validates redirect targets |
| CVE-2026-5530 | SSRF in the model pull API, up to 0.18.1 | NVD record Deferred; vendor did not respond to the reporter |
| CVE-2026-42248, CVE-2026-42249 | Windows updater without signature check, path traversal | Current main verifies the installer signature; first fixed release not determined |

Disclosure handling is poor: four CVE records say the vendor did not respond, release notes
do not flag security fixes, no GitHub security advisory is published, and
`ollama.com/security` returns 404. `SECURITY.md` asks for reports through GitHub advisories.
Fixes do appear in current code, which keeps this dimension at 2 and not 1.

## 5. Pulling from it safely - the practical guideline

- Keep Ollama current and off the network. Run the 0.40 line (0.17.1 is only the floor
  for the loader CVE). Keep the API on `127.0.0.1`: `/api/create` and `/api/push` have no
  authentication, and the loader CVE was exploitable on servers bound to `0.0.0.0`.
- Prefer the official Ollama library or known publishers. Namespace ownership is not
  an identity badge, so treat unknown namespaces as untrusted third-party software.
- Cross-check the checksum against a canonical source. Where the same model exists on
  the publisher's Hugging Face repo, verify the pulled GGUF's SHA256 against it.
  Content-addressing gives integrity, not authenticity.
- Inspect the chat template before serving untrusted models. `ollama show` the model
  and read the template; template injection runs at inference time, on every prompt.
- Read the model licence. `ollama show --license` prints it; nothing requires acceptance,
  including for the Llama community licences.
- Decide on cloud use deliberately. `:cloud` models send prompts to Ollama's servers.
  The Privacy Policy is the binding text; the zero-retention wording elsewhere is marketing.
- Record what was pulled (model, digest, source) in the AI-BOM, since the platform
  does not attest provenance.

## 6. Sources & evidence

Primary documents (extracts in `docs/primary-sources/ollama/`):

- Ollama software licence (MIT), Terms of Service (August 2026) and Privacy Policy (March 2026).
- Cloud docs, Cloud FAQ and pricing page; release notes (v0.40.16 stable, v0.40.17-rc1).
- Registry manifests and server source (manifest lists, runner preference, licence layers).
- NVD records, CERT/CC VU#518910 and VU#915947, CERT Polska and VulnCheck advisories, `SECURITY.md`.

Third-party sources: DeepWiki (registry mechanics), zohaib.me (custom GGUFs rely on
user-supplied provenance), ProtectAI GGUF-101 and JFrog / NeuralTrust (GGUF chat-template
risks).

---

_Scored against [provider rubric v1.0](../../methodology/provider-scoring-rubric.md).
Data: [`entry.yaml`](entry.yaml)._
