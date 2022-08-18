from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:

        N = len(arr)
        arr_dict = dict() 

        for i in range(N):
            arr_dict[ arr[i] ] = i 
        
        
        