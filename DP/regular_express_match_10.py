class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        s_len, p_len = len(s), len(p)

        dp_arr = [ [False]*(p_len+1) for _ in range(s_len+1)] 

        dp_arr[0][0] = True

        def match_char(ch1, ch2):
            if ch1==ch2 or ch1=='.' or ch2=='.':
                return True
            return False
        

        for i in range(s_len+1):
            for j in range(p_len+1):

                if i==0 and j==0:
                    dp_arr[i][j]= True
                    continue
                    
                if i==0 or j==0:
                    if j==2 and p[j-1]=='*':
                        dp_arr[i][j]=True
                    if j>2 and p[j-1]=='*':
                        dp_arr[i][j]=dp_arr[i][j-2]
                    continue

                if match_char(s[i-1],p[j-1]):
                    dp_arr[i][j] = dp_arr[i-1][j-1]
                elif p[j-1]=='*':
                    if match_char(s[i-1], p[j-2]):
                        dp_arr[i][j] = dp_arr[i-1][j] or dp_arr[i][j-2]
                    else:
                        dp_arr[i][j] =  dp_arr[i][j-2]
                # print(i, j, s[i-1],p[j-1],dp_arr[i][j])
        # print(dp_arr)
        return dp_arr[-1][-1]

s = Solution()
print(s.isMatch(s = "aab", p = "c*a*b"))