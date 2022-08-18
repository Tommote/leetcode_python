from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        N = len(nums)
        self.ans = [0]*N 
        self.temp_ans = [0]*N 

        self.index = [i for i in range(N)]
        self.temp_ind = [0]*N 

        self._sort(nums, 0, N-1)
        # print(nums)
        # print(self.index)
        return self.ans
    def _sort(self,nums,s_p,e_p):

        if s_p==e_p:
            return
        
        mid_p = (s_p+e_p)//2

        self._sort(nums, s_p,mid_p)
        self._sort(nums,mid_p+1,e_p)

        p_left, p_right = s_p , mid_p+1
        i = s_p
        while i<=e_p:

            if p_left>mid_p:
                self.temp_ans[i]=nums[p_right]
                self.temp_ind[i]=self.index[p_right]

                i += 1
                p_right += 1
            elif p_right>e_p:
                self.temp_ans[i]=nums[p_left]
                self.temp_ind[i]=self.index[p_left]
                self.ans[ self.index[p_left] ] += p_right-mid_p-1
                i += 1
                p_left += 1
            else:
                if nums[p_left]<=nums[p_right]:
                    self.temp_ans[i]=nums[p_left]
                    self.temp_ind[i]=self.index[p_left]
                    self.ans[ self.index[p_left] ] += p_right-mid_p-1
                    i += 1
                    p_left += 1                    
                else:
                    self.temp_ans[i]=nums[p_right]
                    self.temp_ind[i]=self.index[p_right]
                    i += 1
                    p_right += 1
            
        nums[s_p:e_p+1] = self.temp_ans[s_p:e_p+1]
        self.index[s_p:e_p+1] = self.temp_ind[s_p:e_p+1]

s = Solution()
print(s.countSmaller( [-1,-1] ))