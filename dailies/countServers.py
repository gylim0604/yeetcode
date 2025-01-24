class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        res = 0
        row_count = [0]*len(grid)
        col_count = [0]*len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    row_count[i]+=1
                    col_count[j]+=1
        # Traverse and check for col or row
        for i in range(len(grid)):
            for j in range(len(grid[i])):   
                if grid[i][j]==1 and (row_count[i] > 1 or col_count[j] > 1):
                    res+=1
        return res


sol = Solution()
print(sol.countServers([[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]))