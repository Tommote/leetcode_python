from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        mid = self._get_num_k( nums, 0, len(nums), len(nums)//2 )
        print(nums)
        if len(nums)%2==1:
            p1, p2 = len(nums)//2, len(nums)-1
        else:
            p1, p2 = len(nums)//2-1, len(nums)-1
        temp_nums = nums.copy()

        switch = True

        for i in range(len(nums)):

            if switch and p1>=0 :
                nums[i] = temp_nums[p1]
                p1 -= 1
                switch = not switch
            elif p2 >= 0 :
                nums[i] = temp_nums[p2]
                p2 -= 1
                switch = not switch
        print(nums)
    def _get_num_k(self, nums, l, r, k):

        if l==r:
            return nums[l]

        start, end = l, r

        base_num = nums[start]

        curr = start 
        


        while curr < end :
            print(curr, end, start)
            num = nums[curr]

            if num < base_num:
                self._swap(nums, curr, start)
                curr += 1
                start += 1
            elif num > base_num:
                self._swap(nums, curr, end-1)
                end -= 1
            else:
                curr += 1

        if start <= k and  end >= k :
            return nums[curr-1]
        elif curr < k :
            return self._get_num_k(nums, curr, r, k)
        else:
            return self._get_num_k(nums, l, curr-1, k)

    def _swap(self, nums, i, j):

        temp = nums[i] 
        nums[i] = nums[j]
        nums[j] = temp

s = Solution()
print(s.wiggleSort(
[1,4,3,4,1,2,1,3,1] ))