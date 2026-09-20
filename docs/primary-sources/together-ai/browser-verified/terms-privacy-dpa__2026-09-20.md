doc_type: terms (+ privacy, dpa, subprocessors)
entity: together-ai
source_url: https://www.together.ai/terms-of-service ; https://www.together.ai/privacy ; Together DPA (Website).pdf
document_effective_date: ToS Updated 2026-05-19; Privacy Last Updated 2025-12-17
retrieval_date: 2026-09-20
exists: yes
retrieved: true
tag: publisher

## THE CAP-SETTING FINDING - Sec 9 Confidentiality (Q1) - CONFIRMED UNCHANGED (VERBATIM x2)
[Sec 9 "Confidentiality" - VERBATIM] "The parties will have no confidentiality obligations to each other unless otherwise agreed in writing."
Section title is literally "Confidentiality." Still present, still expressly DISCLAIMS. Confirmed identical on two independent live fetches of the current (Updated 2026-05-19) ToS. It has NOT moved or been reworded.
=> confidentiality = disclaimed. This CAPS the data-governance dimension at 3 regardless of retention/training terms. The cap remains justified.

## Other ToS clauses (VERBATIM)
[Sec 3 "Your Content" - retention/training] "Under ZDR, your data and outputs are not stored, retained, or used for model training, product improvements, or any other purpose beyond the time required to process the specific request or transaction." (ZDR applies only when the customer ENABLES Zero Data Retention - i.e. opt-in.)
[Sec 7 IP - ownership] "As between you and Company, you exclusively own all right, title, and interest in Your Content and Output." ; "You grant Company a limited license to access, host, use, copy, and otherwise operate Your Content and Output solely as necessary to provide the Services."
[Governing law] "This Agreement will be governed by the laws of the State of California ..." (sub-section number uncertain between fetches; California law reliable).
[Sec 13 Liability] "Either party will not be liable ... for (a) any indirect, special, incidental, consequential, or punitive damages ... or (b) any aggregate liability in excess of the amounts paid by customer during the twelve (12) months preceding the claim."

## Privacy Policy (VERBATIM)
[Training - opt-in, default OFF] "We do not use any data collected from you to train our models without your explicit opt-in and consent. You may revoke that consent at any time and request deletion..." (Sec 2.2: "... will not be used to train the Company's models without your explicit opt-in and consent.")
[Retention Sec 2.4] "The Company will retain your Personal Data only for as long as is necessary for the purposes set out in this Policy."
[ZDR Sec 2.6] "By choosing 'No', you are enabling Zero Data Retention ('ZDR') ... the content you submit ... are not stored, retained, or used for model training, product improvements, or any secondary purposes except as needed to provide the Services to you."

## DPA + sub-processors
DPA is a linked PDF (together.ai/legal/dpa 404s; PDF at cdn.prod.website-files.com/.../Together DPA (Website).pdf). Incorporates EU SCCs + UK Addendum + GDPR/UK GDPR. No effective/execution date visible.
[Conflict clause] "In case of any conflict between this Addendum and the Master Agreement, this Addendum shall prevail with regard to the Processing of Personal Data covered by it."
[Annex III sub-processors - named] Amazon Web Services (US); Mailgun Technologies (US); Amplitude (US); Functional Software/Sentry (US); OpenAI OpCo, LLC (US); Together Software Inc. (Canada); Hotjar Ltd (Malta); Intercom (US); Absorb Software (Canada/USA/UK/EU/Australia). NOTE: OpenAI named as a sub-processor.

## Net data-governance posture
Retention: not stored ONLY if customer enables ZDR (opt-in); otherwise standard processing. Training: only with explicit opt-in (never by default). Ownership: customer owns content + output. BUT confidentiality expressly DISCLAIMED (Sec 9) => data_governance capped at 3. This is the entry's key ceiling and it is grounded verbatim.
