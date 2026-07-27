# Supply-chain & Checkpoint Risk Framework

**Version:** `1.0` · **Baseline:** July 2026

A model is not just a benchmark score - it is an **artifact you download and execute**.
This framework governs Dimension 2 (Provenance & Supply-chain Integrity) and answers
OneHill's explicit questions: **where and who distributes a checkpoint, how openly its
history is documented, and what has happened to it.**

Treat an open-weights model the way you treat any third-party dependency in your
supply chain - because that is exactly what it is.

---

## 1. The threat model

What can go wrong between "a lab trained a model" and "the weights run in your
process":

| Threat | Mechanism | Real-world grounding |
|---|---|---|
| **Code execution on load** | Pickle-serialized weights (`.bin`, `.pt`, `.ckpt`) can run arbitrary Python on `torch.load`. | Malicious models found on public hubs abusing pickle `__reduce__`. |
| **Tampered mirror / re-upload** | A copy on a non-canonical repo differs from the original. | Typo-squatted and look-alike model repos. |
| **Poisoned / backdoored weights** | Training-time data poisoning or a planted trigger ("sleeper agent") causes targeted misbehaviour. | Documented research on backdoors that survive safety fine-tuning. |
| **Compromised distribution account** | A publisher's hub token/account is stolen and weights are swapped. | Hub token-leak and account-takeover incidents. |
| **Dependency / loader RCE** | A vulnerability in the loading library, not the weights. | CVEs in model/serialization libraries. |
| **License / provenance laundering** | A restricted model re-uploaded under a permissive label. | Re-uploads stripping original license terms. |

## 2. The provenance questions (recorded per entry)

Every model entry answers these in its `provenance` block. Unanswerable questions are
themselves a risk signal.

**WHO distributes it**
- Is there a named, accountable publisher (org/company/lab)?
- Is the primary distribution a **verified** org on the host?
- Is there a security contact / vulnerability-disclosure process?

**WHERE it lives**
- What is the **canonical** source of truth for the weights?
- What mirrors, quantizations, and re-uploads exist, and are they acknowledged?
- Which formats are offered (safetensors vs pickle)?

**HOW its integrity is guaranteed**
- Are there checksums / a manifest?
- Are the weights **cryptographically signed** (e.g. Sigstore model-signing)?
- Is there build/training **provenance** (SLSA-style attestation)?

**WHAT has happened**
- Has this model or publisher been involved in a security incident?
- Have malicious mirrors or poisoned copies been reported?
- Are there known backdoor/trojan findings?

## 3. Checkpoint trust checklist

Scored per checkpoint (a model may have several - full, quantized, fine-tuned):

```
[ ] Canonical source identified and is the publisher's own verified org
[ ] safetensors format available (no pickle required to use the model)
[ ] File-level checksums published and verified on download
[ ] Cryptographic signature present and verifiable
[ ] Training/build provenance attestation available
[ ] No unresolved malicious-mirror or poisoning report
[ ] Loader/runtime pinned to a version without known RCE CVEs
[ ] Scanned by a model-malware scanner (result recorded)
```

Each unchecked box lowers the Dimension-2 score and may raise a hard flag (see the
[rubric](scoring-rubric.md#hard-flags-override-the-grade)).

## 4. Format safety guidance (the single highest-impact control)

> **Rule:** Prefer **safetensors**. Never `torch.load` a pickle checkpoint from an
> untrusted source in an unsandboxed process.

- **safetensors** - a data-only format; loading cannot execute code. **Default to it.**
- **GGUF** - the llama.cpp format; data-only, safe to load, widely used for local/quantized inference.
- **pickle (`.bin`/`.pt`/`.ckpt`)** - can execute arbitrary code on load. If
  unavoidable: load only from the canonical source, verify the signature/checksum
  first, and load inside a sandbox (no network, least privilege).

## 5. Provenance & signing technologies we credit

An entry earns Dimension-2 points for using these; they are described here so scores
are transparent:

- **OpenSSF Model Signing** (the `model-transparency` project) - Sigstore-based
  signing of model files; a verifiable signature tied to an identity.
- **SLSA provenance** - attestation of how/where the artifact was produced.
- **safetensors-by-default** distribution.
- **Verified-org** status on the distribution host.
- **Published checksums / manifests.**

## 6. How this maps into the entry

```yaml
provenance:
  publisher:
    name: "Meta"
    accountable_entity: true
    verified_org_on_primary_host: true
    security_contact: "https://...security"
  canonical_source: "https://huggingface.co/meta-llama/..."
  formats: [safetensors]          # safetensors | gguf | pickle
  integrity:
    checksums: true
    signed: false                 # signing technology, if any
    provenance_attestation: false
  mirrors_and_quants:
    acknowledged: true
    notable:
      - {name: "unsloth/... (GGUF)", trust: community, note: "popular quant, not canonical"}
  incidents: []                   # list of dated incident records, if any
  scanner_result: {tool: "...", clean: true, date: "2026-07-01"}
  checkpoint_checklist_score: 6   # out of 8
  evidence:
    - {claim: "safetensors available", source_type: onehill_verified, url: "..."}
```

## 7. For organisations: minimum bar before adoption

1. Pull weights **only** from the canonical verified source; pin the exact revision/commit hash.
2. Verify checksum (and signature if available) before use.
3. Use safetensors/GGUF; sandbox any pickle load.
4. Scan the artifact with a model-malware scanner; keep the report.
5. Record the exact source, revision, format, and verification result in your own
   AI bill of materials (AI-BOM) - the EU AI Act's technical-documentation
   expectations assume you can say *exactly which artifact* you deployed.
