# Ollama - releases and versioning (read 2026-11-19)

Source: https://api.github.com/repos/ollama/ollama/releases and /tags (read via GitHub REST API); notes
quoted are from the release bodies at https://github.com/ollama/ollama/releases. Repo state: MIT licence,
about 187.6K stars, last push 2026-11-18.

## Current versions
- Latest stable: v0.40.16, published 2026-11-09. Pre-release: v0.40.17-rc1, published 2026-11-10 (MLX and
  llama.cpp bumps, MLX concurrent generation).
- The v0.40 line began with v0.40.0 on 2026-09-25 and shipped 17 point releases by 2026-11-10 (v0.40.1
  2026-10-07, v0.40.2 2026-10-08, ... v0.40.16 2026-11-09). A v0.35.x branch was still released after
  v0.40.0 (v0.35.0 2026-09-28, v0.35.1 2026-09-29). Earlier lines: v0.34.0 2026-09-05, v0.33.0 2026-08-21,
  v0.32.15 2026-08-19. Tag dates (commit dates): v0.30.10 2026-06-17, v0.30.11 2026-06-26, v0.31.0 2026-06-29,
  v0.32.0 2026-07-13. Cadence is one to four releases per week; the release body is a short feature list and
  has no security section.
- The previous stored entry named no version. The downstream observation (0.30.10 refusing new models) is
  not stated in any release note or doc read; see `docs__registry-manifests-and-library-licences__2026-11-19.md`.

## Notes relevant to this index (verbatim or close paraphrase)
- v0.40.0: "Models run on MLX on Apple Silicon by default" (see the registry file).
- v0.40.2: background upgrade of previously downloaded models to the llama.cpp runner, original kept as a
  backup, re-pull needed after downgrade below 0.40.
- v0.40.1: "cmd: remove account step from CLI onboarding"; "server: proxy cloud usage and balance APIs".
- v0.40.4: "Updated README and documentation with clearer privacy and cloud-services wording"; "`ollama launch`
  can now be used with usage credits without upgrading to a paid plan".
- v0.40.5: "Decision models are now available on cloud - use `clef:cloud` and `clef-flash:cloud` to run decision
  models through ollama.com cloud without pulling them locally"; clearer cloud error messages.
- v0.40.7: "Requests routed to remote models are now cancelled on ollama.com when the client disconnects".
- v0.40.16: `ollama launch` "explains when a cloud model has been retired"; adds the "ripple-preview" model
  from Ricursive Intelligence (65B dense).
- v0.35.1: "Modelfiles now support `CAPABILITY` declarations, so model creators can explicitly declare what a
  model can do."
- v0.17.1 (2026-02-24, named by NVD as the fix for CVE-2026-7482): notes do not mention a security fix.
- No release note in v0.30 to v0.40.16 mentions model signing, publisher verification, malware scanning or an
  advisory.

## Support channels (site footer and repo)
ollama.com footer links: Blog, Docs, GitHub, Discord, X (Twitter), Support, Meetups, Careers. Security
reports: GitHub advisories (SECURITY.md). Account and billing: support@ollama.com (Terms Sec 3, cloud docs);
general: hello@ollama.com.
