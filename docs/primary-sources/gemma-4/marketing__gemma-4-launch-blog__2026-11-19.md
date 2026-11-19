# Gemma 4 launch blog (blog.google)

source_url: https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/
retrieval_date: 2026-11-19
doc_type: marketing
retrieved: true


Google blog post dated Apr 02, 2026 by Clement Farabet and Olivier Lacombe (Google DeepMind). Marketing document: it cannot justify a rating. Extracts are short and verbatim.

```
You gave us feedback, and we listened. Building the future of AI requires a collaborative approach, and we believe in empowering the developer ecosystem without restrictive barriers. That's why Gemma 4 is released under a commercially permissive Apache 2.0 license.
This open-source license provides a foundation for complete developer flexibility and digital sovereignty; granting you complete control over your data, infrastructure, and models. It allows you to build freely and deploy securely across any environment, whether on-premises or in the cloud.
```

```
These models undergo the same rigorous infrastructure security protocols as our proprietary models. By choosing Gemma 4, enterprises and sovereign organizations gain a trusted, transparent foundation that delivers state-of-the-art capabilities while meeting the highest standards for security and reliability.
```

```
- Use your favorite tools: With day-one support for Hugging Face (Transformers, TRL, Transformers.js, Candle), LiteRT-LM, vLLM, llama.cpp, MLX, Ollama, NVIDIA NIM and NeMo, LM Studio, Unsloth, SGLang, Cactus, Baseten, Docker, MaxText, Tunix, Keras, you have the flexibility to choose the best tools for your project.
```

Reading notes by OneHill:
- The blog says "four" sizes (E2B, E4B, 26B MoE, 31B Dense); the 12B Unified model was added later (Hugging Face createdAt 2026-05-23) and the model card now says five sizes.
- "complete control over your data, infrastructure, and models" is marketing wording; the binding grant is the Apache License 2.0 text in license__gemma-4-apache-2.0.
- The day-one ecosystem support list is a publisher claim; only the Ollama library page and a news article corroborate parts of it (see the third_party files).
- The blog says the weights are available from Hugging Face, Kaggle and Ollama.
