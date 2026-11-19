doc_type: license
entity: nemotron-3
variant/applies-to: NVIDIA Nemotron Open Model License (v. December 15, 2025). Governs Nemotron 3 Super and Nano (card tag nvidia-nemotron-open-model-license).
source_url: https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-nemotron-open-model-license/ ; PDF https://www.nvidia.com/content/dam/en-zz/Solutions/license-agreements/enterprise-software/NVIDIA-Nemotron-Open-Model-License-12-12-25.pdf
document_effective_date: Last Modified December 15, 2025 (unchanged since the 2026-08-03 read)
retrieval_date: 2026-11-19
exists: yes
retrieved: true
tag: publisher

## Result of the re-read
The HTML page text was read in full on 2026-11-19. The 10 sections and the grant, termination, redistribution
and governing-law text are word-for-word the text stored in license__nvidia-nemotron-open-model-license__2026-08-03.md.
No revision. No acceptable-use, Trustworthy-AI, guardrail or revocation clause exists. Section 10 (Trade and
Compliance) is an export and sanctions compliance duty, not a use restriction.

## Governing clauses (VERBATIM)
[2 Grant of License] "Subject to the terms and conditions of this License, NVIDIA hereby grants to You a perpetual,
worldwide, non-exclusive, no-charge, royalty-free, irrevocable license to reproduce, prepare Derivative Works of,
publicly display, publicly perform, sublicense, and distribute the Work and such Derivative Works in source or object form."

[2 Termination, the only trigger] "If You institute patent or copyright litigation against any entity (including a
cross-claim or counterclaim in a lawsuit) alleging that the Work or an output from the Work constitutes direct or
contributory patent or copyright infringement, then any licenses granted to You under this License for that Work shall
terminate as of the date such litigation is filed."

[7 Accepting Warranty or Additional Liability, last sentence] "You will indemnify and hold harmless NVIDIA from and
against any claim by any third party arising out of or related to your use or distribution of the Works, Derivative
Works thereof, or output from the Works or Derivative Works."
Note: this indemnity sentence is general in form (it is not limited to the warranty case in the preceding sentence). It
is a liability term, not a use restriction and not a termination trigger. It was not recorded in the 2026-08-03 extract.

[10 Trade and Compliance] "You agree to comply with all applicable export, import, trade and economic sanctions laws and
regulations ... These laws include restrictions on destinations, end-users and end-use."

## Contrast: the generic NVIDIA Open Model License (NOT the licence that governs this entry)
https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/ (Last Modified October 24, 2025) still
carries the terms that Nemotron OML lacks: "If You bypass, disable, reduce the efficacy of, or circumvent any technical
limitation, safety guardrail ... your rights under this Agreement will automatically terminate", a licence "revocable (as
stated in Section 2.1)", and "AI Ethics. Use of the Models under the Agreement must be consistent with NVIDIA's Trustworthy
AI terms".

## Marketing-versus-binding contradiction found on the Nano card (unresolved, report only)
The Nano repo subcard https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16/blob/main/safety.md (read
2026-11-19) says under "Use Case Restrictions": "Abide by the [NVIDIA Open Model License Agreement]" and links
.../nvidia-open-model-license/ , that is, the generic revocable licence above. The same repo's HF licence tag
(nvidia-nemotron-open-model-license), its license_link, and its README line "Governing Terms: Use of this model is
governed by the [NVIDIA Nemotron Open Model License]" all point to the Nemotron OML, and the README badge reads
"NVIDIA Open Model License" but links the Nemotron URL. The Super safety.md says "Abide by the [NVIDIA Nemotron Open Model
License Agreement]" with the correct link. The README Governing Terms line and licence tag are treated as governing; the
Nano safety.md link is a probable wrong link on the card, and is recorded as a residual ambiguity.

## Non-binding advisory on the cards
Super, Nano (and Ultra, Omni) READMEs carry: "We advise against circumvention of any provided safety guardrails contained
in the Model without a substantially similar guardrail appropriate for your use case." This is advice, not a licence term:
the Nemotron OML grant has no guardrail clause.
