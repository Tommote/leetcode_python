from typing import List


class TreeNode:

    def __init__(self) -> None:
        
        self.left = None 
        self.right = None 

class DictTree:

    def __init__(self, max_bit=32) -> None:
        
        self.root = TreeNode()
        self.max_bit = max_bit
    
    def insert(self, x):

        curr = self.root 

        for i in range(self.max_bit-1, -1, -1):

            if x&(1<<i) == 0:
                if curr.left is None:
                    curr.left = TreeNode()
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = TreeNode()
                curr = curr.right
    def find_xor_max(self, x):

        curr = self.root 
        num = []
        for i in range(self.max_bit-1, -1, -1):
            x_bit = 0 if x&(1<<i) == 0 else 1 
            if x_bit==0 :
                if curr.right :
                    num.append('1')
                    curr = curr.right
                else:
                    num.append('0')
                    curr = curr.left
            else:
                if curr.left :
                    num.append('0')
                    curr = curr.left
                else:
                    num.append('1')
                    curr = curr.right 
        num_s = '0b'
        for i in num:
            num_s += i 
        ret = int(num_s,base=0)
        return  ret        
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:


        ret = 0
        t = DictTree(32)

        for num in nums:
            t.insert(num)
        
        for num in nums:

            ret = max( ret, num ^ t.find_xor_max(num) )

        
        return ret 

s = Solution()
print(s.findMaximumXOR([3,10,5,25,2,8]))
