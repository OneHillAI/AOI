# Ollama registry: manifests, runners, pull behaviour and library licences (read 2026-11-19)

Method: public GET requests to the registry (manifests and one small licence blob per model only; no model
weight blobs downloaded), plus the server source on GitHub. Registry: https://registry.ollama.ai

## 1. Manifest shape and runner selection
- Source: https://raw.githubusercontent.com/ollama/ollama/main/manifest/manifest.go
  Constants (verbatim): `MediaTypeManifest = "application/vnd.docker.distribution.manifest.v2+json"`,
  `MediaTypeManifestList = "application/vnd.ollama.manifest.list.v2+json"`, `RunnerMLX = "mlx"`,
  `RunnerGGML = "ggml"`, `RunnerLlamaCPP = "llamacpp"`, `FormatSafetensors = "safetensors"`,
  `FormatGGUF = "gguf"`. The `Manifest` struct carries `runner`, `format` and child `manifests`.
- Client preference order (from `runnerPreferences()`): on darwin/arm64 the order is mlx, llamacpp, ggml; on
  every other platform it is llamacpp, ggml, mlx. A manifest list with no child for the chosen runner returns
  `ErrNoCompatibleManifest` ("no compatible manifest found").
- Manifest-list code is absent in tag v0.35.1 and present in v0.40.0, v0.40.1, v0.40.2 and v0.40.16
  (counted by grepping `MediaTypeManifestList` in `manifest/manifest.go` at each tag).

## 2. What the registry returns (observed 2026-11-19)
- `GET /v2/library/qwen3.8/manifests/latest` with `Accept: application/vnd.ollama.manifest.list.v2+json`
  returns a manifest list with two children: `runner: mlx, format: safetensors` and
  `runner: llamacpp, format: gguf`. The same request for `gemma4` also returns an mlx/safetensors child and a
  llamacpp/gguf child.
- The same URL without that Accept header returns a single manifest with `"runner":"llamacpp","format":"gguf"`
  (observed for qwen3.8, gemma4, gemma4:e4b and flint). So a client that does not ask for the list (an older
  Ollama) is served the llama.cpp GGUF build only.
- The MLX child (`qwen3.8:27b-mlx`) has no single model GGUF layer; it has 1209 layers of media type
  `application/vnd.ollama.image.tensor`, one per safetensors tensor (for example `lm_head.weight`). The
  llama.cpp child has one `application/vnd.ollama.image.model` layer plus `projector`, `template`, `license`
  and `params` layers (some carry a `from` field naming an internal build, for example
  `gemma4-validation-20260929:e4b-imatrix-attention-q6-q8-draft2`).
- The library page https://ollama.com/library/qwen3.8 lists 13 tags including MLX variants
  (`qwen3.8:27b-mlx`, `27b-mlx-bf16`, `27b-mxfp8`, `27b-dflash2-nvfp4`) alongside `latest` (18GB).
- Result: the registry is no longer GGUF-only. MLX builds are safetensors-derived per-tensor layers, and the
  tensor-layer download path is the one named in CVE-2026-85180 (see `security__cve-record__2026-11-19.md`).

## 3. Release notes on the same behaviour
- v0.40.0 (2026-09-25): "Models run on MLX on Apple Silicon by default ... on Apple Silicon devices, model
  architectures supported by the MLX runtime will automatically run on MLX."
- v0.40.2 (2026-10-08): "Models downloaded with earlier versions of Ollama are upgraded in the background the
  first time you run them, for better performance and compatibility when running on llama.cpp. To make
  downgrading safe, Ollama keeps the original copy as a backup ... If you later downgrade to a version older
  than 0.40, you'll need to re-pull those models." The documented clean-up command selects manifests whose
  `runner` is `llamacpp` and removes the `ggml` ones.
- v0.40.4 (2026-10-12): "Improved inference performance by reusing verified manifests and already loaded models".
- v0.40.7 (2026-10-18): `ollama show` "now reports which renderer and parser a model uses and where its chat
  template comes from"; API fields `renderer`, `parser`, `template_source`.
- The release notes and docs do NOT state that v0.30.10 (tagged 2026-06-17) refuses new models. The
  mechanism above (new library models published as llama.cpp-runner or MLX-runner manifests that a pre-0.40
  client cannot select) is consistent with the downstream observation but is our reading of the source, not an
  official statement. Individual docs name a minimum version for a feature (the System One API page says:
  "Requires Ollama v0.35.0 or later, or v0.40.5 or later for cloud models").

## 4. Licence handling in the library
- Each library model carries its licence text as a registry layer of media type
  `application/vnd.ollama.image.license`. Blobs read 2026-11-19: qwen3.8, gemma4 and gpt-oss carry the Apache
  License 2.0 text (about 11 KB); llama3.3 carries "LLAMA 3.3 COMMUNITY LICENSE AGREEMENT"; llama4 carries
  "LLAMA 4 COMMUNITY LICENSE AGREEMENT".
- The text is surfaced by `ollama show --license`. `ollama pull` and `ollama run` do not display a
  click-through, require acceptance or check an access request, including for the Llama community licences.
  The Ollama Terms contain no clause on model licences (see `terms__2026-11-19.md`).
- Docs (https://docs.ollama.com/import.md) say any user can push a model to ollama.com under their username
  (`ollama cp mymodel myuser/mymodel`, `ollama push myuser/mymodel`) after adding an Ollama public key
  (ed25519, `~/.ollama/id_ed25519.pub`). That key identifies a local install to ollama.com; it is not a
  publisher-identity or model-signing mechanism. The pull API (https://docs.ollama.com/api/pull.md) has an
  `insecure` boolean: "Allow downloading over insecure connections".
