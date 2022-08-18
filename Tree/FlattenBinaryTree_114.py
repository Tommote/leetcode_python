class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        self._recur( root ) 

    def _recur(self, root):

        if root.left is None and root.right is None:

            return ( root, root )
        
        elif root.left is None:

            return (root, self._recur( root.right )[1])

        else:

            left_start, left_end = self._recur(root.left)

            right_start, right_end = self._recur(root.right)

            left_end.right = right_start
            root.right = left_start

            return ( root, right_end ) 