from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        nums = sorted(intervals, key= lambda x:x[0])

        print(nums)

        ret = [nums[0]]

        right_ind = 0

        for i in range(1, len(nums)):

            temp_arr = nums[i]
            if temp_arr[1] <= ret[right_ind][1]:
                continue
            elif temp_arr[0]<=  ret[right_ind][1]:
                ret[right_ind][1] = temp_arr[1]
            else:
                ret.append(temp_arr)
                right_ind += 1

        return ret


s = Solution()
print(s.merge(  [[1,4],[4,5]]))