from typing import Iterator, List


def build_max_arr(data: List[int], reverse: bool = False) -> List[int]:
    return list(iter_max_arr(data=data, reverse=reverse))


def iter_max_arr(data: List[int], reverse: bool = False) -> Iterator[int]:
    curr = [0, len(data)-1][reverse]
    step = [1, -1][reverse]
    max_idx = curr
    while 0 <= curr < len(data):
        if data[curr] > data[max_idx]:
            max_idx = curr
        yield max_idx
        curr += step


def safe_get_item(data: list, idx: int):
    if idx is not None and 0 <= idx < len(data):
        return data[idx]


class Solution:

    def trap(self, height: List[int]) -> int:
        left_max_arr = build_max_arr(data=height, reverse=False)
        right_max_arr = build_max_arr(data=height, reverse=True)
        right_max_arr.reverse()

        left_max_arr = [None] + left_max_arr[:-1]
        right_max_arr = right_max_arr[1:] + [None]

        # print(left_max_arr)
        # print(right_max_arr)

        def partial(idx: int) -> int:
            left_idx, right_idx = left_max_arr[idx], right_max_arr[idx]
            left_val, right_val = safe_get_item(height, left_idx), safe_get_item(height, right_idx)
            bounds = min(left_val or 0, right_val or 0)
            result = bounds - height[idx] if height[idx] < bounds else 0
            return result

        return sum(partial(idx) for idx in range(len(height)))


if __name__ == '__main__':
    height: List[int] = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    result = Solution().trap(height)
    assert result == 6, result

    height: List[int] = [4, 2, 0, 3, 2, 5]
    result = Solution().trap(height)
    assert result == 9, result

    height: List[int] = []
    result = Solution().trap(height)
    assert result == 0, result
