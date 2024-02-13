class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        # edge case
        if n == 1:
            return matrix[0][0]

        # new matrix to fill bottom up with min sum values
        _build_row = lambda: [0 for _ in range(n)]
        table = [_build_row() for _ in range(n)]

        # fill bottom row
        row_idx = n-1
        for col_idx in range(n):
            table[row_idx][col_idx] = matrix[row_idx][col_idx]
        
        def get_val(matrix: list[list[int]], row_idx: int, col_idx: int) -> int | None:
            if (0 <= row_idx < n) and (0 <= col_idx < n):
                return matrix[row_idx][col_idx]

        # fill upward rows
        _col_offsets = [-1, 0, 1]
        for row_idx in range(n-2, -1, -1):
            for col_idx in range(n):
                curr = get_val(matrix, row_idx, col_idx)
                #print(row_idx, col_idx, curr)
                below_arr = [get_val(table, row_idx+1, col_idx+dx) for dx in _col_offsets]
                #print(below_arr)
                below_arr = [val for val in below_arr if val is not None]
                min_sum = curr + min(below_arr)
                table[row_idx][col_idx] = min_sum
        
        # for row in table:
            # print(row)

        return min(table[0])