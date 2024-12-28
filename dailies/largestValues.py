# Definition for a binary tree node.
from typing import List, Optional
import sys
import os

# Add the root directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from my_utils import TreeNode, to_binary_tree

from typing import Optional


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            size = len(queue)
            maxVal = float('-inf')
            for _ in range(size):
                curr = queue.pop(0)
                maxVal = max(curr.val, maxVal)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(maxVal)
        return res
    
root = to_binary_tree([1,3,2,5,3,None,9])
sol = Solution()
print(sol.largestValues(root))