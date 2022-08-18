from typing import List


class Solution:
    
    
    
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        self.ret = []
        self.temp_arr = []

        self.k , self.n = k , n

        self.dfs(1, 0)

        return self.ret 

    
    def dfs(self, i, sum_t):
        if len(self.temp_arr)==self.k:
            
            if sum_t==self.n:
                 self.ret.append(self.temp_arr.copy())
            return

        if i>9 :
            return

        if len(self.temp_arr)>self.k:
            return



        if sum_t>self.n:
            return
        

        self.dfs(i+1, sum_t)

        self.temp_arr.append(i)
        self.dfs(i+1, sum_t+i)
        self.temp_arr.remove(i)

s = Solution()
print(s.combinationSum3(9,45))