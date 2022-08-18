# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        nums = []
        self.inorder(root, nums)

        errors= []

        for i in range(1, len(nums)):

            if nums[i-1]>nums[i]:

                errors.append( (i-1,i) )
        
        exchange = {} # ind : val

        if len(errors)==1:

            exchange[ errors[0][0] ] = nums[ errors[0][1] ]
            exchange[ errors[0][1] ] = nums[ errors[0][0] ]
        elif len(errors)==2:
            exchange[ errors[0][0] ] = nums[ errors[1][1] ]
            exchange[ errors[1][1] ] = nums[ errors[0][0] ]

        else:
            raise ValueError('dd')
        
        self.i = 0

        self.recover_inorder(root, exchange)

    def inorder(self, root: Optional[TreeNode], nums: list):

        if root is None:
            return 

        self.inorder(root.left, nums)

        nums.append(root.val)

        self.inorder( root.right, nums )

        

    def recover_inorder( self, root,   exchange):

        if root is None:
            return
        
        self.recover_inorder(root.left, exchange)

        if self.i in exchange:
            root.val = exchange[self.i]
        
        self.i += 1
        
        self.recover_inorder(root.right, exchange)


s = Solution()
