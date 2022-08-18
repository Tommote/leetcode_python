from typing import List


class Solution:

    def search_binary(self, nums:List[int], target:int)->int:

        left, right = 0, len(nums)-1 

        while left <= right :

            mid = (left+right)//2 

            if nums[mid] == target:
                return mid 
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def lengthOfLIS(self, nums: List[int]) -> int:

        stack = []

        for i in range(len(nums)):

            # print(i, stack)
            temp = nums[i]

            if len(stack)==0 or stack[-1] < temp:
                stack.append(nums[i])
                continue 

            ind = self.search_binary(stack, temp)
            print(stack, ind, temp)
            if stack[ind]==temp:
                continue
            elif stack[ind] > temp:
                stack[ind] = nums[i] 
        # print(stack)
        return len(stack)

s = Solution()
print(s.lengthOfLIS([3,5,6,2,5,4,19,5,6,7,12]))

# print( s.search_binary([2, 5, 6], 4) )