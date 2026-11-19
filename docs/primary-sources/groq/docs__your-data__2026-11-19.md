# Groq - Your Data in GroqCloud (re-read 2026-11-19, verbatim extracts)

Source: https://console.groq.com/docs/your-data (HTTP 200, product documentation, not a contract).

- "By default, Groq does not retain customer data for inference requests."
- "Customer data (inputs, outputs, and related state) is only retained in two cases: If you use features
  that require data retention to function (e.g., batch jobs, fine-tuning and LoRAs). If needed to
  protect platform reliability (e.g., to troubleshoot system failures or investigate abuse)."
- Batch: "Input and output files retained for 30 days unless deleted earlier by the customer."
  Fine-tuning: "Model weights and training datasets retained until deleted by the customer."
- "We may temporarily log inputs and outputs only when: Troubleshooting errors that degrade platform
  reliability, or Investigating suspected abuse (e.g. rate-limit circumvention). These logs are
  retained for up to 30 days, unless legally required to retain longer. You may opt out of this storage
  in Data Controls settings".
- Summary table: Inference endpoints (chat/completions, responses, audio) - "System reliability and
  abuse monitoring - Up to 30 days - ZDR Eligible: Yes"; Batch - up to 30 days; Fine-tuning - until
  deleted (both "Yes (feature disabled)" under ZDR).
- "All customers may enable Zero Data Retention (ZDR) in Data Controls settings. When ZDR is enabled,
  Groq will not retain customer data for system reliability and abuse monitoring. ... features that
  rely on data retention to function will be disabled."
- "All customer data is retained in Google Cloud Platform (GCP) buckets located in the United States.
  ... Where applicable, Customers can rely on standard contractual clauses (SCCs) for transfers between
  third countries and the U.S."

Note for the entry: the docs describe up-to-30-day troubleshooting and abuse logs for inference unless
ZDR is on. Earlier passes described inference as simply "not retained by default". The Services
Agreement (Sec 4.2) allows access "to ensure the reliable operation of the Cloud Services or confirm
Customer's compliance with the AUP", which matches the docs.
