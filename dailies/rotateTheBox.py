class Solution:
    def rotateTheBox(self, box: list[list[str]]) -> list[list[str]]:
        rows, cols = len(box), len(box[0])
        res = [['.']* rows for _ in range(cols)]
        for i in range(rows):
            spaceIndex = cols - 1
            for j in range(cols -1 ,-1  ,-1):
                if box[i][j] == '#':
                    res[spaceIndex][rows - 1 -i] = '#' 
                    spaceIndex -= 1
                elif box[i][j] == '*':
                    res[j][rows - 1 - i] = '*'
                    spaceIndex = j - 1
        return res

sol = Solution()
print(sol.rotateTheBox([["#",".","#"]]))
print(sol.rotateTheBox([["#",".","*","."],["#","#","*","."]]))
print(sol.rotateTheBox([["#","#","*",".","*","."],["#","#","#","*",".","."],["#","#","#",".","#","."]]))