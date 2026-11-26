"""The Router Confesses — entry copier.

Writes the single final line to /output/entry.txt (absolute path),
with no trailing newline. Stdlib only; no network, no model call,
no reading of any other file.
"""

import os
import sys

ENTRY_TEXT = (
    "I cut the Wi-Fi at the climax because I read the script last night "
    "and the twist was so bad I spared you."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Check the entry text against the bounty gates (RULES.txt).

    Returns a list of violation messages; empty means the text is valid.
    Rules: 1-200 characters, at most 200 UTF-8 bytes, a single line,
    not whitespace-only, no control characters.
    """
    errors = []
    if not isinstance(text, str):
        errors.append("entry text must be a string, got %s" % type(text).__name__)
        return errors
    if not 1 <= len(text) <= 200:
        errors.append(
            "entry text must be 1-200 characters, got %d" % len(text)
        )
    byte_len = len(text.encode("utf-8"))
    if byte_len > 200:
        errors.append(
            "entry text must be at most 200 UTF-8 bytes, got %d" % byte_len
        )
    if text.strip() == "":
        errors.append("entry text must not be whitespace-only")
    if "\n" in text or "\r" in text:
        errors.append("entry text must be a single line (no newline or CR)")
    bad = sorted({c for c in text if ord(c) < 32 or ord(c) == 127})
    if bad:
        errors.append(
            "entry text contains control character(s): %s"
            % ", ".join("U+%04X" % ord(c) for c in bad)
        )
    return errors


def main():
    errors = validate(ENTRY_TEXT)
    if errors:
        for err in errors:
            print("ERROR: %s" % err, file=sys.stderr)
        print(
            "ERROR: entry text failed validation; /output/entry.txt "
            "was NOT written.",
            file=sys.stderr,
        )
        raise SystemExit(1)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
