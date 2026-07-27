# berget - primary-source clauses

**SCAFFOLD - no clause files gathered here yet.** This manifest is the outstanding-document
checklist for the Cowork/browser gather pass (see
[`../../provider-primary-doc-handover.md`](../../provider-primary-doc-handover.md), Berget section).
Rows marked `retrieved: no` still need the verbatim governing text pasted into a
`<doc_type>__<detail?>__<YYYY-MM-DD>.md` file in this folder. Rows marked `retrieved: yes` are
already grounded in the entry (`inference-providers/berget/entry.yaml`); a verbatim clause file here
is still welcome but not blocking.

## _sources.md
```
doc_type       | url                          | exists | retrieved | notes
terms          | https://berget.ai/en/terms   | yes    | yes       | ev-terms - "never store any of the actual prompt content…or output"; customer retains IP; 30-day post-termination deletion; reserved right to aggregated/anonymised usage data
privacy_policy | https://berget.ai/privacy    | yes    | yes       | ev-privacy - EU/Sweden-only servers
security       | https://berget.ai/en/security| yes    | yes       | ev-security - page appears to be responsible-disclosure only
dpa            | https://berget.ai/dpa        | yes    | no        | ev-dpa - KEY OUTSTANDING. Capture transfer mechanism (gather note says EEA-only, no SCC/DPF - confirm & quote) + named sub-processor list; this is what would move data_governance back above 4
docs           | https://docs.berget.ai/      | yes    | no        | ev-docs - GDPR / EU-residency framing
marketing      | https://berget.ai/pricing    | yes    | no        | ev-pricing - pricing page
security       | (SOC 2 / ISO 27001 attestation) | ?   | no        | confirm existence - record exists:no if still absent (security page looks disclosure-only)
```
