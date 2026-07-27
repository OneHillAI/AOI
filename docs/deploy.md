# Deployment

The site at [ownershipindex.ai](https://ownershipindex.ai) is hosted on **Cloudflare Pages**,
connected to this repository. Cloudflare builds and publishes on every push to `main`. GitHub
Actions no longer deploys the site; `.github/workflows/build-site` only builds it as a CI check,
so a broken build or an inconsistent data set fails the commit before Cloudflare sees it.

## Cloudflare Pages project settings

Create one Pages project connected to `OneHillAI/AOI`:

| Setting | Value |
|---|---|
| Production branch | `main` |
| Root directory | `site` |
| Build command | `npm run build` |
| Build output directory | `dist` |
| Node version | `22` (pinned via `site/.node-version`) |

Cloudflare installs the dependencies in the root directory automatically, then runs the build
command there, so the output lands at `site/dist`. The site's `base` is the domain root, so no
path prefix is configured.

## Custom domain and DNS

1. In the Pages project, add the custom domain `ownershipindex.ai` (and `www` if wanted).
2. If the domain's DNS is on Cloudflare, adding the custom domain creates the records for you.
   Otherwise point a `CNAME` for `ownershipindex.ai` at the project's `*.pages.dev` hostname.
3. Cloudflare issues the TLS certificate once the domain resolves.

There is no `CNAME` file in the build output: that mechanism is specific to GitHub Pages, and
Cloudflare Pages sets the custom domain in its dashboard instead.

## Repository visibility

The repository is intended to be **public**. The project's premise is that the published site
is a projection of this repository, so what a reader sees and what they can audit are the same
thing (see [trust](https://ownershipindex.ai/trust/)). No credentials live in the repository:
Cloudflare Pages authenticates through its own GitHub app, not a committed token, and all
evidence links point at public documents. Keep it private only if a staging period is wanted
before launch; Cloudflare Pages builds either way.

Before flipping to public, confirm nothing sensitive is tracked (there is nothing today):

```bash
git ls-files | grep -Ei 'secret|token|\.env|credential' || echo "clean"
```
