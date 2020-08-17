from nose.tools import assert_equals
from parameterized import parameterized
from typing import Iterator, List, Tuple
import unittest

IntRange = Tuple[int, int]


def compress_series(series: List[int]) -> List[IntRange]:
    return list(_compress_series(series))


def _compress_series(series: List[int]) -> Iterator[IntRange]:
    prev, left, right = None, None, None
    for item in series:
        if prev is None:
            left = item
        elif item - prev > 1:
            right = prev
            yield left, right
            left = item
        prev = item
    if prev is not None:
        yield left, item


class SeriesCompressionTest(unittest.TestCase):

    @parameterized.expand([
        ([1, 2, 3, 5, 6, 8, 10, 11, 12], [(1, 3), (5, 6), (8, 8), (10, 12)]),
        ([], []),
        ([1], [(1, 1)]),
        ([1, 2], [(1, 2)]),
        ([4, 9], [(4, 4), (9, 9)])
    ])
    def test_series_compression(self, series, expected):
        ranges = compress_series(series)
        assert_equals(ranges, expected)
