from typing import List


class UnionFind: 
    def __init__(self, n) -> None:
        
        # self.n = n 

        self.arr = [ i for i in range(n+1) ]
    
    def find(self, x):

        if self.arr[x] == x :
            return x 
        
        else:

            self.arr[x] = self.find( self.arr[x] )
            return self.arr[x]
    
    def merge(self, x, y):

        x_r , y_r = self.find(x), self.find(y) 

        self.arr[y_r] = x_r 


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]: 

        UnionFindSet = UnionFind(len(edges))

        for i in range(len(edges)) :

            edge = edges[i] 

            x1 , x2 = UnionFindSet.find(edge[0]), UnionFindSet.find(edge[1]) 
            # print(x1, x2)
            if x1==x2 :
                return edge
            else:
                UnionFindSet.merge( x1, x2 )

s = Solution()
e = s.findRedundantConnection( [[1,2], [2,3], [3,4], [1,4], [1,5]] )
print(e)