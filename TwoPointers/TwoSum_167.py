from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        N = len(numbers)

        left, right = 0, N-1

        while left < right:

            if numbers[left] + numbers[right] == target:

                return [left+1, right+1]
            
            elif numbers[left] + numbers[right] < target:

                left += 1
            
            else:
                right -= 1
        

s = Solution()
print(s.twoSum([-1, 0], -1))