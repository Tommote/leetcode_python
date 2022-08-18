from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        if root is None:
            return []

        self.ret = []
        self._recall( root, targetSum, root.val, [root.val] )

        return self.ret 

    def _recall(self, root, targetSum, currSum, path: list):

        if currSum > targetSum :
            return
        
        if root.left is None and root.right is None:

            if currSum==targetSum:
                self.ret.append( path.copy() )
                return
            else:
                return
        
        if root.left is not None:
            self._recall( root.left, targetSum, currSum+root.left.val, path.append(root.left.val) )
            path.pop(-1)
        if root.right is not None:
            self._recall( root.right, targetSum, currSum+root.right.val, path.append(root.right.val) )
            path.pop(-1)