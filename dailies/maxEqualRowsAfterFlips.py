class Solution:
    def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:
        
        max_identical_rows = 0
        for current_row in matrix:
            flippedRow = [1 - x for x in current_row]
            identical_row_count = sum(
                1
                for compare_row in matrix
                if compare_row == current_row or compare_row == flippedRow
            )
            max_identical_rows = max(max_identical_rows, identical_row_count)
        return max_identical_rows
sol = Solution()
print(sol.maxEqualRowsAfterFlips([[0,0,0],[0,0,1],[1,1,0]]))