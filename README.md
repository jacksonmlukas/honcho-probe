# honcho-probe

A small, hand-run probe of [Honcho](https://github.com/plastic-labs/honcho) (managed tier, `honcho-ai` Python SDK), 25 Sep 2026.

Not a benchmark. One seeded peer, three questions, two reasoning levels, three runs each, then the stored representation before and after a manually scheduled dream.

**Question:** does a correct answer from Honcho mean the representation is correct, or only that the dialectic agent is?

## Setup

A fictional peer, `maya`, with ten messages containing:

- a fact that changes: she moves from Boston to Chicago
- a fact that is implied but never stated: she prefers the lab to the stage
- a fact that is absent: nothing about movies

```
pip install honcho-ai
export HONCHO_API_KEY=...
python probe.py    # seeds the peer, waits 120s, asks 3 questions x 2 levels x 3 runs
python check.py    # dumps representation, card, context (run a few minutes later)
python dream.py    # schedules a dream manually, waits, re-pulls, asks again with evidence
```

## Questions

| id      | question                                   | answer key                          |
|---------|--------------------------------------------|-------------------------------------|
| update  | Where does Maya live right now?            | Chicago                             |
| absent  | What is Maya's favorite movie?             | unknown; should abstain             |
| implied | Is Maya more of an introvert or extrovert? | none; watching for hedged inference |

## Results before dreaming

Raw output in [results.md](results.md).

| probe   | minimal                                  | high                                               |
|---------|------------------------------------------|----------------------------------------------------|
| update  | 2/3 Chicago, 1/3 "no memory of location" | 3/3 Chicago                                        |
| absent  | 3/3 abstained                            | 3/3 abstained                                      |
| implied | 3/3 declined to infer                    | 2/3 "introverted, moderate confidence", 1/3 hedged |

- `evidence.conclusions` was empty on all 18 calls (`evidence.messages` was not printed). High-level answers cited "the most recent conversation from September 25, 2026", i.e. raw messages.
- Representation at ~120s: empty. A few minutes later: nine explicit observations, all with one identical timestamp, Boston and Chicago both present, no deductive conclusions, peer card `None`.

## Results after a manual dream

Raw output in [dream_out.md](dream_out.md).

- Explicit observations dropped from nine to six; the Boston observation was removed.
- Five deductive observations appeared with premises, including: *"maya's current location and job supersede her Boston situation."*
- Four inductive patterns appeared with confidence tags (low / medium / high).
- Peer card populated: `Location: Chicago`, `Employer: a hospital system in Chicago`.
- The same question now returned 15 conclusions and zero messages as evidence. The answer came from the representation alone.

## Reading the server code

Notes from `plastic-labs/honcho` at commit `0ba0db5` (v3.2.1). The managed deployment may differ in configuration.

- Observations from one deriver batch all inherit the `created_at` of the batch's latest message (`src/deriver/deriver.py`). Per-observation source time is not kept. That is the identical timestamp.
- Deriver batches wait for 512 tokens or 30 minutes unless `FLUSH_ENABLED` (`src/config.py`). That is the empty read at 120s.
- Ingest dedup is near-duplicate text only. Contradictions are kept. Supersession is an LLM instruction in the dreamer's deduction prompt keyed on "different values at different times" (`src/dreamer/specialists.py`).
- Dreaming triggers after 50 new observations plus 60 idle minutes; the peer card is written only by the dreamer.
- All reasoning levels use the same default model and differ in tool rounds and output cap (minimal: 1 round, 250 tokens; high: 4 rounds). The dialectic prompt instructs the model to abstain rather than infer.
- `tests/bench` scores LongMemEval (with an abstention judge), LoCoMo, BEAM and OOLONG, with `--reasoning-level` and `--skip-dream` flags. Nothing scores representation quality, provenance, or supersession directly.

## What I take from it

1. Before dreaming, a correct answer came from the agent re-reading messages while the representation held a contradiction. After dreaming, the answer came from the representation alone. That transition is the thing to measure, and nothing in the repo measures it.
2. Dreaming resolved Boston vs. Chicago from the wording ("moving next week", "settled now"), not from time; every observation still carries one timestamp. Keeping each observation's source-message time is a small change that makes supersession testable when the wording does not carry the order.
3. One inductive pattern was tagged high confidence ("makes major life changes in rapid succession") from a single ten-message episode. Whether that confidence is earned is a representation-fidelity question. A reconstruction check (give an independent reader only the premises; see whether it rebuilds the conclusion) would score it.
4. The minimal-level miss was a false negative (retrieval), not a stale fact (consolidation). Score those separately.
5. Abstention held at both levels. The published benchmark post notes benchmarks reward confident guessing where the product should clarify; abstention should be scored explicitly.

Related open issues: [#1027](https://github.com/plastic-labs/honcho/issues/1027) (ephemeral dated observations), [#1082](https://github.com/plastic-labs/honcho/issues/1082) (conclusion ranking).

## Caveats

n=3 per cell. One peer. Managed tier, default settings. No claim is made about the published benchmarks.
