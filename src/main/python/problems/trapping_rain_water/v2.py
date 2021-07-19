from typing import List


def safe_max(data: list):
    if data:
        return max(data)


class Solution:
    @staticmethod
    def _trap_col(heights: List[int], idx: int) -> int:
        left = safe_max(heights[0:idx])
        right = safe_max(heights[idx:])
        bounds = min(left or 0, right or 0)
        result = bounds - heights[idx] if heights[idx] < bounds else 0
        return result

    def trap(self, height: List[int]) -> int:
        return sum(self._trap_col(heights=height, idx=i) for i in range(len(height)))
