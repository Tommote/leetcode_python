from typing import List



class Solution:

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def _get_minMax(self, nums, s_ind, target):
        ret_ind = -1
        for i in range(s_ind, len(nums)):

            if nums[i]>target:
                if ret_ind==-1 or nums[i]<nums[ret_ind]:
                    ret_ind = i 
        return ret_ind


    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums)==1:
            return 
        if len(nums)==2:
            self.swap(nums, 0, 1)
            return
        
        N = len(nums)

        for i in range(N-2, -1, -1):

            j = self._get_minMax(nums, i+1, nums[i])
            # print(i,j)
            if j==-1 :
                if i!=0:
                    continue
                else:
                    nums[:] = sorted(nums[:])
                    break
            else:
                self.swap(nums, i, j)
                nums[i+1:] = sorted(nums[i+1:])
                break
s = Solution()
nums = [3,2,1]
s.nextPermutation(nums)
print(nums)