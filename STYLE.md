# Style

The house style for the AI Ownership Index, aligned with the OneHill Foundation prose rule.

## Dashes (the rule that changed)

Do not use em dashes or en dashes. This repository previously instructed authors to use em
dashes; that rule is reversed. Use one of these instead:

- a plain hyphen where a short joiner is wanted,
- a comma appositive for a parenthetical aside,
- or two sentences where the thought is separate.

Ranges use the word "to" (for example, "1 to 5"), not an en dash. The docs-lint workflow
fails the build on any em dash or en dash.

## Spelling

British spelling throughout. Licence is the noun, license is the verb. Prefer organisation,
behaviour, centre, catalogue, specialise, standardise, and similar forms.

## Plain, grounded prose (de-slop)

Write plainly and specifically. Avoid filler and marketing register. The docs-lint workflow
flags a banned-words list that includes, among others: delve, tapestry, seamless, leverage,
robust, realm, boasts, unleash, elevate, testament, furthermore, moreover, and underscore.
Prefer the concrete word. Every strong claim points at a primary document; see STANDARD.md.

Also delete these on sight, even though the linter does not catch them all:

- Throat-clearing: "it is important to note that", "it should be noted", "essentially",
  "basically", "as mentioned", "needless to say", "at its core".
- Filler openers and closers: "in today's fast-paced landscape", "in the world of", "when it
  comes to", "at the end of the day", "in conclusion", "overall" as a wrap-up.
- Empty intensifiers and marketing verbs: "unlock", "harness the power of", "supercharge",
  "cutting-edge", "state-of-the-art", "game-changing", "powerful" used without a measured claim.
- Padding structures: "not only X but also Y", "more than just", and rhetorical questions used
  to introduce a point.
- Hollow symmetry: "it is not X, it is Y" unless the contrast is real and load-bearing.

## Structure

Short sentences. One idea per sentence where possible. Headings in sentence case. Tables and
short lists are welcome where they carry data; prose carries argument.

## Lead with the decision

The first sentence of an item is the thing the adopter must know; the caveat comes second. Be
concrete: names, numbers, versions, licences, thresholds. State the verdict and the action,
and back every non-trivial claim with an evidence id.
