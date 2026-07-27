# meta-llama - primary-source clauses (2026-07-25)

## _sources.md
```
license | llama.com/llama4/license/ (verbatim via GitHub mirror meta-llama/llama-models) | yes | true | 700M-MAU; EU/multimodal clause in incorporated AUP
license | llama.com/llama3_1|3_2|3_3/license/ | yes | true | 3.1/3.2/3.3 bodies identical; 700M-MAU; no EU clause in body
terms | llama.com/llama4/use-policy/ | yes | true | contains EU/multimodal clause
terms | llama.com/llama3_2|3_3/use-policy/ | yes | true | 3.2/3.3 identical; EU clause present
terms | llama.com/llama3_1/use-policy/ | yes | true | 3.1 differs; no EU clause
terms | llama.com/responsible-use-guide/ | yes | true | 302 -> developer.meta.com; existence-confirmation only
model_card | huggingface.co/meta-llama | yes | true | license tags per version (via summarizer; HF not raw-reachable in gathering pass)
```

## license Llama 4
[2. 700M-MAU - VERBATIM] "Additional Commercial Terms. If, on the Llama 4 version release date, the monthly active users of the products or services made available by or for Licensee...is greater than 700 million monthly active users in the preceding calendar month, you must request a license from Meta, which Meta may grant to you in its sole discretion..."

[EU/multimodal - VERBATIM, in incorporated AUP] "With respect to any multimodal models included in Llama 4, the rights granted under Section 1(a)...are not being granted to you if you are an individual domiciled in, or a company with a principal place of business in, the European Union. This restriction does not apply to end users of a product or service that incorporates any such multimodal models."

[1.b.i] display "Built with Llama"; prefix derived model names with "Llama". [7] California law.

## license 3.1/3.2/3.3 (identical bodies; deduped)
[2. 700M-MAU] identical verbatim clause as above with "Llama [X]". NO EU clause in the license body (that lives in the AUP for 3.2/3.3 only). California law.

## terms - Llama 4 AUP
Six prohibited-use categories (illegality/rights; death-or-bodily-harm incl. military/weapons/critical-infra; deception/fraud/impersonation; failure to disclose AI dangers; third-party unlawful tooling). EU/multimodal clause present (verbatim above). Report: LlamaUseReport@meta.com.

## terms - 3.2/3.3 AUP (identical; deduped)
EU/multimodal clause present verbatim. FLAG: 3.3 is text-only yet carries the multimodal clause - likely shared-template boilerplate.

## terms - 3.1 AUP
NO EU/multimodal clause; NO third-party-tools item (differs from 3.2/3.3).

## model_card license tags
Llama 4 = `llama4`; 3.3 = `llama3.3`; 3.2 = `llama3.2` (card echoes EU clause); 3.1 = `llama3.1`. CAVEAT: tags via summarizer; governing text is from Meta's GitHub mirror.
