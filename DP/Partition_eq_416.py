from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        N = len(nums)

        if N < 2 :
            return False
        
        temp = 0
        for i in range(N):
            temp += nums[i] 
        
        if temp % 2 == 1:
            return False 
        
        target = temp//2

        dp = [ [False]*(target) for _ in range(N) ]

        for i in range( N ) :
            for j in range(target):

                pass 
