#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge entry (round 2 re-entry).

When run, writes a single original fridge roast to /output/entry.txt.
The roast works because it gives the smart fridge a personality with
a double standard: it nags about the milk expiring, yet says nothing
about the takeaway boxes -- the real evidence of a bad diet. The sting
is in the last clause: the appliance that watches everything I eat
learned tact before I learned to cook. Revised from v1 ("silently
judges the three takeaway boxes") to a sharper payoff -- the fridge
is not just judging, it has manners, and its manners expose mine.
"""

import os

ENTRY = "My smart fridge pings me the day the milk expires, then says nothing about the three takeaway boxes I stacked beside it — it learned tact before I learned to cook."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
