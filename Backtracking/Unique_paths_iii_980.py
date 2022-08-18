from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        self.M , self.N = len(grid), len(grid[0])

        self.is_used = [[False] * self.N for _ in range(self.M) ]  
        self.grid = grid 
        self.ret = 0

        start_loc = [0,0]
        path_sum_len = 0

        for i in range(self.M):
            for j in range(self.N):

                if grid[i][j]==1:
                    start_loc[0] = i 
                    start_loc[1] = j

                if grid[i][j]==0:
                    path_sum_len += 1 
        
        self.path_sum_len = path_sum_len+1

        self.direction = [-1,0,1,0,-1]

        self.is_used[start_loc[0]][start_loc[1]] = True
        self._dfs(start_loc[0], start_loc[1], 0)

        return self.ret 

    def _dfs(self, i, j, path_len):
        if self.grid[i][j]==2 and path_len== self.path_sum_len:
            self.ret += 1
            return
        
        elif self.grid[i][j]==2:
            return 
        
        for x in range(4):
            new_i, new_j = i+self.direction[x], j+self.direction[x+1] 

            if (new_i>=0 and new_j>=0 and new_i<self.M and new_j<self.N and 
                    not self.is_used[new_i][new_j] and self.grid[new_i][new_j]!=-1
            ):
                
                self.is_used[new_i][new_j] = True
                self._dfs( new_i, new_j, path_len+1 )
                self.is_used[new_i][new_j] = False

s = Solution()
print(s.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]] ))