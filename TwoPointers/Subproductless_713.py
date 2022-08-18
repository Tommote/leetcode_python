from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        ret = 0

        N = len(nums)

        mul_section = 1

        left, right, last_right = 0, 0, 0

        while left<N:

            if right<N and mul_section*nums[right]<k :
                mul_section = mul_section*nums[right]
                ret = ret + right-left+1 
                right += 1
            elif left==right:
                left += 1
                right += 1
            else:
                mul_section = mul_section/nums[left]
                left += 1
        return ret 

s = Solution()
print(s.numSubarrayProductLessThanK([10, 5, 200, 6], 100))




