# Groq - Services Agreement, DPA, BAA and AUP (re-read 2026-11-19, verbatim extracts)

Sources (all HTTP 200, server-rendered, read by curl and text conversion):
- https://console.groq.com/docs/legal/services-agreement - "Last Modified: June 22, 2026" (unchanged
  from the version read on 2026-08-06 and 2026-09-21; archived versions listed: October 15, 2025)
- https://console.groq.com/docs/legal/customer-data-processing-addendum - "Effective: October 15, 2025"
- https://console.groq.com/docs/legal/customer-business-associate-addendum
- https://console.groq.com/docs/legal/ai-policy - "Effective: October 15, 2025" (read for the first time
  in this folder; ev-aup is now retrieved)
- https://groq.com/privacy-policy "effective on November 12, 2025"; https://groq.com/terms-of-use
  "effective on October 15, 2025" (website documents, not the API contract)

Result: no clause changed since the 2026-09-21 re-read. The "Eligible Customers" ZDR gap persists.

## Services Agreement Sec 4.2 Inputs and Outputs (verbatim)

"Groq does not access, use, store, or retain Inputs or Outputs except as necessary to provide the
Cloud Services, in accordance with the Customer's permission or instruction, comply with applicable
law, ensure the reliable operation of the Cloud Services, or confirm Customer's compliance with the
AUP. Eligible Customers may enable Groq's zero data retention setting in the Console to prevent
access by Groq to Inputs and Outputs for the purposes of ensuring reliable operation of the Cloud
Services or compliance with the AUP. For clarity, Groq is not permitted to use Inputs or Outputs for
training or fine-tuning any AI Model Services or other models, unless explicitly granted permission or
instructed by Customer."
("Eligible Customers" is not defined in the Services Agreement or the DPA. The your-data docs say "All
customers may enable Zero Data Retention".)

## Definitions (verbatim)

- "Confidential Information ... Subject to the preceding sentence, Customer Data is considered
  Customer's Confidential Information."
- "Customer Data means data provided to Groq by Customer or Authorized Users through the Cloud Services
  under the Account, and data that Customer or Authorized Users derive from that data". "Inputs are
  Customer Data." "Outputs are Customer Data."
- "Groq Contracting Party means (a) Groq LLC for Customers domiciled outside the European Economic
  Area, Switzerland, or the Kingdom of Saudi Arabia; (b) Groq UK Limited for Customers domiciled in the
  European Economic Area or Switzerland; (c) Groq Limited for Customers domiciled in the Kingdom of
  Saudi Arabia; and (d) Groq Public Sector, LLC if designated on the Order Form."

## Sec 10.1 Confidentiality obligations (verbatim, unchanged)

"The recipient will only use the disclosing party's Confidential Information to exercise the
recipient's rights and fulfill its obligations under this Agreement and will use reasonable care to
protect against the disclosure of the disclosing party's Confidential Information. The recipient may
disclose Confidential Information only to its and its Affiliates' employees, agents, subcontractors,
or professional advisors ("Representatives") who need to know it and who have agreed in writing ... to
obligations of confidentiality at least as protective as those provided in this Agreement."

## Other clauses (verbatim)

- Sec 4.1: "Groq may share information, that does not include Customer Data, about your use of an AI
  Model Service that is a Third-Party Offering with the developer, publisher, or provider of that AI
  Model Service." Sec 3.7: Third-Party Offerings "are not Cloud Services provided by Groq and may be
  subject to additional separate terms".
- Sec 4.4: "Groq may deprecate the AI Model Services at any time and will use commercially reasonable
  efforts to provide Customer with reasonable prior notice".
- Sec 8.2: "Groq will not use such Customer Training Data other than to provide the Cloud Services to
  Customer." Sec 8.3: "Feedback may be used by the receiving party without any restriction, obligation,
  or compensation".
- Sec 11.5: Groq will delete Customer Data "in its systems within 30 days" after termination "unless
  otherwise described in this Agreement or the Order Form or if Groq is required to retain any such
  information under applicable law".
- Sec 14.2: liability capped at fees paid in the prior 12 months, "EXCEPT GROQ'S TOTAL AGGREGATE
  LIABILITY ... RELATED TO BETA SERVICES AND ANY CLOUD SERVICES PROVIDED FREE OF CHARGE IS LIMITED TO
  $5,000."
- Sec 5.6 and the definition of URL Terms refer to "Service Credit Terms" and "any service level
  agreements or commitments"; no public SLA exists. A paid "service level commitments" add-on is
  mentioned in the support paragraph.

## DPA (Effective October 15, 2025; verbatim extracts)

- 7.2: "Groq's Subprocessor list is available at https://trust.groq.com/subprocessors ... Groq will notify
  Customer of any changes ... at least 15 days before the changes take effect" for customers who
  subscribe to notifications; objection within 15 days.
- 8.1: "Groq may transfer and Process Personal Data to and in the United States and other countries where
  Groq or its Subprocessors maintain Processing operations."
- 8.2: EU SCCs (Modules 2 and 3), UK Addendum and Swiss FADP terms are deemed signed on entering the
  Agreement; Annex III is "completed by the information available at https://trust.groq.com/subprocessors".
- Deletion on request "within a maximum period of 180 days" before or at termination, backups isolated.
- Annex II: ZTNA for backend resources, vendor security assessments for subprocessors, regular security
  and vulnerability testing; points to the trust centre for the full measures.
No region-pinning or EU-only processing clause appears.

## BAA (Effective October 15, 2025)

Supplements the Services Agreement; Groq acts as business associate or subcontractor for PHI "to the
extent Customer is a covered entity or business associate". "Covered Cloud Services" excludes "Beta
Services and any features, products, or services that are not generally available, in alpha, beta,
pre-production, preview, demo, trial stage" (so preview models such as Qwen3.8-27B are outside the BAA).
The 2026-07-25 read recorded a Compound exclusion; that system was shut down on 2026-09-21.

## AUP (Effective October 15, 2025)

Prohibits use beyond rate limits, illegal or harmful use, automated high-risk decisions without human
supervision, malware, and lethal weapon functions without human control, among others. No data-use
clause beyond the Services Agreement.
