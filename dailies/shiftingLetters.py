class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        n = len(s)
        diff_arr = [0] * (n + 1)

        for left, right, d in shifts:
            diff_arr[right+1] += 1 if d else -1
            diff_arr[left] += -1 if d else 1
        diff = 0
        res = [ord(c) - ord('a') for c in s]
        for i in reversed(range(len(diff_arr))):
            diff += diff_arr[i]
            res[i - 1] = (diff+ res[i-1]+26)%26
        s = [chr(ord("a")+ n) for n in res]
        return "".join(s)
sol = Solution()
print(sol.shiftingLetters("abc",[[0,1,0],[1,2,1],[0,2,1]]))
print(sol.shiftingLetters("dztz",[[0,0,0],[1,1,1]]))