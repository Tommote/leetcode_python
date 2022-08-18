from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:


        dis = [ [float('inf')]*n for _ in range(n)]

        for edge in edges:
            dis[edge[0]][edge[1]] = edge[2]
            dis[edge[1]][edge[0]] = edge[2]
        
        for i in range(n):
            dis[i][i] = 0
        
        # print(dis)

        for k in range(n):
            for i in range(n):
                for j in range(n):

                    dis[i][j] = min(dis[i][j],  dis[i][k]+dis[k][j])
        
        # print(dis)
        ret_arr = [0]*n 

        for i in range(n):
            for j in range(i+1, n):

                if dis[i][j]<=distanceThreshold:
                    ret_arr[i] += 1
                    ret_arr[j] += 1
        
        ret = 0
        # print(ret_arr)
        for i in range(1,n):

            if ret_arr[i]<= ret_arr[ret]:
                ret = i 
        
        return ret 

s = Solution()
print(s.findTheCity(6, [[2,3,7],[2,5,8],[0,2,8],[4,5,5],[1,5,10],[3,4,3],[0,5,9],[1,2,1]], 3269))