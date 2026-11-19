doc_type: terms
entity: boldt
variant/applies-to: upstream terms for Llama-3.3-70B-Instruct, the model that wrote the labels used to train the Boldt quality classifiers (not a Boldt document)
source_url: https://www.llama.com/llama3_3/license/ (the Hugging Face copy, huggingface.co/meta-llama/Llama-3.3-70B-Instruct/raw/main/LICENSE, returns HTTP 401: gated)
retrieval_date: 2026-11-19
exists: yes
retrieved: true (llama.com page text)

## Governing clause (verbatim), section 1.b.i
"If you distribute or make available the Llama Materials (or any derivative works thereof), or a product or service (including another AI model) that contains any of them, you shall (A) provide a copy of this Agreement with any such Llama Materials; and (B) prominently display "Built with Llama" on a related website, user interface, blogpost, about page, or product documentation. If you use the Llama Materials or any outputs or results of the Llama Materials to create, train, fine tune, or otherwise improve an AI model, which is distributed or made available, you shall also include "Llama" at the beginning of any such AI model name."

Heading of the page: "Llama 3.3 Community License Agreement", "Llama 3.3 Version Release Date: December 6, 2024".

## Why it is logged
The Boldt paper and the dataset card say Llama-3.3-70B-Instruct annotated the 500k documents that trained the three released classifiers, and the classifiers' scores picked the Dense-Core documents. The released classifier repos are named "fineweb2-de-*-classifier" with no "Llama" prefix, carry no licence and no Llama notice. Whether the clause reaches the classifiers, the Dense-Core data or the Boldt language models trained on that data is not addressed by the publisher and is not decided here: the Boldt base models were not themselves trained on Llama outputs (the paper's pretraining data is filtered web text), so the clause attaches most directly to the classifier repos.
