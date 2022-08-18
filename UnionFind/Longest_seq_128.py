from collections import defaultdict
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: 

        self.map = {}
        self.N = len(nums)

        temp_num = 0
        for num in nums:
            if num not in self.map :
                self.map[num] = temp_num
                temp_num += 1
        
        self.union_set = [i for i in range(temp_num )]

        for num in nums:

            ind = self.map[num]

            if num-1 in self.map:
                self.merge( ind, self.map[num-1] )
            
            if num+1 in self.map:
                self.merge(ind, self.map[num+1] )

        ret_map = defaultdict(None)
        ret = 0
        for i in range(len(self.union_set)):

            root = self._find( i )
            root_num = ret_map.get(root)

            if root_num is None:
                ret_map[root] = 1
            else :
                ret_map[root] += 1 

            ret = max( ret, ret_map[root] )
        

        return ret 

    def _find( self, x ):

        if self.union_set[x] == x:
            return x 
        else:
            self.union_set[x] = self._find( self.union_set[x] )
            return self.union_set[x]
    
    def merge(self, x, y):

        x_root, y_root = self._find(x), self._find(y) 

        self.union_set[y_root] = x_root

s = Solution()
print(s.longestConsecutive([1,2,3,5,5,8,7,6,9,4]) )