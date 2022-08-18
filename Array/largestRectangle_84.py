from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        """
        """

        N = len(heights)
        left_max = [0]*N
        right_max = [0]*N

        stack = []

        for i in range(N):
            while len(stack) != 0 and stack[-1][0] >= heights[i] :
                stack.pop()

            left_max[i] = stack[-1][1] if len(stack)>0 else -1
            stack.append((heights[i], i))
        
        stack.clear()
        for i in range(N):
            i = N - i -1

            while len(stack) != 0 and stack[-1][0] >= heights[i] :
                stack.pop()
            right_max[i] = stack[-1][1] if len(stack)>0 else N
            stack.append((heights[i], i))

        ret = 0
        for i in range(N):
            
            max_area = heights[i] * ( right_max[i] - left_max[i] -1 )
            ret = max( ret, max_area   )

        return ret 


s = Solution()
y = s.largestRectangleArea([2,4])
print(y)