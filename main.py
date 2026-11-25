"""The Dog Ate My Homework -- the excuse, told by the dog.

This program writes one line -- a dog's account of why the
homework got eaten -- to $MAKEFUN_OUTPUT_DIR/entry.txt
(/output/entry.txt by default, the path the grader sandbox reads).
It first checks the line against the sealed gate on its own: the
text has to be UTF-8, 1 to 200 characters long, more than blank
space, and a single line with no line breaks hiding inside it.

What makes this line the one to send:

* The dog never apologises and never admits a thing. In its
  telling, nothing was eaten that should not have been: the paper
  slipped off the desk, touched the floor, and at that instant
  it changed category. Homework on a desk is homework. Homework
  on the floor is floor food, and floor food gets eaten. That
  is the whole legal argument, delivered without a flicker of
  doubt.
* The joke turns on that relabelling. Rather than begging for
  mercy or blaming the cat, the dog simply rules the charge out
  of order -- the thing it ate was not, by its own definition,
  homework at all. A dog convinced of its own innocence would
  argue exactly this way.
* Every value in the line belongs to a dog: the floor as a
  jurisdiction, food as the only thing worth noticing, and rules
  as something a dog states rather than follows. No shame, no
  grovelling, no "good boy" performance. "Those are the rules."
  is a closing statement from a creature that has already won
  the argument in its own head.
* The line stands alone. There is no preamble, no callback, no
  second sentence needed to explain the first. It also avoids
  every worn-out bit the brief rules out -- the cat, the flavour
  of paper, the good boy -- so the laugh has to come from the
  dog's logic itself, and it does.
"""

import os

MAX_CHARS = 200

LINE = (
    "It wasn't homework anymore once it hit the floor. "
    "Floor food is floor food. Those are the rules."
)


def build_excuse() -> str:
    """Hand back the excuse line, built from its three comic beats."""
    return LINE


def validate(text: str) -> str:
    """Check the line against the gate: one line, 1-200 chars, real text."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("excuse must not be empty or only whitespace")
    if len(stripped) > MAX_CHARS:
        raise ValueError(f"excuse is {len(stripped)} chars, over the 200 limit")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("excuse must be exactly one line")
    return stripped


def main() -> None:
    excuse = validate(build_excuse())
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(excuse)
    print(f"wrote {len(excuse)} chars to {path}")


if __name__ == "__main__":
    main()
