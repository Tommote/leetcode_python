from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


        left_p , right_p = 0, len(nums)-1

        curr = 0 

        while curr<=right_p :
            print(nums , curr)
            x = nums[curr]

            if x < 1:
                self._swap(nums, left_p, curr)
                left_p += 1
                curr += 1
            elif x > 1:
                self._swap(nums, right_p, curr)
                right_p -= 1
                # curr += 1
            else:
                curr += 1 
    

    def _swap(self, arr, x, y):

        temp = arr[x]
        arr[x] = arr[y]
        arr[y] = temp

s = Solution()
nums = [2,0,1,2,2,1,1,0,0,1,2]
s.sortColors(nums)

print(nums)