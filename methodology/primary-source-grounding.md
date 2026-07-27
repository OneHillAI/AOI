# Primary-source grounding - the standard

The library exists to give an adopter documentation they can *rely on*. That only works if every
statement traces to a real primary document that was actually read. The failure to avoid: a
confident claim ("zero retention", "EU-sovereign", "adopt") built on a marketing page, that
collapses the moment someone asks "where does it say that?".

## The rule

**No claim without a receipt, and the receipt must be the right kind of document, actually read.**

- Every non-trivial statement in a documentation item maps to an `evidence[]` entry via `refs`.
- Each evidence entry declares **what kind of document** it is (`doc_type`) and **whether the
  document was actually retrieved and read** (`retrieved`).
- A *binding* document (`terms`, `privacy_policy`, `dpa`, `license`) or a `technical_report` /
  `model_card` outranks `marketing`. An independent `third_party` attestation is strong for
  claims a vendor cannot self-certify.
- `retrieved: false` means the document is known to exist but its text was not read. It may back
  only a **"documented but unverified"** statement, and the prose must say so in those words.

## `doc_type` vocabulary

`terms` · `privacy_policy` · `dpa` · `subprocessors` · `security` · `sla` · `model_card` ·
`license` · `technical_report` · `docs` · `marketing` · `third_party`.

The trust centre / landing page / blog post is `marketing`. The Privacy Policy, the DPA, the
Terms of Service, the LICENSE file are the binding documents that actually govern what happens.

## What the validator enforces (`scripts/validate.py check_grounding`)

For any entry that uses the `doc_type` vocabulary: a **dimension scored 5** must cite at least
one ref that is a **retrieved binding document** or a **third-party attestation**. Marketing or
an unread document cannot justify a top rating. The same expectation applies editorially to an
ownership factor rated **strong** on transparency or data-control.

## The document inventory

Per **inference provider**: Terms of Service · Privacy Policy · Data Processing Agreement (DPA) ·
sub-processor list · Security / Trust page · SLA / status page · pricing · API/developer docs.

Per **model**: model card(s) · LICENSE (per variant) · technical report / paper · acceptable-use
/ usage policy · repository README · published evaluations.

## Retrieval, and its limits in a locked-down session

Outbound web access from a coding session is governed by the org egress proxy, which blocks many
hosts (e.g. `huggingface.co`) and the environment forbids routing around it; some sites also
return 403 to the fetch tool. The working routes, in order:

1. **WebFetch** the primary document URL.
2. When that is blocked, **WebSearch** scoped to the document's domain/URL to extract its indexed
   text, corroborated across several targeted queries.
3. If neither yields the actual text, mark the evidence `retrieved: false` and say "unverified" -
   then a coworker supplies the document (see [`docs/primary-doc-handover.md`](../docs/primary-doc-handover.md))
   and the entry is re-grounded, flipping `retrieved: false → true` with real citations.

The test every entry must pass: **pick any high rating and ask "which primary document, read,
says so?" - there is a concrete answer, or the rating is not high.**
