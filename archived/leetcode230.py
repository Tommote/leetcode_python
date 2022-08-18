# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        arr = []

        self.trace(root,arr)

        print(arr)


    def trace(self, root, arr):

        if root is None:
            return
        
        self.trace(root.left)

        arr.append( root.val )

        self.trace(root.right)

