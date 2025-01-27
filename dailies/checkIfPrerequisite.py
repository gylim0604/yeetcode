class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        res = [False]*numCourses
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