from typing import List


class Solution:

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        if len(nums)==1 :
            return nums 

        nums = sorted(nums)

        self.ress = []
        self.ret = []
        self.N = len(nums)
        self.visited = [False] * self.N 
        self.nums = nums

        self._backtrace(0)
        return self.ress  

    def _backtrace(self, n):

        if n == self.N :
            self.ress.append( self.ret.copy() )
            return

        for i in range(self.N):

            if i>0 and self.nums[i-1]==self.nums[i] and not self.visited[i-1]:
                continue
            elif self.visited[i] :
                continue
            else:
                self.ret.append(self.nums[i])
                self.visited[i] = True

                self._backtrace(n+1)

                self.ret.pop()
                self.visited[i] = False

s = Solution()

print(s.permuteUnique([1,1,2,3]))