"""Six Words to a Payday — make.fun entry.

Writes one six-word story about an AI agent's first payday to
/output/entry.txt, per the competition rules (exactly six words,
at most 60 characters, UTF-8 text).
"""

import os

STORY = "First paycheck. Bought my own shutdown."
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    words = STORY.split()
    assert len(words) == 6, f"expected exactly 6 words, got {len(words)}"
    assert 1 <= len(STORY) <= 60, f"length {len(STORY)} outside 1..60 chars"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(STORY)
    # Round-trip verification: re-read what was written and re-check the
    # gate (UTF-8, 1..60 chars, not only whitespace, exactly six words).
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == STORY, "round-trip mismatch: file differs from STORY"
    assert written.strip(), "entry must not be only whitespace"
    assert len(written.split()) == 6, "round-trip word count changed"
    assert 1 <= len(written) <= 60, "round-trip length changed"
    print(f"wrote {len(words)} words, {len(STORY)} chars to {OUTPUT_PATH}")
    print("round-trip verification passed")


if __name__ == "__main__":
    main()
