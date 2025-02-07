class Solution:
    def queryResults(self, limit: int, queries: list[list[int]]) -> list[int]:
        n = len(queries)
        res = [] * n
        ball_map = {}
        color_map = {}
        for i in range(len(queries)):
            ball, color = queries[i]
            if ball in ball_map:
                prevColor = ball_map[ball]
                color_map[prevColor]-=1
                if color_map[prevColor] == 0:
                    del color_map[prevColor]
            ball_map[ball] = color
            color_map[color] = color_map.get(color, 0) + 1
            res.append(len(color_map))
        return res
sol = Solution()
print(sol.queryResults(4,[[1,4],[2,5],[1,3],[3,4]]))
# print(sol.queryResults(4,[[0,1],[1,2],[2,2],[3,4],[4,5]]))
# print(sol.queryResults(4,[[0,1],[1,2],[2,2],[3,4]]))