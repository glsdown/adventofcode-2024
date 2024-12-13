import sys

import aocd
from dotenv import load_dotenv

load_dotenv()

# Set the day and year
DAY = "12"
YEAR = "2024"


def get_input(path):
    """Load the data from the file"""

    # Open the file
    with open(f"{path}/day-{DAY}.txt", "r") as f:
        values = [list(line.strip()) for line in f.readlines()]

    return values


def part_1(path, submit):
    """Part 1/Star 1"""

    # Get the data
    data = get_input(path)

    answer = 0
    seen_locations = set()

    no_rows = len(data)
    no_cols = len(data[0])

    for row_i, row in enumerate(data):
        for col_j, value in enumerate(row):
            if (row_i, col_j) not in seen_locations:
                seen_locations.add((row_i, col_j))
                area = 1
                perimeter = 0
                stack = [(row_i, col_j)]
                while stack:
                    next_i, next_j = stack.pop()
                    # Identify neighbours on the grid
                    neighbours = [
                        (next_i - 1, next_j),
                        (next_i + 1, next_j),
                        (next_i, next_j - 1),
                        (next_i, next_j + 1),
                    ]
                    # Check the neighbours
                    for n in neighbours:
                        if (
                            not (0 <= n[0] < no_rows and 0 <= n[1] < no_cols)
                            or data[n[0]][n[1]] != value
                        ):
                            perimeter += 1
                        elif n not in seen_locations:
                            area += 1
                            seen_locations.add(n)
                            stack.append(n)

                answer += area * perimeter
                print(f"{value=}, {area=}, {perimeter=}")

    # Print out the response
    print(f"Task 1 Answer: {answer}")

    # Submit the answer
    if submit:
        aocd.submit(answer, part="a", day=int(DAY), year=int(YEAR))


def part_2(path, submit):
    """Part 2/Star 2"""

    # Get the data
    data = get_input(path)

    # TODO: Complete the task
    answer = 0

    # Print out the response
    print(f"Task 2 Answer: {answer}")

    # Submit the answer
    if submit:
        aocd.submit(answer, part="b", day=int(DAY), year=int(YEAR))


if __name__ == "__main__":
    """
    Run using e.g.
        `python day-12.py -test`
        `python day-12.py`
        `python day-12.py -submit`
        `python day-12.py -test -2`
        `python day-12.py -2`
        `python day-12.py -test -both`
        `python day-12.py -both`
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
