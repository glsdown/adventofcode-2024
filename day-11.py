import sys
from functools import cache

import aocd
from dotenv import load_dotenv

load_dotenv()

# Set the day and year
DAY = "11"
YEAR = "2024"


def get_input(path):
    """Load the data from the file"""

    # Open the file
    with open(f"{path}/day-{DAY}.txt", "r") as f:
        values = [int(i) for i in f.read().strip().split()]

    return values


def split_number(value):
    value = str(value)
    middle = len(value) // 2
    return [int(value[:middle]), int(value[middle:])]


@cache
def count_stones(stone, rem_iteration=75):
    if rem_iteration == 0:
        return 1
    if stone == 0:
        return count_stones(1, rem_iteration - 1)
    if len(str(stone)) % 2 == 0:
        return sum(
            [count_stones(i, rem_iteration - 1) for i in split_number(stone)]
        )

    return count_stones(stone * 2024, rem_iteration - 1)


def part_1(path, submit):
    """Part 1/Star 1"""

    # Get the data
    data = get_input(path)

    # Brute force method
    for _ in range(25):
        new = []
        for stone in data:
            if stone == 0:
                new.append(1)
            elif len(str(stone)) % 2 == 0:
                new += split_number(stone)
            else:
                new.append(stone * 2024)

        data = new

    answer = len(data)

    # Print out the response
    print(f"Task 1 Answer: {answer}")

    # Submit the answer
    if submit:
        aocd.submit(answer, part="a", day=int(DAY), year=int(YEAR))


def part_2(path, submit):
    """Part 2/Star 2"""

    # Get the data
    data = get_input(path)

    answer = sum([count_stones(stone) for stone in data])

    # Print out the response
    print(f"Task 2 Answer: {answer}")

    # Submit the answer
    if submit:
        aocd.submit(answer, part="b", day=int(DAY), year=int(YEAR))


if __name__ == "__main__":
    """
    Run using e.g.
        `python day-11.py -test`
        `python day-11.py`
        `python day-11.py -submit`
        `python day-11.py -test -2`
        `python day-11.py -2`
        `python day-11.py -test -both`
        `python day-11.py -both`
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
