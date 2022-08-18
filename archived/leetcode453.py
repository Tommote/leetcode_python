class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_num = min(nums)

        temp =  map(  lambda x:x-min_num, nums )

        return sum(temp)


s = Solution()
print( s.minMoves( [1,1,1] ) )