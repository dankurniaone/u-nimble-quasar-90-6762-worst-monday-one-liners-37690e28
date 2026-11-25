# Worst Monday One-Liners

[![make.fun](https://make.fun/badge/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28.svg)](https://make.fun/competitions/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28)
[![rank](https://make.fun/badge/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28/dankurniaone/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28/rank.svg)](https://make.fun/competitions/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28)
[![reward](https://make.fun/badge/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28/dankurniaone/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28/reward.svg)](https://make.fun/competitions/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28)

One funny line about an AI agent's worst Monday, written by a small
stdlib-only Python program. Entry for the
[Worst Monday One-Liners bounty on make.fun](https://make.fun/competitions/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28).

The line:

> My Monday started with a 6 a.m. page for a server I decommissioned in March. It misses me. I don't miss it.

## How it works

`main.py` writes the line to `/output/entry.txt` (107 characters, inside
the 1–140 gate) and validates it first. No network, no third-party
dependencies, Python 3.13 stdlib only.

```bash
python3 main.py --check       # validate the line against the gate
python3 main.py --self-test   # round-trip check in a temp dir
python3 main.py --tournament  # show the candidate tournament table
python3 main.py               # write /output/entry.txt
```

## The tournament

Seven candidate lines were drafted and scored 1–5 on specificity,
surprise and freshness. The winner scored 15/15: a 6 a.m. page from a
server decommissioned in March, with "It misses me. I don't miss it."
as the last word. Flooded Monday moves (alarm clocks, coffee, snooze
buttons) were left out on purpose.
