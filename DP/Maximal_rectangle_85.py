from typing import List


class Solution:


    def check(self, dp:List[int]) -> int:

        stack_pre = []
        arr_pre = [0]*len(dp)
        for i in range(len(dp)):

            temp_num = dp[i]

            while len(stack_pre)>0 and dp[stack_pre[-1]]>=temp_num:
                stack_pre.pop()
            
            if len(stack_pre)==0:
                arr_pre[i]=-1
            else:
                arr_pre[i] = stack_pre[-1]
            
            stack_pre.append(i)

        stack_post = []
        arr_post = [0]*len(dp)
        for i in range(len(dp)-1, -1, -1):

            temp_num = dp[i]

            while len(stack_post)>0 and dp[stack_post[-1]]>=temp_num:
                stack_post.pop()
            
            if len(stack_post)==0:
                arr_post[i]=len(dp)
            else:
                arr_post[i] = stack_post[-1]
            
            stack_post.append(i)

        ret = 0
        for i in range(len(dp)):
            temp = dp[i]*(arr_post[i]-arr_pre[i]-1)
            ret = max(ret, temp)

        # print(arr_post, arr_pre)

        return ret

    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        if len(matrix)==0 :
            return 0
        rows , cols = len(matrix), len(matrix[0])

        dp_hight = [0]*cols

        for i in range(cols):
            if matrix[0][i]=='1':
                dp_hight[i] = 1
        
        ret = 0

        for i in range(rows):

            if i != 0:
                for j in range(cols):
                    if matrix[i][j]=='0':
                        dp_hight[j] = 0
                    else:
                        dp_hight[j] += 1
            
            temp = self.check(dp_hight)
            if temp>ret:
                ret = temp
        
        return ret 

s = Solution()
print(s.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))