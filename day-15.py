import sys

import aocd
from dotenv import load_dotenv
from tqdm import tqdm

load_dotenv()

# Set the day and year
DAY = "15"
YEAR = "2024"

# Icons
ROBOT = "@"
WALL = "#"
EMPTY = "."
BOX = "O"
BOX_LEFT = "["
BOX_RIGHT = "]"

# Moves
MOVES = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}


def get_input(path):
    """Load the data from the file"""

    # Open the file
    with open(f"{path}/day-{DAY}.txt", "r") as f:
        warehouse_map, directions = f.read().split("\n\n")

    # Tidy up
    warehouse_map = [list(line) for line in warehouse_map.split("\n")]
    directions = directions.replace("\n", "")

    return warehouse_map, directions


def find_robot(warehouse_map):
    # Find the robot starting point
    for row_i, row in enumerate(warehouse_map):
        for col_j, value in enumerate(row):
            if value == ROBOT:
                return (row_i, col_j)


def print_grid(warehouse_map):
    for line in warehouse_map:
        print("".join(line))


def calculate_coordinates(warehouse_map, box=BOX):
    answer = 0
    for row_i, row in enumerate(warehouse_map):
        for col_j, value in enumerate(row):
            if value == box:
                answer += 100 * row_i + col_j
    return answer


def part_1(path, submit):
    """Part 1/Star 1"""

    # Get the data
    warehouse_map, directions = get_input(path)

    # Find the robot starting point
    robot = find_robot(warehouse_map)
    # Remove the robot - no longer required
    warehouse_map[robot[0]][robot[1]] = EMPTY

    # Move the robot
    for move in tqdm(directions):
        new_row, new_col = (
            robot[0] + MOVES[move][0],
            robot[1] + MOVES[move][1],
        )
        if warehouse_map[new_row][new_col] == EMPTY:
            # Clear space, so robot moves
            robot = (new_row, new_col)
        elif warehouse_map[new_row][new_col] == WALL:
            # Wall - don't move
            pass
        else:
            # Box, need to work out whether to move the box

            # Find the end of the line of boxes
            next_row, next_col = new_row, new_col
            while warehouse_map[next_row][next_col] == BOX:
                next_row += MOVES[move][0]
                next_col += MOVES[move][1]

            # Need to check the end of the line of boxes
            if warehouse_map[next_row][next_col] == EMPTY:
                # Boxes can move
                warehouse_map[next_row][next_col] = BOX
                warehouse_map[new_row][new_col] = EMPTY
                # Move the robot
                robot = (new_row, new_col)
            else:
                # Boxes can't move, so nothing happens
                pass

    # Print the grid
    print_grid(warehouse_map)

    # Get GPS coordinates of boxes
    answer = calculate_coordinates(warehouse_map, box=BOX)

    # Print out the response
    print(f"Task 1 Answer: {answer}")

    # Submit the answer
    if submit:
        aocd.submit(answer, part="a", day=int(DAY), year=int(YEAR))


def part_2(path, submit):
    """Part 2/Star 2"""

    # Get the data
    original_warehouse_map, directions = get_input(path)

    # Double the spaces
    warehouse_map = []
    for row in original_warehouse_map:
        new_row = []
        for space in row:
            if space in (EMPTY, WALL):
                new_row += [space, space]
            elif space == ROBOT:
                new_row += [ROBOT, EMPTY]
            else:
                new_row += [BOX_LEFT, BOX_RIGHT]
        warehouse_map.append(new_row)

    # Find the robot starting point
    robot = find_robot(warehouse_map)

    # Print the grid
    print_grid(warehouse_map)

    # Move the robot
    for move in tqdm(directions):
        to_move = {robot}
        stack = [robot]
        while stack:
            row, col = stack.pop()
            # "Move" the item
            row += MOVES[move][0]
            col += MOVES[move][1]
            if (row, col) not in to_move:
                if warehouse_map[row][col] in [BOX_LEFT, BOX_RIGHT]:
                    to_move.add((row, col))
                    stack.append((row, col))
                    if warehouse_map[row][col] == BOX_LEFT:
                        # Need to move the other half of the box
                        to_move.add((row, col + 1))
                        stack.append((row, col + 1))
                    elif warehouse_map[row][col] == BOX_RIGHT:
                        to_move.add((row, col - 1))
                        stack.append((row, col - 1))

        # Check everything can move
        if all(
            [
                warehouse_map[row + MOVES[move][0]][col + MOVES[move][1]]
                != WALL
                for (row, col) in to_move
            ]
        ):
            new_grid = [[EMPTY for _ in row] for row in warehouse_map]
            # Add the new item locations
            for row, col in to_move:
                new_grid[row + MOVES[move][0]][col + MOVES[move][1]] = (
                    warehouse_map[row][col]
                )

            # Add the old item locations
            for row_i in range(len(warehouse_map)):
                for col_j in range(len(warehouse_map[row_i])):
                    if (row_i, col_j) not in to_move and new_grid[row_i][
                        col_j
                    ] == EMPTY:
                        new_grid[row_i][col_j] = warehouse_map[row_i][col_j]

            warehouse_map = new_grid
            # Move the robot
            robot = (robot[0] + MOVES[move][0], robot[1] + MOVES[move][1])

    # Print the grid
    print_grid(warehouse_map)

    # Get GPS coordinates of boxes
    answer = calculate_coordinates(warehouse_map, box=BOX_LEFT)

    # Print out the response
    print(f"Task 2 Answer: {answer}")

    # Submit the answer
    if submit:
        aocd.submit(answer, part="b", day=int(DAY), year=int(YEAR))


if __name__ == "__main__":
    """
    Run using e.g.
        `python day-15.py -test`
        `python day-15.py`
        `python day-15.py -submit`
        `python day-15.py -test -2`
        `python day-15.py -2`
        `python day-15.py -test -both`
        `python day-15.py -both`
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
