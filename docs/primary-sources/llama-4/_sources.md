# llama-4 - primary-source clauses (2026-08-03)

Split from the aggregate `meta-llama` primary-sources. This entry is Llama 4 (multimodal MoE);
the Llama 3.x text line remains the `meta-llama` entry. The Llama 4 licence/AUP clauses below are
carried verbatim from the aggregate `meta-llama/_sources.md` (retrieved 2026-07-25), read from
Meta's canonical GitHub mirror (llama.com is JS-rendered).

## _sources.md (index)
```
doc_type | source_url | retrieval_date | exists | retrieved | notes
license | llama.com/llama4/license/ (verbatim via GitHub mirror meta-llama/llama-models) | 2026-07-25 | yes | true | 700M-MAU; EU/multimodal clause in incorporated AUP
terms | llama.com/llama4/use-policy/ | 2026-07-25 | yes | true | contains the EU/multimodal clause
model_card | huggingface.co/meta-llama | 2026-07-25 | yes | true | llama4 licence tag; gated org; safetensors + checksums
```

## license Llama 4 Community License - VERBATIM
source_url: llama.com/llama4/license/ (via meta-llama/llama-models mirror) | exists: yes | retrieved: true
[2. 700M-MAU - VERBATIM] "Additional Commercial Terms. If, on the Llama 4 version release date, the monthly active users of the products or services made available by or for Licensee...is greater than 700 million monthly active users in the preceding calendar month, you must request a license from Meta, which Meta may grant to you in its sole discretion..." Plus "Built with Llama" attribution; California governing law. The EU/multimodal restriction lives in the incorporated AUP (below).

## terms Llama 4 AUP - EU/multimodal clause - VERBATIM
source_url: llama.com/llama4/use-policy/ | exists: yes | retrieved: true
[EU/multimodal - VERBATIM] "With respect to any multimodal models included in Llama 4, the rights granted under Section 1(a)...are not being granted to you if you are an individual domiciled in, or a company with a principal place of business in, the European Union. This restriction does not apply to end users of a product or service that incorporates any such multimodal models." Six prohibited-use categories (illegality/rights; death-or-bodily-harm incl. military/weapons/critical-infra; deception/fraud/impersonation; failure to disclose AI dangers; third-party unlawful tooling). Report: LlamaUseReport@meta.com.

## boundary (Llama 3.x is the meta-llama entry)
The Llama 3.1 AUP has NO EU/multimodal clause (and its models are text-only); 3.2/3.3 carry the clause but 3.3 is text-only so it is moot there. The EU carve-out only BITES on Llama 4 because Llama 4 is genuinely multimodal. Llama 3.x therefore stays the `meta-llama` entry; this entry is Llama 4 only. Large Llama 4 models (Maverick, Behemoth) exceed 1e25 FLOP (systemic-risk); Meta declined the EU GPAI Code of Practice.

## model_card - meta-llama org
source_url: huggingface.co/meta-llama | exists: yes | retrieved: true
Verified, access-gated org; Llama 4 tagged `llama4`; safetensors with checksums; hosted on Bedrock/Vertex/Together/Groq.
