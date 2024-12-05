import sys
from collections import defaultdict
from functools import cmp_to_key

import aocd
from dotenv import load_dotenv

load_dotenv()

# Set the day and year
DAY = "05"
YEAR = "2024"


def get_input(path):
    """Load the data from the file"""

    # Open the file
    with open(f"{path}/day-{DAY}.txt", "r") as f:
        rules, pages = f.read().split("\n\n")

    rules = [
        [int(i) for i in r.strip().split("|")]
        for r in rules.strip().split("\n")
    ]
    pages = [
        [int(i) for i in p.strip().split(",")]
        for p in pages.strip().split("\n")
    ]

    return rules, pages


def part_1(path, submit):
    """Part 1/Star 1"""

    # Get the data
    rules, pages = get_input(path)

    # Create dict to get what each vale is before
    before = defaultdict(set)
    for first, second in rules:
        before[first].add(second)

    # Check each update
    answer = 0
    for update in pages:
        valid = True
        for i, page in enumerate(update):
            if set(update[:i]).intersection(before[page]):
                # Invalid
                valid = False
                break
        if valid:
            middle = update[len(update) // 2]
            answer += middle

    # Print out the response
    print(f"Task 1 Answer: {answer}")

    # Submit the answer
    if submit:
        aocd.submit(answer, part="a", day=int(DAY), year=int(YEAR))


def part_2(path, submit):
    """Part 2/Star 2"""

    # Get the data
    rules, pages = get_input(path)

    # Create dict to get what each vale is before
    before = defaultdict(set)
    for first, second in rules:
        before[first].add(second)

    # Creates a custom sorting function
    def custom_sort(x, y):
        if y in before[x]:
            return -1
        if x in before[y]:
            return 1
        return 0

    # Check each update
    answer = 0
    for update in pages:
        valid = True
        for i, page in enumerate(update):
            if set(update[:i]).intersection(before[page]):
                valid = False
                break

        # Fix the broken update
        if not valid:
            middle = sorted(update, key=cmp_to_key(custom_sort))[
                len(update) // 2
            ]
            answer += middle

    # Print out the response
    print(f"Task 2 Answer: {answer}")

    # Submit the answer
    if submit:
        aocd.submit(answer, part="b", day=int(DAY), year=int(YEAR))


if __name__ == "__main__":
    """
    Run using e.g.
        `python day-05.py -test`
        `python day-05.py`
        `python day-05.py -submit`
        `python day-05.py -test -2`
        `python day-05.py -2`
        `python day-05.py -test -both`
        `python day-05.py -both`
    """
    # Identify the folder that the input is in
    test = "-test" in sys.argv
    if test:
        path = "input-tests"
    else:
        path = "inputs"
    # Identify if they need to submit the answer
    submit = "-test" not in sys.argv and "-submit" in sys.argv
    # Identify which one to run - 1 is default
    if "-2" in sys.argv:
        part_2(path, submit)
    elif "-both" in sys.argv:
        part_1(path, submit)
        part_2(path, submit)
    else:
        part_1(path, submit)
