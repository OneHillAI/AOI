# Soofi access gate, licence tag and card text, re-read 2026-11-19

Sources: Hugging Face Hub API (`https://huggingface.co/api/models/Soofi-Project/<repo>`) for all
20 repos in the org, and the rendered model pages for Soofi-S-Base, Soofi-S-Instruct-Preview,
Soofi-S-Isar-Preview and Soofi-S-Rhine-Preview. exists: yes, retrieved: true (rendered page).
The raw files (`/raw/main/README.md`, `LICENSE`, `LICENSE.md`, `config.json`) return HTTP 401
"Access to model Soofi-Project/Soofi-S-Base is restricted. You must have access to it and be
authenticated to access it." So the weights and the raw card are not readable without an
approved account; the rendered page shows the card and the gate.

## Access status (Hub API, all 20 repos)

`gated: manual` on every repo (Base, Base-Megatron, Instruct/Isar/Rhine previews, their GGUF,
FP8 and EntQuant 2/3/4-bit builds). "manual" means each access request is approved by the
publisher. Gate text on the page, verbatim: "You need to agree to share your Hugging Face
information to access this model. This repository is publicly accessible, but you have to
accept the conditions to access its files and content." The conditions themselves are visible
only after logging in and were not readable.

Licence metadata on Base and the three previews: `license: other`, `license_name: closed-beta`.
The page header shows "License: closed-beta". No repo in the org lists a LICENSE file in its
file listing. Soofi-S-Base: created 2026-07-01, last modified 2026-07-18. Preview repos created
2026-06-16, last modified 2026-07-17. New since the September sweep: `Soofi-S-Base-Megatron`
(created 2026-08-23, gated manual, Megatron distributed-checkpoint `.distcp` files, no card).
No repo or release dated after 2026-08-24 was found. The Hub page header lists a collection
"Soofi S Beta Models" (last updated 2026-07-17).

## Card text (rendered page, Soofi-S-Base; identical disclaimer on the three previews)

"Closed Beta Release Disclaimer. This model is a beta preview and a research artifact. It is
not an open release. This checkpoint is an intermediate result, currently in a closed beta with
already selected partners to work on an improved version. It is under development and subject
to change based on partner feedback. Outputs, weights, and behavior may differ between
checkpoints. The final model will be released openly under a permissive license, without gated
access. We will share access details as soon as it is ready."

"License/Terms of Use: Will be released under a permissive license."
"This model is for research and development only (Preview)."
"Release Date: Hugging Face Hub - Preview at https://huggingface.co/Soofi-Project/Soofi-S-30B-A3B"
(that URL is a different repo name from the one that exists; no release date is given).

## Project site

https://www.soofi.info/ (WebFetch, 2026-11-19): "Soofi S befindet sich derzeit in der Beta- und
Entwicklungsphase." and "Ein öffentlicher Open-Source-Release ist geplant." and "Weitere
Informationen zum Veröffentlichungszeitpunkt werden bekannt gegeben, sobald dieser feststeht."
No licence stated, no date, no access-request form described, no dated news.

## Result

Marketing and binding text still conflict. The paper title, the organisation name and press
coverage say "open-source" (and the paper abstract says "Among fully open models, Soofi S
obtains the highest English and German evaluation scores"), while the model card says "It is not
an open release", the licence tag is "closed-beta", every repo is manually gated, and the
project site says the open-source release is "planned" with no date. The access status has not
changed since 2026-07-25.
