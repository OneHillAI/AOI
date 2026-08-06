## ADDED Requirements

### Requirement: Provider entries record contractual confidentiality over customer data
Every inference-provider entry MUST record `data_governance.confidentiality`, the contractual
confidentiality/NDA-grade duty over customer data in the provider's STANDARD terms, as one of
`mutual` | `explicit` | `functional_only` | `none` | `disclaimed` | `adverse` | `unknown`. It records
the standard terms, not an enterprise-negotiated exception; `confidentiality_caveats` MAY carry the
clause-level nuance (survival term, conditional drafting, aggregated-data carve-out).

#### Scenario: A provider that disclaims confidentiality is recorded as such
- **WHEN** a provider's standard ToS states the parties have no confidentiality obligations unless
  separately agreed in writing
- **THEN** its entry records `confidentiality: disclaimed`, not `functional_only`

#### Scenario: Adverse confidentiality terms are recorded as adverse
- **WHEN** a provider's standard terms deem customer content non-confidential and take a broad licence
  over it
- **THEN** its entry records `confidentiality: adverse`

### Requirement: Confidentiality informs the data_governance dimension
`confidentiality` MUST be treated as an input to the `data_governance` dimension. An express duty
(`mutual` or `explicit`) is a positive; `disclaimed` or `adverse` is a material negative that caps
`data_governance` (an adverse posture, all else equal, cannot sit at the top of the scale). It MUST
NOT create a new dimension or change dimension weights.

#### Scenario: An adverse confidentiality posture caps data_governance
- **WHEN** a provider is otherwise strong on retention and training but its standard terms are
  `adverse` on confidentiality
- **THEN** the `data_governance` rationale names the confidentiality posture and the score reflects
  the cap

### Requirement: Provider entries record dedicated / single-tenant availability
Every inference-provider entry MUST record `dedicated_availability`, the single-tenant / dedicated /
on-prem / air-gapped deployment availability today, as one of `self_serve` | `available` |
`enterprise_only` | `coming_soon` | `none` | `unknown`, with `dedicated_notes` MAY-carrying the
specifics (on-prem, air-gapped, GPU clusters, BYOC). It records what is actually available, not what
is announced.

#### Scenario: An announced-but-unshipped dedicated product is coming_soon
- **WHEN** a provider advertises a dedicated product with no contract terms, docs, or pricing
- **THEN** its entry records `dedicated_availability: coming_soon`, not `available`

### Requirement: Dedicated availability informs the transparency_lockin dimension
`dedicated_availability` MUST be treated as an input to the `transparency_lockin` dimension: shipped
self-serve dedicated, or on-prem / air-gapped isolation, strengthens control and exit;
`enterprise_only` or `coming_soon` does not. It MUST NOT create a new dimension or change dimension
weights.

### Requirement: Adding these inputs triggers a provider re-score at rubric 1.2
Introducing the two inputs MUST trigger a re-score of every provider entry against them and the
current primary sources; provider `score.rubric_version` MUST move to `1.2`, and every dimension
score that changes MUST be recorded in the entry changelog.

#### Scenario: A field addition re-scores affected entries
- **WHEN** the confidentiality and dedicated-availability fields are added
- **THEN** every provider entry is reviewed and re-scored where the new inputs change the picture,
  with each change recorded
