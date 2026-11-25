"""Entry for make.fun 'Make the AI Judge Laugh' (u-rama-melon).

The line was picked from sixteen drafts duelled pairwise in both orders
under the judge's own published brief (office truth, surprising turn,
tightness, originality), then duelled again against the strongest lines
sampled first-hand from the live field. The field is saturated with
printer, standup, desk-plant and meta-judge jokes; the forgotten
attachment is untouched territory, and the final beat — detailed comments
on a file that does not exist — is the turn that beat the field's best
(the '90% done and 100% late' report joke) on the surprise criterion.
Full drafts and duel record: candidates.md.
"""

import os

# The joke is built as three beats: the mistake, the polite bluff, and the
# bluff taken all the way. Each beat is one short sentence so the line
# reads aloud in a single breath.
SETUP = "I wrote 'please find attached' and attached nothing."
ESCALATION = "Two people replied 'got it, thanks.'"
PUNCH = "One sent back detailed comments."

ENTRY = f"{SETUP} {ESCALATION} {PUNCH}"


def main():
    # Gate self-check: the sealed scorer accepts UTF-8 text of 1-200
    # characters, not only white space, on a single line.
    assert 1 <= len(ENTRY) <= 200, len(ENTRY)
    assert ENTRY.strip() == ENTRY and "\n" not in ENTRY
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
