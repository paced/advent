import math
from enum import Enum
from typing import List, Tuple


class Terrain(Enum):
    SPACE = "."
    TREE = "#"


def calculate_trees_encountered(snowy_map, x_slope: int = 3, y_slope: int = 1) -> int:
    # Assuming snowy_map is not an empty array.

    line_length: int = len(snowy_map[0])
    x_position: int = 0

    tree_count: int = 0

    for index, row in enumerate(snowy_map):
        if index % y_slope:
            # For y-slopes > 1
            continue

        x_position = x_position % line_length

        if row[x_position] == Terrain.TREE:
            tree_count += 1

        x_position += x_slope

    return tree_count


def run_2020_03_1() -> str:
    snowy_map: List[List[Terrain]] = []

    with open("advent_2020/data/03.txt") as f_in:
        lines_text: str = f_in.read()

        # Create the 2D map.

        for line in lines_text.splitlines():
            if not line:
                continue

            snowy_map.append(list(map(lambda item: Terrain(item), list(line))))

        # Run the solution.

        return str(calculate_trees_encountered(snowy_map))


def run_2020_03_2() -> str:
    # Right 1, down 1.
    # Right 3, down 1. (This is the slope you already checked.)
    # Right 5, down 1.
    # Right 7, down 1.
    # Right 1, down 2.

    test_slopes: List[Tuple[int, int]] = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]

    snowy_map: List[List[Terrain]] = []

    # A list of integers to multiply together for the result.

    product_list: List[int] = []

    with open("advent_2020/data/03.txt") as f_in:
        lines_text: str = f_in.read()

        # Create the 2D map.

        for line in lines_text.splitlines():
            if not line:
                continue

            snowy_map.append(list(map(lambda item: Terrain(item), list(line))))

        # Run the for all the test slopes

        for slope in test_slopes:
            product_list.append(
                calculate_trees_encountered(snowy_map, x_slope=slope[0], y_slope=slope[1])
            )

        return str(math.prod(product_list))
