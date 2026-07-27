# The AI Ownership Index Standard

Version 0.1 (draft). Stewarded by the OneHill Foundation. Contact: dev@onehill.org.

## Purpose

The AI Ownership Index rates open-weight language models and the inference providers that
serve them on how open, well governed, and trustworthy they are. Every rating must trace
to a primary document that was actually read, not a marketing page. This file defines the
standard the Index is built to; CONFORMANCE.md defines how an entry proves it meets the
standard.

## Scope

Two entity types are in scope:

1. Models: open-weight model families and their checkpoints.
2. Inference providers: services that host and serve those models over an API.

Closed frontier models and hosted-only assistants are out of scope for this version and
are listed as deferred.

## Grounding requirement (the core rule)

Every claim in an entry must be backed by a primary document. A primary document is the
binding text itself: a licence file, Terms of Service, Privacy Policy, Data Processing
Addendum, model card, technical report, or an official sub-processor or trust page. A
trust-centre summary or a blog post is not sufficient on its own to justify a top rating.

Each piece of evidence carries two auditable fields:

- doc_type: one of terms, privacy_policy, dpa, subprocessors, security, sla, model_card,
  license, technical_report, docs, marketing, third_party.
- retrieved: true only if the document's substantive clause text was actually read; false
  if the document is known to exist but was not reachable. A retrieved:false item may
  support only a "documented but unverified" statement in the prose.

A missing document is itself a finding. Where no DPA, SLA, or licence file exists, the
entry records exists:no rather than leaving the point unstated.

## Scoring dimensions

Each entry scores a small set of dimensions on a 1 to 5 scale. The binding doc-types
(terms, privacy_policy, dpa, license) are the only evidence that can justify a score of 5;
a third-party attestation can also support a 5 for a security dimension. Any dimension
scored 5 must cite at least one retrieved binding document or third-party attestation, or
validation fails.

Models use the seven-dimension AI Ownership Index (AOI): openness and transparency,
provenance and supply-chain integrity, legal and regulatory readiness, safety and alignment,
technical performance, operational readiness, and maintenance and governance. Inference
providers use a provider-appropriate set: data governance, compliance, residency, security,
reliability, transparency and lock-in, and cost. The 0-to-100 headline and its letter grade
(A 85+, B 70 to 84, C 55 to 69, D 40 to 54, F below 40) are derived from the dimensions.

## Assessed signals

Model entries also carry five cross-cutting signals, each tied to one scoring dimension:
train and tune, knowledge and structure, specialisation, exchangeability, and misuse and
exposure. Provider entries carry an equivalent posture set focused on the customer-data
question: retention, training on inputs, data and IP ownership, sovereignty, and portability.

## Ownership factors

Entries record four ownership factors, each with a rationale grounded in the read text:
use_modify, transparency, reliability, and data_control. For a model these read against the
weights (can you run, fine-tune, adjust and specialise it); for a provider they read against
your data (retention, training, ownership, and exit). The overall verdict is recomputed
whenever the underlying clauses change.

## Conformance levels

An entry is Grounded when every strong rating traces to a retrieved binding document, and
Provisional when one or more strong ratings still rest on retrieved:false evidence. The
Index as a whole is Grounded when every published entry is Grounded.

## Versioning

This standard uses semantic versioning. Breaking changes to the dimension set, the doc_type
vocabulary, or the grounding gate increment the major version.
