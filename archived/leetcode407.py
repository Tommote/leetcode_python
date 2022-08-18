import heapq

class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """

        loc = [-1, 0, 1, 0, -1]
        pq = []

        res = 0
        

        # init

        h = len(heightMap)
        w = len(heightMap[0])

        vist = [ [ False for i in range(0,w)] for j in range(0,h) ]

        for i in range(0, h):
            for j in range(0, w):

                if( i==0 or i==h-1 or j==0 or j==w-1 ):

                    heapq.heappush(  pq, (heightMap[i][j] ,i*w+j ) )
                    vist[i][j] = True
        
        while pq :

            high ,temp_loc   = heapq.heappop(pq)

            i = temp_loc//w
            j = temp_loc%w 

            for k in range(0,4):

                temp_i = i + loc[k]
                temp_j = j + loc[k+1]

                if (temp_i>=0 and temp_j>=0 and temp_i<h and temp_j<w and
                    (not vist[temp_i][temp_j])) :
                    
                    if( high > heightMap[temp_i][temp_j] ):

                        res += high - heightMap[temp_i][temp_j]
                        heapq.heappush( pq, (high ,  temp_i*w + temp_j) )
                        vist[temp_i][temp_j] = True
                    
                    else:
                        heapq.heappush(pq, (heightMap[temp_i][temp_j] ,  temp_i*w + temp_j))
                        vist[temp_i][temp_j] = True


        return res