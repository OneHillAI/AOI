# model_card / base-apertus-instruct-2509

source_url: https://huggingface.co/swiss-ai/Apertus-70B-Instruct-2509/raw/main/README.md
retrieval_date: 2026-11-19
retrieved_by: curl, text read in full or in the extracts marked below
note: Base model card for the Apertus-based MeditronFO checkpoints (the 8B card is identical apart from the model name, checked with diff). Extracts: front matter with the gate prompt, summary, Limitations, Legal Aspects. Plus API records for the base repositories.

Verbatim extracts follow. Nothing below is paraphrased unless it is under a heading that says OneHill note.

```
---
license: apache-2.0
base_model:
- swiss-ai/Apertus-70B-2509
pipeline_tag: text-generation
library_name: transformers
tags:
  - multilingual
  - compliant
  - swiss-ai
  - apertus

extra_gated_prompt: "### Apertus LLM Acceptable Use Policy  \n(1.0 | September 1, 2025)\n\"Agreement\" The Swiss National AI Institute (SNAI) is a partnership between the two Swiss Federal Institutes of Technology, ETH Zurich and EPFL. \n\nBy using the Apertus LLM you agree to indemnify, defend, and hold harmless ETH Zurich and EPFL against any third-party claims arising from your use of Apertus LLM. \n\nThe training data and the Apertus LLM may contain or generate information that directly or indirectly refers to an identifiable individual (Personal Data). You process Personal Data as independent controller in accordance with applicable data protection law. SNAI will regularly provide a file with hash values for download which you can apply as an output filter to your use of our Apertus LLM. The file reflects data protection deletion requests which have been addressed to SNAI as the developer of the Apertus LLM. It allows you to remove Personal Data contained in the model output. We strongly advise downloading and applying this output filter from SNAI every six months following the release of the model.  "
extra_gated_fields:
  Your Name: text
  Country: country
  Affiliation: text
  geo: ip_location
  By clicking Submit below I accept the terms of use: checkbox
extra_gated_button_content: Submit
---


[...]
## Model Summary

Apertus is a 70B and 8B parameter language model designed to push the boundaries of fully-open multilingual and transparent models. 
The model supports over 1000 languages and long context, it uses only fully compliant and open training data, and achieves comparable performance to models trained behind closed doors.

![image/png](https://cdn-uploads.huggingface.co/production/uploads/654baf61d625e083383dfd00/gKDv_6dpIpvmgyquenbXt.png)

The model is a decoder-only transformer, pretrained on 15T tokens with a staged curriculum of web, code and math data. The model uses a new xIELU activation function and is trained from scratch with the AdEMAMix optimizer. Post-training included supervised fine-tuning and alignment via QRPO.

### Key features
- **Fully open model**: open weights + open data + full training details including all data and training recipes
- **Massively Multilingual**: 1811 natively supported languages
- **Compliant** Apertus is trained while respecting opt-out consent of data owners (even retrospectivey), and avoiding memorization of training data

For more details refer to our [technical report](https://arxiv.org/abs/2509.14233)


[...]
### Open resources
All elements used in the training process are made openly available
- **Training data reconstruction scripts:** [github.com/swiss-ai/pretrain-data](https://github.com/swiss-ai/pretrain-data)
- The training intermediate checkpoints are available on the different branches of this same repository


## Limitations

Apertus can produce text on a variety of topics, but the generated content may not always be factually accurate, logically consistent, or free from biases present in the training data. These models should be used as assistive tools rather than definitive sources of information. Users should always verify important information and critically evaluate any generated content.


## Legal Aspects

#### EU AI Act Transparency Documentation and Code of Practice
- [Apertus_EU_Public_Summary.pdf](https://huggingface.co/swiss-ai/Apertus-70B-2509/blob/main/Apertus_EU_Public_Summary.pdf)
- [Apertus_EU_Code_of_Practice.pdf](https://huggingface.co/swiss-ai/Apertus-70B-2509/blob/main/Apertus_EU_Code_of_Practice.pdf)

#### Data Protection and Copyright Requests
For removal requests of personally identifiable information (PII) or of copyrighted content, please contact the respective dataset owners or us directly
- llm-privacy-requests@swiss-ai.org
- llm-copyright-requests@swiss-ai.org
  
#### Output Filter for PII
- Currently no output filter is provided.
- Please check this site regularly for an output filter that can be used on top of the Apertus LLM. The filter reflects data protection deletion requests which have been addressed to us as the developer of the Apertus LLM. It allows you to remove Personal Data contained in the model output. We strongly advise downloading and applying this output filter from this site every six months.

## Contact
To contact us, please send an email to
llm-requests@swiss-ai.org


```

## HF API records of base repositories (2026-11-19)
- Apertus-70B-Instruct-2509: gated=False, lastModified=2026-07-17T09:03:01.000Z, license/base tags=['base_model:swiss-ai/Apertus-70B-2509', 'base_model:finetune:swiss-ai/Apertus-70B-2509', 'license:apache-2.0']
- Apertus-8B-Instruct-2509: gated=False, lastModified=2026-07-17T08:57:20.000Z, license/base tags=['base_model:swiss-ai/Apertus-8B-2509', 'base_model:finetune:swiss-ai/Apertus-8B-2509', 'license:apache-2.0']
- OLMo-2-0325-32B-SFT: gated=False, lastModified=2025-03-14T22:59:02.000Z, license/base tags=['base_model:allenai/OLMo-2-0325-32B', 'base_model:finetune:allenai/OLMo-2-0325-32B', 'license:apache-2.0']
- EuroLLM-9B-Instruct: gated=auto, lastModified=2024-12-09T15:44:49.000Z, license/base tags=['base_model:utter-project/EuroLLM-9B', 'base_model:finetune:utter-project/EuroLLM-9B', 'license:apache-2.0']

OneHill note: the Apertus front matter carries an Acceptable Use Policy gate prompt with an indemnity clause, but the Hugging Face API reports gated=False for the base repositories on the retrieval date, so the gate is switched off while the prompt text remains in the card. The MeditronFO cards do not reproduce or mention this policy.

