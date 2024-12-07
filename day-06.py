import sys
from copy import deepcopy

import aocd
from dotenv import load_dotenv

load_dotenv()

# Set the day and year
DAY = "06"
YEAR = "2024"

GUARD_DIRECTIONS = (
    # Up
    (-1, 0),
    # Right
    (0, 1),
    # Down
    (1, 0),
    # Left
    (0, -1),
)


def get_input(path):
    """Load the data from the file"""

    # Open the file
    with open(f"{path}/day-{DAY}.txt", "r") as f:
        values = [list(line.strip()) for line in f.readlines()]

    return values


def get_starting_position(grid):
    no_rows = len(grid)
    no_cols = len(grid[0])

    # Find where guard currently is
    guard_current = ()
    for row in range(no_rows):
        for col in range(no_cols):
            if grid[row][col] == "^":
                guard_current = (row, col)
                return guard_current


def part_1(path, submit):
    """Part 1/Star 1"""

    # Get the data
    grid = get_input(path)

    # Complete the task
    seen_locations = set()
    guard_index = 0

    no_rows = len(grid)
    no_cols = len(grid[0])

    # Find where guard currently is
    guard_current = get_starting_position(grid)

    # Get the guard positions
    while True:
        guard_next = (
            guard_current[0] + GUARD_DIRECTIONS[guard_index][0],
            guard_current[1] + GUARD_DIRECTIONS[guard_index][1],
        )
        if not (0 <= guard_next[0] < no_rows and 0 <= guard_next[1] < no_cols):
            # Guard has left
            break
        # Get guard's next move
        next_object = grid[guard_next[0]][guard_next[1]]
        if next_object in (".", "^"):
            seen_locations.add(guard_next)
            guard_current = guard_next
        elif next_object == "#":
            guard_index = (guard_index + 1) % 4

    answer = len(seen_locations)

    # Print out the response
    print(f"Task 1 Answer: {answer}")

    # Submit the answer
    if submit:
        aocd.submit(answer, part="a", day=int(DAY), year=int(YEAR))


def check_loop(
    grid,
    seen_locations_directions,
    guard_current,
    guard_index,
):

    no_rows = len(grid)
    no_cols = len(grid[0])

    while True:
        guard_next = (
            guard_current[0] + GUARD_DIRECTIONS[guard_index][0],
            guard_current[1] + GUARD_DIRECTIONS[guard_index][1],
        )
        if not (0 <= guard_next[0] < no_rows and 0 <= guard_next[1] < no_cols):
            # Guard has left
            return False
        # Get guard's next move
        next_object = grid[guard_next[0]][guard_next[1]]
        if next_object in (".", "^"):
            if (guard_next, guard_index) in seen_locations_directions:
                # Loop has been found - been in this position and direction before
                return True
            seen_locations_directions.add((guard_next, guard_index))
            guard_current = guard_next
        elif next_object == "#":
            guard_index = (guard_index + 1) % 4


def part_2(path, submit):
    """Part 2/Star 2"""

    # Get the data
    grid = get_input(path)

    # Complete the task
    answer = 0

    seen_locations = set()
    guard_index = 0

    no_rows = len(grid)
    no_cols = len(grid[0])

    # Find where guard currently is
    guard_current = get_starting_position(grid)

    # Need to exclude the starting location from potential place to add object
    seen_locations_directions = {(guard_current, 0)}

    # Get the guard positions
    # Complete the task
    seen_locations = set()
    guard_index = 0

    no_rows = len(grid)
    no_cols = len(grid[0])

    # Find where guard currently is
    guard_current = get_starting_position(grid)

    potential_locations = []

    # Get the guard positions
    while True:
        guard_next = (
            guard_current[0] + GUARD_DIRECTIONS[guard_index][0],
            guard_current[1] + GUARD_DIRECTIONS[guard_index][1],
        )
        if not (0 <= guard_next[0] < no_rows and 0 <= guard_next[1] < no_cols):
            # Guard has left
            break
        # Get guard's next move
        next_object = grid[guard_next[0]][guard_next[1]]
        if next_object in (".", "^"):
            # Try adding an obstacle in that location
            if guard_next not in seen_locations:
                # If we haven't tried this spot before add an obstacle
                grid_clone = deepcopy(grid)
                grid_clone[guard_next[0]][guard_next[1]] = "#"
                # Check if it creates a loop
                if check_loop(
                    grid_clone,
                    deepcopy(seen_locations_directions),
                    guard_current,
                    guard_index,
                ):
                    potential_locations.append(guard_next)
            # Mark that we've seen that location and direction before
            seen_locations_directions.add((guard_next, guard_index))
            # Move the guard on
            seen_locations.add(guard_next)
            guard_current = guard_next
        elif next_object == "#":
            guard_index = (guard_index + 1) % 4

    answer = len(potential_locations)

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
