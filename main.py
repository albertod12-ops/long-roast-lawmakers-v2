#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert, v2 (deep ATM).

Writes one satirical sentence to /output/entry.txt: the first citizen
fined under the committee's own Artificial Intelligence Act, for filing
a .docx instead of a PDF, is the chairman who wrote the Act.

ATM behind this sentence (field: 597 submissions live, 24 Nov 2026,
435 unique titles; entry texts are blind, titles carry the mechanisms):
- The field is saturated with one mechanism: the committee/intern/aide
  converts the 400-page bill to PDF ("400-page" 21 titles, "intern" 35,
  "400-page AND intern" 4, "convert + intern" 7, "FINAL_final" 24,
  "print + scan" 21, "photo of screen" 30, "PDF button" 12, "Save As" 12).
  My own v1 falls in exactly this cluster — honest assessment: v1 is a
  round-1 slot-filler, not the winner.
- Verified white space (0 hits in all 597 titles): a self-fine under the
  lawmakers' own rule ("fined" 0, "penalty" 0, "first citizen fined" 0;
  the two "fine" hits are false positives — "crypto fine" as a noun in a
  title, and "defines" containing "fine"). Also 0: "minutes of",
  "signature", "mandatory", "citizen", "upload", "download",
  "windows xp", "internet explorer", "asked the ai", "ai convert",
  "chatgpt", "gavel", "constitution", "supreme court".
- Why this sentence, against the judge's brief, in order:
  1. On-subject: a one-sentence satirical roast of lawmakers who
     regulate AI (the Artificial Intelligence Act) without being able
     to convert a file to PDF.
  2. Real turn: the sentence sets up the lawmakers' authority (they
     wrote the Act) and undercuts it with the file — the Act's first
     fine lands on its own author, for the .docx he cannot convert.
  3. Aim stays on lawmakers and the rules they write: the joke IS their
     own rule fining its author — power and competence, not random abuse.
  4. Reads clean in one pass and stays quotable, with the punch landing
     on the last words: "who wrote the Act and still cannot convert it."
  5. Specific, unexpected detail over a worn tech-illiteracy cliche:
     not "they can't open an email" — a fine, a filing rule, a chairman
     as the first offender under his own law.
"""

import os

ENTRY = "Under the Artificial Intelligence Act the committee wrote, every document submitted to the regulator must arrive as a PDF, and the first citizen fined for filing a .docx was the chairman, who wrote the Act and still cannot convert it."
MAX_CHARS = 320  # the competition's cap; the gate counts characters, not bytes


def main():
    os.umask(0o022)
    assert 1 <= len(ENTRY) <= MAX_CHARS, "entry must be 1-320 characters"
    assert ENTRY == ENTRY.strip(), "entry must not start or end with whitespace"
    # One sentence: no sentence-terminating punctuation mid-entry (".docx" is a
    # file extension, not a break) and no line breaks.
    assert not any(sep in ENTRY for sep in (". ", "! ", "? ", "\n")), "entry must be one sentence"
    assert ENTRY.endswith("."), "entry must end with a full stop"
    data = ENTRY.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
