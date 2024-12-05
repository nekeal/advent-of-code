import sys
from collections import defaultdict
from pathlib import Path

from aoc.base import BaseChallenge
from aoc.input_providers import SingleFileInputProvider, SmartFileInputProvider


class Challenge(BaseChallenge):
    def part_1(self, input_lines: list[str]) -> int | str:
        raw_dependencies, raw_rules = "\n".join(input_lines).split("\n\n")
        dependencies: dict[str, set[str]] = defaultdict(set)
        rules: list[list[str]] = []
        for line in raw_dependencies.split("\n"):
            parts = line.split("|")
            dependencies[parts[1]].add(parts[0])
        for line in raw_rules.split("\n"):
            rules.append(line.split(","))
        result = 0
        for rule in rules:
            printed = set()
            for page in rule:
                if self.correctly_ordered(rule, dependencies[page], printed):
                    break
                printed.add(page)
            else:
                result += int(rule[len(rule) // 2])
        return result

    def part_2(self, input_lines: list[str]) -> int | str:
        raw_dependencies, raw_rules = "\n".join(input_lines).split("\n\n")
        dependencies: dict[str, list[str]] = defaultdict(list)
        rules: list[list[str]] = []
        for line in raw_dependencies.split("\n"):
            parts = line.split("|")
            dependencies[parts[1]].append(parts[0])
        for line in raw_rules.split("\n"):
            rules.append(line.split(","))
        result = 0
        for rule in rules:
            correct_middle = next(
                page
                for page in rule
                if len(set(dependencies[page]) & set(rule)) == len(rule) // 2
            )  # take page that has half of the dependencies present in the rule
            result += int(correct_middle)
        return result - self.part_1(input_lines)

    @staticmethod
    def correctly_ordered(
        rule: list[str], dependencies: set[str], printed: set[str]
    ) -> bool:
        for dependency in dependencies:
            if dependency in rule and dependency not in printed:
                return True
        return False


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
