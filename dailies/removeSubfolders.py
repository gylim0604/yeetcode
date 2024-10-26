from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        res = []
        folder.sort()
        print(folder)
        for el in folder:
            if not res:
                res.append(el)
                continue  
            if not self.checkPrefix(res[-1], el):
                res.append(el)
        return res
    def checkPrefix(self, prefix: str, curr: str) -> bool:
        i = 0
        while i < len(prefix):
            if prefix[i] != curr[i]:
                return False
            i+=1
        return curr[i] == '/'

sol = Solution()
print(sol.removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"]))

print(sol.checkPrefix("/a","/a/b"))