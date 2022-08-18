from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp_list = [[0]*n] * m 

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]==1:
                    dp_list[i][j] = 0
                elif i==0 and j==0:
                    dp_list[0][0] = 1
                elif i==0:
                    dp_list[i][j] = dp_list[i][j-1]
                elif j==0:
                    dp_list[i][j] = dp_list[i-1][j]
                else:
                    dp_list[i][j] = dp_list[i-1][j] + dp_list[i][j-1]
        return dp_list[m-1][n-1]

s = Solution()
print( s.uniquePathsWithObstacles(  [[0,0,0],[0,1,0],[0,0,0]] ) )