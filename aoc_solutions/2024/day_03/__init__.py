import bisect
import itertools
import re
import sys
from pathlib import Path

from aoc.base import BaseChallenge
from aoc.input_providers import SingleFileInputProvider, SmartFileInputProvider

mul_regex = re.compile("mul\((\d+),(\d+)\)")
do_regex = re.compile(r"(do(n't)?)\(\)")

class Challenge(BaseChallenge):
    def part_1(self, input_lines: list[str]) -> int | str:
        mul_instructions = list(itertools.chain(*(re.finditer(mul_regex, line) for line in input_lines)))
        result = 0
        for match in mul_instructions:
            a,b = int(match.group(1)), int(match.group(2))
            assert a < 1000 and b < 1000
            result += a * b
        return result

    def is_enabled(self, do_instructions: list[re.Match], position: tuple[int, int]) -> bool:
        match = bisect.bisect_left(do_instructions, position[0], key=lambda x: x.span()[0])
        leftmost_instruction = do_instructions[match-1] if match > 0 else None
        enabled = True if leftmost_instruction is None or leftmost_instruction.group(1) == "do" else False
        return enabled

    def part_2(self, input_lines: list[str]) -> int | str:
        all_instructions = "".join(input_lines)
        mul_instructions = re.finditer(mul_regex, all_instructions)
        do_instructions = list(re.finditer(do_regex, all_instructions))
        result = 0
        for match in mul_instructions:
            a,b = int(match.group(1)), int(match.group(2))
            assert a < 1000 and b < 1000
            if self.is_enabled(do_instructions, position=match.span()):
                result += a * b
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
