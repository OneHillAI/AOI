// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// Production is served at the root of ownershipindex.ai (Cloudflare Pages; see
// docs/deploy.md), so there is no base path and internal links resolve from '/'.
// For a pre-launch preview on a project sub-path (for example GitHub Pages at
// onehillai.github.io/AOI), set SITE_BASE=/AOI (and SITE_URL) at build time; every
// internal link is built through import.meta.env.BASE_URL, so both resolve correctly.
const SITE_BASE = process.env.SITE_BASE || undefined;
const SITE_URL = process.env.SITE_URL || 'https://ownershipindex.ai';
const OG_IMAGE = `${SITE_URL}${SITE_BASE || ''}/og/aoi-share.png`;
const OG_ALT = 'AI Ownership Index: who really owns the AI you use?';
export default defineConfig({
  site: SITE_URL,
  ...(SITE_BASE ? { base: SITE_BASE } : {}),
  trailingSlash: 'ignore',
  integrations: [
    starlight({
      title: 'AI Ownership Index',
      description:
        'Independent, continuously-updated documentation for open-source AI models and the providers that serve them: assess, implement, use, and support, with sourced provenance and completeness on every entry.',
      customCss: ['./src/styles/custom.css'],
      head: [
        { tag: 'meta', attrs: { property: 'og:image', content: OG_IMAGE } },
        { tag: 'meta', attrs: { property: 'og:image:width', content: '1200' } },
        { tag: 'meta', attrs: { property: 'og:image:height', content: '630' } },
        { tag: 'meta', attrs: { property: 'og:image:alt', content: OG_ALT } },
        { tag: 'meta', attrs: { name: 'twitter:image', content: OG_IMAGE } },
        { tag: 'meta', attrs: { name: 'twitter:image:alt', content: OG_ALT } },
      ],
      components: {
        Footer: './src/components/StarlightFooter.astro',
        SiteTitle: './src/components/StarlightSiteTitle.astro',
      },
      social: [
        { icon: 'github', label: 'GitHub', href: 'https://github.com/OneHillAI/AOI' },
        { icon: 'email', label: 'Contact', href: 'mailto:contact@ownershipindex.ai' },
      ],
      sidebar: [
        { label: 'Start here', link: '/start-here/' },
        { label: 'Overview', link: '/' },
        // The library (index ledger, entry sheets, documentation sub-pages) is now a
        // custom Astro app-shell section under src/pages/library, generated from the
        // repo's entry.yaml records - it is not a Starlight docs tree.
        { label: 'Library', link: '/library/' },
        {
          label: 'How this works',
          items: [
            { label: 'Why trust this', link: '/trust/' },
            { label: 'Glossary', link: '/glossary/' },
            { label: 'Classification', link: '/classification-matrices/' },
            { label: 'Methodology', link: '/methodology/' },
            { label: 'How we source (provenance)', link: '/methodology/provenance/' },
            { label: 'Documentation taxonomy', link: '/methodology/taxonomy/' },
          ],
        },
      ],
    }),
  ],
});
