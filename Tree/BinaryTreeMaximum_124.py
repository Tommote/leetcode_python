# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.max_ret = -float('inf')  

        self._recur(root)
        return self.max_ret
    def _recur(self, root):

        if root is None:
            return 0
        
        left_max, right_max = self._recur(root.left), self._recur(root.right)

        ret = root.val
        ret = max( ret, ret+left_max )
        ret = max(ret, ret+right_max)

        self.max_ret = max( self.max_ret, ret )

        return ret 



a = float('inf')

print(a>100)