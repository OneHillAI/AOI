# together-ai - primary-source clauses

**UPDATE 2026-09-21:** this manifest predates the confidentiality-disclaimed finding and the
independent Cowork verification pass - see [`browser-verified/`](browser-verified/) for the
current, re-verified capture. Superseded row: line 14 below claimed "ZDR by default"; this is
corrected - ZDR is account-level opt-in (Privacy Policy Sec 2.6, independently re-read verbatim
2026-09-21). The DPA sub-processor list (line 18's "OUTSTANDING ~33 names") is now confirmed:
Annex III names 9 entities, including OpenAI OpCo LLC (see `browser-verified/terms-privacy-dpa__2026-09-20.md`).

**SCAFFOLD - no clause files gathered here yet [as of the original pass].** This manifest was
the outstanding-document checklist for the Cowork/browser gather pass (see
[`../../provider-primary-doc-handover.md`](../../provider-primary-doc-handover.md), Together AI
section). Rows marked `retrieved: no` still need the verbatim governing text pasted into a
`<doc_type>__<detail?>__<YYYY-MM-DD>.md` file here. Rows marked `retrieved: yes` are already
grounded in `inference-providers/together-ai/entry.yaml`.

## _sources.md
```
doc_type       | url                                                                 | exists | retrieved | notes
terms          | https://www.together.ai/terms-of-service                            | yes    | yes       | ev7 - "you exclusively own all right, title and interest in Your Content and Output"; no training without explicit opt-in
privacy_policy | https://www.together.ai/privacy                                     | yes    | yes       | ev1 - CORRECTED 2026-09-21: ZDR is account-level OPT-IN (Sec 2.6, independently re-read verbatim), NOT "by default" as this row previously said.
dpa            | https://cdn.prod.website-files.com/…/Together%20DPA%20(Website).pdf  | yes    | yes       | ev9 - EU SCCs + UK Addendum. Annex III now confirmed: 9 named sub-processors incl. OpenAI OpCo LLC (see browser-verified/).
docs           | https://docs.together.ai/docs/privacy-and-security                  | yes    | yes       | ev2 - security docs
docs           | https://support.together.ai/articles/8079447813-eu-data-centers…    | yes    | yes       | ev4 - EU data centers / dedicated deployment
subprocessors  | https://trust.together.ai/                                          | yes    | no        | JS-gated, unreadable (confirmed again 2026-09-21). The DPA's own Annex III (9 names, not ~33) is the actually-confirmed sub-processor source - see dpa row above.
marketing      | https://www.together.ai/pricing                                     | yes    | yes       | ev5 - pricing page (re-verified live 2026-09-20/21)
security       | (SOC 2 Type II report itself)                                       | no     | no        | only the announcement blog (ev3, confirmed 2025-07-08, auditor unnamed) is public; the report itself is not.
```
