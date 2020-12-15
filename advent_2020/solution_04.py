import re

from dataclasses import dataclass
from typing import Optional, Collection, Dict, List


UNIT_CENTIMETERS: str = "cm"

UNIT_INCHES: str = "in"


@dataclass
class CredentialsDocument:
    birth_year: Optional[str]

    issue_year: Optional[str]

    expiration_year: Optional[str]

    height: Optional[str]

    hair_color: Optional[str]

    eye_color: Optional[str]

    passport_id: Optional[str]

    country_id: Optional[str]

    @property
    def is_simply_valid(self) -> bool:
        return all([
            self.birth_year,
            self.issue_year,
            self.expiration_year,
            self.height,
            self.hair_color,
            self.eye_color,
            self.passport_id,
        ])

    @property
    def is_completely_valid(self) -> bool:
        return all([
            self.is_birth_year_valid,
            self.is_issue_year_valid,
            self.is_expiration_year_valid,
            self.is_height_valid,
            self.is_hair_color_valid,
            self.is_eye_color_valid,
            self.is_passport_id_valid,
        ])

    @property
    def is_birth_year_valid(self) -> bool:
        return (
            self.birth_year
            and len(self.birth_year) == 4
            and self.birth_year.isnumeric()
            and 1920 <= int(self.birth_year) <= 2002
        )

    @property
    def is_issue_year_valid(self) -> bool:
        return (
            self.issue_year
            and len(self.issue_year) == 4
            and self.issue_year.isnumeric()
            and 2010 <= int(self.issue_year) <= 2020
        )

    @property
    def is_expiration_year_valid(self) -> bool:
        return (
            self.expiration_year
            and len(self.expiration_year) == 4
            and self.expiration_year.isnumeric()
            and 2020 <= int(self.expiration_year) <= 2030
        )

    @property
    def is_height_valid(self) -> bool:
        if not self.height or not self.height.isalnum():
            return False

        # Assume unit is always 2 characters long.

        unit: str = self.height[-2:]
        number_text: str = self.height[:-2]

        # Test number is actually a number.

        if not number_text.isnumeric():
            return False

        number: int = int(number_text)

        if unit == UNIT_INCHES:
            return 59 <= number <= 76
        elif unit == UNIT_CENTIMETERS:
            return 150 <= number <= 193

        return False

    """
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    """

    @property
    def is_hair_color_valid(self) -> bool:
        if not self.hair_color:
            return False

        return bool(re.match(r"^#[0-9a-f]{6}$", self.hair_color))

    @property
    def is_eye_color_valid(self) -> bool:
        if not self.eye_color:
            return False

        return self.eye_color in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")

    @property
    def is_passport_id_valid(self) -> bool:
        return self.passport_id and self.passport_id.isnumeric() and len(self.passport_id) == 9


def run_2020_04_1() -> str:
    return str(len(list(filter(lambda doc: doc.is_simply_valid, read_credentials()))))


def run_2020_04_2() -> str:
    return str(len(list(filter(lambda doc: doc.is_completely_valid, read_credentials()))))


def read_credentials() -> List[CredentialsDocument]:
    credentials: List[CredentialsDocument] = []

    with open("advent_2020/data/04.txt") as f_in:
        lines_text: str = f_in.read()

        # Create the passports.

        for person in lines_text.split("\n\n"):
            # We are assuming line feeds split the file.

            fragments: Collection[str] = person.replace("\n", " ").split(" ")

            # For each fragment, we parse to a dictionary containing keys to instance fields.

            key_to_value: Dict[str, str] = {
                fragment[0]: fragment[1]
                for fragment in [
                    fragment.split(":") for fragment in fragments if fragment
                ]
            }

            credentials.append(
                CredentialsDocument(
                    birth_year=key_to_value.get("byr"),
                    issue_year=key_to_value.get("iyr"),
                    expiration_year=key_to_value.get("eyr"),
                    height=key_to_value.get("hgt"),
                    hair_color=key_to_value.get("hcl"),
                    eye_color=key_to_value.get("ecl"),
                    passport_id=key_to_value.get("pid"),
                    country_id=key_to_value.get("cid"),
                )
            )

    return credentials
