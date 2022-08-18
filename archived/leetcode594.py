from typing import Counter


class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        hashmap = Counter(nums)

        # for num in nums:

        #     if num in hashmap.keys():

        #         hashmap[num] += 1
            
        #     else:
        #         hashmap[num] = 1

        ret = 0
        for key, val in hashmap.items():

            if key+1 in hashmap:
                ret = max(  ret, val+hashmap[key+1] )
        
        return ret

nums = [1,3,2,2,5,2,3,7]
s = Solution()
print(s.findLHS(nums))