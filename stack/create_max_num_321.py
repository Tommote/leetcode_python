import heapq
from typing import List

class Node:
    def __init__(self, val) -> None:
        self.val = val

class Solution:

    def get_m_arr(self, nums: List[int], k):

        stack = [0]* k 

        top = -1 
        remain = len(nums)-k 

        for n in nums:
            while top>=0 and stack[top]<n and remain>0:
                top -= 1
                remain -= 1 
            if top<k-1 :
                top += 1
                stack[top]=n 
        return stack

    def merge(self, nums1: List[int], nums2: List[int]) -> List[int]:

        ret = [0]*(len(nums1)+len(nums2))
        p_1 , p_2 = 0, 0

        for i in range(len(ret)):
            # print(i,p_1,p_2)
            if p_1>=len(nums1):
                ret[i] = nums2[p_2]
                p_2 += 1
            elif p_2>=len(nums2):
                ret[i] = nums1[p_1]
                p_1 += 1
            else:
                if nums1[p_1]>nums2[p_2]:
                    ret[i] = nums1[p_1]
                    p_1 += 1      
                elif nums1[p_1]<nums2[p_2]:
                    ret[i] = nums2[p_2]
                    p_2 += 1
                else:
                    # nums1 
                    temp1 = self.merge(nums1[p_1+1:],nums2)

                    temp2 = self.merge(nums1, nums2[p_2+1:])
                    ret[i] = nums1[p_1]
                    if self.compare(temp1,temp2)>0:
                        ret[i+1:] = temp1
                    else:
                        ret[i+1:] = temp2
                    return ret 
        return ret 
    
    def compare(self, nums1: List[int], nums2: List[int]):

        for i in range(len(nums1)):
            if nums1[i]>nums2[i]:
                return 1 
            elif nums1[i]<nums2[i]:
                return -1
        
        return 0

    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:

        ret = [0]*k 

        for i in range(k):

            n1 = min(i, len(nums1))
            n2 = k-n1 

            if n2>len(nums2):
                continue

            max_arr_1, max_arr_2 = self.get_m_arr(nums1, n1), self.get_m_arr(nums2,n2)

            temp_arr = self.merge(max_arr_1,max_arr_2)
            if self.compare(temp_arr,ret)>0:
                ret = temp_arr 

        return ret 




s = Solution()

print(s.maxNumber([6, 7],[6,0,4], 5 ))