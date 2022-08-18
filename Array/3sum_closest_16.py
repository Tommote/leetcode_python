class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        ret = 1e6
        len_nums = len(nums)
        
        nums = sorted(nums)

        def update_ret(ret, n):

            if abs(n-target) < abs(ret-target):
                return n

            else:
                return ret

        for i in range(len_nums):

            third = len_nums-1
            i_target = target - nums[i]
            if i==0 or nums[i-1]!=nums[i]:
                for j in range(i+1, len_nums):

                    if j==i+1 or nums[j-1]!=nums[j] :

                        while j<third and nums[j]+nums[third]>i_target:
                            third -= 1
                        


                        if third+1 <= len_nums-1:
                            ret = update_ret(ret, nums[i]+nums[j]+nums[third+1])

                        if j==third:
                            break
                        ret = update_ret(ret, nums[i]+nums[j]+nums[third])

                        break


        return ret

s = Solution()

print(s.threeSumClosest([-1,2,1,-4], 1))