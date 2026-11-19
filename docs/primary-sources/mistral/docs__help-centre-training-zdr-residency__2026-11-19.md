# Mistral help centre - training, data location and Zero Data Retention (re-read 2026-11-19)

- **doc_type:** docs
- **source_urls:** https://help.mistral.ai/en/articles/347617-do-you-use-my-user-data-to-train-your-artificial-intelligence-models ; https://help.mistral.ai/en/articles/347629-where-do-you-store-my-data-or-my-organisation-s-data ; https://help.mistral.ai/en/articles/347612-can-i-activate-zero-data-retention-zdr ; https://help.mistral.ai/en/articles/347628-how-long-do-you-store-my-data
- **retrieval_date:** 2026-11-19
- **exists:** yes
- **retrieved:** true (page text, HTTP 200; pages show "Updated today", article 347628 shows August 12, 2026)

## Training (article 347617)

"Exception for Labs and Public Preview models: the training opt-out does not apply to Labs and Public Preview models, whichever subscription plan you adhere to. When using these models, your data may be used for training, and cannot be excluded via the opt-out controls."
[Vibe (Free, Pro, Teams, Student)] "Input and output data are used by default to train our artificial intelligence models, unless you opt out of training at any time."
[Vibe (Enterprise)] "Enterprise customers are opted out of training by default. The opt-in toggle is managed at the admin level."
[User feedback] thumbs up or down with a comment "authorize us to use your rating, your input and output".
[Mistral Studio, Free mode] "we may use your data (input and output) to train our artificial intelligence models" with a right to opt out.
[Mistral Studio, Pay-as-you-go] "Customers retain full control over this processing and have the right to opt out at any time." The page does not state the pay-as-you-go default.

## Data location (article 347629)

"By default, your data is hosted in the European Economic Area (EEA). You may, however, explicitly use our US API endpoint, in which case your inference requests are processed in the United States." Some features transfer data outside the EU to the Trust Center sub-processor locations, under GDPR Article 46 safeguards (Standard Contractual Clauses where there is no adequacy decision). Enterprise customers can deactivate some non-EU-transfer features at organisation level.

## Zero Data Retention (article 347612)

"Zero Data Retention (ZDR) is available only with pay-as-you-go and only for stateless API calls." "ZDR is not available for Vibe Work, Chat, libraries, agents, conversations, batch files, or other stateful products." Covered endpoints: /v1/chat/completions, /v1/fim/completions, /v1/embeddings, moderation and classification endpoints, /v1/ocr, /v1/audio/speech, /v1/audio/transcriptions. "ZDR applies to the endpoints listed above across models, except Labs and Public Preview models." Request process: "we will review your request and, at our discretion, approve or deny it." "We cannot sign the DPA offline."

## Retention (article 347628)

Covers account, billing and technical data (for example civil identity data for 5 years after the end of the user contract; technical data for one rolling year). It does not state an API input and output period; that is in the Privacy Policy section 5.

## Differences from the 2026-07-25 reading

- Teams is no longer excepted from default training on Vibe; only Enterprise is opted out by default (the earlier reading said "Team and Enterprise").
- Labs and Public Preview models are outside both the training opt-out and ZDR.
- ZDR is restricted to pay-as-you-go stateless endpoints and is approved at Mistral's discretion, not simply "activated for eligible accounts".
- Article 347629 no longer states the 30-day API retention (it now only covers location); the retention period is cited from the Privacy Policy.
