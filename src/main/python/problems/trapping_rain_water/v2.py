from typing import List


class Solution:
    def _trap_col(self, heights: List[int], idx: int) -> int:
        left, right = None, None
        cursor = idx - 1
        while not left and cursor >= 0:
            left = heights[cursor]
            cursor -= 1
        cursor = idx + 1
        while not right and cursor < len(heights):
            right = heights[cursor]
            cursor += 1
        bounds = min(left or 0, right or 0)
        return bounds if heights[idx] <= bounds else 0

    def trap(self, height: List[int]) -> int:
        return sum(self._trap_col(heights=height, idx=i) for i in range(len(height)))


if __name__ == '__main__':
    height: List[int] = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    result = Solution().trap(height)
    assert result == 6, result
