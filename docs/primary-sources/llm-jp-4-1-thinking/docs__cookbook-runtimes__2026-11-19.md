# docs / cookbook-runtimes

source_url: https://github.com/llm-jp/llm-jp-4-cookbook
retrieval_date: 2026-11-19
exists: yes
retrieved: true

Verbatim extracts (publisher text, not edited). Notes by OneHill are marked NOTE.

NOTE (OneHill): github.com/llm-jp/llm-jp-4-cookbook (Apache-2.0, last pushed 2026-10-07). README.md and llmjp4_llama-cpp/README.md read in full.

## README.md (selected sections, verbatim)
```
# LLM-jp-4 Series Cookbook

Examples for running LLM-jp-4.0/4.1 models with Hugging Face Transformers, vLLM, and
llama.cpp, including chat templates, reasoning output, and Harmony message parsing.

Author: Yusuke Oda (@odashi)

## Choose a runtime

| Runtime | Use case | Entry point |
| --- | --- | --- |
| Transformers | Run inference in Python and inspect generated tokens and parsed messages. | [Basic example](llmjp4_transformers/example_basic.py) |
| vLLM | Run inference in Python or serve a chat API with llm-jp-vllm. | [Basic example](llmjp4_vllm/example_basic.py), [setup and server guide](llmjp4_vllm/README.md) |
| llama.cpp | Run GGUF models with a command-line chat client or local server. | [Installation and usage guide](llmjp4_llama-cpp/README.md) |

The Python examples use `llm-jp/llm-jp-4.1-8b-thinking` by default. Each Python
runtime has its own dependency manifest and lockfile; there is no root Python
project. Install and run commands from the runtime directory you choose.

### Minimum runtime releases

Use the following minimum official stable releases **or later**.
`uv.lock` records the exact Python dependency versions used for reproducible runs.

| Runtime | Minimum official stable release | Required support |
| --- | --- | --- |
| Transformers | [5.0.0](https://github.com/huggingface/transformers/releases/tag/v5.0.0) | `parse_response` for the bundled response schemas. |
| vLLM | [0.30.0](https://github.com/vllm-project/vllm/releases/tag/v0.30.0) | Module-name parser plugins; also use [llm-jp-vllm 0.1.1](https://github.com/llm-jp/llm-jp-vllm/tree/v0.1.1) or later. |
| llama.cpp | [v0.6.0](https://github.com/ggml-org/llama.cpp/releases/tag/v0.6.0) | Native LLM-jp-4.1 Harmony chat parsing for GGUF models. |

## Using LLM-jp-4.0 models

LLM-jp-4.1 is backward-compatible with the 4.0 series and is the default in this
cookbook. To use a 4.0 model with the Python examples or vLLM server, replace
`llm-jp/llm-jp-4.1-8b-thinking` with `llm-jp/llm-jp-4-8b-thinking` in the model
loading calls, server command, and client requests. The 4.0 repository names use
`llm-jp-4-`, not `llm-jp-4.0-`. Keep the bundled tokenizer and parser settings.
Tool-calling improvements are part of 4.1; the function-calling examples target
4.1 models.

The llama.cpp instructions target 4.1 GGUF files. Original 4.0 GGUF chat
templates lack the declaration needed to select the LLM-jp-4.1 Harmony parser.
```
```
### Requirements

- Python 3.13 or later. Both projects select Python 3.13 in `.python-version`.
- `uv` for installing the dependencies recorded in each `uv.lock`.
- Hardware and drivers suitable for the selected runtime and model. The examples
  load the 8B model in `bfloat16`; see the recorded test environment below.
- Network access to download dependencies and model files on the first run, or
  copies already available locally.

The examples enable `trust_remote_code=True` to load the custom tokenizer and
model-bundled helpers. vLLM parsing is provided separately by `llm-jp-vllm`.
The remote-code option allows Python code from the
model repository to run, so use model repositories you trust. The llama.cpp
workflow uses GGUF files and does not use this Python option.
```
```
## Run GGUF models with llama.cpp

Follow the [llama.cpp guide](llmjp4_llama-cpp/README.md) for installation
instructions and `llama cli` / `llama serve` examples.

Use upstream `ggml-org/llama.cpp` **v0.6.0 or later**. The `-hf` option in the
examples downloads the selected GGUF model from Hugging Face and caches it.
Model files are not included in this repository.
```
```
## Recorded test environment

The repository records the following hardware environment for its examples.
This is a reference environment, not a statement of minimum requirements.
For the runtime versions and model sizes tested, see
the [Transformers validation](llmjp4_transformers/README.md#validation),
[vLLM validation](llmjp4_vllm/README.md#validation-environment), and
[llama.cpp validation](llmjp4_llama-cpp/README.md#validation) notes.

| Component | Configuration |
| --- | --- |
| CPU | Intel Core i9-14900K |
| RAM | 32 GiB |
| GPU | NVIDIA RTX 6000 Ada Generation |
| OS | Debian GNU/Linux 12 |
| NVIDIA driver | 580.119.02 |
| CUDA library | 12.8 (Transformers and llama.cpp); 13.0 (vLLM) |
```

## llmjp4_llama-cpp/README.md (verbatim, start and validation)
```
# LLM-jp-4.1 examples for llama.cpp

Run LLM-jp-4.1 GGUF models with
[ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp).

Use **v0.6.0 or later**. [v0.6.0](https://github.com/ggml-org/llama.cpp/releases/tag/v0.6.0)
is the oldest official stable release that includes the
[LLM-jp-4.1 Harmony parser](https://github.com/ggml-org/llama.cpp/pull/29681).
For original 4.0 GGUF files, see the
[compatibility note](../README.md#using-llm-jp-40-models).

## Requirements

Install llama.cpp by following the
[official installation instructions](https://github.com/ggml-org/llama.cpp#quick-start).
```
```
## Validation

Validated a source build of v0.6.0 with GCC 12.2.0 and CUDA 12.8 using
`llm-jp-4.1-33b-thinking-Q4_K_M.gguf`. The upstream `test-chat` suite, CLI chat,
and streaming/non-streaming API chat and tool calls passed. The server used a
4096-token context and one slot. The 8B GGUF example was not tested.
See the [test hardware](../README.md#recorded-test-environment).
```
