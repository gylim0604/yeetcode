class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict1 = [0]*26
        dict2 = [0]*26
        for i in range(len(s)):
            dict1[ord(s[i])- ord('a')] +=1
            dict2[ord(t[i])- ord('a')] +=1
        return dict1 == dict2
        
s,t = "racecar", "carrace"
sol = Solution()
print(sol.isAnagram(s,t))