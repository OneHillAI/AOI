# infercom - primary-source clauses

**SCAFFOLD - no clause files gathered here yet.** This manifest is the outstanding-document
checklist for the Cowork/browser gather pass (see
[`../../provider-primary-doc-handover.md`](../../provider-primary-doc-handover.md), Infercom
section - **highest priority in the provider pass**). Rows marked `retrieved: no` still need the
verbatim governing text pasted into a `<doc_type>__<detail?>__<YYYY-MM-DD>.md` file here. Rows
marked `retrieved: yes` are already grounded in `inference-providers/infercom/entry.yaml`.

## _sources.md
```
doc_type       | url                                                | exists | retrieved | notes
privacy_policy | https://infercom.ai/privacypolicy/                 | yes    | yes       | ev8 - zero prompt/output retention; no training on inference data; metadata-only 90-day logs; conditional-sovereignty clause (Global-Catalog non-EU models route prompt content to SambaNova outside EEA, primarily US, under EC SCCs + EU-US DPF)
dpa            | https://infercom.ai/Infercom_DPA_v1.3_dl.pdf       | yes    | no        | ev9 - HIGHEST-VALUE DOC IN THE WHOLE PROVIDER PASS (PDF is 403 behind the proxy). Capture: EU-hosted vs Global-catalog split; SCCs + EU-US DPF transfer basis; the five named sub-processors; TLS/EEA-processing terms; Luxembourg governing law. ev-dpa maps straight to it
terms          | https://infercom.ai/termsconditions/               | yes    | no        | NO evidence item yet - Terms of Service v2.1. Capture no-training commitment, customer retains input/output, 30-day deletion
security       | https://cloudsecurityalliance.org/star/registry/infercom | yes | no    | ISO 27001 cert # LU-IS-20250253 (issuer Proks, valid 2025-12-16 → 2028-12-15) + CSA STAR for AI (Level 1, CAIQ v1.1.0). Cite the certificate/registry record itself, not the trust-page claim
```
