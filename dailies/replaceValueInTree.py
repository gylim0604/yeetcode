from typing import List, Optional
import sys
import os

# Add the root directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from my_utils import TreeNode, to_binary_tree


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        levelSum = self.sumAll(root, 0, [])
        self.updateVal(root,None,0, levelSum)
        return root

    def sumAll(self, node: Optional[TreeNode], level:int, res: List[int]) -> List[int]:
        if node is None:
            return
        if level == len(res):
            res.append(0)

        res[level]+=node.val
        self.sumAll(node.left, level + 1,res)
        self.sumAll(node.right, level + 1,res)
        return res
    
    def updateVal(self, node: Optional[TreeNode], siblingSum: int, level:int, allSum: List[int]) -> None:
        if node is None:
            return
        
        left_child_val = 0 if node.left is None else node.left.val
        right_child_val = 0 if node.right is None else node.right.val
        if level == 0 or level == 1:
            node.val = 0
        else:
            node.val = allSum[level] - node.val - siblingSum
        self.updateVal(node.left, right_child_val, level + 1 , allSum)
        self.updateVal(node.right, left_child_val, level + 1 , allSum)


arr = [5,4,9,1,10,None,7]
root = to_binary_tree(arr)
sol = Solution()
print(sol.replaceValueInTree(root));