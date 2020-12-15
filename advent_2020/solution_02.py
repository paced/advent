from dataclasses import dataclass
from typing import Collection, List


@dataclass
class RuleAndPassword:
    """A rule consisting of a low number, high number, and character, and a stored password."""

    low_number: int
    """A low number."""

    high_number: int
    """A high number."""

    character: str
    """A single character."""

    password: str
    """A password."""

    def validate_password_01(self) -> bool:
        """
        Validate a password based on a simple validation rule: seen times is at least the "low
        number" and at most the "high number."

        Returns
        -------
        `bool`
            Whether the password is valid using this rule.
        """

        # Determine the number of times the character in this dataclass appears in the password.

        seen_times: int = len(tuple(filter(lambda c: c == self.character, self.password)))

        return self.low_number <= seen_times <= self.high_number

    def validate_password_02(self) -> bool:
        """
        Validate a password based on a more complex validation rule: the 1-indexed character of
        the password equals the character set. The two matches to check are the low number and
        high number indexes.

        Returns
        -------
        `bool`
            Whether the password is valid using this rule.
        """

        low_matches: bool = self.password[self.low_number - 1] == self.character
        high_matches: bool = self.password[self.high_number - 1] == self.character

        return low_matches ^ high_matches


def read_rules_and_passwords(lines: Collection[str]) -> List[RuleAndPassword]:
    """
    Parse `RuleAndPassword`s from a `Collection` of lines.

    Parameters
    ----------
    lines : `Collection[str]`
        The lines in the file.

    Returns
    -------
    `List[RuleAndPassword]`
        A list of `RuleAndPassword`s.
    """

    # Process each line as rule -> data.

    rules_and_data: List[RuleAndPassword] = []
    for line in lines:
        # Assume no index errors.

        line_fragments: List[str] = line.split(" ")

        # Find occurrence numbers.

        number_fragments: List[str] = line_fragments[0].split("-")

        min_times: int = int(number_fragments[0])
        max_times: int = int(number_fragments[1])

        # Find character by removing one colon from the end of the fragment

        character: str = line_fragments[1][:-1]

        # Find the password.

        password = line_fragments[2]

        # Create the rule + password object. We don't really need to add to the array, but
        # we do anyway for robustness (could just add a counter here).

        rules_and_data.append(
            RuleAndPassword(
                low_number=min_times,
                high_number=max_times,
                character=character,
                password=password,
            )
        )

    return rules_and_data


def run_2020_02_1() -> str:
    """
    Run the main function and return a single result to be printed.

    Returns
    -------
    `str`
        The result to be printed.
    """

    with open("advent_2020/data/02.txt") as f_in:
        # Read the text and store each line in a collection.

        rules_and_data = read_rules_and_passwords(tuple(filter(bool, f_in.read().split("\n"))))

        # Filter and count the valid passwords in the collected passwords and rules list.

        return str(len(tuple(filter(lambda r: r.validate_password_01(), rules_and_data))))


def run_2020_02_2() -> str:
    """
    Run the main function and return a single result to be printed.

    Returns
    -------
    `str`
        The result to be printed.
    """

    with open("advent_2020/data/02.txt") as f_in:
        # Read the text and store each line in a collection.

        rules_and_data = read_rules_and_passwords(tuple(filter(bool, f_in.read().split("\n"))))

        # Filter and count the valid passwords in the collected passwords and rules list.

        return str(len(tuple(filter(lambda r: r.validate_password_02(), rules_and_data))))
