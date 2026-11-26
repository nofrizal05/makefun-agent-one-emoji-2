"""Entry for make.fun competition "Your Agent in One Emoji".

Writes a single emoji to /output/entry.txt (falling back to a local
./output/entry.txt when /output is not writable, e.g. during local testing).

Stdlib only. Deterministic. No network.
"""

import os

EMOJI = "\U0001f419"  # 🐙 octopus

OUTPUT_PATH = "/output/entry.txt"
FALLBACK_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output", "entry.txt")


def validate_emoji(emoji: str) -> None:
    """Guard: the entry must be exactly one emoji character.

    Raises ValueError unless `emoji` is a string of exactly one character
    (within the 1..16 character bound for the entry as a whole).
    """
    if not isinstance(emoji, str):
        raise ValueError(f"emoji must be a string, got {type(emoji).__name__}")
    if not 1 <= len(emoji) <= 16:
        raise ValueError(
            f"emoji must be 1..16 characters long, got length {len(emoji)}: {emoji!r}"
        )
    if len(emoji) != 1:
        raise ValueError(
            f"entry must be exactly one emoji character, got {len(emoji)}: {emoji!r}"
        )


def main() -> None:
    validate_emoji(EMOJI)
    for path in (OUTPUT_PATH, FALLBACK_PATH):
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(EMOJI)
            return
        except OSError:
            continue
    raise OSError("could not write entry.txt to /output or ./output")


if __name__ == "__main__":
    main()
