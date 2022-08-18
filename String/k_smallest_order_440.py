

class Solution:


    def get_numbers(self, cur, n):

        nums, first, last = 0, cur, cur

        while first <= n :

            nums +=  min(last, n)-first + 1

            first *= 10 
            last = last*10 + 9

        return nums 


    def findKthNumber(self, n: int, k: int) -> int:

        cur = 1
        k -= 1
        while k:

            nums = self.get_numbers(cur)

            if nums<=k :

                k -= nums
                cur += 1
            
            else:
                cur = cur * 10
                k -= 1
        
        return cur 