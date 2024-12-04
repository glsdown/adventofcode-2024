import sys

import aocd
from dotenv import load_dotenv

load_dotenv()

# Set the day and year
DAY = "04"
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

    # Find XMAS occurrences
    no_rows = len(data)
    no_cols = len(data[0])
    for row_i, row in enumerate(data):
        for col_j, col in enumerate(row):
            if col == "X":
                # Need to check if it starts xmas
                for row_offset in [-1, 0, 1]:
                    for col_offset in [-1, 0, 1]:
                        if not (row_offset == 0 and col_offset == 0):

                            if (
                                0 <= row_i + 3 * row_offset < no_rows
                                and 0 <= col_j + 3 * col_offset < no_cols
                                and data[row_i + row_offset][
                                    col_j + col_offset
                                ]
                                == "M"
                                and data[row_i + 2 * row_offset][
                                    col_j + 2 * col_offset
                                ]
                                == "A"
                                and data[row_i + 3 * row_offset][
                                    col_j + 3 * col_offset
                                ]
                                == "S"
                            ):
                                answer += 1

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

    # Find X-MAS occurrences
    no_rows = len(data)
    no_cols = len(data[0])
    for row_i in range(1, no_rows - 1):
        for col_j in range(1, no_cols - 1):
            col = data[row_i][col_j]
            if col == "A":
                # Need to check if it is the centre of the X
                top_left = (row_i - 1, col_j - 1)
                bottom_right = (row_i + 1, col_j + 1)

                top_right = (row_i - 1, col_j + 1)
                bottom_left = (row_i + 1, col_j - 1)

                if {
                    data[top_left[0]][top_left[1]],
                    data[bottom_right[0]][bottom_right[1]],
                } == {"M", "S"} and {
                    data[top_right[0]][top_right[1]],
                    data[bottom_left[0]][bottom_left[1]],
                } == {
                    "M",
                    "S",
                }:
                    answer += 1

    # Print out the response
    print(f"Task 2 Answer: {answer}")

    # Submit the answer
    if submit:
        aocd.submit(answer, part="b", day=int(DAY), year=int(YEAR))


if __name__ == "__main__":
    """
    Run using e.g.
        `python day-04.py -test`
        `python day-04.py`
        `python day-04.py -submit`
        `python day-04.py -test -2`
        `python day-04.py -2`
        `python day-04.py -test -both`
        `python day-04.py -both`
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
