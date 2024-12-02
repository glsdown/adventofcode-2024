import sys
from statistics import mode

import aocd
from dotenv import load_dotenv

load_dotenv()

# Set the day and year
DAY = "02"
YEAR = "2024"


def get_input(path):
    """Load the data from the file"""

    # Open the file
    with open(f"{path}/day-{DAY}.txt", "r") as f:
        values = [
            [int(i) for i in line.strip().split()] for line in f.readlines()
        ]

    return values


def sign(num1, num2):
    if num1 > num2:
        # Decreasing
        return -1
    elif num1 < num2:
        # Increasing
        return 1
    else:
        # Invalid
        return 0


def check_safe(report):
    """Check a report is safe"""

    offset = sign(report[0], report[1])
    if offset == 0:
        # Invalid
        return 0

    for i in range(len(report) - 1):
        if not (1 <= offset * (report[i + 1] - report[i]) <= 3):
            return 0

    return 1


def part_1(path, submit):
    """Part 1/Star 1"""

    # Get the data
    data = get_input(path)

    # Check safety
    safe = 0
    for report in data:
        safe += check_safe(report)

    # Print out the response
    print(f"Task 1 Answer: {safe}")

    # Submit the answer
    if submit:
        aocd.submit(safe, part="a", day=int(DAY), year=int(YEAR))


def part_2(path, submit):
    """Part 2/Star 2"""

    # Get the data
    data = get_input(path)

    # Check safety
    safe = 0
    for report in data:
        report_safe = check_safe(report)
        # See if removing a value helps
        if not report_safe:
            for i in range(len(report)):
                if check_safe([*report[:i], *report[i + 1 :]]):
                    report_safe = 1
                    break
        safe += report_safe

    # Print out the response
    print(f"Task 2 Answer: {safe}")

    # Submit the answer
    if submit:
        aocd.submit(safe, part="b", day=int(DAY), year=int(YEAR))


if __name__ == "__main__":
    """
    Run using e.g.
        `python day-02.py -test`
        `python day-02.py`
        `python day-02.py -submit`
        `python day-02.py -test -2`
        `python day-02.py -2`
        `python day-02.py -test -both`
        `python day-02.py -both`
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
