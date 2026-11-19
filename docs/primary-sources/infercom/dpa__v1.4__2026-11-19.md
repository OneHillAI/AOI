# Infercom - Data Processing Agreement v1.4 (24 September 2026), read 2026-11-19

Source: https://infercom.ai/Infercom_DPA_v1.4_dl.pdf (HTTP 200, 8 pages, 132 KB; linked from the Trust Centre and
the site footer as infercom.ai/dpa). Text extracted locally with macOS PDFKit. This is the first full read of the
DPA: the stored entry rested on v1.3 (4 March 2026), whose PDF was unreadable. Verbatim extracts:

- Sec 1(1): "Inference processing of Prompts and outputs takes place exclusively within the European Union. Any remote
  administration, support or other access from outside the EU/EEA is subject to Section 7a ... Models whose
  inference is not hosted within the EU/EEA ('Non-EU Models') are not covered by this Agreement. Their use
  requires a separate written addendum that sets out the sub-processors involved, the transfer mechanism under
  Chapter V GDPR and the associated safeguards."
- Sec 2(1): "No training: the Processor does not use Prompts, inputs or outputs to train, retrain, fine-tune or
  otherwise improve models, and does not permit its sub-processors to do so." "No storage of content ... processed
  in memory and are not written to persistent storage ... Personnel of the Processor do not have access to the
  content of Prompts or outputs in the ordinary course." "The Processor does not route inference requests to
  infrastructure outside the EU/EEA, including for fallback, overflow or load-balancing purposes." Remote access by
  a sub-processor "limited to account identifiers and technical metadata".
- Sec 2a(4): "The Controller shall use the Service only with EU-hosted models as designated in the Processor's
  service documentation, unless a separate addendum ... has been concluded for Non-EU Models."
- Sec 5(1)(b): personnel committed to confidentiality "in text form" (an Art. 28(3)(b) personal-data duty, not a
  confidentiality clause over trade secrets).
- Sec 6: remote-first organisation; remote work permitted without separate consent subject to Annex 1 standards.
- Sec 7(2) sub-processors consented to: SambaNova Systems, Inc. (San Jose, US; "Managed operation and remote
  administration of the EU-hosted AI inference platform (SambaManaged)"; account e-mail addresses and API request
  metadata; "Prompts and outputs are not transferred to the United States"; SCCs Module Three); Google Ireland Ltd
  (internal e-mail, calendar, documents); Pipedrive OU (CRM); Stripe Payments Europe Ltd; TECLIB SAS (GLPI ticketing).
  Changes need 14 days' notice with a 14-day objection right. Further sub-processors of SambaNova are in "Annex III
  of the sub-processing agreement" and available on request.
  NOTE: Auth0 and Metronome (named in the Privacy Statement v2.4) are NOT in this table; Google Ireland and
  Pipedrive (named here) are not in the Privacy Statement sub-processor table. The two lists do not match.
- Sec 7a(3)-(5): SambaNova remote access relies on SCCs Module Three; a Transfer Impact Assessment is available on
  request; supplementary measures include no transfer of content data, logging of all remote access, and
  contractual duties "to review and challenge disclosure requests by third-country public authorities".
- Sec 9(1)(b): breach notification "at the latest within 48 hours".
- Sec 11(4): content data "not retained"; API request metadata and logs up to 90 days; authentication logs up to 12
  months. Sec 11(5): deletion within 30 days of termination.
- Sec 13: liability under Art. 82 GDPR. Sec 14: Luxembourg law, Luxembourg City courts. Sec 15(1): third-party
  seizure or insolvency to be notified; "responsibility for and ownership of the data rest exclusively with the
  Controller".
- Annex 1: TLS 1.2 or higher in transit; stateless in-memory processing; multi-tenancy with "hardware-level
  sandboxing within the AI accelerators"; MFA; least privilege; DDoS protection; automated failover; physical
  security supplied by the infrastructure sub-processor at the EU data centre.
- Document history: v1.4 "Scope clarified: inference exclusively on EU-hosted infrastructure; Non-EU Models only by
  separate addendum"; breach notice now 48 hours; SCC Module Three added; "no fallback routing outside the EU".
- Not stated anywhere in the DPA: any CLOUD Act statement. The operator of the platform (SambaNova) is a US company
  with remote administrative access.
