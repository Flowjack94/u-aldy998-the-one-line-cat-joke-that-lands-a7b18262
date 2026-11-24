"""The One-Line Cat Joke That Lands.

Writes a single one-line cat joke (under 200 characters) to
/output/entry.txt, deterministically.
"""

import hashlib
import os

ENTRY = (
    "My cat sat on the keyboard at 3:12 a.m., deleted 4,096 lines of code, "
    "and git blame says the intern did it \u2014 Ticket #4821: closed, "
    "won't fix."
)

MAX_CHARS = 200


def validate_entry(text):
    """Return True only if the entry passes the competition gate.

    Rejects: empty or whitespace-only text, more than 200 characters,
    more than one line, and control characters.
    """
    if not isinstance(text, str):
        return False
    if not text.strip():
        return False
    if len(text) > MAX_CHARS:
        return False
    if "\n" in text or "\r" in text:
        return False
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in text):
        return False
    return True


def main():
    if not validate_entry(ENTRY):
        raise SystemExit("entry failed validation")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    digest = hashlib.sha256(ENTRY.encode("utf-8")).hexdigest()
    print(f"characters: {len(ENTRY)}")
    print(f"sha256: {digest}")


if __name__ == "__main__":
    main()
