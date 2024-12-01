import sys
from collections import Counter

import aocd
from dotenv import load_dotenv

load_dotenv()

# Set the day and year
DAY = "01"
YEAR = "2024"


def get_input(path):
    """Load the data from the file"""

    # Open the file
    with open(f"{path}/day-{DAY}.txt", "r") as f:
        left, right = zip(*[line.strip().split() for line in f.readlines()])

    return sorted([int(l) for l in left]), sorted([int(r) for r in right])


def part_1(path, submit):
    """Part 1/Star 1"""

    # Get the data
    left, right = get_input(path)

    # Find the differences
    answer = sum(abs(i[0] - i[1]) for i in zip(left, right))

    # Print out the response
    print(f"Task 1 Answer: {answer}")

    # Submit the answer
    if submit:
        aocd.submit(answer, part="a", day=int(DAY), year=int(YEAR))


def part_2(path, submit):
    """Part 2/Star 2"""

    # Get the data
    left, right = get_input(path)

    # Get the count of values in the left hand list
    left_count = Counter(left)

    # Get the count of values in the right hand list
    right_count = Counter(right)

    # Calculate the answer
    answer = sum(i * left_count[i] * right_count[i] for i in left_count)

    # Print out the response
    print(f"Task 2 Answer: {answer}")

    # Submit the answer
    if submit:
        aocd.submit(answer, part="b", day=int(DAY), year=int(YEAR))


if __name__ == "__main__":
    """
    Run using e.g.
        `python day-01.py -test`
        `python day-01.py`
        `python day-01.py -submit`
        `python day-01.py -test -2`
        `python day-01.py -2`
        `python day-01.py -test -both`
        `python day-01.py -both`
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
