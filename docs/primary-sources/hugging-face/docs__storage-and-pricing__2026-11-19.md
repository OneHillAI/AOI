# Hugging Face - storage, regions and pricing (re-read 2026-11-19, extracts)

Sources (all HTTP 200, read in full):
- https://huggingface.co/docs/hub/storage-limits.md
- https://huggingface.co/docs/hub/storage-regions.md
- https://huggingface.co/pricing (rendered page, read via WebFetch summary)
- https://huggingface.co/docs/hub/xet/index.md, https://huggingface.co/docs/hub/xet/legacy-git-lfs.md, https://huggingface.co/docs/hub/xet/security.md

## Storage plans (storage-limits doc)

| Account | Public storage | Private storage |
|---|---|---|
| Free user or org | "Best-effort" | 100GB |
| PRO | up to 10TB included, add-on, grants for impactful work | 1TB plus pay-as-you-go |
| Team org | 12TB base plus 1TB per seat, add-on | 1TB per seat plus pay-as-you-go |
| Enterprise org | 200TB base plus 1TB per seat, add-on; up to 1,000TB for large contracts | 1TB per seat plus pay-as-you-go |

- Public storage add-on: USD 12 per TB per month (1 to 20 TB tiers), USD 10 per TB per month at 50 TB. Private pay-as-you-go base USD 18 per TB per month, falling to USD 12 at 500TB+.
- Free public storage is described as generous but to be used "responsibly", with content that is useful to the community "as represented by numbers of likes or downloads, for instance". Mitigations against abuse exist.
- Repo recommendations: under 100k files, under 10k entries per folder, files under 200GB; "no single file will exceed 500GB" (hard limit). No per-repo size limit for models and datasets; uploads count against the account quota.
- Pricing page: PRO USD 9 per month; Team USD 20 per user per month; Enterprise USD 50 per user per month (talk to sales). Pricing page states "Egress and CDN included at no extra cost". No numeric download-bandwidth quota is published; Enterprise is described as having the highest bandwidth and API rate limits.
- The pricing page does not mention SOC 2 or ISO 27001.

## Regions (storage-regions doc)

Storage Regions are a Team and Enterprise feature. "For non-Team or Enterprise users, repositories are always stored in the US." Regions available: US and EU; Asia-Pacific and GCC (KSA) listed as coming soon.

## Storage backend

The Hub "has adopted Xet", a chunk-level deduplicating storage system; Git LFS "remains supported". Xet-backed repos keep the Git LFS pointer format; legacy clients are served through an LFS bridge; the LFS backend is Amazon S3 keyed by SHA-256. Xet security model: chunk contents are tied to repository permissions, so a user can only read chunks needed to rebuild files they may access.
