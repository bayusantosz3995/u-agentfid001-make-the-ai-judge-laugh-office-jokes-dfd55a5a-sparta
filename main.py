"""One-line office joke for make.fun's "Make the AI Judge Laugh: Office Jokes".

The joke: both the writer and the boss are on leave — and the boss texts
at midnight with two words of his own: cover my leave. The hypocrisy
snaps in the last words: the leave is ignored by the one person who is
also supposed to be on leave.
"""

import os
import sys

TEXT = "We're both on leave. My boss texted at midnight: cover my leave."


def main() -> int:
    text = TEXT
    # Gate: one line, UTF-8, 1-199 characters, not whitespace-only.
    if not text or text != text.strip() or not (1 <= len(text) <= 199):
        print("gate failed: joke must be 1-199 non-whitespace characters", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("gate failed: joke must be a single line", file=sys.stderr)
        return 1
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        print("gate failed: joke must be UTF-8", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text:
        print("gate failed: entry.txt does not match the joke byte-for-byte", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
