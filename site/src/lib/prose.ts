/** Render a markdown string to HTML at build time using Astro's own markdown
 * processor (the same remark/rehype pipeline Starlight uses), so the folded-in
 * domain prose matches the rest of the site. The processor is created once. */
import { createMarkdownProcessor, type MarkdownProcessor } from '@astrojs/markdown-remark';

let processor: MarkdownProcessor | null = null;

export async function renderMarkdown(md: string): Promise<string> {
  if (!md) return '';
  if (!processor) processor = await createMarkdownProcessor({ gfm: true, smartypants: false });
  const { code } = await processor.render(md);
  return code;
}
