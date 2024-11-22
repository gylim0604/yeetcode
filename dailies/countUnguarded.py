class Solution:
    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m)]
        for guard in guards:
            grid[guard[0]][guard[1]] = 'g'

        for wall in walls:
            grid[wall[0]][wall[1]] = 'w'
        
        for guard in guards:
            row = guard[0]
            col = guard[1]
            for curr in range(row -1, -1, -1):
                if grid[curr][col]== 'w' or grid[curr][col]== 'g':
                    break
                grid[curr][col] = 'x'
            for curr in range(row + 1, m):
                if grid[curr][col]== 'w' or grid[curr][col]== 'g':
                    break
                grid[curr][col] = 'x'
            for curr in range(col -1, -1, -1):
                if grid[row][curr]== 'w' or grid[row][curr]== 'g':
                    break
                grid[row][curr] = 'x'
            for curr in range(col  + 1, n):
                if grid[row][curr]== 'w' or grid[row][curr]== 'g':
                    break
                grid[row][curr] = 'x'
                
        count = sum(row.count(0) for row in grid)
        return count

sol = Solution()
print(sol.countUnguarded(3,4,[[0,1],[1,2],[2,0],[2,1]],[[1,3],[0,3],[1,0],[2,2],[0,2]]))
print(sol.countUnguarded(4,6,[[0,0],[1,1],[2,3]],[[0,1],[2,2],[1,4]]))
print(sol.countUnguarded(3,3,[[1,1]],[[0,1],[1,0],[2,1],[1,2]]))
print(sol.countUnguarded(3,3,[[1,1]],[]))