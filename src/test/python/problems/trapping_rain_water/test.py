from typing import List
from unittest import TestCase

from nose.tools import assert_equal
from parameterized import parameterized
from problems.trapping_rain_water.v3 import Solution


class SolutionTest(TestCase):
    @parameterized.expand([
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
        ([], 0)
    ])
    def test_multi(self, heights: List[int], water: int):
        actual = Solution().trap(height=heights)
        assert_equal(actual, water)
