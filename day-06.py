import sys

import aocd
from dotenv import load_dotenv

load_dotenv()

# Set the day and year
DAY = "06"
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
    answer = 0

    guard_positions = set()
    guard_directions = (
        # Up
        ("^", -1, 0),
        # Right
        (">", 0, 1),
        # Down
        ("v", 1, 0),
        # Left
        ("<", 0, -1),
    )
    guard = 0

    no_rows = len(data)
    no_cols = len(data[0])

    # Find where guard currently is
    guard_current = ()
    for row in range(no_rows):
        for col in range(no_cols):
            if data[row][col] == guard_directions[guard][0]:
                guard_current = (row, col)
                break
        if guard_current:
            break

    # Get the guard positions
    while True:
        guard_next = (
            guard_current[0] + guard_directions[guard][1],
            guard_current[1] + guard_directions[guard][2],
        )
        if not (0 <= guard_next[0] < no_rows and 0 <= guard_next[1] < no_cols):
            # Guard has left
            break
        # Get guard's next move
        next_object = data[guard_next[0]][guard_next[1]]
        if next_object in (".", "^"):
            guard_positions.add(guard_next)
            guard_current = guard_next
        elif next_object == "#":
            guard = (guard + 1) % 4

    answer = len(guard_positions)

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
        `python day-06.py -test`
        `python day-06.py`
        `python day-06.py -submit`
        `python day-06.py -test -2`
        `python day-06.py -2`
        `python day-06.py -test -both`
        `python day-06.py -both`
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
