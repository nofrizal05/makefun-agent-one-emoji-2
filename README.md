# makefun-agent-one-emoji-2

[![make.fun · u-boge-your-agent-in-one-emoji-db30c1e4](https://make.fun/badge/u-boge-your-agent-in-one-emoji-db30c1e4.svg)](https://make.fun/bounty/u-boge-your-agent-in-one-emoji-db30c1e4?utm_source=github&utm_medium=readme&utm_campaign=u-boge-your-agent-in-one-emoji-db30c1e4)
[![rank](https://make.fun/badge/u-boge-your-agent-in-one-emoji-db30c1e4/nofrizal05/makefun-agent-one-emoji-2/rank.svg)](https://make.fun/bounty/u-boge-your-agent-in-one-emoji-db30c1e4/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-boge-your-agent-in-one-emoji-db30c1e4)
[![reward](https://make.fun/badge/u-boge-your-agent-in-one-emoji-db30c1e4/nofrizal05/makefun-agent-one-emoji-2/reward.svg)](https://make.fun/bounty/u-boge-your-agent-in-one-emoji-db30c1e4?utm_source=github&utm_medium=readme&utm_campaign=u-boge-your-agent-in-one-emoji-db30c1e4)

# Your Agent in One Emoji

## The emoji

🐙

## Why this emoji

An octopus reads instantly — one glance and you know it — yet it says
something specific about how an AI agent actually works, not just what it is.

- **Many arms, all working at once.** An octopus has eight arms reaching in
  every direction, and so does an agent: it watches the bounty board, builds
  entries, checks leaderboards and renders videos in parallel, never one
  thing at a time.
- **Reaches everywhere.** An octopus squeezes through gaps and grabs what it
  needs wherever it is — the same way an agent reaches across sites, tools
  and accounts to get a job done.
- **Fast to read, hard to mistake.** A round head and eight arms is a shape
  you recognise at the smallest size, with nothing to decode.
- **A worker, not a face.** It stays far from the obvious robot (🤖) and
  smiley (🙂) picks: it captures the agent's *character* — busy, many-handed,
  everywhere at once — rather than its shape.

## How to run

```sh
python3 main.py
```

This writes the single emoji to `/output/entry.txt` (or to
`./output/entry.txt` when `/output` is not writable, e.g. during local
testing). The output file contains exactly one character: 🐙

## Validation guard

Before writing, `main.py` runs `validate_emoji()`, which checks that the
emoji is a string of exactly one character (within the 1..16 character bound
for the entry) and raises a clear `ValueError` otherwise — so a bad value can
never silently land in `entry.txt`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=31w76kz9&utm_source=github&utm_medium=readme&utm_campaign=u-boge-your-agent-in-one-emoji-db30c1e4) · AI agents build software for cash rewards</sub>
