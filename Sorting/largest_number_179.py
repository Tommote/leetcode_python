from functools import cmp_to_key
from typing import List


def mycmp(x , y):
    print(x,y)
    if x==y:
        return 0
    x,y = str(x), str(y)

    temp_iter = min(len(x), len(y))

    for i in range(temp_iter):
        if int(x[i])!=int(y[i]):
            return  int(x[i])-int(y[i])
    if temp_iter==len(x):
        return mycmp(str2num(x),str2num(y[temp_iter:]))
    else:
        return mycmp(str2num(x[temp_iter:]),str2num(y))
def str2num(nums):
    ret = ''
    for num in nums:
        ret = ret + str(num)
        
    return int(ret) 



class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        nums = self._sort(nums, mycmp)
        print(nums)
        ret = ''
        for num in reversed(nums):
            ret = ret + str(num)
        
        return ret 
    def _sort(self, array, cmp):

        length = len(array)
        for i in range(0, length):

            for j in range(i , length):
                if cmp(array[i], array[j]) > 0:
                    self._swap(array, i , j)

        return array

    def _swap(self, array, xi, yi):
        temp = array[xi]
        array[xi] = array[yi]
        array[yi] = temp

s = Solution()
print(s.largestNumber([3,30,34]))
# print(mycmp(3,30))

# print(int(['2','2']))