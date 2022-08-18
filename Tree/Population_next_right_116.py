# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        left_most = root

        ret = []
        if root is None:
            return [] 

        while left_most :

            start_node = left_most

            while start_node:

                if start_node.left is not None and start_node.right is not None:
                    start_node.left.next = start_node.right 

                    if start_node.next is not None and start_node.next.left is not None :
                        start_node.right.next = start_node.next.left
                
                ret.append( start_node.val )
                start_node = start_node.next
            ret.append('#')


            left_most = left_most.left

        
        return ret 
    



