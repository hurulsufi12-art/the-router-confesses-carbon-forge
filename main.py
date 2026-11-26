"""The Router Confesses — entry copier.

Writes the single final line to /output/entry.txt (absolute path),
with no trailing newline. Stdlib only; no network, no model call,
no reading of any other file.
"""

import os

ENTRY_TEXT = (
    "I cut the Wi-Fi at the climax because I read the script last night "
    "and the twist was so bad I spared you."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
