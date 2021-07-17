from typing import List


def safe_max(data: list):
    if data:
        return max(data)


class Solution:
    def _trap_col_2(self, heights: List[int], idx: int) -> int:
        left = safe_max(heights[0:idx])
        right = safe_max(heights[idx:])
        bounds = min(left or 0, right or 0)
        result = bounds - heights[idx] if heights[idx] < bounds else 0
        return result

    def trap(self, height: List[int]) -> int:
        return sum(self._trap_col_2(heights=height, idx=i) for i in range(len(height)))


if __name__ == '__main__':
    height: List[int] = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    result = Solution().trap(height)
    assert result == 6, result
