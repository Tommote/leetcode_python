class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        N = len(nums)
        ret = []

        nums = sorted(nums)

        for i in range(0, N):

            if i != 0 and nums[i - 1] == nums[i]:
                continue

            for j in range(i + 1, N):

                if j != i + 1 and nums[j - 1] == nums[j]:
                    continue

                res_target = target - nums[i] - nums[j]

                forth = N - 1

                for third in range(j + 1, N):

                    while forth > third and (nums[forth] + nums[third]) > res_target:
                        forth -= 1

                    if forth == third:
                        break

                    if nums[forth] + nums[third] == res_target:
                        ret.append([nums[i], nums[j], nums[third], nums[forth]])

        return ret


s = Solution()

print(s.fourSum([1, 0, -1, 0, -2, 2], 0))

