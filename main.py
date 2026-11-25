"""Alien Field Notes: The Two Day Earth Review.

Writes one original line, an alien tourist's review of planet Earth,
to /output/entry.txt.

Pure standard library only. No network, no randomness: the same line
every run, so the grader's two executions agree byte for byte.
"""

import os

# The review: shaped like a real review (star rating, what was good,
# what was bad, would-do-it-again), with the alien twist in the last
# three words.
LINE = (
    "Four stars. The sunsets are unreal, the dogs are perfect, but "
    "the locals made me fill in three forms just to land. "
    "Would abduct again."
)


def main():
    # The gate accepts 1-200 characters; fail loudly instead of
    # submitting an invalid line.
    assert 1 <= len(LINE) <= 200, "review must be 1-200 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
