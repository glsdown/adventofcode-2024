import sys

import aocd
from dotenv import load_dotenv

load_dotenv()

# Set the day and year
DAY = "10"
YEAR = "2024"


def get_input(path):
    """Load the data from the file"""

    # Open the file
    with open(f"{path}/day-{DAY}.txt", "r") as f:
        values = [
            [int(i) for i in list(line.strip())] for line in f.readlines()
        ]

    return values


def trailhead_reached(data, coord):
    # Identify the summits that are available from that trailhead
    row, col = coord
    value = data[row][col]
    if value == 9:
        return {coord}
    available = set()

    for new_coord in [
        (row + 1, col),
        (row - 1, col),
        (row, col + 1),
        (row, col - 1),
    ]:
        if 0 <= new_coord[0] < len(data) and 0 <= new_coord[1] < len(data[0]):
            if data[new_coord[0]][new_coord[1]] == value + 1:
                available = available.union(trailhead_reached(data, new_coord))
    return available


def distinct_paths(data, coord, path):
    # Identify the distinct paths to summits that are available from that trailhead
    row, col = coord
    value = data[row][col]
    if value == 9:
        return {path}
    available = set()

    for new_coord in [
        (row + 1, col),
        (row - 1, col),
        (row, col + 1),
        (row, col - 1),
    ]:
        if 0 <= new_coord[0] < len(data) and 0 <= new_coord[1] < len(data[0]):
            if data[new_coord[0]][new_coord[1]] == value + 1:
                available = available.union(
                    distinct_paths(data, new_coord, (*path, new_coord)),
                )

    return available


def part_1(path, submit):
    """Part 1/Star 1"""

    # Get the data
    data = get_input(path)

    answer = 0
    for i_row, row in enumerate(data):
        for j_col, value in enumerate(row):
            if value == 0:
                answer += len(trailhead_reached(data, (i_row, j_col)))

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
    for i_row, row in enumerate(data):
        for j_col, value in enumerate(row):
            if value == 0:
                answer += len(
                    distinct_paths(data, (i_row, j_col), ((i_row, j_col)))
                )

    # Print out the response
    print(f"Task 2 Answer: {answer}")

    # Submit the answer
    if submit:
        aocd.submit(answer, part="b", day=int(DAY), year=int(YEAR))


if __name__ == "__main__":
    """
    Run using e.g.
        `python day-10.py -test`
        `python day-10.py`
        `python day-10.py -submit`
        `python day-10.py -test -2`
        `python day-10.py -2`
        `python day-10.py -test -both`
        `python day-10.py -both`
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
