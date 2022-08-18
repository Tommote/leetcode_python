from functools import lru_cache
from math import inf


class Solution:
    def superEggDrop(self, k: int, n: int) -> int:

        return self.recur(k, n) 

    @lru_cache(maxsize=100000)
    def recur(self, k:int , top:int )->int:
        
        if k == 1:
            return top
        
        if 1>=top:
            return 1
        ret = inf
        for x in range(1, top):
            ret = min(ret, max( self.recur( k,  top-x ), self.recur(k-1, x-1) )+1)
        return ret

s = Solution()
print(s.superEggDrop(1,2))