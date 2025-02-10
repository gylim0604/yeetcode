class Solution:
    def clearDigits(self, s: str) -> str:
        char_stack = []
        for _,val in enumerate(s):
            if val.isnumeric():
                char_stack.pop()
            else:
                char_stack.append(val)
        return "".join(char_stack)
sol = Solution()
print(sol.clearDigits("acb34"))