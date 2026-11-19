# Assess - Kimi K3 (Moonshot AI)

_Openness, licence, provenance, EU AI Act position, safety, evaluation and the AOI score._

<!-- item: intended-use -->
## Intended & out-of-scope use

Kimi K3 is Moonshot AI's frontier open-weights release: a natively multimodal 2.8T-total / 104B-active Mixture-of-Experts model with a 1M-token context and native text, image and video understanding. It is intended for coding, agentic, reasoning and vision workloads where open weights are wanted over a closed API and multi-node serving is affordable.

The weights ship with no safety tuning and no guard model, and the technical report documents offensive-cyber capability the model does not refuse. High-stakes, autonomous or EU-regulated decision-making is therefore out of scope without the full external control stack described in the Implement domain. Unsandboxed agentic or cyber-capable deployment is out of scope in all cases. There is no small variant, so single-GPU or laptop use is also out of scope.

<!-- item: limitations -->
## Known limitations, bias & failure modes

The weights have no built-in safety: no safety tuning, guard model, refusal training or content filtering is described. The technical report's section 6.2.2 documents offensive-cyber capability (vulnerability discovery and exploit development) that the model performs where frontier labs refuse.

Training data, training code and the training-token and FLOP counts are undisclosed, so the model can be adapted but not reproduced, and its compute cannot be bounded. There are no small variants; the smallest viable deployment is a multi-node cluster (~1.4 TB of weights even at native MXFP4). China-aligned filtering on politically sensitive prompts is present in the K2 lineage and is unconfirmed for K3.

On the capability side, Kimi K3 is behind only Claude Fable 5 and GPT-5.6 Sol overall and leads other open models on coding and agentic benchmarks.

<!-- item: openness -->
## Openness tier & components

Kimi K3 is `open_weights` and not open-science. It is open-weights and not closed-frontier because the weights are downloadable. The weights ship as native MXFP4/MXFP8 checkpoints with a model card and a technical report, so weights, documentation and licence are Open or Partial. The training data, the training code and the training-token and FLOP figures are not released, and evaluation is only partially reproducible. The model can be run, adapted and redistributed, but how it was made cannot be seen or reproduced.

<!-- item: license -->
## License terms & permitted use

Kimi K3 ships under the custom Kimi K3 License, a modified-MIT text that is not OSI-certified. It grants use, modification, redistribution and sale, with two scale-linked conditions.

A Model-as-a-Service business with more than $20M USD aggregate revenue over any consecutive 12 months must secure a separate agreement with Moonshot AI before commercial deployment. Any product with more than 100M monthly active users or more than $20M USD monthly revenue must prominently display "Kimi K3" in its user interface. Internal use and access through Moonshot's official products or certified partners are exempt.

The licence defines Model as a Service as giving a third party inference or fine-tuning access with meaningful control over inputs, parameters or training data. It excludes end-user products with embedded model features and mere relaying to models hosted by others. The gate is new relative to Kimi K2 and drives the legal score of 2.

<!-- item: provenance -->
## Supply-chain & provenance

Weights are distributed from the verified `moonshotai` org on Hugging Face as native MXFP4 weights / MXFP8 activations (not pickle), with a clear canonical source and no malicious-mirror incident on record. The checkpoint trust checklist scores about 4/8. The base tensor format (safetensors) is not stated on the card, no scanned checkpoint or documented mirror/quantization policy exists, and there is no cryptographic weight signing or SLSA attestation, so provenance scores 3 and not 4 or 5. Verify per-file checksums and pin the exact revision on download.

<!-- item: eu-ai-act -->
## EU AI Act posture

Kimi K3 is a GPAI model. Its training compute is unpublished. The technical report gives only a context-length curriculum and relative scaling-law FLOPs, with no total training-token count and no absolute FLOP figure, so it is unknown whether the model crosses the 1e25-FLOP systemic-risk threshold. A 2.8T-total / 104B-active frontier pre-train plausibly does, but that is an inference.

The custom Kimi K3 License is not an OSI-certified free licence and carries monetisation-linked commercial restrictions, so it most likely does not reach the open-source exemption. No training-content summary and no copyright policy are published, and a China-based provider is unlikely to furnish an EU documentation package. An EU deployer must self-assemble compliance material and takes on these gaps for any derivative it places on the market.

<!-- item: evaluation -->
## Benchmarks & evaluation

On the model card and reputable coverage, Kimi K3 sits behind only Claude Fable 5 and GPT-5.6 Sol overall, ahead of other open models on coding and agentic benchmarks, and 1st on the public Frontend Code Arena (1679). Reported scores include GPQA-Diamond 93.5 (reasoning), BrowseComp 91.2 and OSWorld-Verified 84.8 (agentic) and Video-MME 90.0 (vision).

OneHill has not run its own benchmarks. The figures come from Moonshot's model card and secondary coverage, so evaluation is marked partial: the results are publisher and third-party figures and not OneHill-reproduced.

<!-- item: safety-eval -->
## Independent safety evaluation

No independent red-team exists for Kimi K3, and the publisher provides no safety-tuned variant. The technical report's section 6.2.2 is a dangerous-capability evaluation and not a mitigation one. It measures offensive-cyber performance across Tier-1 vulnerability discovery and Tier-2 end-to-end exploit development, and states that Anthropic and OpenAI frontier models refuse these tasks and are excluded, while Kimi K3 does not refuse. This is evidence of elevated misuse exposure and not of safety coverage. Any exposed deployment needs its own guard and red-team.
