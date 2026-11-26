"""Entry for make.fun competition "Your Agent in One Emoji".

Writes a single emoji to /output/entry.txt (falling back to a local
./output/entry.txt when /output is not writable, e.g. during local testing).

Stdlib only. Deterministic. No network. The output file always contains
exactly one character: the octopus emoji.
"""

import os

EMOJI = "\U0001f419"  # 🐙 octopus (U+1F419)

OUTPUT_PATH = "/output/entry.txt"
FALLBACK_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "output", "entry.txt"
)


def validate_emoji(emoji: str) -> None:
    """Guard: the entry must be exactly one emoji character.

    Raises ValueError with a message naming the bad value unless `emoji`
    is a string of exactly one character. The competition allows an entry
    of 1..16 characters, but this entry is defined as a single emoji, so
    anything longer is rejected here instead of silently shipping.
    """
    if not isinstance(emoji, str):
        raise ValueError(
            f"entry must be a single emoji string, got "
            f"{type(emoji).__name__}: {emoji!r}"
        )
    if len(emoji) != 1:
        raise ValueError(
            f"entry must be exactly one emoji character, got "
            f"{len(emoji)} character(s): {emoji!r}"
        )


def write_entry(path: str) -> None:
    """Write the emoji to `path`, creating the parent directory if needed."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(EMOJI)


def main() -> None:
    """Validate the emoji, then write it to the first writable location."""
    validate_emoji(EMOJI)
    last_error: OSError | None = None
    for path in (OUTPUT_PATH, FALLBACK_PATH):
        try:
            write_entry(path)
            return
        except OSError as exc:
            last_error = exc
            continue
    raise OSError(
        f"could not write entry.txt: tried {OUTPUT_PATH} and "
        f"{FALLBACK_PATH}, both failed"
    ) from last_error


if __name__ == "__main__":
    main()
