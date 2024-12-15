import re
import sys
from time import sleep

import aocd
from dotenv import load_dotenv

load_dotenv()

# Set the day and year
DAY = "14"
YEAR = "2024"

INPUT_PATTERN = re.compile(r"p\=(\d+)\,(\d+) v\=(\-?\d+),(\-?\d+)")


def get_input(path):
    """Load the data from the file"""

    # Open the file
    with open(f"{path}/day-{DAY}.txt", "r") as f:
        values = [
            INPUT_PATTERN.match(line.strip()).groups()
            for line in f.readlines()
        ]

    return values


def part_1(path, submit):
    """Part 1/Star 1"""

    # Get the data
    data = get_input(path)

    # Get the grid details
    number_steps = 100
    if "tests" in path:
        width = 11
        height = 7
        print_grid = True
    else:
        width = 101
        height = 103
        print_grid = False

    # For display purposes only
    if print_grid:
        grid = [["." for _ in range(width)] for __ in range(height)]

    # Identify which quadrant the robot ends up in
    quads = [0, 0, 0, 0]
    for robot in data:
        # Identify where the robot ends up
        col, row, v_col, v_row = robot
        p_col = (int(col) + number_steps * int(v_col)) % width
        p_row = (int(row) + number_steps * int(v_row)) % height

        # For display purposes only
        if print_grid:
            if grid[p_row][p_col] == ".":
                grid[p_row][p_col] = 1
            else:
                grid[p_row][p_col] += 1

        # Identify the quadrant the robot is in
        if p_col < (width - 1) // 2:
            if p_row < (height - 1) // 2:
                quads[0] += 1
            elif p_row > (height - 1) // 2:
                quads[1] += 1
        elif p_col > (width - 1) // 2:
            if p_row < (height - 1) // 2:
                quads[2] += 1
            elif p_row > (height - 1) // 2:
                quads[3] += 1

    answer = quads[0] * quads[1] * quads[2] * quads[3]

    # Print the grid (visual)
    if print_grid:
        grid[height // 2] = [" " for _ in range(width)]
        for i in range(height):
            grid[i][width // 2] = " "
        for line in grid:
            print("".join([str(i) for i in line]))

    # Print out the response
    print(f"Task 1 Answer: {answer}")

    # Submit the answer
    if submit:
        aocd.submit(answer, part="a", day=int(DAY), year=int(YEAR))


def output_grid(robots, width, height):

    grid = [["." for _ in range(width)] for __ in range(height)]
    for row, col in robots:
        grid[row][col] = "#"

    with open(f"outputs/day-{DAY}.txt", "a") as f:
        f.write("\n".join(["".join(line) for line in grid]))


def part_2(path, submit):
    """Part 2/Star 2"""

    # Get the data
    data = get_input(path)

    with open(f"outputs/day-{DAY}.txt", "w") as f:
        f.write("")

    # Get the grid details
    number_steps = 10000
    if "tests" in path:
        width = 11
        height = 7
    else:
        width = 101
        height = 103
    divider = "-" * (width + 10)

    # Spotted a pattern every 101 steps 
    for step in range(4611, number_steps, 101):
        robots = set()
        for robot in data:
            # Identify where the robot ends up
            col, row, v_col, v_row = robot
            p_col = (int(col) + step * int(v_col)) % width
            p_row = (int(row) + step * int(v_row)) % height

            robots.add((p_row, p_col))

        # For display purposes only
        with open(f"outputs/day-{DAY}.txt", "a") as f:
            f.write(f"\n\n{step}\n{divider}\n")
        output_grid(robots, width, height)

    answer = 7338 # Manually identified in file

    # Print out the response
    print(f"Task 2 Answer: {answer}")

    # Submit the answer
    if submit:
        aocd.submit(answer, part="b", day=int(DAY), year=int(YEAR))


if __name__ == "__main__":
    """
    Run using e.g.
        `python day-14.py -test`
        `python day-14.py`
        `python day-14.py -submit`
        `python day-14.py -test -2`
        `python day-14.py -2`
        `python day-14.py -test -both`
        `python day-14.py -both`
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
