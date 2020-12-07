from dataclasses import dataclass
from typing import Collection, List


@dataclass
class RuleAndPassword:
    low_number: int

    high_number: int

    character: str

    password: str

    def validate_password_01(self):
        # Determine the number of times the character in this dataclass appears in the password.

        seen_times: int = len(tuple(filter(lambda c: c == self.character, self.password)))

        if seen_times > self.high_number or seen_times < self.low_number:
            return False

        return True

    def validate_password_02(self):
        low_matches: bool = self.password[self.low_number - 1] == self.character
        high_matches: bool = self.password[self.high_number - 1] == self.character

        return low_matches ^ high_matches


def run_2020_02_1() -> str:
    with open("advent_2020/data/02.txt") as f_in:
        lines_text: str = f_in.read()

        rules_and_data = read_rules_and_passwords(lines_text)

        # Filter and count the valid passwords in the collected passwords and rules list.

        return str(len(tuple(filter(lambda r: r.validate_password_01(), rules_and_data))))


def run_2020_02_2() -> str:
    with open("advent_2020/data/02.txt") as f_in:
        lines_text: str = f_in.read()

        rules_and_data = read_rules_and_passwords(lines_text)

        # Filter and count the valid passwords in the collected passwords and rules list.

        return str(len(tuple(filter(lambda r: r.validate_password_02(), rules_and_data))))


def read_rules_and_passwords(lines_text):
    # Create a tuple of all non-empty lines.

    lines_with_numbers: Collection[str] = tuple(filter(bool, lines_text.split("\n")))

    # Process each line as rule -> data.

    rules_and_data: List[RuleAndPassword] = []
    for line in lines_with_numbers:
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
