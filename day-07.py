import sys

import aocd
from dotenv import load_dotenv

load_dotenv()

# Set the day and year
DAY = "07"
YEAR = "2024"


def get_input(path):
    """Load the data from the file"""

    # Open the file
    with open(f"{path}/day-{DAY}.txt", "r") as f:
        values = [
            (
                int(line.strip().split(":")[0].strip()),
                [int(i) for i in line.strip().split(":")[1].strip().split()],
            )
            for line in f.readlines()
        ]

    return values


def part_1(path, submit):
    """Part 1/Star 1"""

    # Get the data
    data = get_input(path)

    def get_possiblity(target, total, options):
        if not options:
            return int(target == total)
        if total > target:
            # Only multiplication and addition so can't work
            return False
        if total == 0:
            # Need to handle the 'first' one for multiplication
            next_mult = options[0]
        else:
            next_mult = total * options[0]
        return get_possiblity(
            target, next_mult, options[1:]
        ) or get_possiblity(target, total + options[0], options[1:])

    answer = sum(
        get_possiblity(target, 0, values) * target for target, values in data
    )

    # Print out the response
    print(f"Task 1 Answer: {answer}")

    # Submit the answer
    if submit:
        aocd.submit(answer, part="a", day=int(DAY), year=int(YEAR))


def part_2(path, submit):
    """Part 2/Star 2"""

    # Get the data
    data = get_input(path)

    def get_possiblity(target, total, options):
        if not options:
            return int(target == total)
        if total > target:
            # Only multiplication and addition so can't work
            return False
        if total == 0:
            # Need to handle the 'first' one
            next_mult = options[0]
        else:
            next_mult = total * options[0]
        return (
            get_possiblity(target, next_mult, options[1:])
            or get_possiblity(target, total + options[0], options[1:])
            or get_possiblity(
                target, int(str(total) + str(options[0])), options[1:]
            )
        )

    answer = sum(
        get_possiblity(target, 0, values) * target for target, values in data
    )

    # Print out the response
    print(f"Task 2 Answer: {answer}")

    # Submit the answer
    if submit:
        aocd.submit(answer, part="b", day=int(DAY), year=int(YEAR))


if __name__ == "__main__":
    """
    Run using e.g.
        `python day-07.py -test`
        `python day-07.py`
        `python day-07.py -submit`
        `python day-07.py -test -2`
        `python day-07.py -2`
        `python day-07.py -test -both`
        `python day-07.py -both`
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
