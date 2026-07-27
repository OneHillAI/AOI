import { defineCollection } from 'astro:content';
import { docsLoader } from '@astrojs/starlight/loaders';
import { docsSchema } from '@astrojs/starlight/schema';

// Starlight renders the authored prose pages under src/content/docs/ (home,
// methodology, glossary, classification, trust). The library (index ledger, entry
// sheets, and documentation sub-pages) is a custom Astro app-shell section under
// src/pages/library, built at request time from the repo's entry.yaml via
// src/lib/entries.ts - it is not a Starlight docs tree.
export const collections = {
  docs: defineCollection({ loader: docsLoader(), schema: docsSchema() }),
};
