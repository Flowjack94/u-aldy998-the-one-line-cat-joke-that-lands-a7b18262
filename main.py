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
    more than one line, control characters (C0, DEL, and C1), and any
    stray leading or trailing whitespace.
    """
    if not isinstance(text, str):
        return False
    if not text.strip():
        return False
    if text != text.strip():
        return False
    if len(text) > MAX_CHARS:
        return False
    if "\n" in text or "\r" in text:
        return False
    if any(ord(ch) < 0x20 or 0x7F <= ord(ch) <= 0x9F for ch in text):
        return False
    return True


def run_self_tests():
    """Negative self-tests for validate_entry; raises on any failure."""
    cases = [
        ("control char embedded", ENTRY[:10] + "\x07" + ENTRY[10:], False),
        ("leading/trailing spaces", " " + ENTRY + " ", False),
        ("the entry itself", ENTRY, True),
    ]
    for name, text, expected in cases:
        got = validate_entry(text)
        status = "PASS" if got == expected else "FAIL"
        print(f"self-test [{status}]: {name} -> validate={got} (expected {expected})")
        if got != expected:
            raise SystemExit(f"self-test failed: {name}")
    print("self-tests: 3/3 passed")


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
    run_self_tests()
    main()
