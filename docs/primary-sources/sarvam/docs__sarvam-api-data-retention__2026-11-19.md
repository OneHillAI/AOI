# docs / Sarvam platform data retention documentation

source_url: https://docs.sarvam.ai/api/platform/data-retention.md
retrieval_date: 2026-11-19
exists: yes
retrieved: true

Verbatim extracts (publisher text, not edited). Notes by OneHill are marked NOTE.

```
> Control how long Sarvam keeps your data. Set a workspace-wide default retention period, and override it per product for Model APIs and Voice Agents.

**Data retention is set per workspace**, on **Settings → Workspace → Data policy**. It controls how long Sarvam keeps the data your workspace generates before deleting it automatically.

#### [Open Data policy](https://indus.sarvam.ai/settings/workspace/data-policy?ref=docs)

Log in, then go to Settings → Workspace → Data policy for the current workspace.

> **Warning**
>
> Until an Owner sets a retention period, your workspace's data is retained indefinitely. Nothing is deleted automatically until a period is configured.

> **Note**
>
> Only a workspace's org **Owner** can change data policy settings, including retention and [public signed URLs](#public-signed-urls-for-call-recordings). Other roles can view the current settings but the controls are disabled for them.

## Workspace default

Every workspace has one retention period that applies to all its data unless a product overrides it.

Save shows a confirmation dialog with the old and new period before it takes effect.

> **Warning**
>
> Changing the retention period only affects data going forward. It is not retroactive: data already stored keeps whatever retention applied when it was created, and nothing already stored is deleted early or extended by changing the setting.

## Product overrides

Below the workspace default, **Product overrides** lists retention controls per product for the products your workspace uses.

| Product        | Retention override |

>
> Zero data retention (**No retention**, 0 days) is supported for **Model APIs**. It is not yet supported for **Voice Agents** - picking **No retention** there fails with an error naming the shortest supported period to use instead.

## Retention periods offered

| Period                |
| --------------------- |
| No retention (0 days) |
| 1 day                 |
| 15 days               |
| 1 month (30 days)     |
```

NOTE: this documentation says data is retained indefinitely until an Owner sets a period, while the binding Privacy Policy retention table says Your Content has a default of 30 days after last access (see privacy_policy__sarvam-privacy-policy-2026-07-29). Docs are not a binding document; the two disagree.
