# Hugging Face - Gated models documentation (re-read 2026-11-19, extracts)

Source: https://huggingface.co/docs/hub/models-gated.md (HTTP 200, read in full).

## Behaviour (paraphrased unless quoted)

- Gating is opt-in per repository ("By default, the model is not gated"). A gated model needs an access request; the requester's username and primary email are shared with the model authors unless the authors opt out of collecting them.
- Access requests are granted "to individual users rather than to entire organizations".
- Approval modes: automatic (any user gets access once they submit the request) or manual (authors accept or reject). Authors can reject, cancel or reset access at any time; a rejected user cannot re-request.
- Warning in the docs: model authors "have complete control over model access" and can block access without prior notice even after approval.
- Request flow can only be done from a browser while logged in. Downloading gated files requires authentication: logged-in browser session, or a user token in scripts (`hf auth login`, or `token=` parameter). Fine-grained tokens need the "Request access to gated repos" permission to submit requests via the API (security-tokens doc).
- Custom form fields and a custom prompt can be added through `extra_gated_fields` and `extra_gated_prompt` in the model card metadata (for example a checkbox acknowledging non-commercial use).
- Optional: gate access for the owning organisation's own members; Team and Enterprise organisations can use Gating Group Collections.
- New: an `extra_gated_eu_disallowed: true` metadata flag restricts gated downloads from EU countries, identified by IP address, for models whose licence or terms prohibit EU distribution.
- Programmatic approval via API is documented, including for flows where acceptance happens outside the Hub (Meta's Llama 2 launch and paid-access repositories are given as examples).

## Reading for this entry

Enforcement is per user at the download layer and authors control approval. The click-through is an access-request acceptance; the Hub does not itself verify that the user has understood or complied with the licence, and the docs describe automatic approval as the default once gating is on.
