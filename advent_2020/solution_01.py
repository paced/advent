"""
...you need to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

```
1721
979
366
299
675
1456
```

In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together
produces 1721 * 299 = 514579, so the correct answer is 514579.

Find the two entries (below) that sum to 2020; what do you get if you multiply them together?
"""


from typing import Collection, List

SUM_TARGET: int = 2020
"""The sum target for two numbers to calculate a product of for this solution."""


def find_two_multiples_adding_to_2020(numbers: Collection[int]) -> Collection[int]:
    """
    Iterate and find all permutations of the numbers and return the product of the two numbers that
    sum to 2020.

    Parameters
    ----------
    numbers : `Collection[int]`
        The numbers to add together.

    Returns
    -------
    `str`
        A textual representation of the multiple of the numbers in the input adding to 2020.
    """

    results: List[int] = []

    for index_a, number_a in enumerate(numbers):
        for _, number_b in enumerate(numbers, index_a):
            if number_a + number_b == SUM_TARGET:
                results.append(number_a * number_b)

    if not results:
        raise RuntimeError("Inputs are not valid. Nothing adds to 2020.")

    return results


def find_three_multiples_adding_to_2020(numbers):
    results = []

    for index_a, number_a in enumerate(numbers):
        for index_b, number_b in enumerate(numbers, index_a):
            if number_a + number_b > SUM_TARGET:
                continue

            for _, number_c in enumerate(numbers, index_b):
                if number_a + number_b + number_c == SUM_TARGET:
                    results.append(number_a * number_b * number_c)

    return results


def run_2020_01_1() -> str:
    """
    Run the main function and return a single result to be printed.

    Returns
    -------
    `str`
        The result to be printed.
    """

    with open("advent_2020/data/01.txt") as f_in:
        lines_text: str = f_in.read()

        # Read the file, and pass in the lines as integers into the determining function.

        lines_with_numbers: Collection[int] = tuple(
            map(int, filter(bool, lines_text.split("\n")))
        )

        return str(find_two_multiples_adding_to_2020(lines_with_numbers)[0])


def run_2020_01_2() -> str:
    """
    Run the main function and return a single result to be printed.

    Returns
    -------
    `str`
        The result to be printed.
    """

    with open("advent_2020/data/01.txt") as f_in:
        lines_text: str = f_in.read()

        # Read the file, and pass in the lines as integers into the determining function.

        lines_with_numbers: Collection[int] = tuple(
            map(int, filter(bool, lines_text.split("\n")))
        )

        return find_three_multiples_adding_to_2020(lines_with_numbers)[0]
