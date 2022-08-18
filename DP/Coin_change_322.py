from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:


        dp_arr = [0] + [float('inf')]*amount 

        for t in range(1, amount+1) :

            temp_ret = float('inf')
            for c in coins:

                if t>=c :
                    temp_ret = min( dp_arr[t-c]+1, temp_ret )
            
            dp_arr[t] = temp_ret
        
        return dp_arr[amount] if dp_arr[amount] != float('inf') else -1

s = Solution()
print(s.coinChange([1],0))