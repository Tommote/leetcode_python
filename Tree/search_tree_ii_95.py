# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

        return self._recall( 1, n ) 

    
    def _recall( self, start_n, end_n  ):

        if start_n > end_n:
            return [None]

        if start_n==end_n :
            return [TreeNode(val=start_n)]
        
        ret = []

        for i in range(start_n, end_n+1):
            

            left_trees = self._recall( start_n, i-1 )
            right_trees = self._recall(i+1, end_n)

            for left_sub_tree in left_trees:
                for right_sub_tree in right_trees:

                    mid_node = TreeNode(i, left=left_sub_tree, right=right_sub_tree)
                    ret.append(mid_node)
        
        return ret 