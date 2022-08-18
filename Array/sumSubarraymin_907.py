
from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        N = len(arr)
        left_matrix = [0]*N
        right_matrix = [0]*N

        MOD = 10**9+7

        ret = 0

        stack = []

        for i in range(N):

            while len(stack)!=0 and arr[stack[-1]]>arr[i]:
                stack.pop()

            if len(stack)==0:
                left_matrix[i] = -1
            else:
                left_matrix[i] = stack[-1]
            
            stack.append(i)
        
        stack.clear()
        for j in range(N):

            i = N-1-j

            while len(stack)!=0 and arr[stack[-1]]>=arr[i]:
                stack.pop()

            if len(stack)==0:
                right_matrix[i] = N
            else:
                right_matrix[i] = stack[-1]
            
            stack.append(i)

        for i in range(N):

            ret = ret + ((i-left_matrix[i])*(right_matrix[i]-i)*arr[i])


        return ret

s = Solution()

print( s.sumSubarrayMins([3,1,2,4]) )
                