from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        N = len(nums)

        dp_arr = [ [0] * (target+1) for _ in range( N ) ]
        dp_arr[0][0] = 1

        for i in range(1,len(nums)):
            num = nums[i]
            for j in range(0, target+1):

                if num+j <= target :
                    dp_arr[i][j] += dp_arr[i-1][j+num]

                if j-num >= 0 :
                    dp_arr[i][j] += dp_arr[i-1][j-num]
            
        
        return dp_arr[N-1][target]

s = Solution()
print(s.findTargetSumWays([1,1,1,1,1],3))