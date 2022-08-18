from typing import List


class Solution:
    def longestMountain(self, arr: List[int]) -> int:

        N = len(arr)

        if N < 3:
            return 0
        
        ret = 0
        left, right = 0, 0

        up_tend = True

        while left<N:

            if left==right:
                up_tend = True
                if right<N-1 and arr[right]<arr[right+1]:
                    right += 1
                else:
                    left += 1
                    right += 1
            
            else:

                if up_tend :
                    if right<N-1 and arr[right]<arr[right+1]:
                        right += 1
                    elif right<N-1 and arr[right]==arr[right+1]:
                        left = right+1
                        right = left
                    elif right<N-1 and arr[right]>arr[right+1]:
                        # right += 1
                        up_tend = False
                    else:
                        break
                else:
                    if right<N-1 and arr[right]>arr[right+1]:
                        right += 1
                        ret = max(ret, right-left+1)
                    elif right<N-1 and arr[right]==arr[right+1]:
                        left = right+1
                        right = left
                    elif right<N-1 and arr[right]<arr[right+1]:
                        left = right                        
                    else:
                        break
        

        return ret 

s = Solution()
print(s.longestMountain([0,1,0]))