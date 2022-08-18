from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        self.location = [0]*n 
        self.isUsed = [False]*n 

        self.leftUsed = [False]*(2*n-1)
        self.rightUsed = [False]*(2*n-1)

        self.N = n 

        self.ret = [] 

        # self.grid = [ ['.']*self.N for _ in range(self.N) ]

        self._backTrack(0)
        return self.ret 
    
    def _backTrack(self, i):

        if i==self.N :
            self.ret.append(self._nums2str())
            return 
        
        for j in range(self.N):
            
            left_temp , right_temp = self._left_loc(i,j), self._right_loc(i,j)

            if self.isUsed[j] or self.leftUsed[left_temp] or self.rightUsed[right_temp] :
                continue
            
            self.location[i] = j 
            self.isUsed[j] = True
            self.leftUsed[left_temp] = True
            self.rightUsed[right_temp] = True
            self._backTrack(i+1)
            self.isUsed[j] = False
            self.leftUsed[left_temp] = False
            self.rightUsed[right_temp] = False

    def _nums2str(self):

        grid_temp = [ ['.']*self.N for _ in range(self.N) ]
        ret_temp = []

        for i in range(self.N):
            grid_temp[i][self.location[i]] = 'Q'
            ret_temp.append( ''.join(grid_temp[i]) )

        return ret_temp

    def _left_loc(self, row, col):

        row = self.N-row-1
        return row+col
    def _right_loc(self, row, col):
        row = self.N-row-1
        col = self.N-col-1
        return row+col

s = Solution()

print(s.solveNQueens(4))