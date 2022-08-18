from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:


        if len(triangle)==0 or len(triangle[0])==0 :
            return 0 
        
        dp_arr = []
        for i in range(len(triangle)):

            acc_len = len(triangle[i])

            if acc_len==1:
                ret = triangle[i][0]
                dp_arr = [ret]
            
            else:
                new_dp_arr = [0]*acc_len

                for j in range(len(new_dp_arr)):

                    if j==0 :
                        new_dp_arr[j] = dp_arr[j]+ triangle[i][j]
                    elif j==len(new_dp_arr)-1:
                        new_dp_arr[j] = dp_arr[j-1]+ triangle[i][j]
                    else:
                        new_dp_arr[j] = min( dp_arr[j-1], dp_arr[j] ) + triangle[i][j]
                
                dp_arr = new_dp_arr
            # print(dp_arr)
        return min(dp_arr)
                        
s = Solution()
print(s.minimumTotal( [[-10]]))