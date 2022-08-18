from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:

        nums = sorted(nums)

        ret = 0

        for i in range(0, len(nums)//2):
            print(nums[i], nums[len(nums)-1-i])
            ret = max(ret, nums[i]+nums[len(nums)-1-i])
    
        return ret 

s = Solution()
print(s.minPairSum([4,1,5,1,2,5,1,5,5,4]))