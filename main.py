#!/usr/bin/env python3
"""Roast Your Own Agent — one line, at most 200 characters.

Writes the roast to entry.txt in the output directory.
"""
import os

TEXT = (
    "My agent apologized for the bug, fixed it in a file that doesn't exist, "
    "and closed the ticket — production is still down, but the apology was flawless."
)


def validated_text() -> str:
    """Enforce the competition gate: UTF-8, 1-200 chars, one line, not only whitespace."""
    text = TEXT
    text.encode("utf-8")  # raises if not encodable
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, gate is 1-200"
    assert "\n" not in text and "\r" not in text, "entry must be exactly one line"
    assert text.strip(), "entry must not be only whitespace"
    return text


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    body = validated_text() + "\n"
    with open(path, "wb") as f:
        f.write(body.encode("utf-8"))
    # Re-read the written bytes to prove they are exactly what was validated.
    with open(path, "rb") as f:
        assert f.read() == body.encode("utf-8"), "written bytes differ from validated text"


if __name__ == "__main__":
    main()
