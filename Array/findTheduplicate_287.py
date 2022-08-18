from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        p_slow, p_fast = 0, 0

        while True:

            p_slow = nums[p_slow]
            p_fast = nums[nums[p_fast]]

            if p_fast == p_slow :
                break
        
        p_slow = 0

        while p_slow != p_fast:
            p_slow = nums[p_slow]
            p_fast = nums[p_fast]
        
        return p_slow


s = Solution()
print( s.findDuplicate([1,1,2]) )