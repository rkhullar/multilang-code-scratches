from typing import Iterator, List


def build_max_arr(data: List[int], reverse: bool = False) -> List[int]:
    return list(iter_max_arr(data=data, reverse=reverse))


def iter_max_arr(data: List[int], reverse: bool = False) -> Iterator[int]:
    if not data:
        pass
    curr = [0, len(data)-1][reverse]
    step = [1, -1][reverse]
    max_idx = curr
    while 0 <= curr < len(data):
        if data[curr] > data[max_idx]:
            max_idx = curr
        yield max_idx
        curr += step


class Solution:

    def trap(self, height: List[int]) -> int:
        pass


if __name__ == '__main__':
    # height: List[int] = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    # result = Solution().trap(height)
    # assert result == 6, result
    #
    height: List[int] = [1,2,3,4,5,4,3,2,0]
    max_left_arr = build_max_arr(height)
    max_right_arr = build_max_arr(height, reverse=True)
    print([height[i] for i in max_left_arr])
    print([height[i] for i in max_right_arr])
    # for i in range(len(height)):
    #     print(f'{i=} left={height[:i]} right={height[i:]} max_left={max_left_arr[i]} max_right={max_right_arr[i]}')

    # result = Solution().trap(height)
    # assert result == 6, result

