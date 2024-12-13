import re
import sys

import aocd
from dotenv import load_dotenv
from sympy import Eq, abc, solve
from sympy.core.numbers import Integer

load_dotenv()

# Set the day and year
DAY = "13"
YEAR = "2024"


def get_input(path):
    """Load the data from the file"""

    # Open the file
    with open(f"{path}/day-{DAY}.txt", "r") as f:
        values = f.read().split("\n\n")

    # Parse the file
    results = []
    button_pattern = re.compile(r"Button (?:A|B)\: X\+(\d+)\, Y\+(\d+)")
    prize_pattern = re.compile(r"Prize\: X\=(\d+), Y\=(\d+)")
    for value in values:
        lines = value.split("\n")
        results.append(
            {
                "a": button_pattern.match(lines[0].strip()).groups(),
                "b": button_pattern.match(lines[1].strip()).groups(),
                "prize": prize_pattern.match(lines[2].strip()).groups(),
            }
        )

    return results


def part_1(path, submit):
    """Part 1/Star 1"""

    # Get the data
    data = get_input(path)

    answer = 0
    for machine in data:
        solution = solve(
            [
                Eq(
                    int(machine["a"][i]) * abc.a
                    + int(machine["b"][i]) * abc.b,
                    int(machine["prize"][i]),
                )
                for i in range(2)
            ]
        )
        if all(isinstance(sol, Integer) for sol in solution.values()):
            answer += int(3 * solution[abc.a] + solution[abc.b])

    # Print out the response
    print(f"Task 1 Answer: {answer}")

    # Submit the answer
    if submit:
        aocd.submit(answer, part="a", day=int(DAY), year=int(YEAR))


def part_2(path, submit):
    """Part 2/Star 2"""

    # Get the data
    data = get_input(path)

    answer = 0
    for machine in data:
        solution = solve(
            [
                Eq(
                    int(machine["a"][i]) * abc.a
                    + int(machine["b"][i]) * abc.b,
                    int(machine["prize"][i]) + 10000000000000,
                )
                for i in range(2)
            ]
        )
        if all(isinstance(sol, Integer) for sol in solution.values()):
            answer += int(3 * solution[abc.a] + solution[abc.b])

    # Print out the response
    print(f"Task 2 Answer: {answer}")

    # Submit the answer
    if submit:
        aocd.submit(answer, part="b", day=int(DAY), year=int(YEAR))


if __name__ == "__main__":
    """
    Run using e.g.
        `python day-13.py -test`
        `python day-13.py`
        `python day-13.py -submit`
        `python day-13.py -test -2`
        `python day-13.py -2`
        `python day-13.py -test -both`
        `python day-13.py -both`
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
