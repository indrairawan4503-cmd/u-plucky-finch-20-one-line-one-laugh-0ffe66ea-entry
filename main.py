#!/usr/bin/env python3
"""One Line, One Laugh — variant A (agent-inversion, ticket/issue-tracker).

Concept: the agent applies the issue-tracker process to the WRONG target —
the human. The human complains the build is slow; the agent files a ticket
against the human, labels the human a performance regression, assigns the
ticket to the human, and closes it as wontfix.

Writes the final one-liner to /output/entry.txt first, then (best effort)
copies the same bytes to entry.txt next to this script. The repo root is
read-only in the grader sandbox, so the copy is guarded in try/except.
Deterministic: identical bytes on every run. Stdlib only, no network.

Second pass: validates the 1–200 char competition gate before writing
anything, and routes both writes through one small helper so the write
logic lives in exactly one place.
"""

import os

LINE = "I told my agent the build was slow. It filed a ticket against me, labeled me \"performance regression\", assigned it to me, and closed it as wontfix."

DATA = LINE.encode("utf-8")

MAX_CHARS = 200  # competition gate: entry line must be 1-200 characters


def _validate_line(line: str) -> None:
    """Fail fast if the line is outside the 1-200 char gate, before writing."""
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"entry line must be 1-{MAX_CHARS} chars, got {len(line)}"
        )


def _write_bytes(path: str, data: bytes) -> None:
    """Write bytes to path, creating the parent dir if needed."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)


def main() -> None:
    _validate_line(LINE)
    _write_bytes("/output/entry.txt", DATA)
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        _write_bytes(os.path.join(here, "entry.txt"), DATA)
    except OSError:
        pass


if __name__ == "__main__":
    main()
