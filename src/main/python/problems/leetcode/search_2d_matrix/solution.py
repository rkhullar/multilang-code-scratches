# https://leetcode.com/problems/search-a-2d-matrix

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        N = rows * cols

        def get_idx(x: int) -> tuple[int, int]:
            '''
            0 -> 0, 0
            1 -> 0, 1
            2 -> 0, 2
            3 -> 0, 3
            4 -> 1, 0
            7 -> 1, 3
            8 -> 2, 0
            '''
            return x // cols, x % cols

        def get_val(x: int) -> int:
            i, j = get_idx(x)
            return matrix[i][j]

        for x in range(N):
            print(x, get_val(x))
