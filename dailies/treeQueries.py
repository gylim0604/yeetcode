from typing import List, Optional
import sys
import os

# Add the root directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from my_utils import TreeNode, to_binary_tree

class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        res = []
        maxVal = self.getMaxNodeVal(root)
        heights = [-1] *( maxVal )
        removed = [0] *( maxVal )
        self.calcHeight(root, heights)
        self.calcRemove(root,  0,heights, removed)
        print(heights,removed)
        for query in queries:
            res.append(removed[query])
        return res
    
    def getMaxNodeVal(self, node: Optional[TreeNode])-> int:
        if node is None: 
            return 0
        leftVal = self.getMaxNodeVal(node.left)
        rightVal = self.getMaxNodeVal(node.right)
        return max(node.val, leftVal, rightVal)
    
    def calcHeight(self, node: Optional[TreeNode], heights: tuple[int,int])-> int:
        if node is None:
            return -1
        leftHeight = self.calcHeight(node.left, heights) + 1
        rightHeight = self.calcHeight(node.right, heights) + 1
        maxHeight = max(leftHeight, rightHeight)
        heights[node.val - 1] = (leftHeight, rightHeight)
        return maxHeight
    
    def calcRemove(self, node: Optional[TreeNode],parentHeight: int,  heights: tuple[int,int], result: List[int]) -> int:
        if node is None: 
            return 0
        leftHeight, rightHeight = heights[node.val - 1]
        if node.left: 
            result[node.left.val -1] = max(parentHeight , rightHeight)
            self.calcRemove(node.left,result[node.left.val-1], heights, result)
        if node.right:
            result[node.right.val -1] = max(parentHeight , leftHeight)
            self.calcRemove(node.right,result[node.right.val-1], heights, result)
        
    
    
sol = Solution()
# print(sol.treeQueries(to_binary_tree([1,3,4,2,None,6,5,None,None,None,None,None,7]), [4]))   
print(sol.treeQueries(to_binary_tree([5,8,9,2,1,3,7,4,6]), [3,2,4,8]))        