# Infercom - ISO 27001 certificate, CSA STAR listing, Trust Centre (read 2026-11-19)

## ISO/IEC 27001:2022 certificate (https://infercom.ai/iso-27001-certificate.pdf, HTTP 200, read)
Certificate No LU-IS-20250253, issued by Proks Certification GmbH (Dusseldorf; IAF multilateral arrangement and
DAkkS accreditation marks on the certificate). Certified company: INFERCOM SCS, 29 Boulevard Grande-Duchesse
Charlotte, 1331 Luxembourg, "%100 Remote Work". Scope: "AI & Cloud Infrastructure Services (Inference as a
Service) and the systems that support these services. SoA - 01.11.2025, Vers.2.04". "This certificate is valid
from 16.12.2025 to 15.12.2028." This is an independently issued attestation, read at source.

## CSA STAR registry (https://cloudsecurityalliance.org/star/registry/infercom/services/infercom-inference-as-a-service, read)
"Listed Since: 07/02/2026", "STAR for AI Level 1", "AI CAIQ Self-assessment v1.1.0", "Created or renewed ... July 02,
2026". Level 1 is a self-assessment by the provider, not an audit. Description field: "stateless, zero-retention,
TLS-encrypted" on "Infercom-owned SambaNova hardware at Equinix Munich MU4".

## Trust Centre (https://infercom.ai/trust/, server-rendered, read)
- "ISO 27001 certified. No persistent storage of prompts or outputs. On EU sovereign models, your data stays in
  the EU." Own racks: "SambaRack SN40L-16 systems, operated together with SambaNova".
- FAQ "Are you SOC 2 certified?": "Not yet. We are ISO 27001 certified". The Equinix MU4 facility holds "ISO 27001,
  ISO 22301, SOC 1 and SOC 2 Type II" (facility attestations, not Infercom's).
- FAQ "Who operates the infrastructure?": "Our compute infrastructure is operated by SambaNova under a managed
  services agreement. SambaNova is a US company with operational access to the Munich facility. This is disclosed in
  our DPA."
- "Data Jurisdiction EU law governs, no US parent company"; "Subprocessors Listed Listed in the DPA".
- "Do you support private connectivity? Not today". "TLS 1.3 supported, TLS 1.2 for older clients". "No prompt
  cache: the models we serve today process every prompt in full".
- Vulnerability reports: "Email dpo@infercom.ai" (no bug-bounty programme described).
- Marketing versus binding text: the docs and pricing pages say EU sovereign models carry "no US CLOUD Act
  exposure"; the binding Terms Sec 2.1 and DPA Sec 7 disclose a US operator (SambaNova) with remote administrative
  access under SCCs. Jurisdictional reach through the operator is not addressed in any binding document.
