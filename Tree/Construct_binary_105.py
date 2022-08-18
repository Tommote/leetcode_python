from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        self.loc_inorder = {}

        for i in range(len(inorder)):

             self.loc_inorder[inorder[i]] = i 
            
        self.preorder = preorder
        self.inorder = inorder

        return self._recall( (0, len(preorder)-1), (0, len(inorder)-1) )


    def _recall( self, preorder_ind , inorder_ind  ):

        if preorder_ind[0] > preorder_ind[1] or inorder_ind[0]>inorder_ind[1]:
            return None

        if preorder_ind[0] == preorder_ind[1] :
            return TreeNode( val= self.preorder[ preorder_ind[0] ] )
        
        

        root_val = self.preorder[ preorder_ind[0] ]
        root  = TreeNode( val=root_val )

        root_inorder_ind = self.loc_inorder[root_val]

        left_sub_tree_len = root_inorder_ind - inorder_ind[0]
        # right_sub_tree_len = inorder_ind[1] - root_inorder_ind
        root.left = self._recall( ( preorder_ind[0]+1, preorder_ind[0]+left_sub_tree_len), (inorder_ind[0],root_inorder_ind-1)  )
        root.right = self._recall( ( preorder_ind[0]+left_sub_tree_len+1, preorder_ind[1]), (root_inorder_ind+1,inorder_ind[1])  )

        return root

s = Solution()

s.buildTree( [1,2], [2,1] )