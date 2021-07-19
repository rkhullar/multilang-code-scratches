from typing import List

from data.table import Table


def fill_black(matrix: Table[int], heights: List[int]):
    for col_idx, height in enumerate(heights):
        for row_idx in range(height):
            matrix[row_idx][col_idx] = 1


def fill_blue(matrix: Table[int]) -> int:
    count: int = 0
    for row_idx, col_idx, value in matrix.traverse():
        if should_fill_blue(matrix, row_idx, col_idx):
            matrix[row_idx][col_idx] = 2
            count += 1
    return count


def should_fill_blue(matrix: Table[int], row_idx: int, col_idx: int) -> bool:
    # ensure block is empty
    if matrix[row_idx][col_idx] != 0:
        return False
    has_left, has_right, has_top = False, False, False
    # search left
    cursor = col_idx
    while not has_left and cursor >= 0:
        has_left |= matrix[row_idx][cursor]
        cursor -= 1
    # search right
    cursor = col_idx
    while not has_right and cursor < matrix.width:
        has_right |= matrix[row_idx][cursor]
        cursor += 1
    # search top
    cursor = row_idx
    while not has_top and cursor < matrix.height:
        has_top |= matrix[cursor][col_idx]
        cursor += 1
    return has_left and has_right and not has_top


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        matrix: Table[int] = Table(width=len(height), height=max(height), default=0)
        fill_black(matrix, heights=height)
        blue_count = fill_blue(matrix)
        # print(matrix)
        return blue_count
