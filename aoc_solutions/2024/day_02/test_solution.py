from aoc.base_tests import BaseTestChallenge, Empty

from . import Challenge


class TestChallenge(BaseTestChallenge):
    challenge_class = Challenge
    expected_results_from_test_data = (2, 4)
    expected_results_from_real_data = (585, 626)
