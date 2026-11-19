# Support - EuroLLM (EuroLLM-9B / EuroLLM-1.7B)

_Troubleshooting, versions, security disclosure, channels and deprecation._

<!-- item: troubleshooting -->
## Common problems & fixes

Common pitfalls, not an exhaustive catalogue:

- Garbled or over-verbose Instruct output: the chat template is most likely not applied. Use
  `apply_chat_template` and do not prompt a base checkpoint as a chat model.
- Truncated or silently dropped context: the window is only 4k, so long inputs overflow. Chunk or
  retrieve, and budget the 4k across system prompt, input and output.
- Weak output in a specific language: per-language quality is uneven across the 35 languages.
  Evaluate the target language and consider a light fine-tune for lower-resource ones.
- Non-reproducible results or silent updates: a deployment floating on `main` changes under you.
  Pin an exact HF revision (e.g. a dated `-2512` snapshot) and verify checksums.

<!-- item: release-versioning -->
## Versions, changelog & cadence

Releases follow a generational cadence of 1.7B → 9B → 22B, with dated snapshot revisions (e.g.
`EuroLLM-9B-Instruct-2512`) published on the `utter-project` org, each with base and Instruct
checkpoints. Versions are tracked as immutable Hugging Face revisions, so the revision hash is
the changelog anchor: pin it and diff against a newer revision when upgrading. The EuroLLM-9B
technical report accompanies the release and documents what changed.

<!-- security-disclosure is a `gap` item - no formal published vulnerability-disclosure or
     security policy was found; contact is only the general eurollm.io / Hugging Face
     utter-project org presence. See gap_reason. This absence also holds Governance to 3. -->

<!-- item: channels -->
## Community & support channels

Announcements and docs come from the EuroLLM project site (`eurollm.io`, `ev-eurollm-site`).
Usage questions go to the model discussion tabs on the `utter-project` Hugging Face org
(`ev-hf-9b-instruct`). There is no paid support tier; support is community and consortium based,
around an EU-funded open project.

<!-- deprecation is a `gap` item - no published deprecation/EoL policy. Older HF revisions
     remain downloadable, but no formal support window or sunset commitment is documented.
     See gap_reason. -->

<!-- item: known-issues -->
## Tracked known issues

These come from technical-report caveats and third-party reviews, not a formal issue tracker, so
coverage is partial.

- The context window is only 4k, a real constraint for document workloads.
- Per-language quality is uneven; lower-resource EU languages trail the majors.
- Raw reasoning is in-class, not frontier.
- Base checkpoints are untuned research artifacts and must not be deployed as assistants.
