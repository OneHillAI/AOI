# model_card / Jais-3 sibling cards compared (0.9B, 3.7B, 7B, 32B, MoVA-36B-A4B, 375B-A23B)

source_url: https://huggingface.co/inception42/<repo>/raw/main/README.md for each of the six repos
retrieval_date: 2026-11-19
doc_type: model_card
exists: yes
retrieved: true
tag: publisher

OneHill check: all six raw README files were fetched and compared. They share the same sections and wording for Intended use, Out of scope, Limitations, Artifact Index, Checkpoint Inventory and Best Practices. Only sizes, serving parallelism and linked quantised repos differ.

| repo | YAML front matter (flattened) | first sentence of card | Serving best-practice line | "Code repository | Coming soon" present | four stage branches listed (CPT, Cooldown, FTPO, SFT) | identical Intended use text | identical Limitations text |
|---|---|---|---|---|---|---|---|
| Jais-3-0.9B | pipeline_tag: text-generation; library_name: transformers; model_name: Jais-3-0.9B; language:; - ar; - en; tags:; - jais-3; - 0.9b; - dense; - reasoning; license: apache-2.0 |  | Use the validated SGLang recipe above: BF16, TP=1 on a single H100 node, FlashAttention-3. | True | True | True | True |
| Jais-3-3.7B | pipeline_tag: text-generation; library_name: transformers; model_name: Jais-3-3.7B; language:; - ar; - en; tags:; - jais-3; - 3.7B; - dense; - reasoning; license: apache-2.0 |  | Use the validated SGLang recipe above: BF16, TP=1 on a single H100 node, FlashAttention-3. | True | True | True | True |
| Jais-3-7B | pipeline_tag: text-generation; library_name: transformers; model_name: Jais-3-7B; language:; - ar; - en; tags:; - jais-3; - 7B; - dense; - reasoning; license: apache-2.0 | Jais-3-7B is the medium dense member of the Jais-3 family: a 7B-class decoder-only model with a 512K context window. | Use the validated SGLang recipe above: BF16, TP=1 on a single H100 node, FlashAttention-3. | True | True | True | True |
| Jais-3-32B | pipeline_tag: text-generation; library_name: transformers; model_name: Jais-3-32B; language:; - ar; - en; tags:; - jais-3; - 32B; - dense; - reasoning; license: apache-2.0 | Jais-3-32B is the large dense member of the Jais-3 family: a 32B-class decoder-only model with a 512K context window. | Use the validated SGLang recipe above: BF16, TP=2 on a single H100 node, FlashAttention-3. | True | True | True | True |
| Jais-3-MoVA-36B-A4B | pipeline_tag: text-generation; library_name: transformers; model_name: Jais-3-MoVA-36B-A4B; language:; - ar; - en; tags:; - jais-3; - 36B; - mova; - moe; - reasoning; license: apache-2.0 | Jais-3-MoVA-36B-A4B is the sparse member of the Jais-3 family: a Mixture-of-Experts model with Mixture-of-Values attention (MoVA) that stores 36B parameters and runs 4B per token, with a 512K context window. | Use the validated SGLang recipe above: BF16, TP=2 and EP=2 on a single H100 node, FlashAttention-3. | True | True | True | True |
| Jais-3-375B-A23B | pipeline_tag: text-generation; library_name: transformers; model_name: Jais-3-375B-A23B; language:; - ar; - en; tags:; - jais-3; - 375b; - moe; - reasoning; license: apache-2.0 | Jais-3-375B-A23B is the flagship of the Jais-3 family: a sparse Mixture-of-Experts model that stores 375B parameters and runs 23B per token, with a 512K context window. | Use the validated SGLang recipe above: BF16, TP=16 and EP=16 across two 8× H100 nodes, FlashAttention-3, with multithreaded weight loading disabled. On a single 8× H200 node, use TP=8 and EP=8 instead. | True | True | True | True |

## Verbatim intended use and limitations (same in all six)
```
**Intended use:** The model is designed for Arabic and English assistant and agentic applications, including reasoning and tool-use tasks, as well as for research and experimentation.

**Out of scope:** The model should not be used in ways that violate applicable laws or regulations. The following uses are also considered out of scope:

- **Harmful or malicious use:** generating hateful, extremist, discriminatory, or deliberately misleading content, or using the model to support illegal or harmful activities.
- **Sensitive information:** using the model to generate, expose, or infer personal, confidential, or otherwise sensitive information about individuals or organizations.
- **Unsupported languages:** applications that depend on reliable performance in languages other than Arabic or English.
- **High-stakes decisions:** relying on the model to make medical, legal, financial, or safety-critical decisions without appropriate human oversight.

**Limitations:** The model can produce inaccurate or made-up content and may reflect biases present in its training data. Evaluate it for your use case and add safeguards before deploying it.
```

## Card note shared by all six
```
> [!NOTE]
> Benchmarks marked with ^ will be released by IFM soon.
```
(The 32B card also says: "Starred (*) benchmarks have been audited for sample quality ... The audit methodology, the excluded samples and the verified benchmarks are available in the IFM/Arabic-Bench..." link.)
