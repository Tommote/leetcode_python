from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        N = len(nums)

        NUM = 2**N
        nums = sorted(nums) 
        ret = []

        repeat = False

        for i in range(NUM):
            temp = []
            for j in range(N):
                if (i>>j)&1 == 1 :
                    if j!=0 and nums[j-1]==nums[j] and (i>>(j-1))&1==0:
                        # print(bin(i),j)
                        i = i & ( 2**(N+1)-1-2**j )
                        # print(bin(i))
                        repeat = True
                        break
                    temp.append(nums[j])
                repeat = False
            if not repeat:
                ret.append(temp)
        
        return ret 

s = Solution()
print(s.subsetsWithDup([1,2,2,2,2]))
