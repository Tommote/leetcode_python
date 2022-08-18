
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """

        return self.dfs(root, 0)

    def dfs(self, root, depth):

        if root is None:
            return depth
        
        ret = 0

        for node in root.children:

            ret = max( self.dfs(node, depth), ret )
        
        return depth + ret + 1