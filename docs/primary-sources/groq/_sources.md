# groq - primary-source clauses

**SCAFFOLD - no clause files gathered here yet.** This manifest is the outstanding-document
checklist for the Cowork/browser gather pass (see
[`../../provider-primary-doc-handover.md`](../../provider-primary-doc-handover.md), Groq section).
Rows marked `retrieved: no` still need the verbatim governing text pasted into a
`<doc_type>__<detail?>__<YYYY-MM-DD>.md` file here. Rows marked `retrieved: yes` are already
grounded in `inference-providers/groq/entry.yaml`.

## _sources.md
```
doc_type       | url                                                              | exists | retrieved | notes
terms          | https://console.groq.com/docs/legal/services-agreement           | yes    | yes       | ev-terms - customer retains IP; Groq never trains on Customer Data; no default retention; 30-day deletion
dpa            | https://console.groq.com/docs/legal/customer-data-processing-addendum | yes | yes    | ev-dpa - says sub-processor list is published on the trust center
dpa            | https://console.groq.com/docs/legal/customer-business-associate-addendum | yes | yes | ev-baa - HIPAA BAA
security       | https://trust.groq.com/                                          | yes    | yes       | ev-trust - SOC 2 Type II (trust-center headline)
subprocessors  | https://trust.groq.com/subprocessors                             | yes    | no        | ev-subproc - OUTSTANDING. Prior capture was a manual scrape of a Vanta SPA; re-read and paste the ~21 named entries + regions verbatim
terms          | https://console.groq.com/docs/legal/ai-policy                    | yes    | no        | ev-aup - Acceptable-Use Policy (effective 2025-10-15). Capture governing clauses
security       | (SOC 2 Type II report itself)                                    | yes    | no        | report is gated behind trust-center request - record as exists:yes / retrieved:no unless obtained
```
