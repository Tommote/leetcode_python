from functools import reduce


class Solution:
    def nextGreaterElement(self, n: int) -> int:

        arr_num = [ int(t) for t in str(n) ]

        flag = False

        for i in range( len(arr_num)-1, 0, -1 ):

            if arr_num[i]  > arr_num[i-1]:

                flag = True
                arr_num[i] ,arr_num[i-1] = arr_num[i-1], arr_num[i]
                break
        arr_num[i:] = sorted(arr_num[i:])
        ret = int(reduce(  lambda x, y: str(x)+str(y) , arr_num))


        return  ret if ret<=2**31-1 and flag else -1


s = Solution()
print( s.nextGreaterElement(230241) )