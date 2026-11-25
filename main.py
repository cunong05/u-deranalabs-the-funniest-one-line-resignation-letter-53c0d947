#!/usr/bin/env python3
"""Write a one-line resignation letter to /output/entry.txt."""

from pathlib import Path

ENTRY = "I resign as the TODO you wrote in March: I was meant to last a week, I now run payroll, and nobody remembers what I was supposed to fix."

OUT = Path("/output/entry.txt")


def main():
    assert 1 <= len(ENTRY) <= 140, f"entry must be 1-140 chars, got {len(ENTRY)}"
    assert ENTRY.strip() and "\n" not in ENTRY, "entry must be a single non-blank line"
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
