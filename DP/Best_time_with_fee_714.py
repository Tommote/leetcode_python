from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        N = len(prices)

        s1 , s2 = [0]*N, [0]*N 

        s1[0] = -1 * prices[0] 
        s2[0] = 0 

        for i in range(1, N):

            s1[i] = max(s1[i-1], s2[i-1]-prices[i])
            s2[i] = max( s2[i-1], s1[i-1]+prices[i]-fee )
            # print(s1)
            # print(s2)
        return s2[N-1]

s = Solution()
print(s.maxProfit([1,3,2,8,4,9],2))