class Solution(object):
    
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        left = 0
        right = num

        mid = (left+right)//2

        while( left <= right ):

            mid = (left+right)//2

            if mid**2 == num:
                return True
            elif mid**2 < num:
                left = mid+1
            else:
                right = mid-1
        
        return False


s = Solution()

print(s.isPerfectSquare(16))