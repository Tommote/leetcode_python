from typing import DefaultDict


class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """

        location_dict = {}

        for i in range(len(arr)):

            if arr[i] in location_dict:

                location_dict[ arr[i] ].append(i)
            
            else:
                location_dict[ arr[i] ] = [ i ]

        
        matrix = [1 for _ in range(len(arr)) ]

        for i in range(1, len(arr)):

            according_temp =  arr[i]-difference
            ret = 1

            if according_temp in location_dict:

                ind = location_dict[according_temp]

                for x in ind:

                    if x < i :

                        ret = max( matrix[x]+1, ret )
            

            matrix[i] = ret
        
        return max(matrix)


s = Solution()

print(s.longestSubsequence( arr=[1,5,7,8,5,3,4,2,1], difference=-2 ))

a = DefaultDict