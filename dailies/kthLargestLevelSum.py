# Definition for a binary tree node.
from typing import Optional
import collections

from my_utils import TreeNode, to_binary_tree
    
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        if root is None: 
            return res
        queue = collections.deque()
        queue.append(root)
        while queue:
            currSize = len(queue)
            currList = []
            while currSize > 0:
                currNode = queue.popleft()
                currSize-=1
                currList.append(currNode.val)
                if currNode.left is not None:
                    queue.append(currNode.left)
                if currNode.right is not None:
                    queue.append(currNode.right)
            res.append(sum(currList))
        res.sort()
        return -1 if len(res) < k else res[-k] 


arr = [897935,796748,528909,None,None,None,905326,706311,None,None,282251,None,139169]
root = to_binary_tree(arr)
print(root.val, root.left.val)
sol = Solution()
print(sol.kthLargestLevelSum(root, 4))