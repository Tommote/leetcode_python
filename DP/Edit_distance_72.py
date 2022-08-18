class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        N1, N2 = len(word1), len(word2)

        dp_arr = [[0]*(N2+1) for _ in range(N1+1)]

        for i in range(N1+1):
            for j in range(N2+1):
                # print(i,j,)
                if i==0:
                    dp_arr[i][j] = j 
                elif j==0:
                    dp_arr[i][j] = i
                elif word1[i-1]==word2[j-1]:
                    dp_arr[i][j] = dp_arr[i-1][j-1]
                else:
                    dp_arr[i][j] = min(dp_arr[i-1][j],dp_arr[i-1][j-1],dp_arr[i][j-1])+1
        
        return dp_arr[-1][-1]
                

s = Solution()
print(s.minDistance(word1 = "intention", word2 = "execution"))