import sys
from pathlib import Path

from aoc.base import BaseChallenge
from aoc.input_providers import SingleFileInputProvider, SmartFileInputProvider


class Challenge(BaseChallenge):
    def part_1(self, input_lines: list[str]) -> int | str:
        return

    def part_2(self, input_lines: list[str]) -> int | str:
        result = 0
        for i in range(1, len(input_lines)):
            for j in range(1, len(input_lines[i])):
                result += self.check_match(input_lines, i, j)
        return result

    @staticmethod
    def check_match(input_lines: list[str], i: int, j: int):
        if input_lines[i][j] != "A":
            return 0
        try:
            left_top_right_bottom = {
                input_lines[i - 1][j - 1],
                input_lines[i + 1][j + 1],
            }
            left_bottom_right_top = {
                input_lines[i + 1][j - 1],
                input_lines[i - 1][j + 1],
            }
            if left_top_right_bottom == left_bottom_right_top == {"M", "S"}:
                return 1
        except IndexError:
            return 0
        return 0


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
