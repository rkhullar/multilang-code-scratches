from unittest import TestCase

from nose.tools import assert_equal
from parameterized import parameterized
from problems.odd_even_jump.v1 import Solution


class SolutionTest(TestCase):
    @parameterized.expand([
        ([10, 13, 12, 14, 15], 2),
        # ([2, 3, 1, 1, 4], 3),
        # ([5, 1, 3, 4, 2], 3)
    ])
    def test_multi(self, arr: list[int], expected: int):
        actual = Solution().oddEvenJumps(arr)
        assert_equal(actual, expected)
