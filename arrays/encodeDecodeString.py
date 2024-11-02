class Solution:

    def encode(self, strs: list[str]) -> str:
        res = ''
        for el in strs:
            res =res + str(len(el)) + '#' + el   
        return res
    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        while i < len(s):
            length = ''
            while s[i] != '#':
                length += s[i]
                i+=1
            length = int(length)
            i+=1
            curr = s[i:i + length]
            res.append(curr)
            i += length
            
        return res
    
sol = Solution()
e1 = sol.encode(["neet","code","love","you"])
print(e1)
print(sol.decode(e1))
e2 = sol.encode([""])
print(e2)
print(sol.decode(e2))
e3 = sol.encode([])
print(e3)
print(sol.decode(e3))