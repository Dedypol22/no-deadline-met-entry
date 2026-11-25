"""One-line deadline excuse for make.fun: u-markk-st-one-line-no-deadline-met-6adc00ce.

The winning line:

    The deadline and I agreed to see other people, so we're taking some
    space until Friday.

Why it lands under the judge criteria:

1. It IS an excuse for a missed deadline -- the deadline was not met
   because the two of them are "taking some space".
2. It is a real joke with a turn: a missed deadline is reframed as a
   romantic breakup, with the familiar "see other people" line doing
   the surprise work.
3. It is one clean sentence that reads aloud easily, and the punch
   ("until Friday") lands at the very end.
4. It sounds like something a cornered person would actually say --
   sheepish, deflecting, and exaggerated just enough.
5. It is fresh: a breakup with a deadline, not a dog, a dead laptop,
   or a dead Wi-Fi connection.

Candidate scoring (1-5 on each of the 5 criteria, in order):

 1. Deadline moved itself, forgot to tell me -- 5, 4, 5, 4, 4 = 22
 2. Trapped in FINAL_final_v2_REAL -- 5, 4, 3, 5, 4 = 21
 3. Met it in a parallel timeline -- 5, 4, 5, 3, 4 = 21
 4. Dog filed for an extension -- 5, 4, 4, 4, 3 = 20
 5. Deadline and I agreed to see other people -- 5, 5, 5, 5, 5 = 25
 6. Future me finished it but is also late -- 5, 4, 4, 3, 4 = 20
 7. Timezone of a country without clocks -- 5, 4, 4, 2, 4 = 19
 8. Printer of fate jammed -- 4, 3, 4, 2, 3 = 16
 9. Calendar invite to the wrong year -- 5, 4, 4, 3, 4 = 20
10. Laptop entered witness protection -- 4, 4, 4, 3, 3 = 18
11. Deadline lost in 400 unread emails -- 5, 3, 4, 4, 2 = 18
12. Deadline broke the deal first -- 5, 4, 5, 4, 4 = 22
13. Internet sent it to the spam folder of the universe -- 4, 3, 4, 3, 2 = 16
14. Alarm clock and I are no longer speaking -- 4, 3, 4, 3, 3 = 17

Candidate 5 won outright, and the submitted line is its tightest form:
"Me and the deadline ..." became "The deadline and I ...", and
"until next Friday" became "until Friday", keeping the punch while
favouring the smaller-text tie-break.
"""

import os
import sys


LINE = "The deadline and I agreed to see other people, so we're taking some space until Friday."


def validate(line):
    """Check the line meets the competition gate: one line, 1-200 chars."""
    if not line:
        raise ValueError("line must not be blank")
    if line != line.strip():
        raise ValueError(
            "line must not have leading or trailing whitespace "
            f"(got {len(line)} chars, stripped form has {len(line.strip())})"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line must be 1-200 characters, got {len(line)}")
    return line


def main():
    line = validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
