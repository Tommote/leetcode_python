class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        N = len(height)

        left_max = [0]*N
        right_max = [0]*N

        left_temp, right_temp = 0, 0

        for i in range(N):
            
            if height[i] > left_temp:
                left_max[i] = 0
                left_temp = height[i]
            else:
                left_max[i] = left_temp
            
            j = N-i-1
            if height[j] > right_temp:
                right_max[j] = 0
                right_temp = height[j]
            else:
                right_max[j] = right_temp
        
        ret = 0

        for i in range(N):

            ret = ret + max(  min(left_max[i], right_max[i])-height[i], 0  )
        

        return ret


s = Solution()

print(s.trap([4,2,0,3,2,5]))
