from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        self.inorder_loc = {}

        for i in range(len(inorder)):
            self.inorder_loc[ inorder[i] ] = i 
        
        self.inorder = inorder
        self.postorder = postorder 

        return self._recall( ( 0, len(inorder)-1 ), (0, len(postorder)-1) )

    def _recall(self, inorder_ind, postorder_ind):
        
        print(inorder_ind, postorder_ind)

        if inorder_ind[0]>inorder_ind[1]:
            return None
        
        if inorder_ind[0]==inorder_ind[1]:
            return TreeNode( val = self.inorder[ inorder_ind[0] ] )
        

        root_val = self.postorder[ postorder_ind[1] ]
        root_ind_inorder = self.inorder_loc[ root_val ]

        left_sub_tree_len = root_ind_inorder - inorder_ind[0]

        root = TreeNode(val=root_val)

        root.left = self._recall( ( inorder_ind[0], inorder_ind[0]+left_sub_tree_len-1 ), 
                                    ( postorder_ind[0], postorder_ind[0]+left_sub_tree_len-1 ) )
        root.right = self._recall( ( root_ind_inorder+1, inorder_ind[1] ), 
                                    ( postorder_ind[0]+left_sub_tree_len, postorder_ind[1]-1 ) )

        return root                                    

s = Solution()

s.buildTree([9,3,15,20,7],[9,15,7,20,3])