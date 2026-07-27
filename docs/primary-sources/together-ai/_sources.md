# together-ai - primary-source clauses

**SCAFFOLD - no clause files gathered here yet.** This manifest is the outstanding-document
checklist for the Cowork/browser gather pass (see
[`../../provider-primary-doc-handover.md`](../../provider-primary-doc-handover.md), Together AI
section). Rows marked `retrieved: no` still need the verbatim governing text pasted into a
`<doc_type>__<detail?>__<YYYY-MM-DD>.md` file here. Rows marked `retrieved: yes` are already
grounded in `inference-providers/together-ai/entry.yaml`.

## _sources.md
```
doc_type       | url                                                                 | exists | retrieved | notes
terms          | https://www.together.ai/terms-of-service                            | yes    | yes       | ev7 - "you exclusively own all right, title and interest in Your Content and Output"; no training without explicit opt-in
privacy_policy | https://www.together.ai/privacy                                     | yes    | yes       | ev1 - ZDR by default
dpa            | https://cdn.prod.website-files.com/…/Together%20DPA%20(Website).pdf  | yes    | yes       | ev9 - EU SCCs + UK Addendum
docs           | https://docs.together.ai/docs/privacy-and-security                  | yes    | yes       | ev2 - security docs
docs           | https://support.together.ai/articles/8079447813-eu-data-centers…    | yes    | yes       | ev4 - EU data centers / dedicated deployment
subprocessors  | https://trust.together.ai/                                          | yes    | no        | NO evidence item yet - OUTSTANDING. Capture the ~33 named sub-processors + regions (US/CA/RO/EU/Global). Note especially the AI sub-processors (Anthropic, OpenAI, Perplexity, OpenRouter) - inference can route to third-party model APIs, a real residency/ownership finding
marketing      | https://www.together.ai/pricing                                     | yes    | no        | ev5 - pricing page
security       | (SOC 2 Type II report itself)                                       | no     | no        | only the announcement blog (ev3) is public; the report itself is not - record exists:no for the report. ZDR separately confirmed
```
