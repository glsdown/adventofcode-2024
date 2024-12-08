import sys
from collections import defaultdict

import aocd
from dotenv import load_dotenv

load_dotenv()

# Set the day and year
DAY = "08"
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

    # Complete the task
    no_rows = len(data)
    no_cols = len(data[0])

    antenna_map = defaultdict(list)

    # Find the antennae
    for r, row in enumerate(data):
        for c, value in enumerate(row):
            if value != ".":
                antenna_map[value].append((r, c))

    # Find the antinodes
    antinodes = set()
    for _, locations in antenna_map.items():
        for l, location in enumerate(locations):
            # Get the antinodes for that location and the other pairs
            row, col = location
            for next_row, next_col in locations[l + 1 :]:
                antinode_row = row - (next_row - row)
                antinode_col = col - (next_col - col)
                if 0 <= antinode_row < no_rows and 0 <= antinode_col < no_cols:
                    antinodes.add((antinode_row, antinode_col))

                antinode_row = next_row + (next_row - row)
                antinode_col = next_col + (next_col - col)
                if 0 <= antinode_row < no_rows and 0 <= antinode_col < no_cols:
                    antinodes.add((antinode_row, antinode_col))

    answer = len(antinodes)

    # Print out the response
    print(f"Task 1 Answer: {answer}")

    # Submit the answer
    if submit:
        aocd.submit(answer, part="a", day=int(DAY), year=int(YEAR))


def part_2(path, submit):
    """Part 2/Star 2"""

    # Get the data
    data = get_input(path)

    # Complete the task
    no_rows = len(data)
    no_cols = len(data[0])

    antenna_map = defaultdict(list)

    # Find the antennae
    for r, row in enumerate(data):
        for c, value in enumerate(row):
            if value != ".":
                antenna_map[value].append((r, c))

    # Find the antinodes
    antinodes = set()
    for _, locations in antenna_map.items():
        for l, location in enumerate(locations):
            # Get the antinodes for that location and the other pairs
            row, col = location
            for next_row, next_col in locations[l + 1 :]:
                # Extend in each direction
                row_difference = next_row - row
                col_difference = next_col - col

                # Look in one direction
                offset = 0
                while True:
                    antinode_row = row - offset * row_difference
                    antinode_col = col - offset * col_difference
                    if (
                        0 <= antinode_row < no_rows
                        and 0 <= antinode_col < no_cols
                    ):
                        antinodes.add((antinode_row, antinode_col))
                        offset += 1
                    else:
                        # Outside the grid - stop moving
                        break

                # Look in other direction
                offset = 0
                while True:
                    antinode_row = next_row + offset * row_difference
                    antinode_col = next_col + offset * col_difference
                    if (
                        0 <= antinode_row < no_rows
                        and 0 <= antinode_col < no_cols
                    ):
                        antinodes.add((antinode_row, antinode_col))
                        offset += 1
                    else:
                        # Outside the grid - stop moving
                        break

    answer = len(antinodes)

    # Print out the response
    print(f"Task 2 Answer: {answer}")

    # Submit the answer
    if submit:
        aocd.submit(answer, part="b", day=int(DAY), year=int(YEAR))


if __name__ == "__main__":
    """
    Run using e.g.
        `python day-08.py -test`
        `python day-08.py`
        `python day-08.py -submit`
        `python day-08.py -test -2`
        `python day-08.py -2`
        `python day-08.py -test -both`
        `python day-08.py -both`
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
