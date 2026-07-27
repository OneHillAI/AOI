---
title: "Start here: what you are actually deciding"
description: What to look for when you adopt an open AI model, in plain language, without benchmarks.
---

You do not need to read benchmarks to choose an open model. The decision comes down to how much
you really **own** what you are adopting. This index scores exactly that as the **AI Ownership
Index (AOI)**, and it breaks into three plain questions.

Every model and provider page opens with a **Bottom line** box that answers these three at a
glance, and closes with the full, sourced **Ownership verdict**.

## 1. Can it be restricted?

The worry: can someone stop you doing what you want with it, now or later? Closed services can
change their terms, add usage caps, or cut you off.

What to look for: an **open-weight** model you can download removes most of this risk, because the
weights are already in your hands. The catch is the **licence**. Some are fully permissive (MIT,
Apache) with no user caps or field-of-use limits. Others attach conditions, for example a
monthly-active-user threshold or a restriction on certain uses. Each entry states the licence in
one line and links the full text.

Where to check it: the **Can it be restricted?** line in the Bottom line box, and the **Use and
modify freely** factor in the Ownership verdict.

## 2. What happens to your data?

The worry: does using this expose or give away your data? This is where open and hosted differ the
most.

What to look for: a model you **self-host** runs on your own hardware, so your data never leaves
and nothing is sent back. A **hosted provider** is different: you are trusting their terms, so the
questions become whether they train on your inputs, how long they keep them, whether your data and
outputs stay yours, and where it is processed. The index reads the provider's actual Terms and
Privacy Policy, not their marketing, and says plainly when the two disagree.

Where to check it: the **What happens to your data?** line in the Bottom line box, and the **Does
not extract your data** factor in the Ownership verdict.

## 3. Will you be locked in?

The worry: will you get trapped with one provider and be unable to leave?

What to look for: **open weights are portable**. The same checkpoint runs on many providers or on
your own machine, so you can move. With a hosted API, an OpenAI-compatible interface makes moving
cheap; a proprietary interface means rewriting your integration, though the underlying open model
still runs elsewhere.

Where to check it: the **Will you be locked in?** line in the Bottom line box, and the
**Transparency** factor in the Ownership verdict.

## A note on cost

For a **self-hosted open model**, the cost is your own hardware, not a metered bill that can creep
up, and there is no vendor who can raise a per-token price on you. Hosted providers do charge per
use; each provider page records the pricing model.

## Where this goes next

A later version will show how the best open options compare to the closed frontier, framed on
**ownership** rather than raw performance: how much of a frontier-grade capability you can now have
on terms you actually own.
