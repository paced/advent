"""Run any of the completed solutions."""

from argparse import ArgumentParser, Namespace
from os import environ
from typing import Callable, Dict, Tuple

from advent_2020.solution_01 import run_2020_01_1, run_2020_01_2
from advent_2020.solution_02 import run_2020_02_1, run_2020_02_2
from advent_2020.solution_03 import run_2020_03_1, run_2020_03_2
from advent_2020.solution_04 import run_2020_04_1, run_2020_04_2

SOLUTION_MAP: Dict[Tuple[str, str, str], Callable] = {
    ("2020", "1", "1"): run_2020_01_1,
    ("2020", "1", "2"): run_2020_01_2,
    ("2020", "2", "1"): run_2020_02_1,
    ("2020", "2", "2"): run_2020_02_2,
    ("2020", "3", "1"): run_2020_03_1,
    ("2020", "3", "2"): run_2020_03_2,
    ("2020", "4", "1"): run_2020_04_1,
    ("2020", "4", "2"): run_2020_04_2,
}
"""A mapping from a user input to a function to call."""


def parse_stdin() -> Namespace:
    """
    Read STDIN and run the parser for the specified solution requested.

    Returns
    -------
    `Namespace`
        The `Namespace` for the runner.
    """

    parser: ArgumentParser = ArgumentParser(description="Run a completed AoC solution.")

    parser.add_argument("year", type=str, help="The year of the advent.")
    parser.add_argument("problem", type=str, help="The problem of the advent.")
    parser.add_argument("sub_problem", type=str, help="The sub-problem (either 1 or 2).")

    return parser.parse_args()


def run(year, problem, sub_problem) -> str:
    """
    Run the specified problem's solution.

    Parameters
    ----------
    year : `str`
        The year target.

    problem : `str`
        The problem target.

    sub_problem : `str`
        The sub-problem target.

    Returns
    -------
    `str`
        The text representation of the solution.
    """

    solution_map_key: Tuple[str, str, str] = (year, problem, sub_problem)

    if solution_map_key not in SOLUTION_MAP:
        raise RuntimeError(
            f"Arguments are not valid. No such solution exists (yet) for a [{year}] (year) "
            f"[{problem}] (problem) [{sub_problem}] (sub-problem). Try again!"
        )

    return SOLUTION_MAP[solution_map_key]()


if __name__ == "__main__":
    debug_mode: bool = bool(environ.get("DEBUG", False))

    if debug_mode:
        # Run everything in order and make it look nice.

        for key in SOLUTION_MAP:
            print(f"Solution for {key[0]} P{key[1]}-{key[2]}: {run(key[0], key[1], key[2])}")
    else:
        # If we're not in debug mode, run the specific solution.

        parsed_args: Namespace = parse_stdin()

        parsed_year: str = parsed_args.year
        parsed_problem: str = parsed_args.problem
        parsed_sub_problem: str = parsed_args.sub_problem

        print(run(parsed_year, parsed_problem, parsed_sub_problem))
