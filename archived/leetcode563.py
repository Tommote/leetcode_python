# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution(object):
    
    def __init__(self):
        self.ret = 0
    
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ret = 0
        self.dfs(root)

        return self.ret 

    def dfs(self, root):

        if root is None:
            return 0
        
        left_sum = self.dfs(root.left)
        right_sum = self.dfs(root.right)

        self.ret = self.ret + abs(left_sum-right_sum)

        return left_sum + right_sum + root.val

