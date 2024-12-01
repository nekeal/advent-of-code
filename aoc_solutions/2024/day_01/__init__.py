import sys
from collections import Counter
from pathlib import Path

from aoc.base import BaseChallenge
from aoc.input_providers import SingleFileInputProvider, SmartFileInputProvider


class Challenge(BaseChallenge):
    def parse_input(self, input_lines):
        left, right = [], []
        for line in input_lines:
            l, r = line.split("   ")
            left.append(int(l))
            right.append(int(r))
        return left, right

    def part_1(self, input_lines: list[str]) -> int | str:
        left, right = self.parse_input(input_lines)
        left.sort(), right.sort()
        return sum(abs(l - r) for l, r in zip(left, right, strict=True))

    def part_2(self, input_lines: list[str]) -> int | str:
        left, right = self.parse_input(input_lines)
        right_counter = Counter(right)
        return sum(l * right_counter[l] for l in left)


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
