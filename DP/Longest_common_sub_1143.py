class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        n1, n2 = len(text1), len(text2) 

        dp_arr = [ [0]*n2 for _ in range(n1)]

        for i in range(n1):

            for j in range(n2) :

                temp_ret = 0

                if i-1>=0 :
                    temp_ret = max(temp_ret, dp_arr[i-1][j])
                
                if j-1>=0 :
                    temp_ret = max(temp_ret, dp_arr[i][j-1])
                
                if text1[i]==text2[j]:
                    if i-1>=0 and j-1>=0 :
                        temp_ret = max(temp_ret, dp_arr[i-1][j-1]+1)
                    else:
                        temp_ret = max(temp_ret,1)
                
                dp_arr[i][j] = temp_ret
        

        return dp_arr[n1-1][n2-1]
s = Solution()
print(s.longestCommonSubsequence('abc','dff'))
