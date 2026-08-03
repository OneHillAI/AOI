## ADDED Requirements

### Requirement: Only a release is scored; a family is never scored
Only a model RELEASE entry MUST be scored. A family MUST NOT be a scored unit: it MUST NOT carry a
score, grade, openness tier, licence, ownership verdict, or any dimension. A family exists only to
group and relate release entries. A release is a set of checkpoints whose openness tier, licence
classification, provenance posture and safety posture are uniform.

#### Scenario: A family has no score
- **WHEN** the registry or site presents the "Kimi" family
- **THEN** the family shows no score, grade, tier, licence, or ownership verdict
- **AND** each release under it (Kimi K2, Kimi K3) carries its own score and ownership verdict

### Requirement: Every entry carries a family relation, always
Every model entry MUST carry a `family` relation of `{id, name}` identifying the family it belongs
to. The relation MUST be present for every entry unconditionally, including a family that currently
has only one release (a single-release family still has the relation). It is NOT conditional on
whether the releases within the family differ.

#### Scenario: A single-release family still has the relation
- **WHEN** a family has exactly one release entry
- **THEN** that entry still carries its `family` relation, so it is grouped and shown under its
  family like every other entry

### Requirement: The schema requires the family relation
`schema/model.v2.schema.json` MUST define a required `family` object of `{ id: string, name: string }`
on every model entry, so no entry can validate without a family relation.

#### Scenario: An entry without a family fails validation
- **WHEN** a model entry omits `family`
- **THEN** `scripts/validate.py` reports a schema error

### Requirement: The site showcases every model and groups by family
The reader-facing site MUST show every release entry (the full model showcase) and, for each, its
family relation, and MUST let a reader navigate by family to the releases under it. This grouping is
always present, never conditional on whether a family has one release or several. The family node in
the site MUST NOT display a score.

#### Scenario: Navigate the showcase by family
- **WHEN** a reader opens the site
- **THEN** every release is listed, each tagged with its family
- **AND** opening a family shows the releases under it, each with its own ownership verdict, and the
  family node itself shows no score

### Requirement: An entry scores one uniform release
The registry MUST scope each entry to a single release. Co-released variants that share licence,
openness tier, provenance and safety posture MAY be grouped in one entry via `variants`. A checkpoint
that diverges on any scored attribute MUST NOT be aggregated into the same entry, because an entry
carries one tier, one licence block and one ownership verdict that must be true for every checkpoint
it covers.

#### Scenario: Uniform co-released variants may share an entry
- **WHEN** co-released checkpoints share licence, openness tier, provenance and safety posture, such
  as a Base and an Instruct of one generation
- **THEN** they MAY be represented as `variants` within one entry

### Requirement: Entries are named by release, not by a bare family name
An entry's `id` and `name` MUST identify the specific release. They MUST NOT use a bare family name
that hides which release is scored.

#### Scenario: No bare-family naming
- **WHEN** an entry scores Kimi K2
- **THEN** its `id` is `kimi-k2` and its `name` is "Kimi K2 (Moonshot AI)", not `kimi` or "Kimi"

### Requirement: Split a family into multiple entries only when releases diverge
A family MUST be split into multiple release entries when, and only when, its releases diverge on a
scored attribute: licence, openness tier, provenance posture or safety posture. Where all releases
share those attributes, a single entry MAY represent them, still carrying the `family` relation. The
family relation itself is always present either way; only the number of entries is conditional.

#### Scenario: Uniform family may stay one entry
- **WHEN** every release in a family shares one licence and openness tier
- **THEN** a single entry MAY represent them, still carrying the `family` relation

#### Scenario: Divergent family must be split
- **WHEN** any release in a family diverges on licence or openness tier, as with Mistral's Apache-2.0
  releases versus its MRL non-commercial releases
- **THEN** the family MUST be split so each entry scores a uniform release, each carrying the shared
  `family` relation
