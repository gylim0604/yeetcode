class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        n = len(graph)
        safe_map = {}

        def dfs(i)->bool:
            if i in safe_map:
                return safe_map[i]
            safe_map[i] = False
            for nei in graph[i]:
                if not dfs(nei):
                    return safe_map[i]
            safe_map[i] = True
            return safe_map[i]

        res = []
        for i in range(n):
            if dfs(i):
                res.append(i)
        return res
sol = Solution()
print(sol.eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]))