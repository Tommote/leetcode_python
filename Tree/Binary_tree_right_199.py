# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:

        if root is None:
            return []

        
        ret = []
        node_queue = collections.deque()
        node_queue.append(root)

        while len(node_queue)>0:

            layer_len = len(node_queue)

            while layer_len>0 :

                temp_node = node_queue.pop()
                if temp_node.left:
                    node_queue.append(temp_node.left)
                if temp_node.right:
                    node_queue.append(temp_node.right)
                
                layer_len -= 1
            
            ret.append(temp_node.val)
        
        return ret 


