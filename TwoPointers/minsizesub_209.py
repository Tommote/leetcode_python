from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        N = len(nums)

        ret = N + 1

        sum_section = 0

        left, right = 0, 0

        while left<N :

            if right<N and sum_section+nums[right]<target:

                sum_section += nums[right]
                right += 1
            elif right == N:
                break
            elif sum_section+nums[right]>=target:

                ret = min(ret, right-left+1)
                sum_section -= nums[left]
                left += 1

        return 0 if ret>N else ret

s = Solution()
print(s.minSubArrayLen(target=4, nums=[1,1,1,1]))