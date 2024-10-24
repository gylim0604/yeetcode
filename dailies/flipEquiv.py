from typing import List, Optional
import sys
import os

# Add the root directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from my_utils import TreeNode, to_binary_tree


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.dfs(root1, root2)
        
    def dfs(self, node1: Optional[TreeNode], node2:Optional[TreeNode]) -> bool:
        if node1 is None and node2 is None:
            return True
        if node1 is None and node2 is not None or node1 is not None and node2 is None:
            return False
        if node1.val != node2.val:
            return False
        # display the values, purely for visuals
        child1 = [0 if node1.left is None else node1.left.val, 0 if node1.right is None else node1.right.val ]
        child2 = [0 if node2.left is None else node2.left.val,0 if node2.right is None else node2.right.val]
        res = sorted(child1) == sorted(child2)
        print(node1.val,child1,node2.val, child2,res)
        # Case 1: No flip (compare left-left, right-right)
        noFlip = self.dfs(node1.left, node2.left) and self.dfs(node1.right, node2.right)
        # Case 2: Flip (compare left-right, right-left)
        flip = self.dfs(node1.left, node2.right) and self.dfs(node1.right, node2.left)
        return noFlip or flip
sol = Solution()
print(sol.flipEquiv(to_binary_tree([1,2,3,4,5,6,None,None,None,7,8]),to_binary_tree([1,3,2,None,6,4,5,None,None,None,None,8,7])))