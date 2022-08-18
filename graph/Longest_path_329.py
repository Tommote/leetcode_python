from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        M, N = len(matrix), len(matrix[0])

        flag = [[ -1 for _ in range(N) ] for _ in range(M)]

        self.ret = 0
        self.directions = [-1,0,1,0,-1]
        self.M, self.N = M, N 

        for i in range(M):
            for j in range(N):

                if flag[i][j]==-1:
                    self._dfs(i,j,flag, matrix)
        
        return self.ret 

    def _dfs(self, x, y, flag, matrix):

        if flag[x][y] != -1:
            return flag[x][y]

        curr_val = 1
        flag[x][y] = 0

        for i in range(4):

            new_x, new_y = x+self.directions[i], y+self.directions[i+1]

            if new_x>=0 and new_y>=0 and new_x<self.M and new_y<self.N and matrix[new_x][new_y]>matrix[x][y] :

                curr_val = max(curr_val, 1+self._dfs( new_x,new_y,flag, matrix ))
        
        flag[x][y] = curr_val
        self.ret = max(self.ret, curr_val)

        return curr_val


s = Solution()
print(s.longestIncreasingPath([[1]]))