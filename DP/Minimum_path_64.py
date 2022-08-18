from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        m ,n = len(grid), len(grid[0])

        dp_matrix = [ [0]*n ] * m 

        for i in range(m) :

            for j in range(n):

                if i==0 and j==0:
                    dp_matrix[i][j] = grid[i][j]
                
                elif i==0:
                    dp_matrix[i][j] = dp_matrix[i][j-1] + grid[i][j]
                elif j==0:
                    dp_matrix[i][j] = dp_matrix[i-1][j] + grid[i][j]
                else:
                    dp_matrix[i][j] = min( dp_matrix[i-1][j], dp_matrix[i][j-1] ) + grid[i][j]

        return dp_matrix[m-1][n-1] 