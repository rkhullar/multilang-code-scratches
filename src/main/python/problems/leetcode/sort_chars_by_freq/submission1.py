from collections import defaultdict
from collections.abc import Iterator


def iter_from_pairs(pairs: list[tuple[chr, int]]) -> Iterator[chr]:
    for char, count in pairs:
        for _ in range(count):
            yield char


class Solution:
    def frequencySort(self, s: str) -> str:
        counts = defaultdict(int)
        for char in s:
            counts[char] += 1
        count_pairs = list(counts.items())
        count_pairs.sort(key=lambda pair: pair[1], reverse=True)
        stream = iter_from_pairs(count_pairs)
        return ''.join(stream)
