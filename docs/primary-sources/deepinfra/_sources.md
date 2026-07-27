# deepinfra - primary-source clauses

**SCAFFOLD - no clause files gathered here yet.** This manifest is the outstanding-document
checklist for the Cowork/browser gather pass (see
[`../../provider-primary-doc-handover.md`](../../provider-primary-doc-handover.md), DeepInfra
section). Rows marked `retrieved: no` still need the verbatim governing text pasted into a
`<doc_type>__<detail?>__<YYYY-MM-DD>.md` file here. Rows marked `retrieved: yes` are already
grounded in `inference-providers/deepinfra/entry.yaml`. Several rows are expected to resolve to
`exists: no` - that honest gap is why residency/compliance are capped, so confirm and record it.

## _sources.md
```
doc_type       | url                                          | exists | retrieved | notes
terms          | https://deepinfra.com/terms                  | yes    | yes       | ev7 - customer retains IP; closed-model routing carve-out for Google/Anthropic
privacy_policy | https://docs.deepinfra.com/account/data-privacy | yes | yes       | ev2 - data-privacy statement
docs           | https://deepinfra.com/docs/data              | yes    | yes       | ev1/ev5 - zero-retention default; US data centers
security       | https://trust.deepinfra.com/compliance       | yes    | no        | ev3 - OUTSTANDING (Sprinto SPA did not resolve). Resolve SOC 2 Type 1 vs Type II; confirm ISO 27701 status; confirm whether a named sub-processor list exists (record exists:no if not)
marketing      | https://deepinfra.com/pricing                | yes    | no        | ev4/ev6 - pricing page
dpa            | (none located)                               | no?    | no        | gather found no signable DPA - confirm and record exists:no
sla            | (none located)                               | no?    | no        | ToS disclaims uptime; no SLA located - confirm and record exists:no
```
