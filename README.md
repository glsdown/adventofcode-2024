# Advent of Code 2024

These are my solutions to the [2024 Advent of Code](https://adventofcode.com/2024). They will not be neatly polished solutions, but attempt to simply solve the problem.

To use this, you need to ensure that you have set up the [AOC Session cookie](https://pypi.org/project/advent-of-code-data/). To get this, in a browser, log into AOC and head to one of the pages where you get your input data e.g. day 1 [here](https://adventofcode.com/2024/day/1/input). Then open the inspector, and head to the Network tab. Refresh the page, and look for the "input" request. Click on that, and look at the Headers. There should be one that says "Cookie". The value after `session=` is the AOC session cookie to use.

To automatically generate the files for the next day to complete, first install the requirements:

```sh
pip install -r requirements.txt
```

Then make use of the helper function `get_next_day.py`

```sh
python get_next_day.py
```

This will retrieve your puzzle input, as well as create a template python file to solve it. It will also create a file for you to add the example data in from the question.