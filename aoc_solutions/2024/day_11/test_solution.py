import pytest
from aoc.base_tests import BaseTestChallenge

from . import Challenge


class TestChallenge(BaseTestChallenge):
    challenge_class = Challenge
    expected_results_from_test_data = (55312, 65601038650482)
    expected_results_from_real_data = (203609, 240954878211138)

    @pytest.mark.parametrize(
        "stone,expected_result",
        (
            (0, [1]),
            (10, [1, 0]),
            (1, [2024]),
        ),
    )
    def test_expand_stone(self, stone, expected_result):
        assert Challenge.count_stones(stone, 1) == len(expected_result)

    @pytest.mark.parametrize(
        "stones,expected_result",
        (
            (0, [2024]),
            (10, [2024, 1]),
            (1, [20, 24]),
        ),
    )
    def test_expand_2_blinks(self, stones, expected_result):
        assert Challenge.count_stones(stones, 2) == len(expected_result)
