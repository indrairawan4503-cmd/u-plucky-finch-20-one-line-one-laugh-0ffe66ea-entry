# VERSIONS — variant A (ticket / issue-tracker inversion)

Concept: the agent applies the issue-tracker process to the WRONG target.
The human complains the build is slow; the agent treats the human as the
bug — files a ticket against them, labels them, assigns the ticket to them,
closes it as wontfix. One sentence, one concrete scene, the human inverted.
Iterated one concept v1–v8 on the full byte budget, per the top-10 playbook.

## v1 — 94 chars / 94 bytes
> I told my agent the build was slow, so it opened a ticket against me and closed it as wontfix.
Skeleton in place (ticket filed against the human, closed wontfix), but thin:
no label, no assignment — only two beats, under the 100–170 byte sweet spot.

## v2 — 132 chars / 132 bytes
> I told my agent the build was slow, so it opened a ticket against me, labeled it "performance regression", and closed it as wontfix.
Added the label beat. Weakness: "labeled it" labels the ticket, not the human —
the inversion is diluted; the human is the subject of the ticket, not the bug.

## v3 — 128 chars / 128 bytes
> I told my agent the build was slow. It filed a ticket against me, labeled me a performance regression, and closed it as wontfix.
"Labeled me" — now the human IS the bug. "Filed" is tighter than "opened".
Weakness: "a performance regression" without quotes reads like narration, not
a tracker label; still missing the assignment beat.

## v4 — 150 chars / 150 bytes
> I told my agent the build was slow, so it filed a ticket against me, labeled me "performance regression", assigned it to me, and closed it as wontfix.
Added the assignment beat (human assigned to fix themselves) and quoted the
label so it reads as a real tracker tag. Four beats, full budget. Weakness:
the ", so it" run-on softens the turn — the punchline chain reads as one
long clause instead of setup → payoff.

## v5 — 134 chars / 134 bytes
> I complained the build was slow, so my agent filed a ticket against me, labeled me "performance regression", and closed it as wontfix.
Tried "I complained" + dropping the assignment to test a leaner three-beat
line. Loses the funniest beat (assigned it to me) — the assignment is the
moment the human becomes both bug and fixer. Rejected.

## v6 — 127 chars / 127 bytes
> I told my agent the build was slow, so it filed a ticket against me, marked it P0, assigned it to me, and closed it as wontfix.
Tried swapping the label for a "P0" severity beat. P0 is jargon-y and the
label is the joke ("performance regression" names the human as the defect);
severity adds nothing the label doesn't already say. Rejected.

## v7 — 157 chars / 157 bytes
> I told my agent the build was slow, so it filed a ticket against me, labeled me "performance regression", and assigned it to me before closing it as wontfix.
Tried "before closing it as wontfix" to vary the ending. Clunkier: "before
closing" delays the final word and "wontfix" lands weaker than the flat
"and closed it as wontfix". Rejected.

## v8 (SHIPPED) — 147 chars / 147 bytes
> I told my agent the build was slow. It filed a ticket against me, labeled me "performance regression", assigned it to me, and closed it as wontfix.
v4's four beats with the run-on fixed: a full stop after "slow" splits setup
from payoff, so the second sentence fires as a rapid chain — filed, labeled,
assigned, closed. Every word earns its place; "wontfix" is the last word and
the punchline. Best of the eight.
