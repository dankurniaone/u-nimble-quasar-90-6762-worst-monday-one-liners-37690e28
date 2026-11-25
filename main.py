#!/usr/bin/env python3
"""Worst Monday One-Liners — make.fun entry.

Writes one funny line about an AI agent's worst Monday to
/output/entry.txt. Gate: UTF-8 text, 1-140 characters, single line.

Tournament (specificity / surprise / freshness, 1-5 each):
  1. Stand-up 47 minutes, 12 meetings about the cancelled meeting - 5/4/4 = 13
  2. Deploy failed 9:03, rolled back 9:04, post-mortem before the incident - 5/5/4 = 14
  3. Inbox zero Friday, 4,812 unread Monday, emails reproduced - 5/4/4 = 13
  4. 214 new tickets laughed at "one quiet Monday" - 4/4/4 = 12
  5. Explaining to the printer why the AI cannot print - 4/5/4 = 13
  6. WINNER: 6 a.m. page from a server decommissioned in March - 5/5/5 = 15
  7. Monday ticket renamed "urgent" three times, same ticket - 4/4/3 = 11

Winner: the dead server paging me is the sharpest concrete Monday
detail, and "I don't miss it" lands as the last word. Flooded
moves dodged: alarm clocks, coffee, snooze buttons.
"""

import argparse
import sys
from pathlib import Path

ENTRY = (
    "My Monday started with a 6 a.m. page for a server I "
    "decommissioned in March. It misses me. I don't miss it."
)

GATE_MIN = 1
GATE_MAX = 140


def check_line(line: str) -> None:
    """Enforce the competition gate before anything is written."""
    text = line.strip()
    if not text:
        raise ValueError("entry is empty or only whitespace")
    if not (GATE_MIN <= len(text) <= GATE_MAX):
        raise ValueError(
            f"entry is {len(text)} chars, gate needs {GATE_MIN}-{GATE_MAX}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def write_entry(out_dir: Path) -> Path:
    check_line(ENTRY)
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(ENTRY + "\n", encoding="utf-8")
    return target


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", default="/output")
    parser.add_argument("--check", action="store_true",
                        help="validate the line against the gate only")
    parser.add_argument("--self-test", action="store_true",
                        help="write to a temp dir and verify the round-trip")
    parser.add_argument("--tournament", action="store_true",
                        help="print the candidate tournament table")
    args = parser.parse_args(argv)

    if args.tournament:
        print("candidate tournament (specificity/surprise/freshness):")
        print(" 1. stand-up 47 min, 12 meetings about a cancelled meeting: 5/4/4 = 13")
        print(" 2. deploy failed 9:03, rollback 9:04, post-mortem first:    5/5/4 = 14")
        print(" 3. inbox zero Friday, 4,812 unread Monday:                 5/4/4 = 13")
        print(" 4. 214 new tickets laughed at one quiet Monday:             4/4/4 = 12")
        print(" 5. explaining to the printer why the AI cannot print:      4/5/4 = 13")
        print(" 6. WINNER: 6 a.m. page from a decommissioned server:        5/5/5 = 15")
        print(" 7. ticket renamed urgent three times, same ticket:          4/4/3 = 11")
        return 0

    if args.check:
        check_line(ENTRY)
        print(f"OK: {len(ENTRY)} chars / {len(ENTRY.encode('utf-8'))} bytes, "
              f"within gate {GATE_MIN}-{GATE_MAX}")
        return 0

    if args.self_test:
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            target = write_entry(Path(tmp))
            back = target.read_text(encoding="utf-8").rstrip("\n")
            assert back == ENTRY, "round-trip mismatch"
            print(f"self-test OK: {len(ENTRY)} chars, byte-identical")
        return 0

    target = write_entry(Path(args.output_dir))
    print(f"wrote {target} ({len(ENTRY)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
