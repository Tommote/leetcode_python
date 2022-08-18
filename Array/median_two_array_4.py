from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        t = (len(nums1)+len(nums2))
        if t%2 == 0:
            temp1 = self.findK(nums1,nums2,0,0,t//2)
            temp2 = self.findK(nums1,nums2,0,0,t//2+1)

            print(temp1,temp2)

            return (temp1 + temp2)/2.0 
        else:
            return self.findK(nums1,nums2,0,0,t//2+1) + 0.0

    def findK(self, nums1, nums2, s1, s2, k):
        
        if k <= 0 :
            return

        if s1 == len(nums1) :
            return nums2[s2+k-1]
        
        if s2 == len(nums2) :
            return nums1[s1+k-1]
        
        if k == 1:
            return min(nums1[s1], nums2[s2])
        
        ind1 = ind2 = k//2-1

        if ind1 + s1 + 1 >= len(nums1):
            ind1 = len(nums1)-s1-1 

        if ind2 + s2 + 1 >= len(nums2):
            ind2 = len(nums2)-s2-1 
        
        temp1, temp2 = nums1[ind1+s1], nums2[ind2+s2] 
        print(s1,s2,k,ind1,ind2,temp1,temp2)
        if temp1 >= temp2 :
            return self.findK(nums1,nums2, s1, s2+ind2+1, k-ind2-1)
        else:
            return self.findK(nums1,nums2,s1+ind1+1, s2, k-ind1-1)

s = Solution()
print(s.findMedianSortedArrays([1,3],[2,7]))