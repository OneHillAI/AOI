# Ollama - Privacy Policy (read 2026-11-19, verbatim extracts)

Source: https://ollama.com/privacy (HTTP 200, read in full). Page states: "Last updated: March 2026".
Controller: "Ollama Inc. is the data controller of this Privacy Policy." Contact: hello@ollama.com.

## Summary box (verbatim)
"Ollama runs locally. We don't see your prompts or data when you run locally. When using cloud-hosted models,
we process your prompts and responses transiently to provide the service and never train on it. We collect
basic account info and limited usage metadata that does not include prompt or response content. We don't sell
your data. You can delete your account anytime."

## Sec 2 How Ollama Works (verbatim, the binding text for cloud models)
"When using cloud-hosted models, we process this content transiently to provide the Service and this content
is not stored beyond the time required to fulfill the request. We implement technical measures designed to
minimize retention of prompt and response content. We do not use your inputs or outputs to train any AI models
or request prompt or response content in support requests. If you voluntarily include such content in support
requests, it will be handled solely to resolve your issue and not used for training."

## Sec 3 Information collected automatically (verbatim list items)
"Diagnostic metadata for troubleshooting (does not include prompt or response content)"; "IP address and
general location"; "Model download metadata".

## Sec 5 Information Sharing (verbatim)
"To provide you the Service: Third parties who help us operate (e.g., Stripe for payments, cloud
infrastructure providers, model inference providers)."
"Data may be transferred to and processed in the United States. Where required by law, we use appropriate
safeguards for international transfers."

## Sec 6 Data Retention (verbatim)
"We retain your information for as long as your account is active or as needed to provide the Service."
Metadata and analytics: "retained as needed for service operations, security, and improvement, then deleted or
de-identified." No numeric retention window is stated for any category.

## Marketing versus binding text (reported, not reconciled)
- Binding Privacy Policy: prompts "not stored beyond the time required to fulfill the request" and "technical
  measures designed to minimize retention". This is a minimisation commitment with a hedge.
- Cloud FAQ (docs.ollama.com/cloud/faq) says "Ollama operates with a zero data retention (ZDR) policy" and
  "does not store or log that content". Pricing-page FAQ says "Prompt or response data is never logged or
  trained on." These are stronger than the Privacy Policy wording. The Privacy Policy, Terms and docs name no
  ZDR agreement and no audit.
- No DPA, no SCC/DPF reference, no sub-processor list and no certification (SOC 2, ISO 27001) was found in the
  Terms, Privacy Policy, docs or pricing page. ollama.com/security returns HTTP 404.
