class Solution:
    def numDecodings(self, s: str) -> int:

        N = len(s)

        dp_arr = [0]*N 


        if N==0 or s[0]=='0':
            return 0
        
        dp_arr[0] = 1

        for i in range(1, N):

            acc_num = int(s[i])
            last_num = int(s[i-1])

            if acc_num==0:

                if last_num>=3 or last_num==0:
                    return 0
            
                else:
                    if i-2>=0:
                        dp_arr[i] = dp_arr[i-2]
                    else:
                        dp_arr[i] = 1
            
            else:

                if (last_num*10+acc_num)<=26 and last_num != 0 :
                    if i-2>=0 :
                        dp_arr[i] = dp_arr[i-1] + dp_arr[i-2]
                    else:
                        dp_arr[i] = dp_arr[i-1] + 1
                else:
                    dp_arr[i] = dp_arr[i-1]
            
            # print(dp_arr)    
        return dp_arr[N-1]

s = Solution()
print(s.numDecodings('2101'))