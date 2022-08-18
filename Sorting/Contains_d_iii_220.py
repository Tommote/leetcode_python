from collections import defaultdict
from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:

        boxs_dict = defaultdict(None)

        for i in range(len(nums)):
            num = nums[i] 
            ind = self._get_ind(num, t)

            if boxs_dict.get(ind) is not None :
                return True
            
            if boxs_dict.get(ind-1) is not None and abs( boxs_dict.get(ind-1)-num)<=t :
                return True 
            
            if boxs_dict.get(ind+1) is not None and abs( boxs_dict.get(ind+1)-num)<=t :
                return True 

            boxs_dict[ind] = num 

            if len(boxs_dict) > k :
                boxs_dict.pop( self._get_ind( nums[i-k] , t) )

        return False

    def _get_ind(self, num, t):

        # if num >=0 :
        #     return num//t 
        # else:
        #     return num//t
        if t==0:
            return num
        return num//t

s = Solution()
print(s.containsNearbyAlmostDuplicate( [3,6,0,2], k = 2, t = 2 ))