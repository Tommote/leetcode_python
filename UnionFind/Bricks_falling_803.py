from typing import List


class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:


        self.m, self.n = len(grid), len(grid[0])
        self.dicrection = [-1,0,1,0,-1]


        # grid_next = [ [None for _ in range(n)] for _ in range(m) ]
        # grid_pre = [ [None for _ in range(n)] for _ in range(m) ]

    

    def _dfs(grid: List[List[int]], location , last_location,grid_next, grid_pre ):

        x , y = location[0], location[1]

        if grid[x][y]==0 :
            return
        


        # for k in range(4):



            
        



