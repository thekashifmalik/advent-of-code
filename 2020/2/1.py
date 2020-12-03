from dataclasses import dataclass


with open('input') as f:
    INPUT = f.read().splitlines()


@dataclass
class Password:
    """
    Represents the following line:

        '1-3 a: abcde'
    """
    lower_bound: int
    upper_bound: int
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
        count = self.password.count(self.character)
        if self.lower_bound <= count <= self.upper_bound:
            return True
        return False

print(sum(1 for line in INPUT if Password.parse(line).is_valid()))
