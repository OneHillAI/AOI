# docs / gguf-card-llm-jp-4.1-33b-thinking-gguf

source_url: https://huggingface.co/llm-jp/llm-jp-4.1-33b-thinking-gguf
retrieval_date: 2026-11-19
exists: yes
retrieved: true

Verbatim extracts (publisher text, not edited). Notes by OneHill are marked NOTE.

NOTE (OneHill): the Hugging Face API file list for llm-jp/llm-jp-4.1-33b-thinking-gguf: BF16 GGUF (66,445,273,632 bytes), Q4_K_M GGUF (20,407,544,608 bytes), imatrix.dat, params, README.md; last modified 2026-10-20. The 8B and 32B-A3B GGUF repositories hold BF16 and Q4_K_M files only. Weights were not downloaded.

CONTRADICTION recorded: the GGUF card says llama.cpp needs a publisher fork. The newer-pushed cookbook (2026-10-07 push date; card last modified 2026-10-20) says upstream ggml-org/llama.cpp v0.6.0 or later has the parser. The card text, verbatim:
```
> [!IMPORTANT]
> Running this model with `llama.cpp` currently requires a [fork of `llama.cpp`](https://github.com/llm-jp/llama.cpp/tree/llmjp-harmony-handler). The upstream `ggml-org/llama.cpp` does not yet include the required tokenizer-handling fixes, so chat parsing will fail for this model when using it as-is. See the [LLM-jp-4 llama.cpp guide](https://github.com/llm-jp/llm-jp-4-cookbook/tree/main/llmjp4_llama-cpp) for build and usage instructions.
```
