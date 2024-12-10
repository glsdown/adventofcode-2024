import sys

import aocd
from dotenv import load_dotenv

load_dotenv()

# Set the day and year
DAY = "09"
YEAR = "2024"


def get_input(path):
    """Load the data from the file"""

    # Open the file
    with open(f"{path}/day-{DAY}.txt", "r") as f:
        values = f.read().strip()

    return values


def part_1(path, submit):
    """Part 1/Star 1"""

    # Get the data
    data = get_input(path)

    # Find what it looks like
    file_id = 0
    file_pattern = []
    for i, block in enumerate(data):
        if i % 2 == 0:
            file_pattern += int(block) * [file_id]
            file_id += 1
        else:
            file_pattern += int(block) * ["."]

    # Get the answer
    answer = 0
    last = -1
    for index, block in enumerate(file_pattern):
        # Check if reached the start again
        if len(file_pattern) + last < index:
            break
        # Fill in any empty space
        if block == ".":
            # Get the last file id
            while file_pattern[last] == ".":
                last -= 1
            answer += index * int(file_pattern[last])
            file_pattern[last] = "."
            last -= 1
        # Calculate the checksum
        else:
            answer += index * int(block)

    # Print out the response
    print(f"Task 1 Answer: {answer}")

    # Submit the answer
    if submit:
        aocd.submit(answer, part="a", day=int(DAY), year=int(YEAR))


def part_2(path, submit):
    """Part 2/Star 2"""

    # Get the data
    data = get_input(path)

    # Process the data
    file_id = 0
    block_index = 0
    files = []
    gaps = []
    for data_index, value in enumerate(data):
        detail = {"index": block_index, "length": int(value)}
        block_index += int(value)
        if data_index % 2 == 0:
            files.append({"file_id": file_id, **detail})
            file_id += 1
        else:
            gaps.append(detail)

    # Move the files
    for file in files[::-1]:
        for gap in gaps:
            if gap["index"] > file["index"]:
                break
            if gap["length"] >= file["length"]:
                file["index"] = gap["index"]
                gap["length"] -= file["length"]
                gap["index"] += file["length"]
                break

    # Get the checksum
    answer = sum(
        [
            sum(
                [
                    file["file_id"] * (file["index"] + i)
                    for i in range(file["length"])
                ]
            )
            for file in files
        ]
    )

    # Print out the response
    print(f"Task 2 Answer: {answer}")

    # Submit the answer
    if submit:
        aocd.submit(answer, part="b", day=int(DAY), year=int(YEAR))


if __name__ == "__main__":
    """
    Run using e.g.
        `python day-09.py -test`
        `python day-09.py`
        `python day-09.py -submit`
        `python day-09.py -test -2`
        `python day-09.py -2`
        `python day-09.py -test -both`
        `python day-09.py -both`
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
