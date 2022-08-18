class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """


        ret = []
        len_nums = len(nums)
        
        nums = sorted(nums)

        for i in range(len_nums):

            third = len_nums-1
            target = 0 - nums[i]
            if i==0 or nums[i-1]!=nums[i]:
                for j in range(i+1, len_nums):

                    if j==i+1 or nums[j-1]!=nums[j] :

                        while j<third and nums[j]+nums[third]>target:
                            third -= 1
                        
                        if j<third and nums[j]+nums[third]==target:

                            ret.append([nums[i], nums[j], nums[third]])


        return ret

s = Solution()

print(s.threeSum([]))