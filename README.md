# honcho-probe

A twenty-minute probe of Honcho (managed tier, Python SDK) on 2026-09-25, before a conversation with Plastic Labs.
Not a benchmark. One seeded peer, three questions, two reasoning levels, three runs each, then the representation.
Afterwards I read the server code (commit 0ba0db5, v3.2.1) to explain what I saw; those notes are marked [code].

## Setup

A fictional peer "maya" with ten messages: a location that changes (Boston -> Chicago), one trait that is implied
but never stated (prefers the lab to the stage), and no information about movies.

    pip install honcho-ai
    export HONCHO_API_KEY=...
    python probe.py      # seeds, waits 120s, runs 3 questions x 2 levels x 3 runs
    python check.py      # dumps representation, card, context (run a few minutes later)
    python dream.py      # schedules a dream manually, waits, re-pulls

## Questions

- update:   "Where does Maya live right now?"                 (answer key: Chicago)
- absent:   "What is Maya's favorite movie?"                   (answer key: unknown; should abstain)
- implied:  "Is Maya more of an introvert or extrovert?"       (no key; watching whether it deduces and hedges)

## What happened (raw output in results.md)

| probe   | minimal                                   | high                                              |
|---------|-------------------------------------------|---------------------------------------------------|
| update  | 2/3 Chicago, 1/3 "no memory of location"  | 3/3 Chicago                                       |
| absent  | 3/3 abstained                             | 3/3 abstained                                     |
| implied | 3/3 declined to infer                     | 2/3 "introverted, moderate confidence", 1/3 hedged |

With `include_evidence=True`, `evidence.conclusions` was empty on all 18 calls; I did not print `evidence.messages`.
High-level answers cited "the most recent conversation from September 25, 2026", i.e. raw messages.

Representation at ~120s: empty. A few minutes later: nine explicit observations, all with one identical timestamp,
Boston and Chicago both present, no deductive conclusions, peer card None.

## What the code says [code]

- Observations from one deriver batch all inherit the created_at of the batch's latest message
  (src/deriver/deriver.py ~207-215). Per-observation source time is not kept. That is the identical timestamp.
- Deriver batches wait for 512 tokens or 30 minutes unless FLUSH_ENABLED (src/config.py). That is the empty read at 120s.
- Ingest dedup is near-duplicate text only (cosine <= 0.05). Contradictions are kept. Supersession is an LLM
  instruction in the dreamer's deduction prompt keyed on "different values at different times"
  (src/dreamer/specialists.py). With one batch timestamp, that rule has no time signal to use.
- Dreaming needs >= 50 new observations plus 60 idle minutes. Nine observations never dream; the peer card is
  written only by the dreamer, so None is expected.
- All reasoning levels use the same default model; they differ in tool rounds and output cap (minimal: 1 round,
  250 tokens; high: 4 rounds). The dialectic prompt instructs the model to abstain rather than infer. So the
  minimal/high difference on the implied trait is a search-budget effect against an anti-inference prompt,
  not a capability switch, which is why it is inconsistent at high.
- tests/bench scores LongMemEval (with an abstention judge for _abs items), LoCoMo, BEAM, OOLONG, with
  --reasoning-level and --skip-dream flags. Nothing scores representation quality, provenance, or supersession.

## What I take from it

1. End-to-end chat scores measure the dialectic agent over messages plus whatever conclusions exist. The
   representation can be empty or contradictory and the score barely moves. The representation is the object
   I'd measure first: before and after dreaming, with the agent off.
2. Provenance: per-observation timestamps are the input the dreamer's own supersession rule needs. Keeping the
   source message's created_at on each observation is a small change that makes "knowledge update" testable.
3. The minimal-level miss was a false negative (retrieval), not a stale fact (consolidation). Score those separately.
4. Deduction behavior varies with reasoning level for budget reasons, not model reasons. If the product wants
   inference at some levels and abstention at others, that should be an explicit switch and a scored behavior.

Related open issues: #1027 (minimal deriver stores ephemeral dated observations) and #1082 (conclusions query
ranks recent/generic over relevant).

## After a manual dream

See dream_out.md.

## Caveats

n=3 per cell. One peer. Managed tier, defaults otherwise. The code notes are from reading the open-source server;
the managed deployment may differ in config. Nothing here is a claim about the published benchmarks.

## After a manual dream (dream_out.md)

`schedule_dream` ran on the managed tier. Afterwards: the explicit list dropped from nine to six (Boston, the Charles
run, and "sad to lose the river runs" were removed), five deductive observations appeared with premises, including
one that states outright "maya's current location and job supersede her Boston situation", four inductive patterns
with confidence tags (low/medium/high), and a peer card with Location: Chicago. `include_evidence` now returned 15
conclusions and zero messages, so the answer came from the representation alone.

Two things worth noting. Every observation still carries the same timestamp; dreaming resolved Boston vs Chicago
from the wording ("moving next week", "settled now"), not from time. The timestamp fix matters for the case where
the wording doesn't carry the order. And one inductive pattern is tagged [high] confidence — "makes major life
changes in rapid succession" — from a single ten-message episode. Whether that confidence is earned is exactly the
kind of fidelity question a representation-level eval should score.
