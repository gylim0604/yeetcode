class Solution:
    def canChange(self, start: str, target: str) -> bool:
        start_length = len(start)
        i,j = 0,0
        while i < start_length or j < start_length:
            while i < start_length and start[i] == '_':
                i+=1
            while j < start_length and target[j] == '_':
                j+=1
            print(start[i], target[j])
            if i == start_length or j == start_length:
                return i == start_length and j == start_length
            if start[i] != target[j] or (start[i] == 'L' and i < j) or (start[i] == 'R' and i > j):
                return False
            i+=1
            j+=1
        return True
sol = Solution()
print(sol.canChange("_L","LR"))