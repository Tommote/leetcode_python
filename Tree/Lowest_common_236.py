
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        self.p = p 
        self.q = q

        self.ret = None 

        self._dfs(root)

        return self.ret 
    def _dfs(self, root) -> bool:

        if root is None or self.ret is not None:
            return False
        

        r1 = self._dfs(root.left)
        r2 = self._dfs(root.right)

        if root is self.p or root is self.q :

            if r1 or r2 :
                self.ret = root
                return False 
            else:
                return  True
        else:

            if r1 and r2 :
                self.ret = root
                return False 
            else:
                return r1 or r2 




