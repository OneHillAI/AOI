# Conformance

Version 0.1 (draft). Contact: dev@onehill.org.

This file defines how an entry proves it meets the AI Ownership Index Standard (see
STANDARD.md). Conformance is checked by scripts/validate.py and enforced in continuous
integration.

## Evidence rules

1. Every evidence item has a doc_type and a retrieved field.
2. retrieved:true requires that the document's substantive clause text was read and that a
   short verbatim extract of the governing clause is stored, with the source URL and the
   retrieval date.
3. The primary source clauses live under docs/primary-sources/<entity-id>/, one file per
   document, named <doc_type>__<detail?>__<YYYY-MM-DD>.md, logged in that folder's
   _sources.md.
4. A document that is real but could not be read is recorded exists:yes, retrieved:false
   with the reason. A document that does not exist is recorded exists:no. Neither is left
   blank.

## The grounding gate

Any dimension with a score of 5 must list an evidence_ref that is either a retrieved
binding document (terms, privacy_policy, dpa, license) or a third-party attestation
(third_party). validate.py fails the build otherwise. This is the check that stops a strong
rating from resting on a marketing page.

## The test every finished entry must pass

Pick any strong rating and ask: which primary document, read, says so? There must be a
concrete answer that points at a retrieved clause file.

## Running the checks

    python scripts/validate.py models inference-providers   # must report 0 errors
    cd site && npm run build                                 # must complete cleanly

## The loop

When a new primary document lands under docs/primary-sources/, a maintainer or code session
rewrites the affected entry from the read text with exact citations, flips the matching
evidence to retrieved:true, recomputes the verdict, and notes the change in CHANGELOG.md.
