from functools import reduce


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:

        self.ret = 0
        self.targetSum = 0

        self._dfs(root, [])

        return self.ret

    def _dfs(self, root, sum_list):
        
        for num in sum_list:
            if num == self.targetSum:
                self.ret += 1
        
        if root is None:
            return

        new_sum_list = [ root.val+num  for num in sum_list]
        new_sum_list.append(root.val)

        self._dfs( root.left, new_sum_list)
        self._dfs( root.right, new_sum_list)
