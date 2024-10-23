from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for el in strs:
            arr = [0]*26
            for i in range(0, len(el)):
                arr[ord(el[i])-97]+=1
            key= "#".join(str(val) for val in arr)
            if key in res:
                res[key].append(el)
            else:
                res[key] = [el]
        return list(res.values())

sol = Solution()
# print(sol.groupAnagrams(["act","pots","tops","cat","stop","hat"]))  

print(sol.groupAnagrams(["bdddddddddd","bbbbbbbbbbc"]))  