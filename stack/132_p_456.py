from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:

        min_left = []
        N = len(nums)
        if N <3 :
            return False

        min_temp = nums[0]
        for i in range(N):

            min_left.append(min_temp)

            if nums[i]<min_temp:
                min_temp = nums[i]

        monotonic_stack = []   
        sec_min_right = [0]*N 

        max_k = -1e10
        for i in range(N-1, -1, -1):

            if i==N-1:
                monotonic_stack.append( 1e10)
                sec_min_right[i] = nums[i]
            
            if nums[i]<max_k:
                continue

            while len(monotonic_stack)>0 and monotonic_stack[-1]<nums[i]:
                
                x = monotonic_stack.pop()
                max_k = max(x, max_k)
            
            sec_min_right[i] = max_k
            monotonic_stack.append(nums[i])

        print(min_left)
        print(sec_min_right)

        for i in range(1,N-1):

            if  min_left[i]< nums[i] and min_left[i]<sec_min_right[i]:
                return True
        
        return False


s = Solution()
print(s.find132pattern([1,2,3,4]))