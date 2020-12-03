from dataclasses import dataclass


with open('input') as f:
    INPUT = f.read().splitlines()


@dataclass
class Password:
    """
    Represents the following line:

        '1-3 a: abcde'
    """
    first_position: int
    second_position: int
    character: str
    password: str

    @classmethod
    def parse(cls, line: str):
        elements = line.split()
        bounds_str = elements[0]
        bounds = bounds_str.split('-')
        return cls(
            int(bounds[0]),
            int(bounds[1]),
            elements[1][0],
            elements[2],
        )

    def is_valid(self) -> bool:
        first_match = self.password[self.first_position - 1] == self.character
        second_match = self.password[self.second_position - 1] == self.character
        return first_match ^ second_match

print(sum(1 for line in INPUT if Password.parse(line).is_valid()))
