class Solution(object):

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        self.ret = []
        self.temp_arr = []
        self.nums = nums

        self.dfs(0)

        return self.ret


    def dfs(self, i):

        if i == len(self.nums):

            self.ret.append( self.temp_arr.copy() )

            return
        
        self.temp_arr.append( self.nums[i] )
        self.dfs(i+1)

        self.temp_arr.pop()
        self.dfs(i+1)


s = Solution()
print(s.subsets([1,2,3]))