# Support - EuroLLM (EuroLLM-9B / EuroLLM-1.7B)

_How do we keep it running and get help? Troubleshooting, versions/changelog, channels;
security-disclosure and deprecation policy are current gaps._

<!-- item: troubleshooting -->
## Common problems & fixes

Aggregated common pitfalls (not an exhaustive catalogue):

- **Garbled or over-verbose Instruct output.** You are almost certainly not applying the chat
  template - use `apply_chat_template`, and don't prompt a *base* checkpoint as a chat model.
- **Truncated or silently dropped context.** The window is only **4k** - long inputs overflow;
  chunk or retrieve, and budget the 4k across system/input/output.
- **Weak output in a specific language.** Per-language quality is uneven across the 35
  languages; evaluate your target language and consider a light fine-tune for lower-resource
  ones.
- **Non-reproducible results / silent updates.** You floated on `main`; pin an exact HF
  revision (e.g. a dated `-2512` snapshot) and verify checksums.

<!-- item: release-versioning -->
## Versions, changelog & cadence

Releases follow a **generational cadence - 1.7B → 9B → 22B** - with dated snapshot revisions
(e.g. `EuroLLM-9B-Instruct-2512`) published on the `utter-project` org, each with base and
Instruct checkpoints. Individual versions are tracked as **immutable Hugging Face revisions**,
so the revision hash is your changelog anchor: pin it, and diff against a newer revision when
you choose to upgrade. The EuroLLM-9B technical report accompanies the release and documents
what changed.

<!-- security-disclosure is a `gap` item - no formal published vulnerability-disclosure or
     security policy was found; contact is only the general eurollm.io / Hugging Face
     utter-project org presence. See gap_reason. This absence also holds Governance to 3. -->

<!-- item: channels -->
## Community & support channels

- **EuroLLM project site** (`eurollm.io`, `ev-eurollm-site`) for announcements and docs.
- **Hugging Face** model discussion tabs on the `utter-project` org (`ev-hf-9b-instruct`) for
  usage questions.

There is no paid support tier - this is community and consortium/maintainer support around an
EU-funded open project.

<!-- deprecation is a `gap` item - no published deprecation/EoL policy. Older HF revisions
     remain downloadable, but no formal support window or sunset commitment is documented.
     See gap_reason. -->

<!-- item: known-issues -->
## Tracked known issues

Drawn from technical-report caveats and third-party reviews rather than a formal issue tracker
(hence *partial*):

- Context window is **only 4k** - a real constraint for document workloads.
- Per-language quality is **uneven**; lower-resource EU languages trail the majors.
- Raw reasoning is **in-class rather than frontier** - it is a 9B (or 1.7B) model.
- Base checkpoints are **untuned research artifacts** and must not be deployed as assistants.
