doc_type: docs
entity: GGUF file format specification
source_url: https://raw.githubusercontent.com/ggml-org/ggml/master/docs/gguf.md (834 lines)
retrieval_date: 2026-11-19
exists: yes
retrieved: true
tag: publisher

## Where the spec lives and who controls it
- The specification is a single Markdown file, docs/gguf.md, in the ggml-org/ggml repository. There is no separate standards body, versioned RFC process or independent governance document; changes land as ordinary pull requests by ggml-org maintainers.
- Commit history of docs/gguf.md (GitHub API, read 2026-11-19; the API rate-limited later queries): 2026-11-08 "docs : sync ggml_type enum in gguf.md (#1685)"; 2026-07-09 formatting fix (#1556); 2026-05-21 "add Sidecar prefix slot (mmproj, mtp); drop MTP from Type (#1496)"; 2026-05-13 "add MTP to GGUF Type slot (#1488)"; 2025-09-16 ggml_types sync; 2024-07-22 naming convention synced to llama.cpp.
- Since the 2026-09-21 check, the only spec edit is the 2026-11-08 ggml_type enum sync. None of the 2026 edits change file structure.

## Structure clauses (VERBATIM from the header definition)
- "Must be `GGUF` at the byte level: `0x47` `0x47` `0x55` `0x46`."
- "The version of the format implemented. Must be `3` for version described in this spec, which introduces big-endian support."
- "This version should only be increased for structural changes to the format. Changes that do not affect the structure of the file should instead update the metadata to signify the change."
- "Models are little-endian by default. They can also come in big-endian for use with big-endian computers ... At the time of writing, there is no way to determine if a model is big-endian; this may be rectified in future versions."
- Design goals listed verbatim: "Single-file deployment", "Extensible", "`mmap` compatibility", "Easy to use", "Full information: all information needed to load a model is contained in the model file".

## Naming convention (new slot since the entry was written)
The filename convention is now `[<Sidecar>]<BaseName><SizeLabel><FineTune><Version><Encoding><Type><Shard>.gguf`. Sidecar prefixes: `mmproj` (multimodal projector) and `mtp` (multi-token-prediction heads for speculative decoding). `Type` values: `LoRA`, `vocab`.

## Reading (OneHill)
- Format version is still 3. There is no format revision, so the entry's "no format-spec revision" statement holds.
- The spec contains no signing, hash, provenance or attestation field. The file header holds magic, version, tensor_count and metadata_kv_count; integrity and origin cannot be established from the file itself. This supports provenance_integrity 2.
- The spec states that the format carries the chat template and tokenizer inside metadata ("all information needed to load a model"), which is the reason template and metadata inspection matters.
