import re
import sys

import aocd
from dotenv import load_dotenv

load_dotenv()

# Set the day and year
DAY = "03"
YEAR = "2024"

# Regex Patterns
PATTERN = re.compile(r"mul\((\d+)\,(\d+)\)")
PATTERN_ENABLE = re.compile(r"(do\(\)|don\'t\(\)|mul\((\d+)\,(\d+)\))")


def get_input(path):
    """Load the data from the file"""

    # Open the file
    with open(f"{path}/day-{DAY}.txt", "r") as f:
        values = f.read().strip()

    return values


def part_1(path, submit):
    """Part 1/Star 1"""

    # Get the data
    data = get_input(path)

    # Get the matches
    pairs = PATTERN.findall(data)
    answer = sum([int(i[0]) * int(i[1]) for i in pairs])

    # Print out the response
    print(f"Task 1 Answer: {answer}")

    # Submit the answer
    if submit:
        aocd.submit(answer, part="a", day=int(DAY), year=int(YEAR))


def part_2(path, submit):
    """Part 2/Star 2"""

    # Get the data
    data = get_input(path)

    # Get the matches
    pairs = PATTERN_ENABLE.findall(data)
    answer = 0
    enabled = True
    for match in pairs:
        if match[0] == "do()":
            enabled = True
        elif match[0] == "don't()":
            enabled = False
        elif enabled:
            answer += int(match[1]) * int(match[2])

    # Print out the response
    print(f"Task 2 Answer: {answer}")

    # Submit the answer
    if submit:
        aocd.submit(answer, part="b", day=int(DAY), year=int(YEAR))


if __name__ == "__main__":
    """
    Run using e.g.
        `python day-03.py -test`
        `python day-03.py`
        `python day-03.py -submit`
        `python day-03.py -test -2`
        `python day-03.py -2`
        `python day-03.py -test -both`
        `python day-03.py -both`
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
