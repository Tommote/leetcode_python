from typing import List
from queue import Queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:

        ret_stack = []
        temp_queue = Queue()

        temp_queue.put( root )


        while  not temp_queue.empty():

            temp_len = temp_queue.qsize()
            temp_ret = []
            while temp_len:
                node = temp_queue.get()
                temp_ret.append(node.val)

                if node.left :
                    temp_queue.put( node.left )
                if node.right :
                    temp_queue.put( node.right )
                
                temp_len -= 1
            
            ret_stack.append( temp_ret )
        ret = []
        while len(ret_stack) > 0:
            ret.append( ret_stack.pop() )

        return ret 
