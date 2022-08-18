from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        if root is None:
            return []

        ret = []
        node_queue = []

        h = 1
        node_queue.append(root)

        while len(node_queue) > 0 :

            temp_l = len(node_queue)
            temp_ret = []

            if h%2 == 1 :

                for i in range(0, temp_l):
                    temp_node = node_queue[i]
                    temp_ret.append(temp_node.val)
            else:
                for i in range(temp_l-1, -1, -1):
                    temp_node = node_queue[i]
                    temp_ret.append(temp_node.val)

            while temp_l > 0 :

                temp_node = node_queue.pop(0)
                if temp_node.left is not  None:
                    node_queue.append(temp_node.left)
                if temp_node.right is not None :
                    node_queue.append(temp_node.right)

                
                temp_l -= 1

            h += 1
            ret.append(temp_ret)

        return ret 
