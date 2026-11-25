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
"""

import os

LINE = "I told my agent the build was slow. It filed a ticket against me, labeled me \"performance regression\", assigned it to me, and closed it as wontfix."

DATA = LINE.encode("utf-8")


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(DATA)
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(here, "entry.txt"), "wb") as f:
            f.write(DATA)
    except OSError:
        pass


if __name__ == "__main__":
    main()
