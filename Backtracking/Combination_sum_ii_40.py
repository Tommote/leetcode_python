from collections import Counter
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        
        self.freq = Counter(candidates)
        self.candidates = list(self.freq)
        self.N = len(self.candidates)

        self.temp = []
        self.ret = []
        # print(self.freq, self.candidates)
        self._dfs(0, target)

        return self.ret 

    def _dfs(self, i, res):

        # print(i, res)
        # print(self.temp)
        if res==0:
            self.ret.append(self.temp.copy())
        elif res<0 or i==self.N :
            return

        else:    
            num =  self.candidates[i]
            repeat_time = self.freq[num]
            for x in range(repeat_time+1):
                for _ in range(x):
                    self.temp.append(num)
                self._dfs( i+1, res-num*x )
                for _ in range(x):
                    self.temp.pop()
            

class Solution2:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        self.N = len(candidates)
        self.candidates = sorted(candidates)

        self.temp = []
        self.ret = []

        self._dfs(0, target)

        return self.ret 

    def _dfs(self, i, res):

        # print(i, res)
        # print(self.temp)
        if res==0:
            self.ret.append(self.temp.copy())
        elif res<0 or i==self.N :
            return
        else:
            
            for j in range(i, self.N):
                if j>i and self.candidates[j-1]==self.candidates[j]:
                    continue
                # if self.candidates[j]>res:
                #     break
                self.temp.append(self.candidates[j])
                self._dfs( j+1, res-self.candidates[j] )
                self.temp.pop() 
            


s = Solution()
print(s.combinationSum2( [10,1,2,7,6,1,5], 8))

