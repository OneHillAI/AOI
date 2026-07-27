/**
 * Build-time data layer for the AI Ownership Index library.
 *
 * Reads the repository's source-of-truth records (../models/<id>/entry.yaml and
 * ../inference-providers/<id>/entry.yaml) and maps each onto the four-factor
 * "entry sheet" record the custom Astro pages render. The four ownership factors
 * and the evidence/documentation blocks are uniform across models and providers;
 * only the seven scored dimensions differ, so the dimension->factor grouping is
 * per type. Nothing here re-scores: levels, ratings and dimension scores are read
 * straight from the validated YAML (rubric 1.1).
 */
import fs from 'node:fs';
import path from 'node:path';
import yaml from 'js-yaml';

const SITE = process.cwd();
const REPO = path.resolve(SITE, '..');

export type Rating = 'strong' | 'moderate' | 'weak';
export type Level = 'none' | 'limited' | 'partial' | 'substantial' | 'full';
export const SCALE: Level[] = ['none', 'limited', 'partial', 'substantial', 'full'];
export const DOMAINS = ['assess', 'implement', 'use', 'support'] as const;
export type Domain = (typeof DOMAINS)[number];

const FACTOR_META = [
  { key: 'use_modify', short: 'Use & modify', gloss: "what you're allowed to do", name: 'Use and modify freely',
    q: { model: 'Can you run, modify and adapt it with no gate and no field-of-use trap?', provider: 'Can you use it freely and leave without lock-in?' } },
  { key: 'transparency', short: 'Transparency', gloss: 'what you can see', name: 'Transparency',
    q: { model: 'Do you know what it is: weights, training, behaviour, and legible terms?', provider: 'Are the binding terms published, legible and independently checkable?' } },
  { key: 'reliability', short: 'Reliability', gloss: 'dependable and good enough', name: 'Reliability',
    q: { model: 'Is it reliable and good enough for the job?', provider: 'Does it stay up and stay secure?' } },
  { key: 'data_control', short: 'Data control', gloss: 'stays yours', name: "Doesn't extract your data",
    q: { model: 'Does running it keep your knowledge and data yours?', provider: 'Do the binding terms keep your data and IP yours?' } },
] as const;

const DIM_MAP: Record<string, Record<string, string[]>> = {
  model: {
    use_modify: ['openness', 'legal'],
    transparency: ['provenance', 'governance'],
    // Ownership reliability is dependability + safety only; raw performance/capability
    // feeds the AOI score, not this factor (see methodology/ownership.md).
    reliability: ['operational', 'safety'],
    data_control: [],
  },
  provider: {
    use_modify: ['transparency_lockin', 'cost'],
    // Provider transparency is structural (were the binding terms read and legible),
    // not a scored dimension - it maps to the read/unverified evidence, mirroring how
    // the factor is actually justified. Compliance certifications sit under reliability
    // (independent attestation that it will not fail you).
    transparency: [],
    reliability: ['reliability', 'security', 'compliance'],
    data_control: ['data_governance', 'residency'],
  },
};

// Dimension weights, mirroring scripts/score.py. Headline = round(100 * sum(w * score/5)),
// so each dimension contributes (weight * score * 20) points out of 100.
const WEIGHTS: Record<string, Record<string, number>> = {
  model: { openness: 0.18, provenance: 0.16, legal: 0.16, safety: 0.16, performance: 0.14, operational: 0.12, governance: 0.08 },
  provider: { data_governance: 0.24, compliance: 0.18, residency: 0.16, security: 0.14, reliability: 0.12, transparency_lockin: 0.1, cost: 0.06 },
};

const DIM_INFO: Record<string, { label: string; gloss: string }> = {
  // model
  openness: { label: 'Openness', gloss: 'how much is released - weights, data, code, licence - and how freely' },
  legal: { label: 'Legal', gloss: 'how permissive and clean the licence is for real commercial use' },
  provenance: { label: 'Provenance', gloss: 'how well we can trace and verify what went into the model' },
  governance: { label: 'Governance', gloss: 'how accountable and well-documented the publisher is' },
  performance: { label: 'Performance', gloss: 'how capable it is relative to its class' },
  operational: { label: 'Operational', gloss: 'how practical it is to run, serve and maintain in production' },
  safety: { label: 'Safety', gloss: 'whether misuse risks are evaluated and guardrails are provided' },
  // provider
  transparency_lockin: { label: 'Transparency & lock-in', gloss: 'how portable it is and how easily you can leave' },
  cost: { label: 'Cost', gloss: 'how the pricing model compares and how predictable it is' },
  compliance: { label: 'Compliance', gloss: 'which independent certifications and attestations it holds' },
  reliability: { label: 'Reliability', gloss: 'whether it stays up, with an SLA and status history' },
  security: { label: 'Security', gloss: 'the controls protecting your traffic and data' },
  data_governance: { label: 'Data governance', gloss: 'retention, training-on-inputs and data ownership' },
  residency: { label: 'Residency', gloss: 'where your data is processed and stored' },
};

const DOC_LABEL: Record<string, string> = {
  license: 'Licence', terms: 'Terms of service', privacy_policy: 'Privacy Policy',
  dpa: 'Data Processing Addendum', model_card: 'Model card', docs: 'Documentation',
  marketing: 'Vendor announcement', third_party: 'Third-party analysis', reference: 'Reference',
};

// Domain -> which factors that documentation domain projects (handover section 3c).
export const DOMAIN_FACTORS: Record<Domain, string[]> = {
  assess: ['use_modify', 'transparency'],
  implement: ['data_control', 'reliability'],
  use: ['reliability'],
  support: ['transparency'],
};
export const DOMAIN_QUESTION: Record<Domain, string> = {
  assess: 'Can you own it?',
  implement: 'Can you run it?',
  use: 'Is it good enough?',
  support: 'Will it last?',
};

function cap(s: string) { return s.charAt(0).toUpperCase() + s.slice(1); }
function firstSentence(s: string) {
  const t = String(s || '').replace(/\s+/g, ' ').trim();
  const m = t.match(/^(.*?[.!?])(\s|$)/);
  return (m ? m[1] : t).trim();
}
function pct(scores: any[]): number {
  const v = scores.filter((n) => typeof n === 'number');
  return v.length ? Math.round(v.reduce((a, b) => a + b, 0) / v.length) : 0;
}

/** Plain-language reason a level sits where it does, naming the specific factor(s)
 * that set the ceiling. Rendered after the bold "Floor-weighted, not averaged."
 * lead in the entry sheet, so it starts mid-thought. */
function floorSentence(level: Level, factors: Record<string, any>): string {
  const named = (k: string) => FACTOR_META.find((f) => f.key === k)!.short.toLowerCase();
  const list = (a: string[]) => (a.length <= 1 ? a[0] || '' : `${a.slice(0, -1).join(', ')} and ${a[a.length - 1]}`);
  const weak = Object.entries(factors).filter(([, v]) => v.level === 'weak').map(([k]) => named(k));
  const mod = Object.entries(factors).filter(([, v]) => v.level === 'moderate').map(([k]) => named(k));
  const gating = Object.entries(factors)
    .filter(([k, v]) => (k === 'use_modify' || k === 'data_control') && v.level === 'moderate')
    .map(([k]) => named(k));

  if (level === 'full')
    return 'Nothing is weak or even moderate, so nothing sets a ceiling: you can use it, see it, rely on it and keep your data - outright.';
  if (weak.length)
    return `${cap(list(weak))} ${weak.length > 1 ? 'are' : 'is'} weak, and the weakest factor sets the ceiling, so the verdict stays ${level} however strong the rest.`;
  if (level === 'substantial')
    return `Nothing is weak and both use & modify and data control are strong, so the floor is high; ${list(mod)} ${mod.length > 1 ? 'sit' : 'sits'} at moderate, which is what keeps it short of full.`;
  if (level === 'partial' && gating.length)
    return `Nothing is weak, but ${list(gating)} ${gating.length > 1 ? 'are' : 'is'} only moderate, so it misses the bar for substantial - strong on both use & modify and data control - and lands at partial.`;
  if (level === 'partial')
    return `Nothing is weak, but ${list(mod)} ${mod.length > 1 ? 'sit' : 'sits'} at moderate with real unknowns, which holds the verdict at partial rather than substantial.`;
  return `${cap(list(weak.length ? weak : mod))} sets the ceiling, so the verdict is ${level}.`;
}

function readYaml(file: string): any { return yaml.load(fs.readFileSync(file, 'utf8')); }

function listEntries(dir: string, type: 'model' | 'provider') {
  const root = path.join(REPO, dir);
  if (!fs.existsSync(root)) return [];
  return fs.readdirSync(root)
    .filter((id) => fs.existsSync(path.join(root, id, 'entry.yaml')))
    .map((id) => ({ id, type, dir, data: readYaml(path.join(root, id, 'entry.yaml')) }));
}

function buildFactors(e: any, type: 'model' | 'provider') {
  const dims = e.score?.dimensions || {};
  const map = DIM_MAP[type];
  return FACTOR_META.map((meta, i) => {
    const src = e.ownership?.factors?.[meta.key] || {};
    const rating: Rating = (src.level || 'moderate') as Rating;
    const dimKeys = map[meta.key] || [];
    const subscores = dimKeys
      .filter((dk) => dims[dk])
      .map((dk) => ({
        name: DIM_INFO[dk]?.label || dk,
        score: dims[dk].score,
        max: 5,
        exp: DIM_INFO[dk]?.gloss || '',
        detail: firstSentence(dims[dk].rationale || ''),
      }));
    let struct: string | null = null;
    if (subscores.length === 0) {
      if (meta.key === 'data_control') {
        struct = 'Not a scored AOI dimension. For a self-hosted model, data-control is a structural property of running the weights yourself, strong by default unless the model phones home or the licence claws back rights. For a hosted API this factor is the retention + train-on-inputs + residency read, scored from the binding terms.';
      } else if (meta.key === 'transparency') {
        struct = 'Not a scored AOI dimension. For a hosted provider, transparency is whether the binding terms are published, legible and were actually read - the read/unverified evidence below, not a certification. A strong rating here must trace to a retrieved binding document.';
      }
    }
    return {
      id: `f${i + 1}`, n: i + 1, key: meta.key, rating,
      short: meta.short, gloss: meta.gloss, name: meta.name,
      question: meta.q[type],
      lede: src.rationale || '',
      subscores, struct,
    };
  });
}

function identity(e: any, type: 'model' | 'provider') {
  if (type === 'model') {
    const lic = e.openness?.license || e.license || {};
    const ctx = (e.variants || []).map((v: any) => v.context_window).filter(Boolean);
    return [
      { k: 'Publisher', v: `${e.publisher?.name || 'Unknown'}${e.publisher?.country ? ` (${e.publisher.country})` : ''}` },
      { k: 'Openness', v: e.openness?.tier || 'unknown' },
      { k: 'Licence', v: lic.name || lic.spdx || lic.classification || 'see licence' },
      { k: 'Context', v: ctx.length ? [...new Set(ctx)].join(' / ') : 'varies by variant' },
    ];
  }
  return [
    { k: 'HQ', v: e.hq_country || 'Unknown' },
    { k: 'Serves', v: `${(e.models_served || []).length} open model families` },
    { k: 'Pricing', v: e.pricing?.model || 'see pricing' },
    { k: 'API', v: e.lock_in?.openai_compatible_api ? 'OpenAI-compatible' : 'proprietary' },
  ];
}

function sources(e: any) {
  return (e.evidence || []).map((ev: any) => ({
    doc: DOC_LABEL[ev.doc_type] || cap(ev.doc_type || 'source'),
    status: ev.retrieved ? 'read' : 'unverified',
    date: ev.date || '',
    claim: firstSentence(ev.claim || ''),
  }));
}

export function toRecord(item: { id: string; type: 'model' | 'provider'; dir: string; data: any }) {
  const e = item.data;
  const type = item.type;
  const nameParts = String(e.name || item.id).match(/^(.*?)\s*\((.*)\)\s*$/);
  const title = type === 'model' && nameParts ? nameParts[1].trim() : e.name || item.id;
  const family = type === 'model' && nameParts ? nameParts[2].trim() : '';
  const level: Level = (e.ownership?.level || 'partial') as Level;
  const factors = buildFactors(e, type);
  const dossier = DOMAINS.map((d) => ({ k: cap(d), v: `${Math.round(e.documentation?.[d]?.completeness ?? 0)}%` }));
  const docsGauge = pct(DOMAINS.map((d) => e.documentation?.[d]?.completeness ?? null));
  const idf = identity(e, type);
  if (family) idf.splice(1, 0, { k: 'Family', v: family });
  const dims = e.score?.dimensions || {};
  const calc = Object.entries(WEIGHTS[type]).map(([k, weight]) => {
    const s = dims[k]?.score ?? 0;
    return { name: DIM_INFO[k]?.label || k, score: s, weight, points: Math.round(weight * s * 20 * 10) / 10 };
  });
  return {
    id: item.id,
    type,
    dir: item.dir, // 'models' | 'inference-providers'
    kicker: type === 'model' ? 'Model' : 'Inference provider',
    title,
    name: e.name || item.id,
    summary: firstSentence(e.summary || ''),
    identity: idf,
    grade: e.score?.grade || '',
    score: e.score?.headline ?? null,
    opennessTier: type === 'model' ? (e.openness?.tier || '') : '',
    licence: type === 'model' ? (e.openness?.license?.name || e.openness?.license?.classification || '') : (e.hq_country || ''),
    publisher: type === 'model' ? (e.publisher?.name || '') : (e.name || item.id),
    regionCode: type === 'model' ? (e.publisher?.country || '') : (e.hq_country || ''),
    ownership: {
      level,
      scale: SCALE,
      aoi: `AOI ${e.score?.grade || ''} · ${e.score?.headline ?? ''}/100`,
      verdict_sentence: e.ownership?.verdict || '',
      floor: floorSentence(level, e.ownership?.factors || {}),
    },
    factors,
    calc,
    hardFlags: e.score?.hard_flags || [],
    dossier,
    docsGauge,
    sources: sources(e),
  };
}

/** Build-step validation (handover section 5): a factor rated `strong` on
 * transparency or data-control must trace to a retrieved binding document, never a
 * marketing page. Throws at build time so a violation cannot ship. */
function validate(items: { id: string; type: string; data: any }[]) {
  const problems: string[] = [];
  for (const { id, data } of items) {
    const factors = data.ownership?.factors || {};
    const hasRead = (data.evidence || []).some((ev: any) => ev.retrieved);
    for (const key of ['transparency', 'data_control']) {
      if (factors[key]?.level === 'strong' && !hasRead) {
        problems.push(`${id}: ${key} rated 'strong' but no retrieved (read) evidence document`);
      }
    }
  }
  if (problems.length) throw new Error(`AOI entry validation failed:\n  - ${problems.join('\n  - ')}`);
}

export function getAllEntries() {
  const items = [
    ...listEntries('models', 'model'),
    ...listEntries('inference-providers', 'provider'),
  ];
  validate(items);
  return items.map(toRecord).sort((a, b) => (b.score ?? 0) - (a.score ?? 0));
}

export function getEntry(dir: string, id: string) {
  return getAllEntries().find((r) => r.dir === dir && r.id === id) || null;
}

/** Raw domain prose for a sub-page: the long-form <domain>.md for an entry, with
 * the leading H1 + italic tagline and the `<!-- item: KEY -->` section markers
 * stripped (the markers were badge anchors for the old generator). Returns '' if
 * the file is absent. */
export function getDomainMarkdown(dir: string, id: string, domain: Domain): string {
  const file = path.join(REPO, dir, id, `${domain}.md`);
  if (!fs.existsSync(file)) return '';
  let md = fs.readFileSync(file, 'utf8');
  const firstItem = md.indexOf('<!-- item:');
  if (firstItem > -1) {
    md = md.slice(firstItem);
  } else {
    md = md.replace(/^#[^\n]*\n/, '').replace(/^\s*_[^]*?_\s*\n/, '');
  }
  return md.replace(/<!--\s*item:[^>]*-->\s*\n?/g, '').trim();
}
