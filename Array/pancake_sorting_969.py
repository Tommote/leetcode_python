from typing import List


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:


        ret = []

        N = len(arr)

        for i in range(N):

            j = N-1-i

            max_loc = arr.index(j+1)

            if max_loc == j:
                continue
            elif max_loc == 0 :
                self.__reverse(arr, j)
                ret.append(j+1)
            else:
                self.__reverse(arr, max_loc)
                self.__reverse(arr, j)

                ret.append(max_loc+1)
                ret.append(j+1)

        return ret

    def __reverse(self, arr, k):

        left = 0
        right = k

        while left < right :

            self.__swap(  arr, left, right )

            left += 1
            right -= 1
 
    
    def __swap(self, arr, i ,j):

        temp = arr[j]
        arr[j] = arr[i]
        arr[i] = temp


s = Solution()
print( s.pancakeSort([3,2,4,1]) )