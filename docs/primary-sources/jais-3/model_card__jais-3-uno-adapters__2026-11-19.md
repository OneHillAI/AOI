# model_card / inception42/Jais-3-32B-Uno (representative adapter card)

source_url: https://huggingface.co/inception42/Jais-3-32B-Uno (raw README)
retrieval_date: 2026-11-19
doc_type: model_card
exists: yes
retrieved: true
tag: publisher

NOTE (OneHill): the four Uno adapter repos carry no licence tag in the hub API and the card contains no licence statement (a search for "licen" in the card text returned nothing). They are outside the scored release and are listed as a follow-up. Verbatim opening of the card:
```
---
base_model: inception42/Jais-3-32B
base_model_relation: adapter
library_name: peft
pipeline_tag: text-generation
language:
- ar
- en
tags:
- peft
- lora
- uno
- diffusion-language-model
- conditional-lora
- lossless-acceleration
---

# Jais-3-32B-Uno

**Jais-3-32B-Uno** makes [inception42/Jais-3-32B](https://huggingface.co/inception42/Jais-3-32B) generate text **2.15× faster** on average,
**with exactly the same output distribution as the base model**.

It is a small diffusion adapter (LoRA, rank 128) trained with the [Uno](https://huggingface.co/papers/2609.04010) recipe
on top of the frozen Jais-3-32B weights. This repository contains the adapter only; the base weights are in
```
