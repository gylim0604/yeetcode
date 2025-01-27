from collections import defaultdict


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        adj = defaultdict(list)
        for prereq, crs in prerequisites:
            adj[crs].append(prereq)

        prereq_map = {}

        def dfs(crs):
            if crs not in prereq_map:
                prereq_map[crs] = set()
                for prereq in adj[crs]:
                    prereq_map[crs] |=dfs(prereq)
                prereq_map[crs].add(crs)
            return prereq_map[crs]
        
        for crs in range(numCourses):
            dfs(crs)
        res = []
        for u, v in queries:
            res.append(u in prereq_map[v])
        return res


    def floydWarshall(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        isReachable = [[False]* numCourses for _ in range(numCourses)]
        # reachability
        for u, v in prerequisites:
            print(u,v)
            isReachable[u][v] = True

        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    isReachable[i][j] = isReachable[i][j] or (isReachable[i][k] and isReachable[k][j])
        return [isReachable[u][v] for u,v in queries]
sol = Solution()
print(sol.checkIfPrerequisite(3,[[1,2],[1,0],[2,0]],[[1,0],[1,2]]))