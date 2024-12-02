import sys
from pathlib import Path

from aoc.base import BaseChallenge
from aoc.input_providers import SingleFileInputProvider, SmartFileInputProvider


class Challenge(BaseChallenge):
    @staticmethod
    def parse_line(line: str) -> list[int]:
        return list(map(int, line.split()))

    @staticmethod
    def have_same_sign(a: int, b: int) -> bool:
        return a * b >= 0

    def is_safe(self, numbers: list[int]) -> bool:
        if 1 > abs(base_diff := numbers[0] - numbers[1]) or base_diff > 3:
            return False
        for i in range(0, len(numbers) - 1):
            diff = numbers[i] - numbers[i + 1]
            if abs(diff) not in {1, 2, 3} or not self.have_same_sign(base_diff, diff):
                return False
        return True

    def is_safe_part2(self, numbers: list[int]) -> bool:
        for i in range(len(numbers)):
            if self.is_safe(numbers[:i] + numbers[i + 1 :]):
                return True
        return False

    def part_1(self, input_lines: list[str]) -> int | str:
        result = 0
        for line in input_lines:
            numbers = self.parse_line(line)
            result += self.is_safe(numbers)
        return result

    def part_2(self, input_lines: list[str]) -> int | str:
        result = 0
        for line in input_lines:
            numbers = self.parse_line(line)
            result += self.is_safe_part2(numbers)
        return result


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_provider = SingleFileInputProvider(
            Challenge.year, Challenge.day, input_path=Path(sys.argv[1])
        )
        Challenge(input_provider).run()
    else:
        Challenge(
            SmartFileInputProvider(Challenge.year, Challenge.day, use_test_data=True)
        ).run()
        Challenge(SmartFileInputProvider(Challenge.year, Challenge.day)).run()
