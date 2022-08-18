from typing import List

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:

        row_n, col_m = len(matrix), len(matrix[0])

        ret = 0

        for ni in range(row_n):

            sum_num = [0]*col_m

            for nj in range(ni, row_n):

                for mi in range(col_m):

                    sum_num[mi] = sum_num[mi] + matrix[nj][mi]

                ret += self.pre_hash_target(sum_num, target)

        return ret 


    def pre_hash_target(self, nums, target):

        num_dict = {}
        ret , pre = 0, 0

        num_dict[0] = 1

        for i in range(len(nums)):

            pre += nums[i]

            if (pre - target) in num_dict:
                ret += num_dict[pre - target]
            
            num_dict[pre] = num_dict.pop(pre, 0) + 1

        return ret 


s = Solution()
print(s.numSubmatrixSumTarget([[11]], 0))