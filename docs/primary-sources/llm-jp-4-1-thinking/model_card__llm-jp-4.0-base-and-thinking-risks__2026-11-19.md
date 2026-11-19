# model_card / llm-jp-4.0-base-and-thinking-risks

source_url: https://huggingface.co/llm-jp/llm-jp-4-33b-base (raw README.md)
retrieval_date: 2026-11-19
exists: yes
retrieved: true

Verbatim extracts (publisher text, not edited). Notes by OneHill are marked NOTE.

NOTE: these are the LLM-jp-4 (4.0) cards. They carry a different Risks and Limitations statement from the 4.1 cards, which is why 4.0 is listed as a follow-up entry and not folded into this one.

## llm-jp-4-33b-base, Risks and Limitations
```
## Risks and Limitations

The models released here are in the early stages of our research and development and have not been tuned to ensure outputs align with human intent and safety considerations.
```

## llm-jp-4-33b-thinking, Risks and Limitations
```
## Risks and Limitations

The models released here are in the early stages of our research and development and have not been tuned to ensure outputs align with human intent and safety considerations.
```
(source: https://huggingface.co/llm-jp/llm-jp-4-33b-thinking raw README.md, same text)

## llm-jp-4-33b-base, pre-training and post-training data links
```
## Training

### Pre-training

This model is trained through a multi-stage pipeline consisting of pre-training and mid-training phases, using a total of 11.7T tokens.

![pretraining_overview](./v4_pretraining_overview.png)

The corpora used for pre-training and mid-training are publicly available at the following links:
- [Pre-training](https://gitlab.llm-jp.nii.ac.jp/datasets/llm-jp-corpus-v4.1)
- [Mid-training](https://gitlab.llm-jp.nii.ac.jp/datasets/llm-jp-corpus-midtraining-v2)

> [!NOTE]
> Although most of the corpora have been released, some portions are excluded from public release due to licensing constraints.

### Post-training

We have fine-tuned the pre-trained checkpoint using SFT and further aligned it with DPO.

The datasets used for post-training are also publicly available at the following links:
- [SFT](https://huggingface.co/datasets/llm-jp/llm-jp-4-thinking-sft-data)
- [DPO (for llm-jp-4-8b-thinking model)](https://huggingface.co/datasets/llm-jp/llm-jp-4-8b-thinking-dpo-data)
- [DPO (for llm-jp-4-32b-a3b-thinking model)](https://huggingface.co/datasets/llm-jp/llm-jp-4-32b-a3b-thinking-dpo-data)
- [DPO (for llm-jp-4-33b-thinking model)](https://huggingface.co/datasets/llm-jp/llm-jp-4-33b-thinking-dpo-data)
```

## llm-jp-4-33b-base, licence line
```
## License

[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)


## Acknowledgement

To develop this model, we used the NINJAL Web Japanese Corpus (whole-NWJC) from the National Institute for Japanese Language and Linguistics (NINJAL).
```
