


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.

        
        """


        N = len(nums)

        lt , gt , i = 0, N-1, 0

        while i <= gt :

            if nums[i] < 1 :

                self.swap(nums, i, lt)
                lt += 1
                i += 1
            elif nums[i] > 1:

                self.swap(nums, i, gt)
                gt -= 1
            else:
                i += 1

        return nums 


    def swap(self, nums, i , j):

        temp = nums[i]

        nums[i] = nums[j]
        nums[j] = temp 


s = Solution()

print(s.sortColors([1,0]))

