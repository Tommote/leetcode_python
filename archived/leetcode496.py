class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        stack = []
        res = {}

        for i in range( len(nums2) ):

            index = len(nums2) - i - 1

            num_temp = nums2[index]

            while stack and num_temp>stack[-1]:
                stack.pop()
            
            res[num_temp] = stack[-1] if stack else -1
            stack.append(num_temp)
        

        return [ res[j] for j in nums1 ]