from collections import defaultdict
from collections.abc import Iterator


class Solution:
    def frequencySort(self, s: str) -> str:
        char_to_count: dict[chr, int] = defaultdict(int)
        for char in s:
            char_to_count[char] += 1
        # print(char_to_count)

        count_to_char: dict[int, set[chr]] = defaultdict(set)
        for char, count in char_to_count.items():
            count_to_char[count].add(char)
        # print(count_to_char)

        counts = sorted(count_to_char.keys(), reverse=True)

        def iter_chars() -> Iterator[chr]:
            for count in counts:
                for char in count_to_char[count]:
                    for _ in range(count):
                        yield char

        stream = iter_chars()
        return ''.join(stream)
