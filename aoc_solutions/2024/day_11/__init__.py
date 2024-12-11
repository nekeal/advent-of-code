import sys
from functools import cache
from pathlib import Path

from aoc.base import BaseChallenge
from aoc.input_providers import SingleFileInputProvider, SmartFileInputProvider


class Challenge(BaseChallenge):
    def part_1(self, input_lines: list[str]) -> int | str:
        stones = list(map(int, input_lines[0].split()))
        result = 0
        for stone in stones:
            result += self.count_stones(stone, 25)
        return result

    def part_2(self, input_lines: list[str]) -> int | str:
        stones = list(map(int, input_lines[0].split()))
        result = 0
        for stone in stones:
            result += self.count_stones(stone, 75)
        return result

    @classmethod
    @cache
    def count_stones(cls, stone: int, blinks_num: int) -> int:
        if blinks_num == 0:
            return 1
        if stone == 0:
            return cls.count_stones(1, blinks_num - 1)
        if len(str_stone := str(stone)) % 2 == 0:
            left, right = (
                int(str(stone)[: len(str_stone) // 2]),
                int(str(stone)[len(str_stone) // 2 :]),
            )
            return cls.count_stones(left, blinks_num - 1) + cls.count_stones(
                right, blinks_num - 1
            )
        return cls.count_stones(stone * 2024, blinks_num - 1)


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
