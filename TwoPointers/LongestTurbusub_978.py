from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:


        if arr is None or len(arr)==0:
            return 0
        
        if len(arr)==1 or ( len(arr)==2 and arr[0]==arr[1]):
            return 1
        
        # if len(arr)==2:
        #     return 2
        
        left = 0

        while left<len(arr)-1 and arr[left]==arr[left+1]:
            left += 1

        right = left+1
        max_ret = 1 if right>=len(arr) or arr[left]==arr[right] else 2

        while left < len(arr):

            if right>=len(arr)-1:
                break
            
            if ( (arr[right]>arr[right-1] and arr[right]>arr[right+1]) or
                  (arr[right]<arr[right-1] and arr[right]<arr[right+1]  )  ):

                  right += 1
                  max_ret = max( max_ret, right-left+1 )
            
            else:
                left = right
                right = right+1

            print(left, right)

        return max_ret

s = Solution()
print(s.maxTurbulenceSize([4,4]))